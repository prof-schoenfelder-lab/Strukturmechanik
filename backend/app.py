"""LTI backend (1.3 with 1.1 fallback) for the Strukturmechanik answer checker.

Hosting-neutral prototype: Flask + SQLite. OPAL launches via LTI 1.3
(/lti/login -> OIDC -> /lti/launch13) or LTI 1.1 (POST /lti/launch); the user
is pseudonymized (salted hash), receives a signed token via URL fragment and is
redirected to the static site. The site posts answer results to /api/results
with that token.

Environment variables (see .env.example):
  LTI_CONSUMER_KEY / LTI_CONSUMER_SECRET  shared with the OPAL course element
  SECRET_KEY                              signs session tokens
  USER_SALT                               salt for pseudonymization
  SITE_URL                                where to redirect after launch
  ALLOWED_ORIGINS                         comma-separated CORS origins
  DB_PATH                                 SQLite file (default: results.db)
"""

import base64
import hashlib
import os
import secrets
import sqlite3
import time
import urllib.parse

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from flask import Flask, g, jsonify, redirect, request
from itsdangerous import BadSignature, URLSafeTimedSerializer
from oauthlib.oauth1 import RequestValidator, SignatureOnlyEndpoint

CONSUMER_KEY = os.environ.get("LTI_CONSUMER_KEY", "strukturmechanik")
CONSUMER_SECRET = os.environ.get("LTI_CONSUMER_SECRET", "change-me")
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
USER_SALT = os.environ.get("USER_SALT", "dev-salt-change-me")
SITE_URL = os.environ.get("SITE_URL", "https://prof-schoenfelder-lab.github.io/Strukturmechanik/")
ALLOWED_ORIGINS = [o.strip() for o in os.environ.get(
    "ALLOWED_ORIGINS", "https://prof-schoenfelder-lab.github.io,http://localhost:8000"
).split(",") if o.strip()]
DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "results.db"))
TOKEN_MAX_AGE = 60 * 60 * 24 * 90  # 90 days

# LTI 1.3 platform data — in OPAL unter "Tool Konfiguration" ablesbar
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:5000")
LTI13_ISSUER = os.environ.get("LTI13_ISSUER", "https://bildungsportal.sachsen.de/opal")
LTI13_CLIENT_ID = os.environ.get("LTI13_CLIENT_ID", "")
LTI13_AUTH_URL = os.environ.get("LTI13_AUTH_URL", "https://bildungsportal.sachsen.de/opal/ltiauth/")
LTI13_KEYSET_URL = os.environ.get("LTI13_KEYSET_URL", "https://bildungsportal.sachsen.de/opal/restapi/lti/keys")
LTI13_DEPLOYMENT_ID = os.environ.get("LTI13_DEPLOYMENT_ID", "1")
PRIVATE_KEY_PATH = os.environ.get("PRIVATE_KEY_PATH", os.path.join(os.path.dirname(__file__), "lti_private.pem"))

app = Flask(__name__)
serializer = URLSafeTimedSerializer(SECRET_KEY, salt="ac-session")


# --- database ---------------------------------------------------------------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            pseudonym TEXT PRIMARY KEY,
            context_id TEXT,
            outcome_url TEXT,
            result_sourcedid TEXT,
            created_at REAL
        );
        CREATE TABLE IF NOT EXISTS results (
            pseudonym TEXT NOT NULL,
            qid TEXT NOT NULL,
            best REAL NOT NULL DEFAULT 0,
            max REAL NOT NULL DEFAULT 0,
            attempts INTEGER NOT NULL DEFAULT 0,
            updated_at REAL,
            PRIMARY KEY (pseudonym, qid)
        );
        """
    )
    db.commit()
    db.close()


# --- LTI 1.1 signature validation -------------------------------------------

class LTIValidator(RequestValidator):
    enforce_ssl = False  # TLS termination happens at the reverse proxy
    client_key_length = (3, 64)
    nonce_length = (8, 64)

    @property
    def dummy_client(self):
        return "dummy-" + CONSUMER_KEY

    def validate_client_key(self, client_key, request):
        return client_key == CONSUMER_KEY

    def get_client_secret(self, client_key, request):
        if client_key == CONSUMER_KEY:
            return CONSUMER_SECRET
        return "dummy-secret"

    def validate_timestamp_and_nonce(self, client_key, timestamp, nonce,
                                     request, request_token=None, access_token=None):
        try:
            return abs(time.time() - int(timestamp)) < 900
        except (TypeError, ValueError):
            return False


lti_endpoint = SignatureOnlyEndpoint(LTIValidator())


def pseudonymize(user_id):
    return hashlib.sha256((USER_SALT + ":" + user_id).encode()).hexdigest()[:32]


def finish_launch(user_id, context_id, outcome_url=None, result_sourcedid=None):
    """Upsert the pseudonymized user and redirect to the site with a session token."""
    pseudonym = pseudonymize(user_id)
    db = get_db()
    db.execute(
        """INSERT INTO users (pseudonym, context_id, outcome_url, result_sourcedid, created_at)
           VALUES (?, ?, ?, ?, ?)
           ON CONFLICT(pseudonym) DO UPDATE SET
             context_id=excluded.context_id,
             outcome_url=COALESCE(excluded.outcome_url, users.outcome_url),
             result_sourcedid=COALESCE(excluded.result_sourcedid, users.result_sourcedid)""",
        (pseudonym, context_id, outcome_url, result_sourcedid, time.time()),
    )
    db.commit()
    token = serializer.dumps({"sub": pseudonym})
    return redirect(SITE_URL + "#ac_token=" + token)


# --- LTI 1.3 (OIDC) ----------------------------------------------------------

def load_or_create_private_key():
    if os.path.exists(PRIVATE_KEY_PATH):
        with open(PRIVATE_KEY_PATH, "rb") as f:
            return serialization.load_pem_private_key(f.read(), password=None)
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pem = key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(pem)
    os.chmod(PRIVATE_KEY_PATH, 0o600)
    return key


private_key = load_or_create_private_key()
state_serializer = URLSafeTimedSerializer(SECRET_KEY, salt="lti13-state")


def int_to_b64(n):
    b = n.to_bytes((n.bit_length() + 7) // 8, "big")
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


@app.get("/lti/jwks")
def jwks():
    """Public keyset of this tool ("Keyset URL des Tools" in OPAL)."""
    pub = private_key.public_key().public_numbers()
    return jsonify({"keys": [{
        "kty": "RSA", "use": "sig", "alg": "RS256", "kid": "strukturmechanik-1",
        "n": int_to_b64(pub.n), "e": int_to_b64(pub.e),
    }]})


@app.get("/lti/pubkey")
def pubkey():
    """Public key as PEM — zum Einfügen in OPAL (Schlüsseltyp "Schlüssel"),
    wenn OPAL die Keyset-URL nicht erreichen kann (VPN-only Backend)."""
    pem = private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return pem.decode(), 200, {"Content-Type": "text/plain"}


@app.route("/lti/login", methods=["GET", "POST"])
def lti13_login():
    """OIDC third-party login initiation ("Login URL des Tools" in OPAL)."""
    p = request.values
    iss = p.get("iss")
    login_hint = p.get("login_hint")
    if iss != LTI13_ISSUER:
        return f"Unbekannter Issuer: {iss}", 400
    if not login_hint:
        return "login_hint fehlt.", 400
    nonce = secrets.token_urlsafe(16)
    state = state_serializer.dumps({"nonce": nonce})
    params = {
        "scope": "openid",
        "response_type": "id_token",
        "response_mode": "form_post",
        "prompt": "none",
        "client_id": p.get("client_id") or LTI13_CLIENT_ID,
        "redirect_uri": BACKEND_URL + "/lti/launch13",
        "login_hint": login_hint,
        "state": state,
        "nonce": nonce,
    }
    if p.get("lti_message_hint"):
        params["lti_message_hint"] = p.get("lti_message_hint")
    return redirect(LTI13_AUTH_URL + "?" + urllib.parse.urlencode(params))


@app.post("/lti/launch13")
def lti13_launch():
    """OIDC launch callback ("Launch URL des Tools" in OPAL)."""
    id_token = request.form.get("id_token")
    state = request.form.get("state")
    if not id_token or not state:
        return "id_token oder state fehlt.", 400
    try:
        state_data = state_serializer.loads(state, max_age=600)
    except BadSignature:
        return "Ungültiger oder abgelaufener state.", 401
    try:
        signing_key = jwt.PyJWKClient(LTI13_KEYSET_URL).get_signing_key_from_jwt(id_token)
        claims = jwt.decode(
            id_token, signing_key.key, algorithms=["RS256"],
            audience=LTI13_CLIENT_ID or None,
            options={"verify_aud": bool(LTI13_CLIENT_ID)},
            issuer=LTI13_ISSUER,
        )
    except Exception as e:
        return f"id_token-Validierung fehlgeschlagen: {e}", 401
    if claims.get("nonce") != state_data.get("nonce"):
        return "nonce stimmt nicht überein.", 401
    if claims.get("https://purl.imsglobal.org/spec/lti/claim/message_type") != "LtiResourceLinkRequest":
        return "Unerwarteter LTI message type.", 400

    context = claims.get("https://purl.imsglobal.org/spec/lti/claim/context") or {}
    # Assignment&Grade-Service-Endpunkt für späteren Noten-Rückkanal aufheben
    ags = claims.get("https://purl.imsglobal.org/spec/lti-ags/claim/endpoint") or {}
    return finish_launch(
        user_id=claims["sub"],
        context_id=context.get("id"),
        outcome_url=ags.get("lineitem") or ags.get("lineitems"),
    )


# --- LTI 1.1 (Fallback) ------------------------------------------------------

@app.post("/lti/launch")
def lti_launch():
    valid, _ = lti_endpoint.validate_request(
        request.url,
        http_method="POST",
        body=request.get_data(as_text=True),
        headers={"Content-Type": request.headers.get("Content-Type", "")},
    )
    if not valid:
        return "Ungültige LTI-Signatur. Bitte Key/Secret im OPAL-Kursbaustein prüfen.", 401

    user_id = request.form.get("user_id")
    if not user_id:
        return "LTI-Launch ohne user_id.", 400
    return finish_launch(
        user_id=user_id,
        context_id=request.form.get("context_id"),
        outcome_url=request.form.get("lis_outcome_service_url"),
        result_sourcedid=request.form.get("lis_result_sourcedid"),
    )


# --- API for the static site -------------------------------------------------

def current_pseudonym():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    try:
        data = serializer.loads(auth[7:], max_age=TOKEN_MAX_AGE)
        return data.get("sub")
    except BadSignature:
        return None


@app.after_request
def add_cors(resp):
    origin = request.headers.get("Origin", "")
    if origin in ALLOWED_ORIGINS:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return resp


@app.route("/api/<path:_any>", methods=["OPTIONS"])
def cors_preflight(_any):
    return "", 204


@app.post("/api/results")
def post_results():
    pseudonym = current_pseudonym()
    if not pseudonym:
        return jsonify({"error": "unauthorized"}), 401
    payload = request.get_json(silent=True) or {}
    results = payload.get("results") or {}
    if not isinstance(results, dict):
        return jsonify({"error": "bad payload"}), 400

    db = get_db()
    now = time.time()
    for qid, rec in list(results.items())[:500]:
        if not isinstance(rec, dict):
            continue
        try:
            best = float(rec.get("best", 0) or 0)
            qmax = float(rec.get("max", 0) or 0)
            attempts = int(rec.get("attempts", 0) or 0)
        except (TypeError, ValueError):
            continue
        # never lower an already stored best score
        db.execute(
            """INSERT INTO results (pseudonym, qid, best, max, attempts, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(pseudonym, qid) DO UPDATE SET
                 best=MAX(results.best, excluded.best),
                 max=excluded.max,
                 attempts=MAX(results.attempts, excluded.attempts),
                 updated_at=excluded.updated_at""",
            (pseudonym, str(qid)[:200], best, qmax, attempts, now),
        )
    db.commit()
    return jsonify({"ok": True, "stored": len(results)})


@app.get("/api/me")
def me():
    pseudonym = current_pseudonym()
    if not pseudonym:
        return jsonify({"error": "unauthorized"}), 401
    row = get_db().execute(
        "SELECT COALESCE(SUM(best),0) AS total, COALESCE(SUM(max),0) AS max, COUNT(*) AS n "
        "FROM results WHERE pseudonym=?",
        (pseudonym,),
    ).fetchone()
    return jsonify({
        "pseudonym": pseudonym,
        "total_points": row["total"],
        "max_points": row["max"],
        "questions": row["n"],
    })


@app.get("/api/stats")
def stats():
    """Anonymous aggregate per question (no auth needed, no personal data)."""
    rows = get_db().execute(
        "SELECT qid, COUNT(*) AS participants, AVG(best) AS avg_best, "
        "AVG(attempts) AS avg_attempts, MAX(max) AS max "
        "FROM results GROUP BY qid ORDER BY qid"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
