---
hide:
 - toc
---

# Durchbiegung von Photovoltaikwafern im Carrier

In der Herstellung von Solarzellen werden die Rohlinge (sogenannte Wafer) in Carriern gelagert:

<figure style="text-align:center;">
  <img src="../images/Wafer_Carrier.jpg" alt="Wafer Carrier" width="400" class="no-lightbox">
</figure>

Bei besonders dünnen Wafern und bei der vertikalen Ausrichtung der Carrier kann es da bereits zu sehr großen Durchbiegungen durch das Eigengewicht kommen, die wir nun berechnen wollen:

<figure style="text-align:center;">
  <img src="../images/Uebung04.excalidraw.png" alt="Uebung 4 - Wafer im Carrier" width="800" class="no-lightbox">
</figure>

## Gegeben

### Material

multikristallines Silizium

- Elastizitätsmodul: \(E = 163\,\mathrm{GPa}\)
- Querkontraktionszahl: \(\nu = 0{,}22\)
- Dichte: \(\rho = 2329 \frac{kg}{m^3}\)

## Symmetrie

- Verwenden Sie eine Viertelsymmetrie

### Geometrie

- Wafergrundfläche: \(156\,\mathrm{mm}\) x \(156\,\mathrm{mm}\)
- Waferdicke: \(0{,}1\,\mathrm{mm}\)

### Vernetzung

- Netzgröße global: \(1\,\mathrm{mm}\)

### Randbedingungen

**Lagerung:**

- An den Mittelpunkten der Kanten wird der Wafer jeweils in z-Richtung gehalten
- Die restliche Lagerung erfolgt durch die Symmetrie

**Belastung:**

- Fügen Sie `Standard Earth Gravity` hinzu (über die Dichte des Materials wird dadurch die Durchbiegung durch das Eigengewicht berechnet)  

## Aufgabenstellung

!!! abstract "Lösen Sie die Aufgabe mit der 2D-Abstraktion mit SHELL-Elementen und voller Ausnutzung jeglicher Symmetrien"

## Hinweise

??? tip "<code>HINWEIS</code> – Flächen erstellen (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/05_Flaechenstrukturen/Umsetzung.md:Flaechen_erstellen"

??? tip "<code>HINWEIS</code> – Dicke einstellen (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/05_Flaechenstrukturen/Umsetzung.md:Dicke_einstellen"

??? tip "<code>HINWEIS</code> – Elementdarstellung (klicken zum Aufklappen)"

    --8<-- "P4_Abstraktionen/04_Linienstrukturen/Umsetzung.md:Elementdarstellung"

## Gesucht

Berechnen Sie die folgenden Größen:

### Die maximale Durchbiegung im Bauteil \(u_\text{max}\) in mm

<div class="numeric-question" data-answer="0.4328" data-tolerance="0.02" data-points="5" data-attempts="5"  data-hints="Material zugeordnet? Dicke auf 0,1mm gestellt? Symmetrie richtig eingestellt? Gewichtskraft in richtige Richtung? Punkte nur in z-Richtung festhalten? (restliche Lagerung macht Symmetrie)">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung04_Sym.png" alt="Symmetrie" width="900">
  <figcaption>Symmetrie</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung04_RB.png" alt="Randbedingungen" width="900">
  <figcaption>Randbedingungen</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung04_umax.png" alt="maximale Durchbiegung" width="900">
  <figcaption>maximale Durchbiegung</figcaption>
</figure>

</div>
