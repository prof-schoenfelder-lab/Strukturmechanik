---
hide:
 - toc
---

# Kugel-Ring Versuch

Das Beispiel für die Rotationssymmetrie ist ein klassischer Werksttoffversuch für spröde Materialien, der Kugel-Ring Versuch. Dabei liegt eine Scheibe auf einem Auflagerring auf und wird in der Mitte mit einer Kugel belastet (hier als Einzelkraft abstrahiert):

<figure style="text-align:center;">
  <img src="../images/KugelRing.excalidraw.png" alt="Kugel-Ring Versuch" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Glas

- Elastizitätsmodul: \(E = 70\,\mathrm{GPa}\)
- Querkontraktionszahl: \(\nu = 0{,}23\)

### Geometrie

Balken mit rechteckigem Querschnitt

- Auflagerradius \(r = 30\,\mathrm{mm}\)
- Probenradius \(R = 40\,\mathrm{mm}\)
- Probendicke \(h = 5\,\mathrm{mm}\)

### Vernetzung

- Netzgröße global: \(0,5\,\mathrm{mm}\) (in 2D können wir feiner vernetzen)

### Randbedingungen

**Lagerung:**

- entsprechend Skizze

**Belastung:**

- Die Kraft $F=1000\,\mathrm{N}$ wird aus numerischen Gründen auf eine Fläche mit dem Radius von 1mm verteilt.

## Aufgabenstellung

!!! abstract "Lösen Sie die Aufgabe mit der 2D Abstraktion / Rotationssymmetrie"

## Hinweise


??? tip "<code>HINWEIS</code> – Geometrie (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/03_Rotationssymmetrie/Umsetzung.md:Geometrie"

??? tip "<code>HINWEIS</code> – Workbench Projektmenü Einstellungen (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/03_Rotationssymmetrie/Umsetzung.md:WBProjektmenue"

??? tip "<code>HINWEIS</code> – Mechanical-Einstellungen (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/03_Rotationssymmetrie/Umsetzung.md:Mechanical"

??? tip "<code>HINWEIS</code> – Randbedingungen (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/03_Rotationssymmetrie/Umsetzung.md:Randbedingungen"

??? tip "<code>HINWEIS</code> 1. Hauptspannung (klicken zum aufklappen)"

    Die erste Hauptspannung befindet sich unter `Stress` > `Maximum Principal Stress`

    Die erste Hauptspannung wird als Versagenskriterium für spröde Werkstoffe verwendet. 


## Gesucht

Berechnen Sie die folgenden Größen:

### Die maximale Durchbiegung im Bauteil \(u_\text{max}\) in mm

<div class="numeric-question" data-answer="0.64" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Loslager am Ring eingestellt? Material zugeordnet? Rotationssymmetrie eingestellt?">
</div>

### Die maximale 1. Hauptspannung im Bauteil \(\sigma_\text{1}\) in MPa

<div class="numeric-question" data-answer="82.5" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Loslager am Ring eingestellt? Material zugeordnet? Rotationssymmetrie eingestellt?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung03_umax.png" alt="maximale Durchbiegung" width="900">
  <figcaption>Maximale Durchbiegung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung03_sigmamax.png" alt="maximale Vergleichsspannung" width="900">
  <figcaption>Maximale Vergleichsspannung</figcaption>
</figure>

</div>
