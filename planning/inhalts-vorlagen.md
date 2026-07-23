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

<div class="numeric-question" data-answer="7.378" data-tolerance="0.1" data-points="5" data-attempts="5" data-hints="Einheit auf mm?"></div>

## Hinweise
!!! tip "Vorgehen"
    Im Strukturbaum `Rechtsklick Solution > Insert > Deformation`.

<div class="solution-images" markdown="1">
### 🎯 Lösung
**Wichtige Punkte:** …
</div>
```

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
