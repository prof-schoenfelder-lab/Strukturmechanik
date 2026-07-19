---
hide:
 - toc
---

# Übung 3 - Kurbelarm

Im dritten Beispiel wenden wir nun das Gelernte bezüglich der Vernetzung an einem Kurbelarm an.

<figure style="text-align:center;">
  <img src="../images/Kurbelarm.png" alt="Kurbelarm" width="500" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminium

- Elastizitätsmodul $E=70 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}34$

### Geometrie

Es ist die Geometrie gegeben:

[:material-paperclip: Geometrie: Uebung-03-Kurbelarm.scdoc](assets/Uebung-03-Kurbelarm.scdoc)

### Vernetzung

- Eine konvergierte Netzgröße im Bereich der maximalen Spannung verwenden

### Randbedingungen

Lagerung:

- Der Kurbelarm soll an der Stelle (Einspannung) so gelagert werden, als wäre er an einer feststehenden Achse befestigt.

Belastung:

- Die Gewichtskraft einer Person auf das Pedal soll abstrahiert werden. Dazu wird eine Kraft $F=800 \mathrm{N}$ in negativer x-Richtung auf die (Bohrung) ausgeübt, wobei der Angriffspunkt 50 mm in negativer y-Richtung vom Mittelpunkt der (Bohrung) entfernt liegt. 

## Aufgabenstellung

Die maximale Verformung und maximale von-Mises Vergleichsspannung für das Bauteil mit einem konvergiertem Netz berechnen.

## Gesucht

Die folgenden Größen berechnen:

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="1.0" data-tolerance="0.05" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Kraft in negative x-Richtung mit 50mm Abstand von Mittelpunkt der Bohrung?">
</div>

### Die maximale von-Mises Vergleichsspannung $\sigma_{von Mises}$ in MPa

<div class="numeric-question" data-answer="99.5" data-tolerance="2" data-points="5" data-attempts="5"  data-hints="Spannung außerhalb der festen Einspannung ausgewertet? Netz genug verfeinert?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<br>

Netz: global 3mm , im Bereich des Spannungsmaximums: 0,1 mm

<figure style="text-align:center;">
  <img src="../images/Loesung-Uebung03-FixedSupport.png" alt="Lagerung Spannung Fixed Support" width="900">
  <figcaption>Spannung mit Fixed Support</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Loesung-Uebung03-RemoteDisplacement.png" alt="Lagerung Spannung Fixed Support" width="900">
  <figcaption>Spannung mit Remote Displacement</figcaption>
</figure>

</div>

