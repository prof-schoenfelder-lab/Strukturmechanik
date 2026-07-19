---
hide:
 - toc
---

# Zweiseitig gelagerter Balken mit Flächenlast

Wieder unser bekanntes Beispiel, diesmal in 2D Abstraktion

<figure style="text-align:center;">
  <img src="../images/Uebung01-2D.excalidraw.png" alt="Uebung 1 2D" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul: \(E = 210\,\mathrm{GPa}\)
- Querkontraktionszahl: \(\nu = 0{,}3\)

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge \(L = 1000\,\mathrm{mm}\)
- Breite \(b = 30\,\mathrm{mm}\)
- Höhe \(h = 30\,\mathrm{mm}\)

### Vernetzung

- Netzgröße global: \(5\,\mathrm{mm}\) (in 2D können wir feiner vernetzen)

### Randbedingungen

**Lagerung:**

- entsprechend Skizze

**Belastung:**

- Gleichmäßig verteilte Belastung mit einer resultierenden Kraft  
  \(F = 1000\,\mathrm{N}\) über die gesamte Balkenlänge  
  (entspricht einer Streckenlast \(q_0 = 1\,\mathrm{N/mm}\)).

## Aufgabenstellung

!!! abstract "Die Aufgabe mit der 2D Abstraktion / Ebener Spannungszustand lösen"

!!! abstract "Zusatz: Alle möglichen Symmetrien verwenden"


## Hinweise


??? tip "<code>HINWEIS</code> – Geometrie (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/02_ESZ/Umsetzung.md:Geometrie"

??? tip "<code>HINWEIS</code> – Workbench Projektmenü Einstellungen (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/02_ESZ/Umsetzung.md:WBProjektmenue"

??? tip "<code>HINWEIS</code> – Mechanical (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/02_ESZ/Umsetzung.md:Mechanical"

## Gesucht

Die folgenden Größen berechnen:

### Die maximale Durchbiegung im Bauteil \(u_\text{max}\) in mm

<div class="numeric-question" data-answer="0.921" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Dicke auf 30mm gestellt? Kraft in negative y-Richtung?">
</div>

### Die maximale von-Mises-Vergleichsspannung im Bauteil \(\sigma_\text{von Mises}\) in MPa

<div class="numeric-question" data-answer="27.784" data-tolerance="0.25" data-points="5" data-attempts="5"  data-hints="Dicke auf 30mm gestellt? Kraft in negative y-Richtung?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung01_2D_umax.png" alt="maximale Durchbiegung" width="900">
  <figcaption>Maximale Durchbiegung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung01_2D_sigmamax.png" alt="maximale Vergleichsspannung" width="900">
  <figcaption>Maximale Vergleichsspannung</figcaption>
</figure>

</div>
