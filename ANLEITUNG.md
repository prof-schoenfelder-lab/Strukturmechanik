# Betriebsanleitung: Punktesystem, OPAL-Anbindung & Startseite

Stand: Juli 2026. Diese Anleitung fasst zusammen, wie das System aufgebaut ist,
wie der Alltag läuft und was bei Problemen zu tun ist.

---

## 1. Architektur-Überblick

| Baustein | Wo | Was |
|---|---|---|
| Lehrseite (MkDocs Material) | GitHub Pages, deployt automatisch bei Push auf `main` | Inhalte, Übungsfragen, 3D-Startseite, Fortschrittsseite |
| Backend (Flask) | `fing-spool.htwk-leipzig.de`, Pfad `/fem/`, nur HTWK-Netz/VPN | OPAL-Login (LTI 1.3), Antwortprüfung, Punktespeicherung, AGS-Noten, Dashboard |
| OPAL | LTI-Kursbaustein im Kurs | Login-Einstieg; optional Bewertungsanzeige pro Person |

- Backend-Installation: `/home/guacamole/fem-backend/` (systemd-Dienst `fem-backend`,
  gunicorn auf `127.0.0.1:8100`, nginx-Location `/fem/` im Guacamole-vHost).
- Konfiguration: `~/fem-backend/.env` (Secrets, OPAL-URLs, Client-ID, Dashboard-Token).
- Daten: `~/fem-backend/data/results.db` (SQLite) + `lti_private.pem` (LTI-Schlüssel).
- Die Seite kennt das Backend über [docs/assets/js/backend-config.js](docs/assets/js/backend-config.js)
  (`AC_BACKEND_URL`, `AC_OPAL_URL`). Leerer `AC_BACKEND_URL` = alles läuft rein lokal.

## 2. Punktesystem (Mastery-Prinzip)

- **Lösen zählt voll** — egal beim wievielten Versuch. **+1 Bonuspunkt** bei
  Lösung im ersten Versuch („Volltreffer").
- Pro Frage 5 Versuche (`data-attempts`); nach jedem Fehlversuch der nächste
  Hinweis aus `data-hints`; nach dem letzten Versuch wird die Lösung angezeigt
  (0 Punkte). Formulierungen sind bewusst aufmunternd („Noch nicht richtig",
  „Beim nächsten Mal!").
- **Gäste** (ohne OPAL-Login): volle Nutzung inkl. richtig/falsch-Feedback und
  Lösungsanzeige, aber keine Punkte/Abzeichen. Dafür ist HTWK-Netz/VPN nötig
  (die Prüfung läuft serverseitig). Unter jeder richtigen Antwort steht der
  Link zum OPAL-Login.
- **Antworten stehen nicht im HTML**: Ein Build-Hook
  ([scripts/answers_hook.py](scripts/answers_hook.py)) entfernt
  `data-answer`/`data-correct` und erzeugt `answers.json` fürs Backend.
  (Im öffentlichen Repo stehen sie weiterhin — bewusste Entscheidung, es sind
  freiwillige Übungen ohne Prüfungsrelevanz.)
- Der Server zählt Versuche und Punkte für eingeloggte Nutzer — Manipulation
  über den Browser-Speicher ist damit wirkungslos.

## 3. Gamification

- **Header-Ring** (neben dem Logo): füllt sich mit dem persönlichen
  Gesamtfortschritt („x von y Aufgaben gelöst" im Tooltip), verlinkt auf
  „Mein Fortschritt". Ein separates Level-System gibt es bewusst nicht —
  Fortschritt zeigen die Ringe, Meilensteine feiern die Abzeichen.
- **Abzeichen** (9 Stück, z.B. 🚀 Erste Schritte, 💪 Comeback, 🏆 FEM-Vollprofi):
  werden im Moment des Verdienens mit Konfetti gefeiert. Einmal verdient
  bleibt verdient — auch wenn später neue Aufgaben dazukommen.
- **Navigation links**: grüner Haken = Seite komplett gelöst, sonst Zähler
  („1/2"). 0 Punkte ergeben nie einen Haken.
- **„Mein Fortschritt"**: Ringe pro Praktikum, Punkte, Abzeichen, Sync-Status.
- **Kurs-Statistik** unter jeder Frage („73 % des Kurses haben diese Aufgabe
  gelöst") — anonym, erscheint ab 5 Teilnehmenden.
- Account-Wechsel im selben Browser wird erkannt (kein Punkte-Übertrag);
  anonym gesammelte Gast-Punkte übernimmt der **erste** Login als Feature.

## 4. Alltag: Inhalte pflegen

**Frage einbauen** (im Markdown, wie gehabt):

```html
<div class="numeric-question" data-answer="7.378" data-tolerance="0.1"
     data-points="5" data-attempts="5" data-hints="Hinweis 1|Hinweis 2"></div>
```

**Nach jedem Inhalts-Update mit neuen/geänderten Fragen:**

```bash
./backend/deploy.sh     # baut die Site, erzeugt answers.json, kopiert sie aufs Backend
git add ... && git commit && git push   # deployt die Seite via GitHub Actions
```

Kein Server-Restart nötig (answers.json wird automatisch neu geladen).
Neue Aufgaben im laufenden Semester sind unkritisch: alles passt sich an,
verdiente Abzeichen bleiben erhalten.

**Ein Server-Restart ist NUR nötig, wenn sich `backend/app.py` ändert:**

```bash
ssh fing-spool.htwk-leipzig.de
sudo systemctl restart fem-backend
```

## 5. OPAL-Kursbaustein (LTI 1.3)

Kursbaustein „LTI-Seite" → Tab „Konfiguration":

| Feld | Wert |
|---|---|
| LTI Version | LTI 1.3, „Eigenes Tool" |
| Login URL | `https://fing-spool.htwk-leipzig.de/fem/lti/login` |
| Launch URL | `https://fing-spool.htwk-leipzig.de/fem/lti/launch13` |
| Schlüsseltyp | „Schlüssel" — PEM-Text von `https://fing-spool.htwk-leipzig.de/fem/lti/pubkey` einfügen |
| ClientID | `strukturmechanik-fem` (muss zu `LTI13_CLIENT_ID` in der `.env` passen) |
| Anzeige | **„Neues Fenster öffnen"** (sonst klemmt die Seite im OPAL-iFrame) |
| Datenschutz-Optionen | **Übertragung von Vor-/Nachname aktivieren**, damit das Dashboard Klarnamen zeigen kann (optional — ohne bleibt alles pseudonym) |

- Tab **„Bewertung" aktivieren** → die Punktestände laufen per AGS in OPAL ein
  und sind dort **pro Person mit Namen** im Bewertungswerkzeug sichtbar.
- Zieht der Baustein um: neue Baustein-URL in `backend-config.js`
  (`AC_OPAL_URL`) eintragen — sie wird Gästen als Login-Link angezeigt.

## 6. Server-Betrieb

| Aufgabe | Befehl / Ort |
|---|---|
| Dienst neu starten | `sudo systemctl restart fem-backend` |
| Logs | `journalctl -u fem-backend -n 50` |
| Dashboard (aggregierte Kursübersicht) | `https://fing-spool.htwk-leipzig.de/fem/dashboard?key=<TOKEN>` — Token: `grep DASHBOARD_TOKEN ~/fem-backend/.env` |
| Hilfe-Warteschlange | Studierende melden sich über den 🙋-Button unten rechts auf jeder Kursseite (geht auch ohne Login — Zuordnung dann über die Pool-IP). Das Dashboard zeigt die Warteschlange in Meldereihenfolge mit Platz/Name/Seite/Wartezeit; „✓ erledigt" schließt das Ticket und der Button beim Studierenden meldet „Hilfe ist unterwegs". Offene Tickets verfallen nach 3 h automatisch. |
| Dashboard im Praktikum | Seite einfach offen lassen (aktualisiert sich alle 30 s). Die Praktikums-Ansicht oben zeigt pro heute aktiver Person: Pool-PC-Name (Reverse-DNS, sonst Pseudonym-Kürzel), Fortschritt im Praktikum, aktuelle Aufgabe, Status (arbeitet / hängt ab 3 Fehlversuchen / Aufgabe aufgegeben / pausiert / fertig) — sortiert von der Spitze zum Schlusslicht, plus Spannweite (Spitze/Median/Schlusslicht). **Nicht am Beamer zeigen** (PC-Namen = Sitzplätze). |
| Backup | automatisch täglich 3:17 Uhr nach `~/fem-backend/backups/` (14 Stände) |
| Komplett-Backup von Hand | `data/results.db`, `data/lti_private.pem`, `.env` sichern |
| **Kurs-Reset (Semesterende)** | `~/fem-backend/reset-course.sh` |

**Kurs-Reset:** legt ein Backup an, leert Ergebnisse + Nutzer und rotiert die
**Kurs-Generation**. Browser mit Daten aus dem alten Semester räumen sich beim
nächsten Besuch **automatisch selbst auf** — niemand muss manuell den
Browser-Speicher löschen.

## 7. Datenschutz

- Gespeichert werden **Pseudonyme** (salted Hash der OPAL-ID) und Punktzahlen.
  Überträgt der OPAL-Baustein zusätzlich den Namen, wird dieser **verschlüsselt**
  abgelegt (`users.name_enc`) und ausschließlich im Dashboard (hinter dem Token)
  angezeigt — Zweck: persönliche Ansprache im Praktikum. Der Semester-Reset
  löscht die Namen mit; die OPAL-Option abschalten beendet die Erhebung.
- Für den AGS-Noten-Rückkanal liegt die OPAL-ID **verschlüsselt** vor
  (`users.sub_enc`); abschaltbar mit `AGS_ENABLED=0` in der `.env`.
- Statistik/Dashboard sind aggregiert bzw. pseudonym; namentliche Zuordnung
  passiert ausschließlich in OPAL selbst.
- Die Pool-PC-Namen der Praktikums-Ansicht liegen **nur im RAM** des Dienstes
  (nach Restart leer, nichts davon in der Datenbank) und sind nur über das
  Dashboard-Token sichtbar.
- Backend ist nur im HTWK-Netz/VPN erreichbar (gewollt — Studierende brauchen
  VPN ohnehin für die ANSYS-Lizenz).

## 8. Troubleshooting

| Symptom | Ursache / Lösung |
|---|---|
| Änderung nicht sichtbar | Browser-Cache: hart neu laden (`Cmd+Shift+R` / `Strg+F5`) |
| „Antwortprüfung nicht erreichbar" | Kein HTWK-Netz/VPN — oder Backend down (`systemctl status fem-backend`) |
| Fortschrittsseite lädt nicht / neue Endpunkte fehlen (404/405) | Nach app.py-Änderung wurde der Restart vergessen |
| Punkte tauchen nach Reset wieder auf | Nur bei altem Frontend-Stand; seit der Kurs-Generation räumen Browser automatisch auf. Notnagel: `localStorage.clear()` in der Browser-Konsole auf der Seite |
| LTI-Launch scheitert (401) | Key/ClientID im OPAL-Baustein passt nicht zur `.env` — nach Änderung Restart |
| Ergebnisse zählen nicht | `answers.json` nach Inhalts-Update nicht deployt → `./backend/deploy.sh` |

## 9. Offene Punkte

- **P3 Globale_Netzverfeinerung:** Anleitung und Lösungstabelle ordnen dieselben
  Spannungswerte um eine Netzstufe verschoben zu (Text: 2/1/0,5 mm — Tabelle:
  4/2/1 mm). Am ANSYS-Originalprojekt klären, welche Zuordnung stimmt.
- **P1 Übung 1:** Drei Lösungs-Screenshots fehlen
  (`docs/P1_Einfuehrung/03_Selbsttests/images/Uebung-01_Loesung_*.png`);
  die `<figure>`-Blöcke sind bis dahin auskommentiert (TODO im Markdown).
- **FolgeMeBackup/** (32 MB Tutorial-Rohaufnahmen im Repo): behalten oder entfernen?

Details zum Backend: [backend/README.md](backend/README.md) ·
Deployment: [backend/DEPLOY.md](backend/DEPLOY.md)
