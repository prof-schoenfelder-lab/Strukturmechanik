---
hide:
 - toc
---

# Kragarm mit Einzelkraft

Und nun unser zweites Beispiel in 2D:

<figure style="text-align:center;">
  <img src="../images/Uebung02-2D.excalidraw.png" alt="Kragarm mit Einzelkraft" width="400" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminium

- Elastizitätsmodul $E=70 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}34$

### Geometrie

Balken mit rechteckigem Querschnitt

- Länge $L=500 \mathrm{mm}$
- Breite $b=30 \mathrm{mm}$
- Breite $h=60 \mathrm{mm}$

### Vernetzung

- Netzgröße global: 5 mm

### Randbedingungen

Lagerung:

- Feste Einspannung auf der Stirnseite links

Belastung:

- Kraft $F=3000 \mathrm{N}$ auf der Kante rechts

!!! danger "Wird die Kraftangriffsfläche geteilt, muss die Kraft auch durch Anzahl der Symmetrie geteilt werden"

    Die Kraft würde sich im Vollmodell auf die ganze Fläche aufteilen. Hier wird durch die Symmetrie aber eine kleinere Fläche verwendet und daher muss auch der Kraftwert geändert werden. 

## Aufgabenstellung

!!! abstract "Lösen Sie die Aufgabe mit der 2D Abstraktion / Ebener Spannungszustand"

## Hinweise

??? tip "<code>HINWEIS</code> – Geometrie (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/02_ESZ/Umsetzung.md:Geometrie"

??? tip "<code>HINWEIS</code> – Workbench Projektmenü Einstellungen (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/02_ESZ/Umsetzung.md:WBProjektmenue"

??? tip "<code>HINWEIS</code> – Mechanical (klicken zum aufklappen)"

    --8<-- "P4_Abstraktionen/02_ESZ/Umsetzung.md:Mechanical"

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="3.3462" data-tolerance="0.1" data-points="5" data-attempts="5"  data-hints="Material richtig? Dicke richtig? Kraft in negative y-Richtung?">
</div>
