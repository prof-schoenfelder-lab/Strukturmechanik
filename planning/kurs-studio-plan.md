# Plan: Kurs-Studio — grafische Weboberfläche für den gesamten Kursinhalt

Stand: 22.07.2026 · Status: **Plan, noch nicht umgesetzt** · Umsetzung geplant in
mehreren fokussierten Sessions (Opus). Dieses Dokument ist die Arbeitsgrundlage.

## 1. Ziel

Eine lokale Weboberfläche („Kurs-Studio"), mit der der komplette Kursinhalt
grafisch erstellt und gepflegt wird — ohne Markdown-Handarbeit, ohne
mkdocs.yml-Editieren:

- **Praktika** anlegen; jedes Praktikum beginnt mit einer **Übersichtsseite**
  (Lernziele + automatisch erzeugte Inhaltsliste).
- Drei **Inhaltstypen** je Praktikum:
  1. **Theorie** — Text + Bilder (+ Boxen, Menüpfade, eingebettete Tutorials)
  2. **Vorzeigebeispiel** — das Tabs+Stepper-Muster (Aufgabe / Lösung in
     Schritten / ggf. analytische Lösung)
  3. **Übung** — immer gleiches Gerüst: Gegeben, Gesucht, Hinweise, Lösung,
     optional numerische/MC-Fragen mit Punkten (answer-checker)
- **Tutorials** (Klick-Anleitungen) einbetten oder direkt neu erstellen
  (bestehendes Tutorial-Studio wird integriert/verlinkt).
- **Navigation** (mkdocs.yml-Nav + Übersichtsseiten) erzeugt sich automatisch.

## 2. Machbarkeits-Urteil

**Ja, das ist mit der aktuellen Architektur sauber machbar** — sie ist sogar
ungewöhnlich gut dafür vorbereitet. Begründung:

- **„Repo als Datenbank" ist bereits bewiesen:** Die Tutorial-Datenbank
  (docs/tutorials/ als JSON + Renderer tutorials.js + Studio mit File System
  Access API) ist exakt dieses Muster im Kleinen. Das Kurs-Studio ist die
  Verallgemeinerung auf den ganzen Kurs.
- **Alle visuellen Primitive existieren schon** als Konventionen in
  modern.css/modern-ui.js: Serifen-Typo, typografische Boxen (Lernziele,
  Aufgabe, Checkpoint …), Menüpfad-Chips/Klick-Pillen, Tastenkappen,
  Varianten-Tabs + Schritt-Stepper, prakt-cards-Übersichten, Timeline-Schritte.
  Der Generator muss nur diese Konventionen ausspucken — kein neues Design.
- **Die Inhaltstypen sind real schon uniform:** Übungen folgen bereits dem
  Gegeben/Gesucht/Fragen-Muster (`div.numeric-question` mit data-Attributen,
  answers_hook.py extrahiert die Antworten beim Build). Das Balken-Beispiel
  folgt dem Tabs+Stepper-Muster (WF_GROUPS in modern-ui.js). Beides ist
  1:1 generierbar.
- **Deploy bleibt unberührt:** MkDocs + GitHub Actions + LTI-Backend ändern
  sich nicht. Studierende sehen weiterhin eine statische Site.

**Die eine echte Architektur-Entscheidung** (siehe §3): Quelle der Wahrheit
wird strukturiertes JSON, Markdown wird generiert — nicht umgekehrt.
Rück-Parsen von freiem Markdown in einen grafischen Editor wäre verlustbehaftet
und fragil; Generieren aus Struktur ist robust und im Repo bereits erprobt.

## 3. Architektur

```
content/                        ← QUELLE DER WAHRHEIT (JSON, nicht deployt)
  course.json                   ← Praktika-Baum, Reihenfolge, Lernziele
  P2/
    theorie-lagerungen.json
    beispiel-balken.json
    uebung-3.json
docs/                           ← GENERIERT (+ Bestand), wird deployt
  P2_…/…​.md                     ← vom Generator erzeugte Seiten (mit Kopfmarker)
  P2_…/images/…                 ← Medien (vom Studio dorthin kopiert)
  assets/wf-groups.json         ← Stepper/Tabs-Konfig (statt hardcoded im JS)
  tutorials/…                   ← bestehende Tutorial-DB (unverändert)
mkdocs.yml                      ← Nav-Block zwischen Markern generiert
tools/kurs-studio.html (+ tools/studio/*.js)  ← die Oberfläche
```

Prinzipien:

1. **Studio = lokale HTML-App** (wie Tutorial-Studio): kein Server, kein Abo,
   Chrome/Edge mit File System Access API; einmal Repo-Ordner wählen,
   dann liest/schreibt sie content/, docs/ und den Nav-Block.
2. **Generator läuft im Studio** (JS-Modul `tools/studio/generator.js`):
   Speichern erzeugt sofort die fertigen md-Seiten, Übersichtsseiten,
   wf-groups.json und den Nav-Block. Kein Terminal nötig (außer git).
   Das Modul ist so geschnitten, dass es später auch headless (Node) laufen
   könnte — nice-to-have, kein Muss.
3. **Generierte Seiten sind markiert**: Kopfkommentar
   `<!-- GENERIERT aus content/P2/uebung-3.json — Änderungen im Kurs-Studio machen -->`
   + Inhalts-Checksumme. Das Studio warnt, wenn eine generierte Datei von Hand
   verändert wurde (statt sie stumm zu überschreiben).
4. **Koexistenz mit Bestand**: Nicht migrierte, handgeschriebene Seiten werden
   in course.json als `extern`-Einheiten geführt (Pfad-Referenz). Sie
   erscheinen in Nav + Übersichten, bleiben aber unangetastet. Migration kann
   Seite für Seite erfolgen — kein Big Bang.
5. **mkdocs.yml**: Der Nav-Abschnitt wird zwischen zwei Markerzeilen
   (`# >>> AUTO-NAV` / `# <<< AUTO-NAV`) als Text ersetzt; alles außerhalb
   (Theme, Plugins, manuelle Einträge wie FAQ/Fortschritt) bleibt unberührt.

## 4. Inhaltsmodell (Schemas, vereinfacht)

**course.json**
```json
{ "praktika": [
    { "id": "P2", "slug": "P2_Geometrie_Randbedingungen",
      "titel": "Geometrieaufbereitung und Randbedingungen",
      "icon": "material/cube", "lernziele": ["…", "…"],
      "sektionen": [
        { "titel": "Lagerungen", "einheiten": [
            { "typ": "theorie",  "id": "theorie-lagerungen" },
            { "typ": "uebung",   "id": "uebung-3" },
            { "typ": "extern",   "pfad": "P2_…/Cylindrical.md", "titel": "…" }
        ]}
      ]}
]}
```

**Gemeinsames Block-Modell** (Theorie-Body, Lösungen, Schritt-Inhalte):
```json
{ "art": "text", "md": "Lagerungen verhindern … `Strukturbaum Rechtsklick Mesh`" }
{ "art": "bild", "datei": "images/lager.png", "breite": 700 }
{ "art": "box",  "typ": "warning|abstract|question|check|tip", "titel": "…", "blocks": […] }
{ "art": "tutorial", "slug": "festlager-anbringen" }
{ "art": "tabelle", "kopf": […], "zeilen": [[…]] }
```
Inline gilt unsere bestehende Syntax (Backticks → Chips/Pillen/Tastenkappen,
`>` → Pfeil) — der Editor zeigt sie live gerendert (Engine aus dem
Tutorial-Studio wiederverwenden).

**Übung**
```json
{ "titel": "Übung 3 — Lineal über Kante", "gegeben": [blocks], "gesucht": [blocks],
  "hinweise": [blocks], "loesung": [blocks],
  "fragen": [ { "typ": "numerisch", "frage": "…", "antwort": 7.378,
                "toleranz": 0.1, "punkte": 5, "versuche": 5, "hinweise": "…" } ] }
```
→ generiert das bestehende Übungs-Muster inkl. `div.numeric-question`-Markup;
answers_hook.py funktioniert unverändert.

**Vorzeigebeispiel**
```json
{ "titel": "Zweiseitig gelagerter Balken", "basisordner": "losung-mit-ansys",
  "tabs": [ {"label": "Aufgabe", "seite": "aufgabenstellung"}, … ],
  "aufgabe": [blocks],
  "schritte": [ { "slug": "material", "label": "Material",
                  "banner": "Material E=210 GPa anlegen", "blocks": […] } ],
  "analytisch": [blocks] }
```
→ generiert Schrittseiten + task-tabs-Markup + einen Eintrag in
`docs/assets/wf-groups.json` (Vorarbeit: WF_GROUPS aus modern-ui.js dorthin
auslagern; modern-ui.js lädt die Datei — kleiner, risikoarmer Refactor).

**Theorie** = Titel + Icon + Block-Liste.

## 5. Editor-Oberfläche

- **Linke Spalte:** Kurs-Baum (Praktika → Sektionen → Einheiten), anlegen,
  umbenennen, per Drag sortieren. Reihenfolge = Nav-Reihenfolge.
- **Mitte:** Editor je Typ:
  - *Theorie:* Block-Liste (Text/Bild/Box/Tutorial/Tabelle), Bilder per
    Drag&Drop oder Strg+V (landen in docs/<ziel>/images/), Slash-Menü wie im
    Tutorial-Studio, Live-Vorschau je Block.
  - *Übung:* vier feste Bereiche (Gegeben/Gesucht/Hinweise/Lösung) + Fragen-
    Liste mit Antwort/Toleranz/Punkten/Versuchen/Hinweisen.
  - *Vorzeigebeispiel:* Tab-Konfiguration, Schritt-Liste (Label fürs
    Stepper-Kurzwort, „Jetzt:"-Banner, Blocks je Schritt).
  - *Übersichtsseite:* nur Lernziele editieren — Inhaltsliste ist automatisch.
- **Vollvorschau** wie im Tutorial-Studio (Overlay im Kurs-Look).
- **Speichern** = content/-JSON + generierte docs/-Dateien + Nav-Block in einem
  Schritt; danach normal `git commit/push` (optional später ein Git-Helfer).

## 6. Umgang mit dem Bestand / Migration

- Phase „Migration" ist skriptgestützt (Python, durch Claude): bestehende
  Übungen (Muster ist uniform) und das Balken-Beispiel lassen sich maschinell
  nach content/ überführen; Theorie-Seiten je nach Freiform ggf. als `extern`
  belassen oder halbautomatisch übernehmen. QA Seite für Seite.
- Bis dahin: alles Bestehende läuft unverändert weiter (extern-Einheiten).

## 7. Risiken & Grenzen (ehrlich)

- **Chromium-Pflicht** fürs Studio (File System Access API). Fallback ZIP wäre
  für Ganzkurs-Editing unpraktisch → bewusst Chrome/Edge voraussetzen.
- **Zwei Repos** (Strukturmechanik/Thermo): Tool im Struktur-Repo pflegen und
  wie bisher rüberkopieren; beim Öffnen wählt man den Repo-Ordner.
- **Hand-Edits an generierten Seiten** gehen beim nächsten Generieren verloren
  → Checksummen-Warnung (§3.3) ist Pflichtteil, nicht Nice-to-have.
- **Block-Editor-Umfang**: bewusst KEIN WYSIWYG-Richtext; Blöcke + Inline-
  Markdown mit Live-Vorschau (im Tutorial-Studio bewährt). Das hält den
  Editor klein und die Ausgabe deterministisch.
- **mkdocs.yml** wird als Text (Marker-Block) manipuliert, nicht als YAML
  geparst — robust gegen Formatierung, erfordert die zwei Markerzeilen.

## 8. Erwogene Alternative

Git-basiertes Fertig-CMS (Decap/Sveltia): generische Feld-Editoren vorhanden,
aber unsere Spezialitäten (Stepper-Gruppen, Chips-Live-Vorschau, GIF-Encoder,
answers-Hook, Nav-Generierung, prakt-cards) müssten als Custom-Widgets
nachgebaut werden; dazu Hosting/Auth-Fragen. Das lokale Studio passt besser
zum „Repo als DB ohne Server"-Prinzip — und ~70 % der Primitive existieren
schon im Tutorial-Studio.

## 9. Phasenplan (je Phase eine fokussierte Session)

- **Phase 0 — Fundament (klein):** WF_GROUPS + Tabs-Konfig nach
  `docs/assets/wf-groups.json` auslagern (modern-ui.js lädt sie);
  AUTO-NAV-Marker in mkdocs.yml einziehen; content/-Schemas final festlegen
  (dieses Dokument als Basis). *Risikoarm, sofort mergebar.*
- **Phase 1 — Studio-Shell + Struktur:** Repo öffnen, course.json anlegen/lesen,
  Kurs-Baum-UI (anlegen/sortieren, extern-Einheiten), Generator für
  Übersichtsseiten + Nav-Block. Ergebnis: Struktur & Navigation komplett
  grafisch pflegbar, Inhalte noch extern.
- **Phase 2 — Übungs-Editor:** kompletter Übungs-Typ inkl. Fragen
  (numerisch/MC), Medien-Handling, Vollvorschau. Ergebnis: neue Übungen
  entstehen vollständig im Studio.
- **Phase 3 — Theorie-Editor:** Block-Editor + Tutorial-Embed-Block
  (+ Absprung ins Tutorial-Studio zum Neu-Erstellen).
- **Phase 4 — Vorzeigebeispiel-Editor:** Schritte/Tabs/Banner/Stepper-Konfig.
- **Phase 5 — Migration + Härtung:** Bestand skriptgestützt überführen,
  Checksummen-Schutz, optional Git-Helfer / Node-Headless-Generator.

Jede Phase liefert etwas eigenständig Nutzbares; Abbruch nach jeder Phase
hinterlässt einen konsistenten Zustand.
