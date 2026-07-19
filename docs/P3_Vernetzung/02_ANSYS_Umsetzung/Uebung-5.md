---
hide:
 - toc
---

# Übung 5 - bikelab ROTOR Rahmen 

Im fünften Beispiel nehmen wir den ROTOR Rahmen der für unser Messfahrrad im bikelab von ROTOR hergestellt wurde. 

<figure style="text-align:center;">
  <img src="../images/Uebung-05.png" alt="Rahmen" width="700" class="no-lightbox">
</figure>

## Gegeben

### Material

Stahl

- Elastizitätsmodul $E=210 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}3$

### Geometrie

Es ist die Geometrie gegeben:

[:material-paperclip: Geometrie: Uebung-05-bikelab-Rahmen.scdoc](assets/Uebung-05-bikelab-Rahmen.scdoc)

### Vernetzung

- Verwenden Sie ein konvergierte Netzgröße im Bereich der Schweißnähte vom Steuerrohr zum Ober- und Unterrohr

### Randbedingungen


<figure style="text-align:center;">
  <img src="../images/Uebung-05-RB.excalidraw.png" alt="Einspannung" width="700" class="no-lightbox">
</figure>

Lagerung:

- die feste Lagerung im Bereich wo die Hinterradachse liegt mit Drehpunkt 390mm zum Boden (Verformung starr)
- Das Steuerrohr soll sich nur in Kraftrichtung bewegen können im Abstand wo sonst die Vorderradachse ist (x=210mm/y=-460mm vom Mittelpunkt des Steuerrohrs)

Belastung:

- Wo das Steuerrohr gelagert ist soll ebenfalls eine Kraft mit F=5000N in x-Richtung angreifen

## Aufgabenstellung

Berechnen Sie die Spannung in den Schweißnähten vom Steuerrohr zum Ober- und Unterrohr. Vernetzen Sie diese Schweißnähte entsprechend

## Hinweise

- Achten Sie darauf, dass sich die Bereiche wo normalerweise der Gabelschaft ist (Bereich des Kraftangriffs und der Lagerung vorne) der Bereich steif genug ist (so wie es normalerweise wäre, wenn sich dort diese Geometrien befinden). Schalten Sie ggf. für die Remote Forces/Displacement die Verformung aus.

- Nutzen Sie das Split Tool von SpaceClaim um den Bereich der maximalen Spannung kleiner zu machen

- Es könnte sein, dass die Rechentechnik im PC Pool nicht ausreicht für eine konvergierte Netzlösung

## Gesucht

Berechnen Sie die folgenden Größen:

### Die maximale von-Mises Vergleichsspannung in den Schweißnähten zum Steuerrohr $\sigma_{von Mises}$ in MPa

<div class="numeric-question" data-answer="86.1" data-tolerance="1" data-points="5" data-attempts="5"  data-hints="Remote/Force/Displacement auf rigid gestellt?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<br>

Netz: global 5mm , im Bereich des Spannungsmaximums: 0,25 mm
<br>
5mm: 62,635MPa
<br>
1mm : 72,44MPa
<br>
0,5mm : 74,662MPa
<br>
0,25mm : 86,16MPa

<figure style="text-align:center;">
  <img src="../images/Loesung-Uebung05-0-25mm.png" alt="Spannung 0,25mm Vernetzung" width="900">
  <figcaption>Spannung für 0,25mm Vernetzung</figcaption>
</figure>

</div>

