"""Self-contained end-to-end test: starts the backend with a mocked OPAL
platform (local JWKS server + signed id_tokens) and tests LTI 1.3, LTI 1.1
and the results API.

Run:  .venv/bin/python test_launch.py
"""

import http.server
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse

import jwt
import requests
from cryptography.hazmat.primitives.asymmetric import rsa
from requests_oauthlib import OAuth1

HERE = os.path.dirname(os.path.abspath(__file__))
BACKEND = "http://127.0.0.1:5099"
PLATFORM = "http://127.0.0.1:5098"
CLIENT_ID = "test-client-id"
KEY = "strukturmechanik"
SECRET = "change-me"

failures = []


def check(name, cond, info=""):
    print(("PASS" if cond else "FAIL") + f"  {name}  {info}")
    if not cond:
        failures.append(name)


# --- mock OPAL platform (serves its JWKS) ------------------------------------

platform_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
platform_jwk = json.loads(jwt.algorithms.RSAAlgorithm.to_jwk(platform_key.public_key()))
platform_jwk.update({"kid": "opal-key-1", "alg": "RS256", "use": "sig"})


ags_received = []  # von der Mock-Plattform empfangene Score-Posts


class JWKSHandler(http.server.BaseHTTPRequestHandler):
    def _json(self, obj, status=200):
        body = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._json({"keys": [platform_jwk]})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode()
        if self.path == "/token":
            form = dict(urllib.parse.parse_qsl(raw))
            claims = jwt.decode(form.get("client_assertion", ""), options={"verify_signature": False})
            if claims.get("iss") != CLIENT_ID:
                return self._json({"error": "bad assertion"}, 400)
            return self._json({"access_token": "mock-ags-token", "expires_in": 3600})
        if self.path.startswith("/lineitem/7/scores"):
            if self.headers.get("Authorization") != "Bearer mock-ags-token":
                return self._json({"error": "unauthorized"}, 401)
            ags_received.append(json.loads(raw))
            return self._json({"ok": True})
        return self._json({"error": "not found"}, 404)

    def log_message(self, *a):
        pass


def make_id_token(nonce, sub="opal-user-13", override=None):
    now = int(time.time())
    claims = {
        "iss": PLATFORM,
        "aud": CLIENT_ID,
        "sub": sub,
        "iat": now,
        "exp": now + 300,
        "nonce": nonce,
        "https://purl.imsglobal.org/spec/lti/claim/message_type": "LtiResourceLinkRequest",
        "https://purl.imsglobal.org/spec/lti/claim/version": "1.3.0",
        "https://purl.imsglobal.org/spec/lti/claim/deployment_id": "1",
        "https://purl.imsglobal.org/spec/lti/claim/context": {"id": "kurs-fem-2026"},
        "https://purl.imsglobal.org/spec/lti-ags/claim/endpoint": {
            "lineitem": PLATFORM + "/lineitem/7",
        },
    }
    if override:
        claims.update(override)
    return jwt.encode(claims, platform_key, algorithm="RS256", headers={"kid": "opal-key-1"})


def main():
    jwks_srv = http.server.HTTPServer(("127.0.0.1", 5098), JWKSHandler)
    threading.Thread(target=jwks_srv.serve_forever, daemon=True).start()

    tmp = tempfile.mkdtemp()
    with open(os.path.join(tmp, "answers.json"), "w") as f:
        json.dump({
            "/T/Ueb:q0": {"answer": 7.378, "tolerance": 0.1, "points": 5, "attempts": 5,
                          "diagnose": [{"value": 7.747, "hint": "Material zugeordnet?", "knoten": "koerper.material"}]},
            "/T/Ueb:mc0": {"correct": ["a", "c"], "points": 4, "attempts": 3},
            "/T/Det:det0": {"correct": ["balken.material"], "points": 5, "attempts": 3,
                            "explain": {"netz.groesse": "Richtig: 5 mm."},
                            "aufloesung": "Gefunden: Material nicht zugeordnet."},
        }, f)
    env = dict(os.environ,
               ANSWERS_PATH=os.path.join(tmp, "answers.json"),
               DB_PATH=os.path.join(tmp, "test.db"),
               PRIVATE_KEY_PATH=os.path.join(tmp, "key.pem"),
               BACKEND_URL=BACKEND,
               LTI13_ISSUER=PLATFORM,
               LTI13_AUTH_URL=PLATFORM + "/auth",
               LTI13_KEYSET_URL=PLATFORM + "/keys",
               LTI13_TOKEN_URL=PLATFORM + "/token",
               LTI13_CLIENT_ID=CLIENT_ID,
               LTI_CONSUMER_KEY=KEY,
               LTI_CONSUMER_SECRET=SECRET,
               DASHBOARD_TOKEN="test-dashboard-key",
               PCNAMES_PATH=os.path.join(tmp, "pc-names.json"),
               VAPID_PATH=os.path.join(tmp, "vapid.pem"),
               HILFE_TEST="1",
               FLASK_RUN_PORT="5099")
    with open(os.path.join(tmp, "pc-names.json"), "w") as f:
        json.dump({"10.0.0.7": "N103 Platz 7", "10.0.0.8": "N103 Platz 8"}, f)
    server = subprocess.Popen(
        [sys.executable, "-c",
         "import app; app.app.run(host='127.0.0.1', port=5099)"],
        cwd=HERE, env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(50):
            try:
                requests.get(BACKEND + "/api/stats", timeout=1)
                break
            except requests.ConnectionError:
                time.sleep(0.2)

        # ---- LTI 1.3 -----------------------------------------------------
        # 1. OIDC login initiation
        r = requests.get(BACKEND + "/lti/login", params={
            "iss": PLATFORM, "login_hint": "hint-1", "client_id": CLIENT_ID,
            "target_link_uri": BACKEND + "/lti/launch13",
        }, allow_redirects=False)
        check("1.3 login redirects to platform", r.status_code == 302
              and r.headers["Location"].startswith(PLATFORM + "/auth?"))
        q = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(r.headers["Location"]).query))
        check("1.3 login passes nonce+state", bool(q.get("nonce")) and bool(q.get("state")))
        check("1.3 redirect_uri correct", q.get("redirect_uri") == BACKEND + "/lti/launch13")

        # 2. platform posts signed id_token back
        r = requests.post(BACKEND + "/lti/launch13",
                          data={"id_token": make_id_token(q["nonce"]), "state": q["state"]},
                          allow_redirects=False)
        check("1.3 launch accepted", r.status_code == 302, f"status={r.status_code} {r.text[:200]}")
        frag = urllib.parse.urlparse(r.headers.get("Location", "")).fragment
        token13 = dict(urllib.parse.parse_qsl(frag)).get("ac_token")
        check("1.3 token issued", bool(token13))

        # 3. wrong nonce rejected
        r = requests.post(BACKEND + "/lti/launch13",
                          data={"id_token": make_id_token("wrong-nonce"), "state": q["state"]},
                          allow_redirects=False)
        check("1.3 wrong nonce rejected", r.status_code == 401)

        # 4. token signed by foreign key rejected
        foreign = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        bad = jwt.encode({"iss": PLATFORM, "aud": CLIENT_ID, "sub": "x",
                          "nonce": q["nonce"], "exp": int(time.time()) + 300},
                         foreign, algorithm="RS256", headers={"kid": "opal-key-1"})
        r = requests.post(BACKEND + "/lti/launch13",
                          data={"id_token": bad, "state": q["state"]}, allow_redirects=False)
        check("1.3 foreign signature rejected", r.status_code == 401)

        # 5. tool JWKS is served
        r = requests.get(BACKEND + "/lti/jwks")
        check("tool jwks served", r.status_code == 200 and r.json()["keys"][0]["kty"] == "RSA")

        # ---- LTI 1.1 (fallback) ------------------------------------------
        params = {"lti_message_type": "basic-lti-launch-request", "lti_version": "LTI-1p0",
                  "resource_link_id": "el-1", "user_id": "opal-user-11", "context_id": "kurs"}
        r = requests.post(BACKEND + "/lti/launch", data=params,
                          auth=OAuth1(KEY, SECRET, signature_type="body"), allow_redirects=False)
        check("1.1 launch accepted", r.status_code == 302, f"status={r.status_code}")
        r = requests.post(BACKEND + "/lti/launch", data=params,
                          auth=OAuth1(KEY, "wrong", signature_type="body"), allow_redirects=False)
        check("1.1 bad signature rejected", r.status_code == 401)

        # ---- results API (with the 1.3 token) ----------------------------
        headers = {"Authorization": f"Bearer {token13}"}
        results = {"/P1/Uebung-1:q0": {"best": 5, "max": 5, "attempts": 1},
                   "/P1/Uebung-1:q1": {"best": 3, "max": 5, "attempts": 3}}
        r = requests.post(BACKEND + "/api/results", json={"results": results}, headers=headers)
        check("results stored", r.status_code == 200 and r.json().get("ok"), r.text[:100])
        r = requests.post(BACKEND + "/api/results", headers=headers,
                          json={"results": {"/P1/Uebung-1:q0": {"best": 1, "max": 5, "attempts": 2}}})
        check("downgrade request ok", r.status_code == 200)
        r = requests.get(BACKEND + "/api/results", headers=headers)
        pulled = r.json().get("results", {})
        check("results pullable for merge",
              pulled.get("/P1/Uebung-1:q0", {}).get("best") == 5 and len(pulled) == 2, str(pulled))
        me = requests.get(BACKEND + "/api/me", headers=headers).json()
        check("me total = 8 (best kept)", me.get("total_points") == 8, str(me))
        check("me is pseudonymous", "opal-user" not in str(me))
        check("no token -> 401", requests.get(BACKEND + "/api/me").status_code == 401)
        r = requests.get(BACKEND + "/api/stats")
        check("stats anonymous + solved count", r.status_code == 200 and "opal-user" not in r.text
              and all("solved" in row for row in r.json()))
        r = requests.get(BACKEND + "/api/questions")
        check("question catalog public, no answers",
              r.status_code == 200 and "/T/Ueb:q0" in r.json() and "answer" not in r.text)
        check("dashboard needs key", requests.get(BACKEND + "/dashboard").status_code == 403)
        r = requests.get(BACKEND + "/dashboard", params={"key": "test-dashboard-key"})
        check("dashboard renders overview",
              r.status_code == 200 and "Teilnehmende" in r.text and "Praktikum 1" in r.text
              and "opal-user" not in r.text)

        # ---- server-side checking (/api/check) ---------------------------
        # guest: correct within tolerance, no points but solution on success
        r = requests.post(BACKEND + "/api/check",
                          json={"qid": "/T/Ueb:q0", "value": "7,4", "attemptsUsed": 0}).json()
        check("guest numeric correct", r["correct"] and not r["authed"] and "earned" not in r, str(r))
        r = requests.post(BACKEND + "/api/check",
                          json={"qid": "/T/Ueb:q0", "value": 9.9, "attemptsUsed": 0}).json()
        check("guest wrong, no solution yet", not r["correct"] and "solution" not in r
              and "diagnosis" not in r, str(r))

        # Diagnose: aufgabenspezifischer Fehlwert vor den typischen Faktoren
        def diag(value):
            return requests.post(BACKEND + "/api/check", json={
                "qid": "/T/Ueb:q0", "value": value, "attemptsUsed": 0}).json().get("diagnosis", "")
        check("diagnosis: data-diagnose-Wert", diag("7,75") == "Material zugeordnet?")
        check("diagnosis: Faktor 1000 (Einheit)", "1000-mal zu klein" in diag(0.007378))
        check("diagnosis: doppelte Last", "doppelt" in diag(14.8))
        check("diagnosis: Vorzeichen", "Vorzeichen" in diag(-7.378))

        def knoten(value):
            return requests.post(BACKEND + "/api/check", json={
                "qid": "/T/Ueb:q0", "value": value, "attemptsUsed": 0}).json().get("diagnosisKnoten")
        check("diagnosis: Baumknoten aus data-diagnose", knoten(7.75) == "koerper.material")
        check("diagnosis: Baumknoten Einheiten bei Faktor 1000", knoten(0.007378) == "einheiten")
        check("diagnosis: Baumknoten Last bei Vorzeichen", knoten(-7.378) == "last")
        check("diagnosis: ohne Ursache kein Knoten", knoten(9.9) is None)
        for v in (7.75, 7.75, 7.76, 0.007378, 9.9, 9.8):
            requests.post(BACKEND + "/api/check", json={"qid": "/T/Ueb:q0", "value": v, "attemptsUsed": 0})
        r = requests.post(BACKEND + "/api/check", json={"qid": "/T/Ueb:q0", "value": 9.7, "attemptsUsed": 0}).json()
        v = r.get("verteilung") or {}
        check("diagnosis: Verteilung je Baumeintrag ab 10 Fehlwerten",
              v.get("n", 0) >= 10 and v["anteile"].get("koerper.material", 0) > 0
              and abs(sum(v["anteile"].values()) - 1) < 0.05, str(v))
        # Spiele sind aus, bis sie im Dashboard freigeschaltet werden
        check("spiele standardmäßig aus",
              requests.get(BACKEND + "/api/spiele").json() == {"det": False, "hs": False, "kp": False})
        check("ausgeschaltetes Spiel fehlt im Katalog",
              "/T/Det:det0" not in requests.get(BACKEND + "/api/questions").json())
        check("ausgeschaltetes Spiel nicht prüfbar", requests.post(BACKEND + "/api/check", json={
            "qid": "/T/Det:det0", "selected": ["netz.groesse"]}).status_code == 403)
        r = requests.get(BACKEND + "/dashboard-spiel-toggle", allow_redirects=False,
                         params={"key": "test-dashboard-key", "spiel": "det"})
        check("dashboard schaltet Spiel frei",
              r.status_code == 302 and requests.get(BACKEND + "/api/spiele").json()["det"]
              and "/T/Det:det0" in requests.get(BACKEND + "/api/questions").json())

        # Modell-Detektiv: Begründung je Klick, Auflösung erst bei Treffer
        def det(row, used=0):
            return requests.post(BACKEND + "/api/check", json={
                "qid": "/T/Det:det0", "selected": [row], "attemptsUsed": used}).json()
        r = det("netz.groesse")
        check("detektiv: falscher Klick begründet, keine Auflösung",
              not r["correct"] and r.get("diagnosis") == "Richtig: 5 mm."
              and "aufloesung" not in r and "solution" not in r, str(r))
        r = det("geometrie.koerper")
        check("detektiv: Zeile ohne Begründung", r.get("diagnosis") == "Diese Einstellung ist in Ordnung.", str(r))
        r = det("balken.material")
        check("detektiv: Treffer mit Auflösung",
              r["correct"] and r.get("aufloesung") == "Gefunden: Material nicht zugeordnet.", str(r))
        r = det("netz.groesse", used=2)
        check("detektiv: letzter Versuch zeigt Lösung und Auflösung",
              r.get("solution") == ["balken.material"] and "aufloesung" in r, str(r))

        # Knackpunkt-Bestenliste: nur mit Schalter, Bestes je Person, Spitzname plus Platz
        KP = BACKEND + "/api/kp"
        TEIL = "b2u6.abc.wL006.Tt5160u"
        p7, p8 = {"X-Forwarded-For": "10.0.0.7"}, {"X-Forwarded-For": "10.0.0.8"}
        check("kp: aus, solange nicht freigeschaltet", requests.get(KP, params={"teil": TEIL}).json() == {"an": False})
        requests.get(BACKEND + "/dashboard-spiel-toggle", params={"key": "test-dashboard-key", "spiel": "kp"})
        r = requests.post(KP, headers=p7, json={"teil": TEIL, "prozent": 41.26, "entwurf": "AB_-"}).json()
        check("kp: Platz ohne Namen", r["liste"] == [{"rang": 1, "anzeige": "N103 Platz 7", "prozent": 41.3, "ich": True}]
              and r["platz"] == "N103 Platz 7", str(r))
        r = requests.post(KP, headers=p7, json={"teil": TEIL, "prozent": 30, "entwurf": "AB"}).json()
        check("kp: schlechteres Ergebnis überschreibt nicht", r["ich"]["prozent"] == 41.3, str(r))
        r = requests.post(KP + "/name", headers=p7, json={"teil": TEIL, "name": " <b>Ada</b>12345678901234 "}).json()
        check("kp: Spitzname gesäubert, gekürzt, mit Platz", r["liste"][0]["anzeige"] == "bAda/b1234567890 (N103 Platz 7)"
              and r["name"] == "bAda/b1234567890", str(r))
        r = requests.post(KP, headers=p8, json={"teil": TEIL, "prozent": 55, "entwurf": "AB"}).json()
        check("kp: Rangfolge nach Prozent, eigener Rang", [e["anzeige"] for e in r["liste"]] == ["N103 Platz 8", "bAda/b1234567890 (N103 Platz 7)"]
              and r["ich"]["rang"] == 1 and r["anzahl"] == 2, str(r))
        r = requests.post(KP, headers={"X-Forwarded-For": "10.9.9.9"}, json={"teil": TEIL, "prozent": 10, "entwurf": "AB"}).json()
        check("kp: ohne Platz und Namen", r["ich"]["anzeige"] == "ohne Namen" and r["platz"] == "", str(r))
        r = requests.post(KP, headers=headers, json={"teil": TEIL, "prozent": 20, "entwurf": "AB"}).json()
        check("kp: eingeloggt ohne Platz im Pool", r["ich"]["anzeige"] == "ohne Namen" and r["ich"]["rang"] == 3, str(r))
        for bad in ({"teil": "x", "prozent": 5, "entwurf": "A"}, {"teil": TEIL, "prozent": 101, "entwurf": "A"},
                    {"teil": TEIL, "prozent": 5, "entwurf": "<script>"}):
            check("kp: ungültig abgelehnt %s" % bad, requests.post(KP, json=bad).status_code == 400)
        requests.post(KP, headers=p7, json={"teil": "f0", "prozent": 12, "entwurf": "AB",
                                            "titel": "Kragarm (Übung 2)", "seite": "/Strukturmechanik/P1/Uebung-2/"})
        r = requests.get(KP + "/meine", headers=p7).json()
        check("kp: Mein Fortschritt mit Platz je Bauteil",
              r["an"] and [(t["titel"], t["rang"], t["anzahl"], t["prozent"]) for t in r["teile"]]
              == [("Knackpunkt", 2, 4, 41.3), ("Kragarm (Übung 2)", 1, 1, 12.0)]
              and r["teile"][1]["seite"] == "/Strukturmechanik/P1/Uebung-2/", str(r))
        r = requests.post(KP, headers=p8, json={"teil": "f0", "prozent": 5, "entwurf": "A", "seite": "javascript:alert(1)"}).json()
        check("kp: unsichere Seite verworfen", requests.get(KP + "/meine", headers=p8).json()["teile"][1]["seite"] is None)
        r = requests.get(BACKEND + "/dashboard", params={"key": "test-dashboard-key"})
        check("kp: Spitzname im Dashboard", "bAda/b1234567890 <a href" in r.text)
        requests.get(BACKEND + "/dashboard-kp-name-loeschen", params={"key": "test-dashboard-key", "name": "bAda/b1234567890"})
        r = requests.get(KP, headers=p7, params={"teil": TEIL}).json()
        check("kp: Name im Dashboard entfernt", r["ich"]["anzeige"] == "N103 Platz 7" and r["name"] == "", str(r))

        # Hilfe-App: Schlüssel nötig, Warteschlange mit Platz, Push bei neuer Anfrage, erledigt
        import base64
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric import ec
        HK = {"X-Key": "test-dashboard-key"}
        pushes = []

        class PushSink(http.server.BaseHTTPRequestHandler):
            def do_POST(self):
                pushes.append({"auth": self.headers.get("Authorization", ""), "enc": self.headers.get("Content-Encoding"),
                               "body": self.rfile.read(int(self.headers.get("Content-Length", 0)))})
                self.send_response(201)
                self.end_headers()

            def log_message(self, *a):
                pass
        sink = http.server.HTTPServer(("127.0.0.1", 5096), PushSink)
        threading.Thread(target=sink.serve_forever, daemon=True).start()
        check("hilfe: ohne Schlüssel gesperrt", requests.get(BACKEND + "/api/hilfe").status_code == 403)
        check("hilfe: Seite und Manifest", requests.get(BACKEND + "/hilfe/").status_code == 200
              and "manifest+json" in requests.get(BACKEND + "/hilfe/manifest.webmanifest").headers["Content-Type"])
        r = requests.post(BACKEND + "/api/hilfe/schalter", headers=HK, json={"an": True}).json()
        check("hilfe: Schalter an, VAPID-Schlüssel da", r["an"] and len(base64.urlsafe_b64decode(r["vapid"] + "==")) == 65, str(r))
        geraet = ec.generate_private_key(ec.SECP256R1()).public_key().public_bytes(
            serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint)
        abo = {"endpoint": "http://127.0.0.1:5096/push/1", "keys": {
            "p256dh": base64.urlsafe_b64encode(geraet).rstrip(b"=").decode(),
            "auth": base64.urlsafe_b64encode(os.urandom(16)).rstrip(b"=").decode()}}
        check("hilfe: Push-Abo gespeichert", requests.post(BACKEND + "/api/hilfe/abo", headers=HK, json={"abo": abo}).json() == {"ok": True})
        requests.post(BACKEND + "/api/help", headers=p7, json={"page": "/Strukturmechanik/P1_Einfuehrung/03_Selbsttests/Uebung-3"})
        requests.post(BACKEND + "/api/help", headers=p8, json={"page": "/Strukturmechanik/P1_Einfuehrung/03_Selbsttests/Uebung-1"})
        for _ in range(40):
            if len(pushes) >= 2:
                break
            time.sleep(0.25)
        check("hilfe: Push je neuer Anfrage, verschlüsselt mit VAPID",
              len(pushes) == 2 and all(x["enc"] == "aes128gcm" and x["auth"].startswith("vapid") for x in pushes), str(pushes)[:300])
        r = requests.get(BACKEND + "/api/hilfe", headers=HK).json()
        e = r["eintraege"]
        check("hilfe: Reihenfolge mit Raum, Platz, Seite",
              [(x["raum"], x["platz"], x["seite"]) for x in e] == [("N103", 7, "P1 Übung 3"), ("N103", 8, "P1 Übung 1")], str(r))
        check("hilfe: aktiver Raum aus den Anfragen", r["raum_aktiv"] == "N103", str(r.get("raum_aktiv")))
        r = requests.post(BACKEND + "/api/hilfe/erledigt", headers=HK, json={"id": e[0]["id"]}).json()
        check("hilfe: erledigt, Platz 8 ist der nächste", [x["platz"] for x in r["eintraege"]] == [8], str(r))
        requests.post(BACKEND + "/api/help", headers=p8, json={"page": "x"})
        check("hilfe: kein zweiter Push für offene Anfrage", len(pushes) == 2)
        import sqlite3
        tdb = sqlite3.connect(os.path.join(tmp, "test.db"))
        tdb.execute("INSERT INTO results (pseudonym, qid, best, max, attempts, updated_at) VALUES (?, ?, 0, 5, 5, ?)",
                    ("test-aufgegeben", "/T/Ueb:q0", time.time()))
        tdb.execute("INSERT INTO results (pseudonym, qid, best, max, attempts, updated_at) VALUES (?, ?, 0, 5, 3, ?)",
                    ("test-haengt", "/T/Ueb:q0", time.time()))
        tdb.commit()
        r = requests.get(BACKEND + "/api/hilfe", headers=HK).json()
        check("hilfe: empfohlen mit aufgegeben vor hängt",
              [(x["aufgegeben"], x["versuche"], x["frage"]) for x in r["empfohlen"]] == [(True, 5, "T Ueb · Frage 1"), (False, 3, "T Ueb · Frage 1")]
              and r["empfohlen"][0]["label"].startswith("…"), str(r["empfohlen"]))
        tdb.execute("DELETE FROM results WHERE pseudonym IN ('test-aufgegeben', 'test-haengt')")
        tdb.commit()
        tdb.close()
        r = requests.post(BACKEND + "/api/hilfe/schalter", headers=HK, json={"an": False}).json()
        check("hilfe: ausschalten schließt offene Anfragen", not r["an"] and r["eintraege"] == [], str(r))
        sink.shutdown()

        r = requests.get(BACKEND + "/dashboard", params={"key": "test-dashboard-key"})
        check("dashboard zeigt Fehlwerte mit Ursache",
              "Häufige Fehlwerte heute" in r.text and "Material zugeordnet?" in r.text
              and "<em>unbekannt</em>" in r.text)
        r = requests.post(BACKEND + "/api/check",
                          json={"qid": "/T/Ueb:q0", "value": 9.9, "attemptsUsed": 4}).json()
        check("guest exhausted -> solution", not r["correct"] and r.get("solution") == 7.378, str(r))
        check("unknown qid -> 404", requests.post(
            BACKEND + "/api/check", json={"qid": "/nix", "value": 1}).status_code == 404)

        # authed: attempts server-tracked, points scale with attempt number
        r = requests.post(BACKEND + "/api/check", headers=headers,
                          json={"qid": "/T/Ueb:q0", "value": 9.9}).json()
        check("authed wrong attempt 1", not r["correct"] and r["attempts"] == 1 and r["authed"], str(r))
        r = requests.post(BACKEND + "/api/check", headers=headers,
                          json={"qid": "/T/Ueb:q0", "value": 7.378}).json()
        check("authed correct attempt 2 -> volle 5 P. (Mastery)",
              r["correct"] and r["attempts"] == 2 and r["earned"] == 5 and r["best"] == 5, str(r))
        r = requests.post(BACKEND + "/api/check", headers=headers,
                          json={"qid": "/T/Ueb:q0", "value": 7.378}).json()
        check("authed re-check keeps attempts/best",
              r["attempts"] == 2 and r["best"] == 5, str(r))
        r = requests.post(BACKEND + "/api/check", headers=headers,
                          json={"qid": "/T/Ueb:mc0", "selected": ["a", "c"]}).json()
        check("authed MC first try -> 4 P. + 1 Bonus",
              r["correct"] and r["earned"] == 5 and r.get("solution") == ["a", "c"], str(r))
        me2 = requests.get(BACKEND + "/api/me", headers=headers).json()
        check("checked points land in /api/me", me2["total_points"] == 18, str(me2))

        # ---- AGS: Score-Push an die Mock-Plattform -----------------------
        # Meldungen laufen nacheinander; warten, bis die letzte den Endstand trägt
        for _ in range(40):
            if ags_received and ags_received[-1].get("scoreGiven") == 18:
                break
            time.sleep(0.25)
        check("AGS score received by platform", len(ags_received) > 0, str(ags_received))
        if ags_received:
            last = ags_received[-1]
            check("AGS userId is original sub", last.get("userId") == "opal-user-13", str(last))
            check("AGS scoreGiven = total points", last.get("scoreGiven") == 18, str(last))
            # (5+1) q0 + (4+1) mc0 + (5+1) det0
            check("AGS scoreMaximum incl. Bonus", last.get("scoreMaximum") == 17, str(last))
            check("AGS grading complete", last.get("gradingProgress") == "FullyGraded")

    finally:
        server.terminate()
        jwks_srv.shutdown()

    if failures:
        print(f"\n{len(failures)} Tests fehlgeschlagen: {failures}")
        sys.exit(1)
    print("\nAlle Tests bestanden.")


if __name__ == "__main__":
    main()
