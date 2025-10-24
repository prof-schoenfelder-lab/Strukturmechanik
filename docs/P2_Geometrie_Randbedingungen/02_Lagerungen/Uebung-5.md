---
hide:
 - toc
---

# vereinfachte Fahrradbremse (v-Break)

Im fünften Beispiel schauen wir uns ein Teil einer stark vereinfachten Fahrradbremse an die drehbar gelagert wird und an der Stelle wo normalerweise die Bremsbelege sind gehalten werden soll und mit einer Zugkraft beaufschlagt wird.


<figure style="text-align:center;">
  <img src="../images/Uebung-05.png" alt="vereinfachte v-Break" width="700" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul $E=210\,\mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}3$

### Geometrie

stark vereinfachte v-Break: 

[:material-paperclip: v_Break_vereinfacht.scdoc](../assets/v_Break_vereinfacht.scdoc)

### Vernetzung

- Netzgröße global: 1 mm

### Randbedingungen

Lagerung:

- Drehbar gelagert 
- Elastische Bettung m Bereich des Bremsklotz mit Fundamentsteifigkeit $k=30/,N/mm^3 $ 

Belastung:

- Kraft $F_z=-200\,\mathrm{N}$

## Gesucht

Berechnen Sie anschließend die folgenden Größen:

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="1.666" data-tolerance="0.1" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Beim cylindrical Suppprt die tangentiale Richtung freigegeben?">
</div>

### Betrag der mittleren Verschiebung der elastischen Bettung in z-Richtung $u_{z,}$ in mm

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Fläche auswählen</p>
    <p>Die Fläche an der die elastische Bettung wirkt auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Directional Deformation einfügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> > <code>Insert</code> > <code>Deformation</code> > <code>Directional</code></p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">z-Achse auswählen</p>
    <p>Im Detailfenster: Unter <code>Orientation</code> die <code>z-Achse</code> auswählen</p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">Mittelwert auslesen</p>
    <p>Im Detailfenster: Unter <code>Results</code> den Mittelwert auslesen</p>
  </div>

</div>

<div class="numeric-question" data-answer="0.5" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Betrag eingegeben? Fläche ausgewählt? in z-Richtung ausgewertet?">
</div>

### Die maximale von-Mises Vergleichsspannung $\sigma_{Mises, \max }$ in MPa

<div class="numeric-question" data-answer="27.473" data-tolerance="0.25" data-points="5" data-attempts="5"  data-hints="Einheit auf mm (MPa) gewechselt?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Loesung-RB.png" alt="Lagerung" width="500">
  <figcaption>Lagerung (cylindrical mit tangential frei)</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Loesung-stress.png" alt="Spannung Lösung" width="500">
  <figcaption>Spannung Lösung"</figcaption>
</figure>

</div>

