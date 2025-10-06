# MkDocs Inline Tutorial Player — Kurzanleitung

Diese README erklärt, wie der kompakte, inline Tutorial-Player in diesem MkDocs-Projekt organisiert ist, wie du die Default-Höhe einstellst und wie du Tutorials (imported.json + screenshots) einbettest.

Kurz: Die Spieler-Assets liegen in `docs/assets/tutorials/`. Tutorial-Content (Beispiel) liegt unter `docs/assets/tutorials/vendor_demo/` (enthält `imported.json` und `img/`).

## Wo werden die Dateien platziert?

- Player-Code und Styles (bereitgestellt): `docs/assets/tutorials/`
  - `player.js` — Kern-Player
  - `player-bootstrap.js` — Auto‑Initializer, liest `data-tutorial` und ruft `TutorialPlayer.init`
  - `player.css` — Styles
- Tutorials / Inhalte (Beispiel): `docs/assets/tutorials/<folder>/`
  - `imported.json` — Tutorial-Metadaten (Schritte)
  - `img/` — Screenshots (z. B. `step-0.jpeg`)

Beim Build kopiert MkDocs alles unter `docs/` nach `site/` — daher werden die Assets beim Deploy mitgenommen.

## GitHub Pages Deployment

Die MkDocs-Dokumentation wird automatisch auf GitHub Pages bereitgestellt. Bei jedem Push auf den `main`-Branch wird der GitHub Actions Workflow `.github/workflows/deploy-mkdocs.yml` ausgeführt:

1. Der Workflow installiert Python und die erforderlichen MkDocs-Pakete
2. Erstellt die statische Website mit `mkdocs build`
3. Erstellt eine `.nojekyll`-Datei (wichtig für die korrekte Darstellung aller Assets)
4. Deployed die Website auf GitHub Pages

Die Website ist dann verfügbar unter: `https://<username>.github.io/<repository>/`

**Hinweis:** Beim ersten Deployment muss in den Repository-Einstellungen unter **Settings → Pages** die Source auf "GitHub Actions" gesetzt werden.

**Wichtig:** Die `.nojekyll`-Datei stellt sicher, dass GitHub Pages die Website nicht mit Jekyll verarbeitet, was dazu führen kann, dass Bilder und andere Assets nicht korrekt angezeigt werden.

## Default-Höhe einstellen

Es gibt drei einfache Wege, die Höhe des Players zu setzen:

1. Global (Site-weit) — änder das CSS-Root in `docs/styles/overrides.css`:

```css
:root {
  --tp-fixed-height: 480px; /* Standardhöhe */
}
```

2. Pro-Embed (inline) — setze die CSS-Variable direkt auf dem Embed-Container:

```html
<div
  class="tutorial-embed"
  data-tutorial="/assets/tutorials/vendor_demo"
  style="--tp-fixed-height:420px; --tp-max-width:800px"
></div>
```

3. Pro-Embed per data-Attribut — der Bootstrap-Lader unterstützt `data-height` (z. B. `data-height="420px"`):

```html
<div
  class="tutorial-embed"
  data-tutorial="/assets/tutorials/vendor_demo"
  data-height="420px"
></div>
```

Hinweis: `player-bootstrap.js` setzt `el.style.setProperty('--tp-fixed-height', el.dataset.height)` wenn `data-height` vorhanden ist.

## API (kurz)

- `window.TutorialPlayer.init(container, opts)`
  - `container` — DOM-Element, in das der Player gerendert wird
  - `opts` — Optionen (Kurzüberblick):
    - `jsonUrl` — exakte URL zur `imported.json` (z. B. `/assets/tutorials/vendor_demo/imported.json`). Wenn gesetzt, wird diese direkt geladen.
    - `t` — Fallback-Shortname (z. B. `vendor_demo`) — Player probiert eine Reihe plausibler Pfade
    - `zoom` — initialer Zoom (number)
    - `fit` — `'cover'` oder `'contain'` (standard `'contain'`)

Beispiel (manuell initialisieren):

```js
const container = document.getElementById("tutorial-embed-container");
window.TutorialPlayer.init(container, {
  jsonUrl: "/assets/tutorials/vendor_demo/imported.json",
  zoom: 1.0,
  fit: "cover",
});
```

Wenn du die automatische Initialisierung über HTML bevorzugst, füge stattdessen in eine Markdown-Seite ein:

```html
<div
  class="tutorial-embed"
  data-tutorial="/assets/tutorials/vendor_demo"
  style="--tp-fixed-height:420px"
></div>
```

Der `player-bootstrap.js` liest `data-tutorial` und baut eine `jsonUrl` (z. B. `/assets/tutorials/vendor_demo/imported.json`) und ruft `TutorialPlayer.init` auf.

## Wie werden Bildpfade aufgelöst?

- In `imported.json` sollten die Bildpfade relativ zum JSON liegen, z. B. `"image": "img/step-0.jpeg"`.
- Der Player lädt die `imported.json` und löst relative Bildpfade automatisch relativ zur URL der JSON-Datei auf — du musst also nur `img/step-0.jpeg` in der JSON angeben, wenn `imported.json` im selben Ordner wie `img/` liegt.

## CSS-Variablen und Anpassungen

- `--tp-fixed-height` — Höhe des Players (z. B. `480px`)
- `--tp-max-width` — max. Breite des Embed-Containers
- `--tp-pill-min-height` — Mindesthöhe der Schritt‑Pille

Du kannst diese Variablen global in `docs/styles/overrides.css` setzen oder pro-Embed überschreiben (siehe Beispiele oben).

## Verhalten & Features (Kurz)

- Prev / Next Buttons, Tastatur-Left/Right zur Navigation
- Pan per Pointer (Drag) auf dem Screenshot
- Zoom-Buttons (+ / −) (Mouse-wheel deaktiviert)
- Action-Highlights: nur Textteile in Backticks (`...`) werden als Aktionspills hervorgehoben
- Fortschrittsbalken und Schrittzähler (Deutsch: "Schritt X von Y")

## Einbinden in `mkdocs.yml`

Stelle sicher, dass `mkdocs.yml` die Player-Dateien lädt (bei uns so konfiguriert):

```yaml
extra_javascript:
  - "assets/tutorials/player.js"
  - "assets/tutorials/player-bootstrap.js"

extra_css:
  - "assets/tutorials/player.css"
  - "styles/overrides.css"
```

## Troubleshooting (häufige Probleme)

- 404 auf `imported.json` oder Bilder: prüfe, ob `imported.json` und `img/` im richtigen `docs/...`-Pfad liegen (in diesem Repo: `docs/assets/tutorials/<folder>/`).
- Bilder werden auf GitHub Pages nicht angezeigt: Der Workflow erstellt automatisch eine `.nojekyll`-Datei. Falls Bilder trotzdem nicht sichtbar sind, überprüfe die Browser-Konsole auf Fehler.
- Browser-Cache: harte Neuladung (Cmd+Shift+R) oder Inkognito-Fenster benutzen.
- Alte `mkdocs serve` Instanz: beende den Prozess und starte `mkdocs serve` neu.
- Wenn der Player falsche Pfade probiert: setze `jsonUrl` explizit auf `/assets/tutorials/<folder>/imported.json` im Embed (oder im `TutorialPlayer.init`).

## Beispiele — schnell

- Minimal (Bootstrap auto-init):

```html
<div
  class="tutorial-embed"
  data-tutorial="/assets/tutorials/vendor_demo"
  style="--tp-fixed-height:420px"
></div>
```

- Manueller Init (z. B. in einer eigenen Seite mit Cache-Busting):

```html
<script>
  const c = document.getElementById("tutorial-embed-container");
  window.TutorialPlayer.init(c, {
    jsonUrl: "/assets/tutorials/vendor_demo/imported.json",
    zoom: 1,
    fit: "contain",
  });
</script>
```

---

Wenn du willst, schreibe ich noch ein kurzes Beispielskript, das automatisch alle `docs/assets/<folder>/imported.json`-Tutorials listet, oder ich ergänze eine kleine Testseite im `docs/` mit eingebettetem Player. Welche Ergänzung hättest du gern?
