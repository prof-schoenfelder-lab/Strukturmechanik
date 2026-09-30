# Inhalts-Vorlagen (Markdown) + Auto-Übersicht

Inhalte werden ganz normal als Markdown-Seiten geschrieben. Damit eine Seite
**automatisch als Karte auf der Praktikums-Startseite** erscheint, bekommt sie
ein paar Frontmatter-Zeilen (Feld `sektion:` ist der Schalter). Der Build-Hook
`scripts/overview_hook.py` baut die Übersicht daraus — auf der Startseite steht
nur `<!-- uebersicht -->`. Navigation bleibt wie gehabt in `mkdocs.yml` von Hand.

**Nur getaggte Seiten werden zu Karten.** Unterseiten (z.B. die Schritte eines
Beispiels) einfach ohne `sektion:` lassen — dann tauchen sie nicht als Karte auf.

Frontmatter-Felder:
- `sektion:` — Gruppe auf der Übersicht (**Schalter**; ohne das keine Karte)
- `title:` — Kartentitel (sonst erste H1 der Seite)
- `kurz:` — kurze Beschreibung unter dem Titel (optional)
- `thumb:` — Vorschaubild, relativ zur Seite (optional; sonst erstes Bild der Seite)
- `order:` — Zahl für die Reihenfolge; steuert auch die Reihenfolge der Sektionen (optional)
- `typ:` — optionales Badge: `inhalt` · `beispiel` · `uebung`

---

## Vorlage: Inhalt (Theorie)

```markdown
---
title: Lager
sektion: Lagerungen
kurz: Fest-, Los- und weitere Lagerungen richtig anbringen
thumb: images/Lager.png
typ: inhalt
order: 20
hide: [toc]
---

# Lager

Fließtext … `Reiter Environment > Fixed Support` … **fett**, `Enter`.

<figure style="text-align:center;"><img src="images/Lager.png" width="600"></figure>

!!! tip "Tipp"
    Kurzer Hinweis.
```

## Vorlage: Vorzeigebeispiel

Nur die **Aufgaben-/Startseite** des Beispiels bekommt `sektion:` (→ eine Karte).
Die Schrittseiten (`01-material.md` …) bleiben ohne Frontmatter-`sektion:` und
nutzen weiter das Tabs+Stepper-Muster (task-banner / task-tabs-src wie bisher).

```markdown
---
title: Zweiseitig gelagerter Balken
sektion: Lösungsbeispiel
kurz: Kompletter Ablauf einer Simulation — Schritt für Schritt
thumb: images/Aufgabe.png
typ: beispiel
order: 10
---

# Zweiseitig gelagerter Balken

Aufgabenstellung … (Schritte liegen in Unterseiten, per Nav verlinkt)
```

## Vorlage: Übung

```markdown
---
title: Übung 3 — Lineal über Kante
sektion: Lagerungen
kurz: Lagerungsbeispiel Lineal über Kante belastet
thumb: images/Uebung-03.png
typ: uebung
order: 30
hide: [toc]
---

# Übung 3 — Lineal über Kante

## Gegeben
- Material: Stahl, $E = 210\,\mathrm{GPa}$
- …

## Gesucht
### Maximale Durchbiegung $u_{\max}$ in mm

<div class="numeric-question" data-answer="7.378" data-tolerance="0.1" data-points="5" data-attempts="5" data-hints="Einheit auf mm?" data-diagnose="7.747: Wert passt zu Standardmaterial Structural Steel (200 GPa). Material zugeordnet?"></div>

## Hinweise
!!! tip "Vorgehen"
    Im Strukturbaum `Rechtsklick Solution > Insert > Deformation`.

<div class="solution-images" markdown="1">
### 🎯 Lösung
**Wichtige Punkte:** …
</div>
```

`data-diagnose` (optional): typische Fehlwerte mit Ursache, `Wert: Text | Wert: Text`.
Passt eine falsche Eingabe dazu (Aufgabentoleranz, mindestens 3 %), zeigt die Seite
den Text statt des allgemeinen Hinweises. Faktor 1000, Faktor 2/4 und Vorzeichen
erkennt das Backend ohnehin; hier gehören aufgabenspezifische Fehler hin (z. B.
Material vergessen, falsche Lagerung). Kandidaten liefert das Dashboard unter
„Häufige Fehlwerte".

## Vorlage: Modell-Detektiv-Fall

Ein Fall ist ein falsches Modell mit genau einer Fehlerursache. Die Seite zeigt
Strukturbaum und Details, die Studierenden klicken die verursachende Zeile an.

```markdown
<div class="detektiv-fall" data-fall="p1-kragarm-material" data-points="5" data-attempts="3"></div>
```

Inhalt in `content/detektiv/<name>.json` (wird nicht deployt):

- `titel`, `uebung`, `fall` (Situation mit falschem und erwartetem Wert), `tipp` (nach dem ersten Fehlgriff)
- `baum`: Liste der Knoten `{id, label, art, ebene, details}`; `art` färbt den Marker (einheiten, geometrie, material, netz, lager, symmetrie, last, ergebnis, ordner)
- `details`: Zeilen `{id, name, wert, grund}`; `grund` erklärt, warum die Zeile in Ordnung ist
- `fehler`: id der Fehlerzeile (sie bekommt keinen `grund`), `aufloesung`: Erklärung nach Treffer

Lösung und Begründungen landen beim Build nur in `answers.json`, nie im HTML.
Zahlenwerte am besten aus bekannten Fehlwerten (Dashboard, `data-diagnose`).

## Startseite eines Praktikums

```markdown
---
title: Geometrieaufbereitung und Randbedingungen
icon: material/cube
hide: [toc]
---

# Geometrieaufbereitung und Randbedingungen

!!! abstract "Lernziele"
    - [ ] …

<!-- uebersicht -->
```
