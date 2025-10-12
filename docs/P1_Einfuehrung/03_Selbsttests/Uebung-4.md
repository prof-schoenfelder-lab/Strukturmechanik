---
hide:
---

# Lenker

Dies ist ebenfalls eher ein realistischeres (wobei immer noch sehr vereinfachtes Bauteil). 

<figure style="text-align:center;">
  <img src="../images/Uebung-04.png" alt="Lenker" width="600" class="no-lightbox">
</figure>

## Gegeben

### Material

Alu

- Elastizitätsmodul $E=70 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0,34$

### Vernetzung

- Netzgröße global: 1,5 mm

### Geometrie

[:material-paperclip: Lenker.scdoc](../assets/Lenker.scdoc)


### Randbedingungen

Lagerung:

- feste Einspannung im mittleren Bereich auf einer Breite von 50mm (Klemmung Vorbau)

Belastung:

Linke Handauflage auf einer Breite von 80mm:<br>
- Kraft $F_y=-200 \mathrm{N}$ (Richtung Boden)<br>
- Kraft $F_z=-500 \mathrm{N}$ (Fahrtrichtung)<br>

Rechte Handauflage auf einer Breite von 80mm:<br>
- Kraft $F_y=-200 \mathrm{N}$ (Richtung Boden)<br>
- Kraft $F_z=-500 \mathrm{N}$ (Fahrtrichtung)<br>

## Hinweise

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">von-Mises Spannung einfügen</p>
    <p>im Strukturbaum: <code>Rechtsklick</code> auf <code>Solution</code> und anschließend auf <code>Insert</code> > <code>Stress</code> > <code>Equivalent (von-Mises)</code> klicken.</p>
    <figure style="text-align:center;">
    <img src="../images/vonMisesSpannung.png" alt="von Mises Spannung einfügen" width="600" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ort der maximalen Spannung anzeigen</p>
    <p>Im Strukturbaum (unter Solution) von Mises Spannung auswählen</p> 
    <p>In der Menüleiste oben: Reiter<code>Result</code> auf <code>Maximum</code> klicken.</p>
    <figure style="text-align:center;">
    <img src="../images/Stress_Maximum.png" alt="Ort der Maximalen Spannung anzeigen" width="600" class="no-lightbox">
    <p>Im Grafikfenster erscheint ein Hinweis mit dem Maximum</p> 
    </figure>
  </div>

</div>

## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="17.8" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Material zugeordnet? Kraft jeweils auf beide Handflächen separat mit richtigen Kraftkomponenten?">
</div>

<!---
Fixed Support: 17.361mm
RemoteDisp+Frictionless Support (Fläche): 18.24mm
-->

### Die maximale Spannung in von-Mises Spannung 

<div class="numeric-question" data-answer="271.05" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Spannung an Singularität? (Oben Tab Result > Maximum) ggf. Randbedingung für fixierte Lagerung überdenken">
</div>

<!---
Fixed Support: 288,8MPa
RemoteDisp+Frictionless Support (Fläche): 271.05MPa
-->