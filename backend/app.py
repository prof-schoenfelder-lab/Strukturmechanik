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
import datetime
import hashlib
import json
import os
import secrets
import sqlite3
import threading
import time
import urllib.parse

import jwt
import requests as http_requests
from cryptography.fernet import Fernet
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
ANSWERS_PATH = os.environ.get("ANSWERS_PATH", os.path.join(os.path.dirname(__file__), "answers.json"))
TOKEN_MAX_AGE = 60 * 60 * 24 * 90  # 90 days

# LTI 1.3 platform data — in OPAL unter "Tool Konfiguration" ablesbar
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:5000")
LTI13_ISSUER = os.environ.get("LTI13_ISSUER", "https://bildungsportal.sachsen.de/opal")
LTI13_CLIENT_ID = os.environ.get("LTI13_CLIENT_ID", "")
LTI13_AUTH_URL = os.environ.get("LTI13_AUTH_URL", "https://bildungsportal.sachsen.de/opal/ltiauth/")
LTI13_KEYSET_URL = os.environ.get("LTI13_KEYSET_URL", "https://bildungsportal.sachsen.de/opal/restapi/lti/keys")
LTI13_DEPLOYMENT_ID = os.environ.get("LTI13_DEPLOYMENT_ID", "1")
LTI13_TOKEN_URL = os.environ.get("LTI13_TOKEN_URL", "https://bildungsportal.sachsen.de/opal/restapi/lti/token")
AGS_ENABLED = os.environ.get("AGS_ENABLED", "1") == "1"
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
            sub_enc TEXT,
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
    # Migration für Bestandsdatenbanken
    try:
        db.execute("ALTER TABLE users ADD COLUMN sub_enc TEXT")
        db.commit()
    except sqlite3.OperationalError:
        pass
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


# Verschlüsselte Ablage der OPAL-Nutzer-ID — nötig NUR für den Noten-Rückkanal
# (AGS verlangt die originale LTI-sub). Nur der Server kann sie entschlüsseln.
fernet = Fernet(base64.urlsafe_b64encode(hashlib.sha256((SECRET_KEY + ":sub-enc").encode()).digest()))


def finish_launch(user_id, context_id, outcome_url=None, result_sourcedid=None):
    """Upsert the pseudonymized user and redirect to the site with a session token."""
    pseudonym = pseudonymize(user_id)
    sub_enc = fernet.encrypt(user_id.encode()).decode() if AGS_ENABLED else None
    db = get_db()
    db.execute(
        """INSERT INTO users (pseudonym, context_id, outcome_url, result_sourcedid, sub_enc, created_at)
           VALUES (?, ?, ?, ?, ?, ?)
           ON CONFLICT(pseudonym) DO UPDATE SET
             context_id=excluded.context_id,
             outcome_url=COALESCE(excluded.outcome_url, users.outcome_url),
             result_sourcedid=COALESCE(excluded.result_sourcedid, users.result_sourcedid),
             sub_enc=COALESCE(excluded.sub_enc, users.sub_enc)""",
        (pseudonym, context_id, outcome_url, result_sourcedid, sub_enc, time.time()),
    )
    db.commit()
    token = serializer.dumps({"sub": pseudonym})
    return redirect(SITE_URL + "#ac_token=" + token)


# --- AGS: Punkte als Bewertung an OPAL zurückmelden ---------------------------

_ags_token = {"value": None, "exp": 0}


def ags_access_token():
    now = time.time()
    if _ags_token["value"] and _ags_token["exp"] > now + 30:
        return _ags_token["value"]
    assertion = jwt.encode(
        {"iss": LTI13_CLIENT_ID, "sub": LTI13_CLIENT_ID, "aud": LTI13_TOKEN_URL,
         "jti": secrets.token_urlsafe(12), "iat": int(now), "exp": int(now) + 300},
        private_key, algorithm="RS256", headers={"kid": "strukturmechanik-1"},
    )
    r = http_requests.post(LTI13_TOKEN_URL, data={
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": assertion,
        "scope": "https://purl.imsglobal.org/spec/lti-ags/scope/score",
    }, timeout=10)
    r.raise_for_status()
    data = r.json()
    _ags_token["value"] = data["access_token"]
    _ags_token["exp"] = now + int(data.get("expires_in", 3600))
    return _ags_token["value"]


def push_score_async(pseudonym):
    """Gesamtpunktzahl des Users als Score an OPAL melden (fire-and-forget)."""
    if not (AGS_ENABLED and LTI13_CLIENT_ID):
        return

    def work():
        try:
            db = sqlite3.connect(DB_PATH)
            db.row_factory = sqlite3.Row
            user = db.execute("SELECT outcome_url, sub_enc FROM users WHERE pseudonym=?",
                              (pseudonym,)).fetchone()
            if not user or not user["outcome_url"] or not user["sub_enc"]:
                return
            total = db.execute("SELECT COALESCE(SUM(best),0) t FROM results WHERE pseudonym=?",
                               (pseudonym,)).fetchone()["t"]
            db.close()
            answers = load_answers()
            score_max = sum(q.get("points", 0) for q in answers.values()) or 100
            sub = fernet.decrypt(user["sub_enc"].encode()).decode()
            lineitem = user["outcome_url"]
            base, _, query = lineitem.partition("?")
            scores_url = base.rstrip("/") + "/scores" + (("?" + query) if query else "")
            http_requests.post(scores_url, json={
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "scoreGiven": total,
                "scoreMaximum": score_max,
                "activityProgress": "Submitted",
                "gradingProgress": "FullyGraded",
                "userId": sub,
            }, headers={
                "Authorization": "Bearer " + ags_access_token(),
                "Content-Type": "application/vnd.ims.lis.v1.score+json",
            }, timeout=10).raise_for_status()
        except Exception as e:
            app.logger.warning("AGS-Score-Push fehlgeschlagen: %s", e)

    threading.Thread(target=work, daemon=True).start()


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
    push_score_async(pseudonym)
    return jsonify({"ok": True, "stored": len(results)})


# --- server-side answer checking ---------------------------------------------

_answers_cache = {"mtime": None, "data": {}}


def load_answers():
    """answers.json (vom MkDocs-Hook erzeugt), mit Reload bei Dateiänderung."""
    try:
        mtime = os.path.getmtime(ANSWERS_PATH)
    except OSError:
        return {}
    if _answers_cache["mtime"] != mtime:
        try:
            with open(ANSWERS_PATH) as f:
                _answers_cache["data"] = json.load(f)
            _answers_cache["mtime"] = mtime
        except (OSError, ValueError):
            return _answers_cache["data"]
    return _answers_cache["data"]


def earned_points(points, attempt_number, attempts_allowed):
    """Gleiche lineare Staffelung wie bisher im Client."""
    if attempt_number <= 1:
        earned = round(points)
    else:
        earned = int(points * ((attempts_allowed - attempt_number + 1) / attempts_allowed))
    return max(0, min(earned, round(points)))


@app.post("/api/check")
def check_answer():
    payload = request.get_json(silent=True) or {}
    qid = str(payload.get("qid") or "")
    q = load_answers().get(qid)
    if not q:
        return jsonify({"error": "unbekannte Frage"}), 404

    attempts_allowed = int(q.get("attempts", 5))
    if "answer" in q:
        try:
            val = float(str(payload.get("value")).replace(",", "."))
        except (TypeError, ValueError):
            return jsonify({"error": "keine Zahl"}), 400
        correct = abs(val - q["answer"]) <= q.get("tolerance", 0)
        solution = q["answer"]
    else:
        selected = payload.get("selected")
        if not isinstance(selected, list):
            return jsonify({"error": "keine Auswahl"}), 400
        correct = sorted(str(s) for s in selected) == sorted(q["correct"])
        solution = q["correct"]

    pseudonym = current_pseudonym()
    if pseudonym:
        db = get_db()
        row = db.execute("SELECT best, attempts FROM results WHERE pseudonym=? AND qid=?",
                         (pseudonym, qid)).fetchone()
        prev_best = row["best"] if row else 0
        attempts = (row["attempts"] if row else 0)
        exhausted = prev_best <= 0 and attempts >= attempts_allowed
        if prev_best <= 0 and not exhausted:
            attempts += 1
        earned = earned_points(q["points"], attempts, attempts_allowed) if (correct and not exhausted) else 0
        best = max(prev_best, earned)
        db.execute(
            """INSERT INTO results (pseudonym, qid, best, max, attempts, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(pseudonym, qid) DO UPDATE SET
                 best=excluded.best, max=excluded.max,
                 attempts=excluded.attempts, updated_at=excluded.updated_at""",
            (pseudonym, qid, best, q["points"], attempts, time.time()),
        )
        db.commit()
        if best > prev_best:
            push_score_async(pseudonym)
        resp = {"authed": True, "correct": correct, "earned": earned, "best": best,
                "attempts": attempts, "attemptsAllowed": attempts_allowed}
        if correct or attempts >= attempts_allowed:
            resp["solution"] = solution
        return jsonify(resp)

    # Gast: keine Speicherung, Versuche zählt der Client (Selbstbetrug erlaubt)
    attempts = min(int(payload.get("attemptsUsed", 0) or 0) + 1, attempts_allowed)
    resp = {"authed": False, "correct": correct,
            "attempts": attempts, "attemptsAllowed": attempts_allowed}
    if correct or attempts >= attempts_allowed:
        resp["solution"] = solution
    return jsonify(resp)


@app.get("/api/results")
def get_results():
    """Full stored state of the current user — for merging into localStorage."""
    pseudonym = current_pseudonym()
    if not pseudonym:
        return jsonify({"error": "unauthorized"}), 401
    rows = get_db().execute(
        "SELECT qid, best, max, attempts FROM results WHERE pseudonym=?", (pseudonym,)
    ).fetchall()
    return jsonify({"results": {r["qid"]: {"best": r["best"], "max": r["max"],
                                           "attempts": r["attempts"]} for r in rows}})


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
