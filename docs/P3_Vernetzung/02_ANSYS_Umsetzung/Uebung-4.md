---
hide:
 - toc
---

# Übung 4 – Vorbau 

Im vierten Beispiel betrachten wir einen aktuell im bikelab laufenden Dauerversuch an einem Vorbau. 

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Vorbau.jpeg" alt="Vorbau" width="700" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminium

- Elastizitätsmodul: \(E = 70\,\text{GPa}\)
- Querkontraktionszahl: \(\nu = 0{,}34\)

### Geometrie

Folgende Geometrie ist gegeben:

[:material-paperclip: Geometrie: Uebung-04-Vorbau.scdoc](assets/Uebung-04-Vorbau.scdoc)

### Vernetzung

- Eine **konvergierte Netzgröße** im Bereich der maximalen Spannung verwenden.

### Randbedingungen

**Lagerung:**

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Vorbau-Einspannung.png" alt="Einspannung" width="700" class="no-lightbox">
</figure>

- Im Bereich, in dem normalerweise der Gabelschaft angreift, soll der Vorbau fest eingespannt sein.

**Belastung:**

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Vorbau-Kraft0.png" alt="Kraft Angriffsfläche" width="700" class="no-lightbox">
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Vorbau-Kraft1.png" alt="Kraft Abstand in y-Richtung" width="700" class="no-lightbox">
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Vorbau-Kraft2.png" alt="Kraft Abstände in y- und z-Richtung" width="700" class="no-lightbox">
</figure>

- Es greifen zwei Kräfte im markierten Bereich an, die in negativer \(y\)-Richtung einen Abstand von \(120\,\text{mm}\) besitzen und in \(z\)-Richtung vom Nullpunkt jeweils \(220\,\text{mm}\) entfernt sind.  
  Der Kraftvektor zeigt in negative \(x\)-Richtung mit einem Betrag von \(600\,\text{N}\).

## Aufgabenstellung

Die maximale Verformung und die maximale von-Mises-Vergleichsspannung für das Bauteil mit einem konvergierten Netz berechnen.

## Hinweise

- Mit dem **Split-Tool** lässt sich der Bereich, in dem das Netz verfeinert wird, etwas kleiner machen.
- Darauf achten, dass die Bereiche, in denen sich normalerweise der Gabelschaft befindet (Bereich der festen Einspannung) und in denen der Lenker angreift (Kraftangriffsfläche), insgesamt steif genug sind – so, wie es im realen Aufbau mit eingebautem Gabelschaft und Lenker der Fall wäre.  
  Ggf. bei den **Remote Forces** die Verformung (Deformation) ausschalten.

## Gesucht

Die folgenden Größen berechnen:

### Die maximale Durchbiegung \(u_{\max}\) in mm

<div class="numeric-question" data-answer="0.35953" data-tolerance="0.05" data-points="5" data-attempts="5" data-hints="Einheit auf mm gewechselt? Kräfte mit richtigem Abstand und Richtung?">
</div>

### Die maximale von-Mises-Vergleichsspannung \(\sigma_\text{von Mises}\) in MPa

<div class="numeric-question" data-answer="161.23" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Spannung außerhalb der festen Einspannung ausgewertet? Kraftangriffsfläche auf starr gestellt? Netz fein genug?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<br>

Netz: global 1&nbsp;mm, im Bereich des Spannungsmaximums: 0,25&nbsp;mm  
<br>
1&nbsp;mm: 162,58&nbsp;MPa  
<br>
0,5&nbsp;mm: 161,58&nbsp;MPa  
<br>
0,25&nbsp;mm: 161,48&nbsp;MPa  
<br>
0,1&nbsp;mm: 161,96&nbsp;MPa

<figure style="text-align:center;">
  <img src="../images/Loesung-Uebung04-0-25mm.png" alt="Spannung 0,25 mm Vernetzung" width="900">
  <figcaption>Spannung für 0,25&nbsp;mm Vernetzung</figcaption>
</figure>

</div>