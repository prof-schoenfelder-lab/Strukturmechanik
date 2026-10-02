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
  PCNAMES_PATH                            JSON {ip: "Pool-PC 07"} fürs Dashboard
                                          (default: pc-names.json, auto-reload)
"""

import base64
import datetime
import re
import socket
import hashlib
import json
import math
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
from html import escape

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
DASHBOARD_TOKEN = os.environ.get("DASHBOARD_TOKEN", "")
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
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
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
        CREATE TABLE IF NOT EXISTS help_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            who TEXT NOT NULL,
            page TEXT,
            created_at REAL,
            done_at REAL
        );
        -- Knackpunkt-Bestenliste: bestes gehaltenes Ergebnis je Person und Bauteil
        CREATE TABLE IF NOT EXISTS kp_scores (
            who TEXT NOT NULL,
            teil TEXT NOT NULL,
            prozent REAL NOT NULL,
            entwurf TEXT,
            platz TEXT,
            updated_at REAL,
            PRIMARY KEY (who, teil)
        );
        -- selbst gewählter Spitzname (keine echten Namen)
        CREATE TABLE IF NOT EXISTS kp_namen (
            who TEXT PRIMARY KEY,
            name TEXT NOT NULL
        );
        -- falsche Zahlenwerte, anonym (ohne Pseudonym): welche Fehler passieren?
        CREATE TABLE IF NOT EXISTS wrong_values (
            qid TEXT NOT NULL,
            value REAL NOT NULL,
            created_at REAL NOT NULL
        );
        """
    )
    db.commit()
    # Kurs-Generation: ändert sich beim Semester-Reset; Browser mit alter
    # Generation leeren ihren localStorage automatisch statt Altdaten hochzuladen
    if not db.execute("SELECT value FROM meta WHERE key='generation'").fetchone():
        db.execute("INSERT INTO meta (key, value) VALUES ('generation', ?)",
                   (secrets.token_urlsafe(8),))
        db.commit()
    # Migration für Bestandsdatenbanken
    for stmt in ("ALTER TABLE users ADD COLUMN sub_enc TEXT",
                 "ALTER TABLE users ADD COLUMN name_enc TEXT"):
        try:
            db.execute(stmt)
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


# Akademische Grade/Anreden, die OPAL vor den Namen setzt (Fallback-Pfad,
# wenn nur der zusammengesetzte "name"-Claim kommt)
_TITLES = {"master", "bachelor", "dr.", "dr", "prof.", "prof", "dipl.-ing.",
           "m.eng.", "b.eng.", "m.sc.", "b.sc.", "herr", "frau"}


def strip_titles(name):
    if not name:
        return None
    words = name.split()
    while words and words[0].lower().rstrip(",") in _TITLES:
        words = words[1:]
    return " ".join(words) or None


def finish_launch(user_id, context_id, outcome_url=None, result_sourcedid=None,
                  display_name=None):
    """Upsert the pseudonymized user and redirect to the site with a session token."""
    pseudonym = pseudonymize(user_id)
    sub_enc = fernet.encrypt(user_id.encode()).decode() if AGS_ENABLED else None
    # Klarname (falls der OPAL-Baustein ihn überträgt): verschlüsselt abgelegt,
    # entschlüsselt nur fürs Dashboard — hilft beim Namenlernen im Praktikum.
    name_enc = fernet.encrypt(display_name.encode()).decode() if display_name else None
    db = get_db()
    db.execute(
        """INSERT INTO users (pseudonym, context_id, outcome_url, result_sourcedid,
                              sub_enc, name_enc, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(pseudonym) DO UPDATE SET
             context_id=excluded.context_id,
             outcome_url=COALESCE(excluded.outcome_url, users.outcome_url),
             result_sourcedid=COALESCE(excluded.result_sourcedid, users.result_sourcedid),
             sub_enc=COALESCE(excluded.sub_enc, users.sub_enc),
             name_enc=COALESCE(excluded.name_enc, users.name_enc)""",
        (pseudonym, context_id, outcome_url, result_sourcedid, sub_enc, name_enc,
         time.time()),
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


_ags_lock = threading.Lock()


def push_score_async(pseudonym):
    """Gesamtpunktzahl des Users als Score an OPAL melden (fire-and-forget)."""
    if not (AGS_ENABLED and LTI13_CLIENT_ID):
        return

    def work():
        with _ags_lock:  # nacheinander: die zuletzt gesendete Meldung trägt den aktuellen Stand
            try:
                db = sqlite3.connect(DB_PATH)
                db.row_factory = sqlite3.Row
                user = db.execute("SELECT outcome_url, sub_enc FROM users WHERE pseudonym=?",
                                  (pseudonym,)).fetchone()
                if not user or not user["outcome_url"] or not user["sub_enc"]:
                    return
                an = spiele_an(db)  # Punkte aus ausgeschalteten Spielen zählen nicht
                total = sum(r["best"] for r in db.execute(
                    "SELECT qid, best FROM results WHERE pseudonym=?", (pseudonym,))
                    if an.get(spieltyp(r["qid"]), True))
                answers = aktive_answers(db)
                db.close()
                # max inkl. des möglichen +1-Volltreffer-Bonus je Frage
                score_max = sum(q.get("points", 0) + 1 for q in answers.values()) or 100
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
    # given/family bevorzugen — OPALs "name"-Claim enthält den akademischen
    # Grad ("Master Felix Kaule"), der im Sitzplan stören würde
    name = " ".join(
        s for s in (claims.get("given_name"), claims.get("family_name")) if s) \
        or strip_titles(claims.get("name")) or None
    return finish_launch(
        user_id=claims["sub"],
        context_id=context.get("id"),
        outcome_url=ags.get("lineitem") or ags.get("lineitems"),
        display_name=name,
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
    name = " ".join(
        s for s in (request.form.get("lis_person_name_given"),
                    request.form.get("lis_person_name_family")) if s) \
        or strip_titles(request.form.get("lis_person_name_full")) or None
    return finish_launch(
        user_id=user_id,
        context_id=request.form.get("context_id"),
        outcome_url=request.form.get("lis_outcome_service_url"),
        result_sourcedid=request.form.get("lis_result_sourcedid"),
        display_name=name,
    )


# --- API for the static site -------------------------------------------------

# Zuletzt gesehene Client-Adresse je Pseudonym — bewusst NUR im RAM
# (nach Restart leer, nichts wird gespeichert). Grundlage für die
# Pool-PC-Spalte in der Praktikums-Ansicht des Dashboards.
LAST_SEEN = {}
_HOST_CACHE = {}


def client_ip():
    fwd = request.headers.get("X-Forwarded-For", "")
    return (fwd.split(",")[0].strip() if fwd else request.remote_addr) or ""


# Optionale feste Zuordnung IP -> Anzeigename (z.B. "Pool-PC 07 / Platz 7").
# Datei wird bei Änderung automatisch neu geladen — kein Restart nötig.
PCNAMES_PATH = os.environ.get(
    "PCNAMES_PATH", os.path.join(os.path.dirname(__file__), "pc-names.json"))
_pcnames_cache = {"mtime": None, "data": {}}


def load_pcnames():
    try:
        mtime = os.path.getmtime(PCNAMES_PATH)
    except OSError:
        return {}
    if _pcnames_cache["mtime"] != mtime:
        try:
            with open(PCNAMES_PATH) as f:
                _pcnames_cache["data"] = json.load(f)
            _pcnames_cache["mtime"] = mtime
        except (OSError, ValueError):
            pass
    return _pcnames_cache["data"]


def host_label(ip):
    """Anzeigename eines Pool-PCs: erst pc-names.json, dann Reverse-DNS."""
    if not ip:
        return ""
    name = load_pcnames().get(ip)
    if name:
        return str(name)
    if ip not in _HOST_CACHE:
        label = ip
        try:
            label = socket.gethostbyaddr(ip)[0].split(".")[0]
        except OSError:
            pass
        _HOST_CACHE[ip] = label
    return _HOST_CACHE[ip]


def current_pseudonym():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    try:
        data = serializer.loads(auth[7:], max_age=TOKEN_MAX_AGE)
        pseu = data.get("sub")
        if pseu:
            try:
                LAST_SEEN[pseu] = {"ip": client_ip(), "t": time.time()}
            except Exception:
                pass
        return pseu
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
        # never lower an already stored best score; updated_at nur bei echter
        # Änderung bewegen — sonst würde jeder Sammel-Sync alle Zeilen als
        # "gerade bearbeitet" stempeln (Live-Ansicht im Dashboard!)
        db.execute(
            """INSERT INTO results (pseudonym, qid, best, max, attempts, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(pseudonym, qid) DO UPDATE SET
                 best=MAX(results.best, excluded.best),
                 max=excluded.max,
                 attempts=MAX(results.attempts, excluded.attempts),
                 updated_at=CASE
                   WHEN excluded.best > results.best
                     OR excluded.attempts > results.attempts
                   THEN excluded.updated_at ELSE results.updated_at END""",
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


DIAG_REL = 0.03  # Eingabe passt zu einem Fehlwert bis 3 % Abweichung (mind. Aufgabentoleranz)

# Eingabe = Faktor × Lösung → typische Ursache (gilt für alle Zahlenfragen)
DIAG_FACTORS = [
    (-1, "Der Betrag stimmt, das Vorzeichen nicht: Ist nach dem Betrag gefragt, "
         "oder zeigt die Last in die falsche Richtung?"),
    (1e3, "Genau 1000-mal zu groß: Stimmen die Einheiten? Gefragt ist in mm, N und MPa."),
    (1e-3, "Genau 1000-mal zu klein: Stimmen die Einheiten (mm statt m, MPa statt GPa)?"),
    (1e6, "Genau 1 000 000-mal zu groß: Spannung in Pa statt MPa? Einheitensystem auf mm umstellen."),
    (2, "Genau doppelt so groß wie erwartet: Wirkt die Last doppelt, "
        "oder wurde sie im Symmetriemodell nicht halbiert?"),
    (0.5, "Genau halb so groß wie erwartet: Wurde die Last zu oft geteilt, "
          "oder fehlt ein Teil der Last?"),
    (4, "Genau viermal so groß wie erwartet: Wurde die Last im Viertelmodell durch 4 geteilt?"),
    (0.25, "Nur ein Viertel des erwarteten Werts: Wurde die Last zu oft geteilt, "
           "oder ist das Modell steifer gelagert als vorgegeben?"),
]


def diagnose(q, val):
    """Wahrscheinliche Ursache eines falschen Zahlenwerts, sonst None.
    Zuerst die aufgabenspezifischen Fehlwerte (data-diagnose), dann die Faktoren."""
    for d in q.get("diagnose", []):
        if abs(val - d["value"]) <= max(q.get("tolerance", 0), DIAG_REL * abs(d["value"])):
            return d["hint"]
    if q["answer"]:
        for factor, hint in DIAG_FACTORS:
            if abs(val / (factor * q["answer"]) - 1) <= DIAG_REL:
                return hint
    return None


def earned_points(points, attempt_number, attempts_allowed):
    """Mastery-Prinzip: Lösen zählt voll, egal beim wievielten Versuch.
    +1 Bonuspunkt für den Volltreffer im ersten Versuch."""
    return round(points) + (1 if attempt_number <= 1 else 0)


@app.post("/api/check")
def check_answer():
    payload = request.get_json(silent=True) or {}
    qid = str(payload.get("qid") or "")
    q = load_answers().get(qid)
    if not q:
        return jsonify({"error": "unbekannte Frage"}), 404
    if spieltyp(qid) and not spiele_an(get_db())[spieltyp(qid)]:
        return jsonify({"error": "Spiel nicht freigeschaltet"}), 403

    attempts_allowed = int(q.get("attempts", 5))
    diagnosis = None
    if "answer" in q:
        try:
            val = float(str(payload.get("value")).replace(",", "."))
        except (TypeError, ValueError):
            return jsonify({"error": "keine Zahl"}), 400
        correct = abs(val - q["answer"]) <= q.get("tolerance", 0)
        solution = q["answer"]
        if not correct and math.isfinite(val):
            diagnosis = diagnose(q, val)
            db = get_db()
            db.execute("INSERT INTO wrong_values (qid, value, created_at) VALUES (?, ?, ?)",
                       (qid, val, time.time()))
            db.commit()
    else:
        selected = payload.get("selected")
        if not isinstance(selected, list):
            return jsonify({"error": "keine Auswahl"}), 400
        correct = sorted(str(s) for s in selected) == sorted(q["correct"])
        solution = q["correct"]
        if not correct and "explain" in q and len(selected) == 1:
            # Modell-Detektiv: warum die angeklickte Einstellung in Ordnung ist
            diagnosis = q["explain"].get(str(selected[0]), "Diese Einstellung ist in Ordnung.")

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
            if "aufloesung" in q:
                resp["aufloesung"] = q["aufloesung"]
        if diagnosis:
            resp["diagnosis"] = diagnosis
        return jsonify(resp)

    # Gast: keine Speicherung, Versuche zählt der Client (Selbstbetrug erlaubt)
    attempts = min(int(payload.get("attemptsUsed", 0) or 0) + 1, attempts_allowed)
    resp = {"authed": False, "correct": correct,
            "attempts": attempts, "attemptsAllowed": attempts_allowed}
    if correct or attempts >= attempts_allowed:
        resp["solution"] = solution
        if "aufloesung" in q:
            resp["aufloesung"] = q["aufloesung"]
    if diagnosis:
        resp["diagnosis"] = diagnosis
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


def course_generation():
    row = get_db().execute("SELECT value FROM meta WHERE key='generation'").fetchone()
    return row["value"] if row else "0"


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
        "generation": course_generation(),
        "total_points": row["total"],
        "max_points": row["max"],
        "questions": row["n"],
    })


@app.get("/api/stats")
def stats():
    """Anonymous aggregate per question (no auth needed, no personal data)."""
    rows = get_db().execute(
        "SELECT qid, COUNT(*) AS participants, AVG(best) AS avg_best, "
        "SUM(CASE WHEN best > 0 THEN 1 ELSE 0 END) AS solved, "
        "AVG(attempts) AS avg_attempts, MAX(max) AS max "
        "FROM results GROUP BY qid ORDER BY qid"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


# --- Hilfe-Warteschlange (Mini-Ticketsystem fürs Praktikum) ------------------
# Studierende melden per Button Hilfebedarf an; das Dashboard zeigt die
# Warteschlange in Meldereihenfolge. Identität: Login-Pseudonym, sonst die
# Client-IP (im Pool = Sitzplatz). Tickets verfallen automatisch.

HELP_OPEN_MAX_AGE = 3 * 3600      # offene Tickets nach 3 h automatisch schließen
HELP_DONE_KEEP = 24 * 3600        # erledigte nach einem Tag löschen


def help_enabled(db):
    """Hilfe-Button nur während der Lehrveranstaltung — Schalter im Dashboard."""
    row = db.execute("SELECT value FROM meta WHERE key='help_enabled'").fetchone()
    return bool(row and row["value"] == "1")


def _help_cleanup(db):
    now = time.time()
    db.execute("UPDATE help_requests SET done_at=? WHERE done_at IS NULL AND created_at < ?",
               (now, now - HELP_OPEN_MAX_AGE))
    db.execute("DELETE FROM help_requests WHERE done_at IS NOT NULL AND done_at < ?",
               (now - HELP_DONE_KEEP,))
    db.commit()


def _help_identity():
    pseu = current_pseudonym()
    if pseu:
        return pseu
    ip = client_ip()
    return ("ip:" + ip) if ip else None


@app.get("/api/help")
def help_status():
    who = _help_identity()
    db = get_db()
    if not help_enabled(db):
        return jsonify({"enabled": False, "open": False, "position": None, "queue": 0})
    _help_cleanup(db)
    open_rows = db.execute(
        "SELECT who FROM help_requests WHERE done_at IS NULL ORDER BY created_at").fetchall()
    pos = next((i + 1 for i, r in enumerate(open_rows) if r["who"] == who), None)
    return jsonify({"enabled": True, "open": pos is not None, "position": pos,
                    "queue": len(open_rows)})


@app.post("/api/help")
def help_request():
    payload = request.get_json(silent=True) or {}
    who = _help_identity()
    if not who:
        return jsonify({"error": "keine Identität"}), 400
    db = get_db()
    if not help_enabled(db):
        return jsonify({"enabled": False, "open": False, "position": None, "queue": 0})
    _help_cleanup(db)
    if payload.get("cancel"):
        db.execute("UPDATE help_requests SET done_at=? WHERE who=? AND done_at IS NULL",
                   (time.time(), who))
        db.commit()
    elif not db.execute("SELECT id FROM help_requests WHERE who=? AND done_at IS NULL",
                        (who,)).fetchone():
        db.execute("INSERT INTO help_requests (who, page, created_at) VALUES (?, ?, ?)",
                   (who, str(payload.get("page") or "")[:200], time.time()))
        db.commit()
    return help_status()


@app.get("/dashboard-help-toggle")
def help_toggle():
    if not DASHBOARD_TOKEN or request.args.get("key") != DASHBOARD_TOKEN:
        return "Zugriff nur mit gültigem key-Parameter.", 403
    db = get_db()
    new = "0" if help_enabled(db) else "1"
    db.execute("INSERT OR REPLACE INTO meta (key, value) VALUES ('help_enabled', ?)", (new,))
    if new == "0":
        # beim Ausschalten offene Meldungen mit schließen
        db.execute("UPDATE help_requests SET done_at=? WHERE done_at IS NULL", (time.time(),))
    db.commit()
    return redirect("dashboard?key=" + DASHBOARD_TOKEN)


# --- Spiele freischalten (Schalter im Dashboard) ------------------------------
# Spieltyp = Endung der qid. Ausgeschaltete Spiele verschwinden von der Seite und
# zählen weder im Fragenkatalog noch im Dashboard oder im OPAL-Maximum.
# Knackpunkt (kp) hat keine Fragen: der Schalter zeigt nur das Zwischenspiel am Ende jedes Praktikums.
SPIELE = {"det": "Modell-Detektiv", "hs": "Wo knallt's?", "kp": "Knackpunkt"}


def spieltyp(qid):
    typ = qid.rsplit(":", 1)[-1].rstrip("0123456789")
    return typ if typ in SPIELE else None


def spiele_an(db):
    an = {r[0][len("spiel_"):] for r in
          db.execute("SELECT key FROM meta WHERE key LIKE 'spiel_%' AND value='1'")}
    return {typ: typ in an for typ in SPIELE}


def aktive_answers(db):
    """Fragenkatalog ohne ausgeschaltete Spiele."""
    an = spiele_an(db)
    return {qid: q for qid, q in load_answers().items() if an.get(spieltyp(qid), True)}


@app.get("/api/spiele")
def spiele():
    return jsonify(spiele_an(get_db()))


@app.get("/dashboard-spiel-toggle")
def spiel_toggle():
    if not DASHBOARD_TOKEN or request.args.get("key") != DASHBOARD_TOKEN:
        return "Zugriff nur mit gültigem key-Parameter.", 403
    typ = request.args.get("spiel")
    if typ in SPIELE:
        db = get_db()
        neu = "0" if spiele_an(db)[typ] else "1"
        db.execute("INSERT OR REPLACE INTO meta (key, value) VALUES (?, ?)", ("spiel_" + typ, neu))
        db.commit()
    return redirect("dashboard?key=" + DASHBOARD_TOKEN)


# --- Knackpunkt-Bestenliste ----------------------------------------------------
# Die Kursseite bettet Knackpunkt ein und meldet gehaltene Runden (ohne Live-
# Spannungen). Gespeichert wird das Beste je Person und Bauteil. Angezeigt werden
# nur Spitzname und Sitzplatz, nie Pseudonym oder echter Name. Das Ergebnis
# rechnet der Browser; der Entwurf wird zum Nachprüfen mitgespeichert.
KP_TEIL_RE = re.compile(r"^(f[0-2]|z[1-9]\d{0,4}|b[0-9A-Za-z._-]{1,300})$")
KP_ENTWURF_RE = re.compile(r"^[A-Za-z0-9_-]{1,2000}$")
KP_PLATZ_RE = re.compile(r"^N\d{3} Platz \d+$")
KP_TOP = 10


def kp_name_sauber(v):
    return re.sub(r"[\x00-\x1f\x7f<>&\"']", "", str(v or "")).strip()[:16]


def kp_anzeige(name, platz):
    if name and platz:
        return "%s (%s)" % (name, platz)
    return name or platz or "ohne Namen"


def kp_liste(db, teil, who):
    rows = db.execute(
        "SELECT s.who, s.prozent, s.platz, n.name FROM kp_scores s "
        "LEFT JOIN kp_namen n ON n.who = s.who WHERE s.teil=? "
        "ORDER BY s.prozent DESC, s.updated_at ASC", (teil,)).fetchall()
    liste, ich = [], None
    for i, (w, prozent, platz, name) in enumerate(rows):
        eintrag = {"rang": i + 1, "anzeige": kp_anzeige(name, platz), "prozent": prozent, "ich": w == who}
        if w == who:
            ich = eintrag
        if i < KP_TOP:
            liste.append(eintrag)
    name = db.execute("SELECT name FROM kp_namen WHERE who=?", (who,)).fetchone() if who else None
    platz = host_label(client_ip())
    return jsonify({"an": True, "liste": liste, "ich": ich, "anzahl": len(rows),
                    "name": name[0] if name else "",
                    "platz": platz if KP_PLATZ_RE.match(platz or "") else ""})


@app.route("/api/kp", methods=["GET", "POST"])
def kp_bestenliste():
    db = get_db()
    if not spiele_an(db)["kp"]:
        return jsonify({"an": False})
    who = _help_identity()
    if request.method == "GET":
        teil = request.args.get("teil", "")
    else:
        data = request.get_json(silent=True) or {}
        teil = str(data.get("teil", ""))
        try:
            prozent = round(float(data.get("prozent")), 1)
        except (TypeError, ValueError):
            return jsonify({"error": "prozent fehlt"}), 400
        entwurf = str(data.get("entwurf", ""))
        if not KP_TEIL_RE.match(teil) or not (0 < prozent <= 100) or not KP_ENTWURF_RE.match(entwurf) or not who:
            return jsonify({"error": "ungültig"}), 400
        platz = host_label(client_ip())
        platz = platz if KP_PLATZ_RE.match(platz or "") else None
        alt = db.execute("SELECT prozent FROM kp_scores WHERE who=? AND teil=?", (who, teil)).fetchone()
        if not alt or prozent > alt[0]:
            db.execute("INSERT OR REPLACE INTO kp_scores (who, teil, prozent, entwurf, platz, updated_at) "
                       "VALUES (?, ?, ?, ?, ?, ?)", (who, teil, prozent, entwurf, platz, time.time()))
            db.commit()
    if not KP_TEIL_RE.match(teil):
        return jsonify({"error": "teil fehlt"}), 400
    return kp_liste(db, teil, who)


@app.post("/api/kp/name")
def kp_name_setzen():
    db = get_db()
    if not spiele_an(db)["kp"]:
        return jsonify({"an": False})
    who = _help_identity()
    data = request.get_json(silent=True) or {}
    name, teil = kp_name_sauber(data.get("name")), str(data.get("teil", ""))
    if not who or not KP_TEIL_RE.match(teil):
        return jsonify({"error": "ungültig"}), 400
    if name:
        db.execute("INSERT OR REPLACE INTO kp_namen (who, name) VALUES (?, ?)", (who, name))
    else:
        db.execute("DELETE FROM kp_namen WHERE who=?", (who,))
    db.commit()
    return kp_liste(db, teil, who)


@app.get("/dashboard-kp-name-loeschen")
def kp_name_loeschen():
    if not DASHBOARD_TOKEN or request.args.get("key") != DASHBOARD_TOKEN:
        return "Zugriff nur mit gültigem key-Parameter.", 403
    db = get_db()
    db.execute("DELETE FROM kp_namen WHERE name=?", (request.args.get("name", ""),))
    db.commit()
    return redirect("dashboard?key=" + DASHBOARD_TOKEN)


@app.get("/dashboard-help-done")
def help_done():
    if not DASHBOARD_TOKEN or request.args.get("key") != DASHBOARD_TOKEN:
        return "Zugriff nur mit gültigem key-Parameter.", 403
    db = get_db()
    db.execute("UPDATE help_requests SET done_at=? WHERE id=? AND done_at IS NULL",
               (time.time(), request.args.get("id")))
    db.commit()
    return redirect("dashboard?key=" + DASHBOARD_TOKEN)


def wrong_value_rows(db, answers, since):
    """Häufigste falsche Eingaben seit `since`: gruppiert nach erkannter Ursache,
    ohne Diagnose nach dem auf 2 Stellen gerundeten Wert (Kandidaten für data-diagnose)."""
    groups = {}
    for r in db.execute("SELECT qid, value FROM wrong_values WHERE created_at > ?", (since,)):
        q = answers.get(r["qid"])
        if not q or "answer" not in q:
            continue
        hint = diagnose(q, r["value"])
        groups.setdefault((r["qid"], hint or "", "" if hint else "%.2g" % r["value"]),
                          []).append(r["value"])
    rows = ""
    for (qid, hint, _), vals in sorted(groups.items(), key=lambda kv: -len(kv[1]))[:10]:
        vals.sort()
        rows += ('<tr><td title="%s">%s</td><td class="num">%.4g</td><td class="num">%.4g</td>'
                 '<td class="num">%d</td><td>%s</td></tr>'
                 % (escape(qid), short_qid(qid), vals[len(vals) // 2],
                    answers[qid]["answer"], len(vals), hint or "<em>unbekannt</em>"))
    return rows


# --- Dashboard: Darstellung ---------------------------------------------------
# Aufgaben und Seiten lesbar statt als Pfad; Logos von der öffentlichen Kursseite.
_QTYP = {"q": "Frage", "mc": "Frage", "det": "Fall", "hs": "Runde"}


def short_page(path):
    """'P1_Einfuehrung/03_Selbsttests/Uebung-3' -> 'P1 Übung 3'."""
    parts = [x for x in path.replace("/Strukturmechanik/", "").strip("/").split("/") if x]
    if not parts:
        return ""
    name = parts[-1].replace("Modell_Detektiv", "Modell-Detektiv")
    m = re.match(r"Uebung-?0*(\d+)-?(.*)$", name)
    name = ("Übung %s %s" % m.groups()).strip() if m else name.replace("_", " ")
    return ("%s %s" % (parts[0].split("_")[0], name)) if len(parts) > 1 else name


def short_qid(qid):
    """'.../P1_Einfuehrung/03_Selbsttests/Uebung-1:q0' -> 'P1 Übung 1 · Frage 1'."""
    page, _, q = qid.rpartition(":")
    m = re.match(r"([a-z]+)(\d+)$", q)
    if not page or not m:
        return escape(qid.replace("/Strukturmechanik/", ""))
    return escape("%s · %s %d" % (short_page(page), _QTYP.get(m.group(1), m.group(1)), int(m.group(2)) + 1))


DASH_LOGOS = ("https://prof-schoenfelder-lab.github.io/Strukturmechanik/assets/images/HTWK_white_text.svg",
              "https://prof-schoenfelder-lab.github.io/Strukturmechanik/assets/images/MecSim_weiss.png")
# HTWK-Farben: Dunkelblau, Cyan als Akzent; Ampel für den Status (ohne Gelb)
DASH_CSS = """
:root{--blau:#022541;--cyan:#009EE3;--grau:#2E3639;--silber:#BEC3C6;--bg:#F2F4F6;--line:#E1E5E8;--muted:#68757C;
--ok:#00964E;--ok-bg:#E2F3E9;--warn:#C96A00;--warn-bg:#FDEEDC;--alarm:#E53009;--alarm-bg:#FCE7E2;--idle:#87929A;--idle-bg:#EDF0F2}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--grau);
font:15px/1.45 "Source Sans 3","Source Sans Pro",-apple-system,"Segoe UI",system-ui,sans-serif}
.wrap{max-width:78rem;margin:0 auto;padding:0 1.25rem}
header.top{background:var(--blau);color:#fff}
.topin{display:flex;align-items:center;gap:.8rem 1.6rem;padding:.9rem 1.25rem;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:1rem}
.logo-htwk{height:1.45rem}.logo-ms{height:1.9rem}
.ttl h1{margin:0;font-size:1.35rem;font-weight:700}
.ttl p{margin:0;color:#9DB4C6;font-size:.85rem}
.stamp{margin-left:auto;text-align:right;font-size:.82rem;color:#C6D4DF;line-height:1.5}
.stamp b{color:#fff}
main{padding-top:1.25rem;padding-bottom:1rem}
h2{font-size:1.12rem;color:var(--blau);margin:1.5rem 0 .7rem}
h3{font-size:.95rem;color:var(--blau);margin:0 0 .55rem}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:1rem 1.1rem;margin:0 0 1rem}
.card>h2:first-child{margin-top:0}
.row2{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr);gap:1rem;align-items:start}
.queue.busy{border-color:#F3A58F;box-shadow:inset 4px 0 0 var(--alarm)}
.queue.busy h2{color:var(--alarm)}
p.empty{margin:0;color:var(--muted)}
ul.sw{list-style:none;margin:0;padding:0}
ul.sw li{display:grid;grid-template-columns:1fr auto auto;gap:.6rem;align-items:center;padding:.45rem 0;border-top:1px solid #EEF1F3}
ul.sw li:first-child{border-top:0;padding-top:0}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(8.5rem,1fr));gap:.75rem;margin:0 0 1rem}
.kpi{background:#fff;border:1px solid var(--line);border-radius:12px;padding:.8rem 1rem}
.kpi b{display:block;font-size:1.9rem;line-height:1.1;color:var(--blau);font-weight:700;font-variant-numeric:tabular-nums}
.kpi span{display:block;font-size:.74rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin-top:.25rem}
.kpi.good b{color:var(--ok)}
.kpi.alarm{background:var(--alarm-bg);border-color:#F3A58F}.kpi.alarm b{color:var(--alarm)}
.pill,b.ok,b.done,b.warn,b.alarm,b.idle{display:inline-block;border-radius:999px;padding:.08rem .6rem;
font-size:.78rem;font-weight:600;white-space:nowrap}
b.ok,.pill.on{background:var(--ok-bg);color:var(--ok)}
b.done{background:var(--ok);color:#fff}
b.warn{background:var(--warn-bg);color:var(--warn)}
b.alarm{background:var(--alarm-bg);color:var(--alarm)}
b.idle,.pill.off{background:var(--idle-bg);color:var(--idle)}
a.btn{display:inline-block;padding:.28rem .75rem;border-radius:8px;font-size:.82rem;font-weight:600;text-decoration:none;
border:1px solid var(--line);color:var(--grau);background:#fff;white-space:nowrap}
a.btn:hover{border-color:var(--silber)}
a.btn.go{background:var(--cyan);border-color:var(--cyan);color:#fff}
a.btn.done{background:var(--ok);border-color:var(--ok);color:#fff}
.alert{background:var(--alarm-bg);border:1px solid #F3A58F;box-shadow:inset 4px 0 0 var(--alarm);border-radius:12px;
padding:.8rem 1rem;margin:0 0 1rem}
.alert h3{color:var(--alarm)}
ul.chips{display:flex;flex-wrap:wrap;gap:.45rem;list-style:none;margin:0;padding:0}
ul.chips li{background:#fff;border:1px solid #F3A58F;border-radius:8px;padding:.25rem .65rem;font-size:.88rem}
ul.chips li span{color:var(--alarm);font-weight:600;margin-left:.3rem}
p.spans{font-size:.88rem;color:var(--muted);margin:0 0 1rem}
p.spans b{color:var(--grau)}
.rooms{display:flex;flex-wrap:wrap;gap:1rem;align-items:flex-start}
.room{margin:0}
.roommap{display:grid;grid-template-columns:repeat(2,6.2rem) 1.1rem repeat(2,6.2rem);gap:.35rem}
.seat{border:1px solid var(--line);border-radius:8px;padding:.25rem .4rem;font-size:.72rem;min-height:2.7rem;
background:#FAFBFC;color:#A6AFB5;font-variant-numeric:tabular-nums}
.seat b{display:block;font-size:.76rem;color:inherit}
.seat u{display:block;text-decoration:none;font-weight:600;font-size:.74rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.seat.s-ok{background:var(--ok-bg);border-color:#9AD3B4;color:#006B37}
.seat.s-done{background:var(--ok);border-color:var(--ok);color:#fff}
.seat.s-warn{background:var(--warn-bg);border-color:#F1B878;color:#8F4B00}
.seat.s-alarm{background:var(--alarm-bg);border-color:#F09A84;color:#A32100}
.seat.s-idle{background:var(--idle-bg);border-style:dashed;color:var(--idle)}
p.front{font-size:.74rem;color:var(--muted);margin:.5rem 0 0;text-align:center}
p.legend{display:flex;flex-wrap:wrap;gap:.4rem;margin:0 0 1rem}
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%}
th{font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);font-weight:600;text-align:left;
padding:.4rem .6rem;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:.45rem .6rem;border-bottom:1px solid #EEF1F3;font-size:.9rem;vertical-align:middle}
tr:last-child td{border-bottom:0}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
td.act{text-align:right}
small{color:var(--muted);font-size:.8rem}
tr.lowq td{background:var(--alarm-bg)}
.bar{display:inline-block;width:11rem;height:.55rem;background:#E3E9EE;border-radius:99px;vertical-align:middle;
margin-right:.6rem;overflow:hidden}
.bar span{display:block;height:100%;background:var(--cyan);border-radius:99px}
em{font-style:normal;color:var(--muted);font-size:.85rem}
details.card{padding:0}
details.card summary{cursor:pointer;font-weight:600;color:var(--blau);padding:.85rem 1.1rem;list-style:none}
details.card summary::-webkit-details-marker{display:none}
details.card summary::before{content:"▸";display:inline-block;width:1.1em;color:var(--cyan);transition:transform .15s}
details.card[open] summary::before{transform:rotate(90deg)}
details.card>.tablewrap,details.card>p{margin:0 1.1rem 1rem}
p.note{font-size:.82rem;color:var(--muted)}
footer{font-size:.78rem;color:var(--muted);padding-bottom:2rem}
@media (max-width:760px){
.row2{grid-template-columns:minmax(0,1fr)}
.stamp{margin-left:0;text-align:left}
.kpi b{font-size:1.5rem}
.roommap{grid-template-columns:repeat(2,minmax(2.9rem,1fr)) .7rem repeat(2,minmax(2.9rem,1fr))}
.seat{font-size:.62rem;padding:.2rem .25rem}
.bar{width:6rem}
td,th{padding:.35rem .45rem;font-size:.82rem}
}
"""


@app.get("/dashboard")
def dashboard():
    """Lehrenden-Übersicht: wie viele sind wie weit (aggregiert, pseudonym).
    Zugriff nur mit ?key=<DASHBOARD_TOKEN>."""
    if not DASHBOARD_TOKEN or request.args.get("key") != DASHBOARD_TOKEN:
        return "Zugriff nur mit gültigem key-Parameter (DASHBOARD_TOKEN).", 403

    db = get_db()
    answers = aktive_answers(db)  # ausgeschaltete Spiele zählen nicht mit
    total_q = len(answers) or 1
    praktika = [("P1_Einfuehrung", "Praktikum 1"), ("P2_Geometrie_Randbedingungen", "Praktikum 2"),
                ("P3_Vernetzung", "Praktikum 3"), ("P4_Abstraktionen", "Praktikum 4")]
    q_per_p = {key: sum(1 for qid in answers if "/" + key + "/" in qid) or 1 for key, _ in praktika}

    rows = [r for r in db.execute("SELECT pseudonym, qid, best, attempts FROM results")
            if r["qid"] in answers]
    per_user = {}
    for r in rows:
        u = per_user.setdefault(r["pseudonym"], {"solved": 0, "points": 0, "per_p": {}})
        if r["best"] > 0:
            u["solved"] += 1
            u["points"] += r["best"]
            for key, _ in praktika:
                if "/" + key + "/" in r["qid"]:
                    u["per_p"][key] = u["per_p"].get(key, 0) + 1

    # --- Praktikums-Ansicht: heute Aktive einzeln, mit Pool-PC statt Name ---
    # Pro Person zählt die zuletzt bearbeitete Aufgabe als "ist gerade hier".
    now_ts = time.time()
    midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    today_raw = db.execute(
        "SELECT pseudonym, qid, best, attempts, updated_at FROM results WHERE updated_at > ?",
        (midnight,)).fetchall()
    today_raw = [r for r in today_raw if r["qid"] in answers]
    latest = {}
    for r in today_raw:
        prev = latest.get(r["pseudonym"])
        if prev is None or r["updated_at"] > prev["updated_at"]:
            latest[r["pseudonym"]] = r
    active_now = sum(1 for r in latest.values() if now_ts - r["updated_at"] < 15 * 60)

    # Klarnamen (nur vorhanden, wenn der OPAL-Baustein sie überträgt)
    names = {}
    for u in db.execute("SELECT pseudonym, name_enc FROM users WHERE name_enc IS NOT NULL"):
        try:
            names[u["pseudonym"]] = fernet.decrypt(u["name_enc"].encode()).decode()
        except Exception:
            pass

    entries = []
    for pseu, r in latest.items():
        pk = next((k for k, _ in praktika if "/" + k + "/" in r["qid"]), None)
        psolved = per_user.get(pseu, {"per_p": {}})["per_p"].get(pk, 0)
        ptotal = q_per_p.get(pk, 0)
        allowed = int(answers.get(r["qid"], {}).get("attempts", 5))
        idle = now_ts - r["updated_at"]
        if pk and ptotal and psolved >= ptotal:
            skey, status = "done", '<b class="done">Praktikum fertig</b>'
        elif r["best"] <= 0 and r["attempts"] >= allowed:
            skey, status = "alarm", '<b class="alarm">aufgegeben, Hilfe anbieten</b>'
        elif r["best"] <= 0 and r["attempts"] >= 3:
            skey, status = "warn", '<b class="warn">hängt, %d. Versuch</b>' % r["attempts"]
        elif idle > 15 * 60:
            skey, status = "idle", '<b class="idle">pausiert</b>'
        else:
            skey, status = "ok", '<b class="ok">arbeitet</b>'
        seen = LAST_SEEN.get(pseu) or {}
        pc = host_label(seen.get("ip", "")) or ("&hellip;" + pseu[:6])
        pname = next((nm for k, nm in praktika if k == pk), "")
        entries.append({"pc": pc, "pname": pname, "pk": pk, "solved": psolved,
                        "total": ptotal, "qid": r["qid"], "attempts": r["attempts"],
                        "idle": idle, "status": status, "skey": skey,
                        "name": names.get(pseu, ""),
                        "pshort": pk.split("_")[0] if pk else ""})
    entries.sort(key=lambda e: (-e["solved"], e["idle"]))

    # KPI-Kacheln: die Zahlen, die man im Praktikum ständig braucht.
    # Spannweite bezieht sich aufs dominante Praktikum (typisch läuft eins).
    by_pk = {}
    for e in entries:
        if e["pk"]:
            by_pk.setdefault(e["pk"], []).append(e["solved"])
    kpis = [("%d" % active_now, "gerade aktiv", ""), ("%d" % len(latest), "heute aktiv", "")]
    if by_pk:
        dom = max(by_pk, key=lambda k: len(by_pk[k]))
        vals = sorted(by_pk[dom])
        dom_name = next(nm for k, nm in praktika if k == dom)
        kpis += [("%d/%d" % (vals[-1], q_per_p.get(dom, 0)), "Spitze, " + dom_name, ""),
                 ("%d" % vals[len(vals) // 2], "Median", ""),
                 ("%d" % vals[0], "Schlusslicht", "")]
    need_help = [e for e in entries if e["skey"] in ("warn", "alarm")]
    kpis.append(("%d" % len(need_help), "Hilfe empfohlen", " alarm" if need_help else " good"))
    kpi_html = '<div class="kpis">%s</div>' % "".join(
        '<div class="kpi%s"><b>%s</b><span>%s</span></div>' % (c, v, l) for v, l, c in kpis)

    # Hilfe-Warteschlange (aktiv gemeldete), in Meldereihenfolge
    _help_cleanup(db)
    h_on = help_enabled(db)
    queue_rows = db.execute(
        "SELECT id, who, page, created_at FROM help_requests WHERE done_at IS NULL "
        "ORDER BY created_at").fetchall()
    items = ""
    for i, qr in enumerate(queue_rows, start=1):
        if qr["who"].startswith("ip:"):
            label = host_label(qr["who"][3:]) or qr["who"][3:]
            who_name = ""
        else:
            seen = LAST_SEEN.get(qr["who"]) or {}
            label = host_label(seen.get("ip", "")) or ("…" + qr["who"][:6])
            who_name = names.get(qr["who"], "")
        wait_min = max(0, round((now_ts - qr["created_at"]) / 60))
        items += ('<tr><td class="num"><b>%d.</b></td><td><b>%s</b>%s</td>'
                  '<td>%s<br><small>wartet %d min</small></td>'
                  '<td class="act"><a class="btn done" href="dashboard-help-done?key=%s&amp;id=%d">erledigt</a></td></tr>'
                  % (i, escape(label), ("<br><small>%s</small>" % escape(who_name)) if who_name else "",
                     escape(short_page(qr["page"] or "")), wait_min, DASHBOARD_TOKEN, qr["id"]))
    if items:
        queue_body = ('<div class="tablewrap"><table><tr><th></th><th>Platz</th><th>Seite</th><th></th></tr>%s'
                      '</table></div>' % items)
    else:
        queue_body = ('<p class="empty">%s</p>' % ("Keine offenen Meldungen." if h_on else
                      "Der Hilfe-Button ist aus. Einschalten unter „Schalter auf der Kursseite“."))
    queue_html = ('<section class="card queue%s"><h2>Hilfe-Warteschlange%s</h2>%s</section>'
                  % (" busy" if queue_rows else "", " (%d)" % len(queue_rows) if queue_rows else "", queue_body))

    # Schalter auf der Kursseite: Hilfe-Button und Spiele
    an = spiele_an(db)
    switches = [("Hilfe-Button", h_on, "dashboard-help-toggle?key=%s" % DASHBOARD_TOKEN, "einschalten")]
    switches += [(name, an[typ], "dashboard-spiel-toggle?key=%s&amp;spiel=%s" % (DASHBOARD_TOKEN, typ), "freischalten")
                 for typ, name in SPIELE.items()]
    switch_html = ('<section class="card switches"><h2>Schalter auf der Kursseite</h2><ul class="sw">%s</ul></section>'
                   % "".join('<li><span>%s</span><b class="pill %s">%s</b><a class="btn%s" href="%s">%s</a></li>'
                             % (name, "on" if on else "off", "AN" if on else "AUS", "" if on else " go", url,
                                "ausschalten" if on else verb)
                             for name, on, url, verb in switches))
    # Knackpunkt: selbst gewählte Spitznamen der Bestenliste, anstößige hier entfernen
    kp_namen = [r[0] for r in db.execute("SELECT DISTINCT name FROM kp_namen ORDER BY name")]
    if kp_namen:
        switch_html = switch_html.replace("</ul></section>", "</ul><p>Spitznamen in der Knackpunkt-Bestenliste: %s</p></section>" % ", ".join(
            '%s <a href="dashboard-kp-name-loeschen?key=%s&amp;name=%s">entfernen</a>'
            % (escape(n), DASHBOARD_TOKEN, urllib.parse.quote(n)) for n in kp_namen), 1)

    # Direkt handlungsleitend: wo hingehen?
    help_html = ""
    if need_help:
        help_html = ('<div class="alert"><h3>Hilfe empfohlen</h3><ul class="chips">%s</ul></div>'
                     % "".join('<li><b>%s</b>%s <span>%s</span></li>'
                               % (e["pc"], (" " + escape(e["name"])) if e["name"] else "",
                                  "aufgegeben" if e["skey"] == "alarm" else "%d. Versuch" % e["attempts"])
                               for e in need_help[:10]))

    # Arbeiten Leute in unterschiedlichen Praktika (Vorzieher/Nachzügler),
    # bekommt jedes aktive Praktikum seine eigene Spannweiten-Zeile.
    multi_html = ""
    if len(by_pk) > 1:
        parts = []
        for k in sorted(by_pk, key=lambda k: -len(by_pk[k])):
            v = sorted(by_pk[k])
            nm = next(nm for kk, nm in praktika if kk == k)
            if len(v) == 1:
                parts.append("%s: <b>%d/%d</b> (1 Person)" % (nm, v[0], q_per_p.get(k, 0)))
            else:
                parts.append("%s: Spitze <b>%d/%d</b> · Median <b>%d</b> · Schlusslicht <b>%d</b> (%d Personen)"
                             % (nm, v[-1], q_per_p.get(k, 0), v[len(v) // 2], v[0], len(v)))
        multi_html = '<p class="spans">Parallel aktiv: ' + " &nbsp;|&nbsp; ".join(parts) + "</p>"

    # Brennpunkt heute: an welcher Aufgabe arbeiten/hingen heute die meisten?
    # Lohnt sich für eine Ansage an alle statt zehn Einzelerklärungen.
    hot = {}
    for r in today_raw:
        d = hot.setdefault(r["qid"], {"n": 0, "solved": 0, "att": 0})
        d["n"] += 1
        d["att"] += r["attempts"]
        if r["best"] > 0:
            d["solved"] += 1
    hot_rows = "".join(
        '<tr><td title="%s">%s</td><td class="num">%d</td><td class="num">%d</td><td class="num">%.1f</td></tr>'
        % (escape(qid), short_qid(qid), d["n"], d["solved"], d["att"] / d["n"])
        for qid, d in sorted(hot.items(), key=lambda kv: -kv[1]["n"])[:8])
    hot_html = ""
    if hot_rows:
        hot_html = ('<div class="card"><h3>Brennpunkt heute: meistbearbeitete Aufgaben</h3>'
                    '<div class="tablewrap"><table><tr><th>Aufgabe</th><th>Personen heute</th>'
                    '<th>davon gelöst</th><th>ø Versuche</th></tr>%s</table></div></div>' % hot_rows)

    # Häufige Fehlwerte heute: welcher Fehler passiert gerade vielen? (Ansage an alle)
    wrong_head = ('<tr><th>Aufgabe</th><th>typische Eingabe</th><th>Lösung</th>'
                  '<th>Anzahl</th><th>erkannte Ursache</th></tr>')
    wrong_today = wrong_value_rows(db, answers, midnight)
    wrong_html = ""
    if wrong_today:
        wrong_html = ('<div class="card"><h3>Häufige Fehlwerte heute</h3><div class="tablewrap"><table>%s%s'
                      '</table></div></div>' % (wrong_head, wrong_today))

    # Raumkarte: Plätze örtlich wie im Pool (vorn unten; pro Reihe zwei
    # Zweiergruppen mit Mittelgang; Platz 1 vorne rechts, dann 2/3/4 nach
    # links, nächste Reihe dahinter zählt weiter).
    ROOMS = {"N102": 32, "N103": 20, "N104": 16}
    seat_of = {}
    for e in entries:
        m = re.match(r"^(N\d{3}) Platz (\d+)$", e["pc"])
        if m and m.group(1) in ROOMS:
            seat_of[(m.group(1), int(m.group(2)))] = e
    map_html = ""
    for room in sorted(ROOMS):
        if not any(k[0] == room for k in seat_of):
            continue
        total_seats = ROOMS[room]
        n_rows = (total_seats + 3) // 4
        cells = ""
        for row in range(n_rows, 0, -1):          # hinterste Reihe zuerst
            base = (row - 1) * 4
            for offset in (4, 3, 0, 2, 1):        # links: 4,3 · Gang · rechts: 2,1
                if offset == 0:
                    cells += '<i class="aisle"></i>'
                    continue
                seat = base + offset
                if seat > total_seats:
                    cells += '<i class="aisle"></i>'
                    continue
                e = seat_of.get((room, seat))
                if e:
                    cells += ('<span class="seat s-%s" title="%s%s · zuletzt %s · vor %d min">'
                              '<b>%d</b><u>%s</u>%s%d/%d</span>'
                              % (e["skey"],
                                 escape(e["name"]) + " · " if e["name"] else "", e["pname"],
                                 escape(short_qid(e["qid"])), max(0, round(e["idle"] / 60)),
                                 seat, escape(e["name"]) or "&nbsp;",
                                 ("%s " % e["pshort"]) if e["pshort"] else "",
                                 e["solved"], e["total"]))
                else:
                    cells += '<span class="seat"><b>%d</b></span>' % seat
        map_html += ('<div class="card room"><h3>Raum %s</h3><div class="roommap">%s</div>'
                     '<p class="front">▲ vorne, Tafel</p></div>' % (room, cells))
    if map_html:
        map_html = ('<div class="rooms">%s</div><p class="legend"><b class="ok">arbeitet</b>'
                    '<b class="done">Praktikum fertig</b><b class="warn">hängt</b><b class="alarm">aufgegeben</b>'
                    '<b class="idle">pausiert</b></p>' % map_html)

    person_rows = "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td class="num">%d/%d</td><td title="%s">%s</td>'
        '<td class="num">%d</td><td class="num">vor %d min</td><td>%s</td></tr>'
        % (e["pc"], escape(e["name"]), e["pname"], e["solved"], e["total"],
           escape(e["qid"]), short_qid(e["qid"]), e["attempts"],
           max(0, round(e["idle"] / 60)), e["status"])
        for e in entries[:60])
    live_html = (
        '<div class="row2">' + queue_html + switch_html + "</div>"
        + "<h2>Praktikum heute: wer ist wie weit?</h2>"
        + kpi_html
        + help_html
        + multi_html
        + map_html
        + hot_html
        + wrong_html
        + ('<div class="card"><h3>Alle heute Aktiven</h3><div class="tablewrap"><table>'
           "<tr><th>Platz</th><th>Name</th><th>Praktikum</th><th>gelöst</th><th>zuletzt an</th>"
           "<th>Versuche</th><th>zuletzt aktiv</th><th>Status</th></tr>%s</table></div></div>"
           % person_rows
           if person_rows else '<div class="card"><p class="empty">Heute war noch niemand aktiv.</p></div>'))

    n = len(per_user)
    buckets = [("noch nichts gelöst", 0, 0), ("bis 25 %", 0.0001, 0.25), ("bis 50 %", 0.25, 0.5),
               ("bis 75 %", 0.5, 0.75), ("bis 99 %", 0.75, 0.9999), ("alles gelöst", 0.9999, 10)]
    dist = []
    for label, lo, hi in buckets:
        c = sum(1 for u in per_user.values() if lo <= u["solved"] / total_q <= hi)
        dist.append((label, c))

    def bar(count):
        pct = int(100 * count / n) if n else 0
        return ('<span class="bar"><span style="width:%d%%"></span></span><em>%d (%d %%)</em>'
                % (max(pct, 1) if count else 0, count, pct))

    p_rows = ""
    for key, name in praktika:
        started = sum(1 for u in per_user.values() if u["per_p"].get(key, 0) > 0)
        done = sum(1 for u in per_user.values() if u["per_p"].get(key, 0) >= q_per_p[key])
        p_rows += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (name, bar(started), bar(done))

    # Pro Aufgabe: Lösequote und Volltreffer-Quote (= im 1. Versuch gelöst,
    # erkennbar am Bonuspunkt) zeigen, welche Aufgaben zu schwer/leicht sind.
    qagg = {}
    for r in rows:
        d = qagg.setdefault(r["qid"], {"n": 0, "solved": 0, "att": 0, "first": 0})
        d["n"] += 1
        d["att"] += r["attempts"]
        if r["best"] > 0:
            d["solved"] += 1
            if r["best"] > answers.get(r["qid"], {}).get("points", 1):
                d["first"] += 1
    q_rows = ""
    for qid in sorted(qagg):
        d = qagg[qid]
        quote = 100 * d["solved"] / d["n"] if d["n"] else 0
        cls = ' class="lowq"' if d["n"] >= 5 and quote < 40 else ""
        q_rows += ('<tr%s><td title="%s">%s</td><td class="num">%d/%d</td><td class="num">%d %%</td>'
                   '<td class="num">%.1f</td><td class="num">%s</td></tr>'
                   % (cls, escape(qid), short_qid(qid), d["solved"], d["n"],
                      quote, d["att"] / d["n"] if d["n"] else 0,
                      "%d %%" % (100 * d["first"] / d["solved"]) if d["solved"] else ""))

    dist_rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (label, bar(c)) for label, c in dist)
    html = """<!doctype html><html lang="de"><meta charset="utf-8">
<meta http-equiv="refresh" content="30">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FEM-Kurs Dashboard</title>
<style>""" + DASH_CSS + """</style>
<header class="top"><div class="wrap topin">
<div class="brand"><img src="%s" alt="HTWK Leipzig" class="logo-htwk"><img src="%s" alt="MecSim" class="logo-ms"></div>
<div class="ttl"><h1>FEM-Kurs Dashboard</h1><p>Angewandte FEM in der Strukturmechanik</p></div>
<div class="stamp"><b>%d</b> Teilnehmende mit Login · <b>%d</b> Aufgaben im Katalog<br>Stand %s · aktualisiert sich alle 30 s</div>
</div></header>
<main class="wrap">
%s
<h2>Kurs gesamt</h2>
<details class="card" open><summary>Wie weit ist der Kurs? Anteil gelöster Aufgaben pro Person</summary>
<div class="tablewrap"><table>%s</table></div></details>
<details class="card"><summary>Pro Praktikum: begonnen und komplett</summary>
<div class="tablewrap"><table><tr><th></th><th>mind. 1 Aufgabe gelöst</th><th>komplett gelöst</th></tr>%s</table></div></details>
<details class="card"><summary>Pro Aufgabe: Lösequote, ø Versuche, Volltreffer im 1. Versuch</summary>
<div class="tablewrap"><table><tr><th>Aufgabe</th><th>gelöst</th><th>Lösequote</th><th>ø Versuche</th><th>Volltreffer</th></tr>%s</table></div>
<p class="note">Rot hinterlegt: Lösequote unter 40 %% (ab 5 Personen), Kandidaten zum Nachschärfen.</p></details>
<details class="card"><summary>Häufige Fehlwerte, gesamt und anonym</summary>
<div class="tablewrap"><table>%s%s</table></div>
<p class="note">Ohne erkannte Ursache: Kandidaten für neue data-diagnose-Einträge in der Übungsseite.</p></details>
</main>
<footer class="wrap">PC-Namen stehen nur im Arbeitsspeicher, Namen nur hinter dem Schlüssel. Nicht am Beamer zeigen.</footer>
</html>""" % (DASH_LOGOS[0], DASH_LOGOS[1], n, len(answers), datetime.datetime.now().strftime("%d.%m.%Y, %H:%M"),
              live_html, dist_rows, p_rows, q_rows, wrong_head,
              wrong_value_rows(db, answers, 0)
              or '<tr><td colspan="5"><p class="empty">Noch keine falschen Eingaben.</p></td></tr>')
    return html


@app.get("/api/questions")
def questions():
    """Public question catalog: qid -> max points/attempts (keine Antworten!).
    Grundlage für die Fortschrittsanzeige (wie viele Fragen gibt es je Praktikum)."""
    out = {}
    for qid, q in aktive_answers(get_db()).items():
        out[qid] = {"points": q.get("points", 1), "attempts": q.get("attempts", 5)}
    return jsonify(out)


init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
