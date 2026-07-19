---
hide:
 - toc
---

# Lagerungsbeispiel Lineal über Kante belastet

Im dritten Beispiel versuchen wir Lagerungsbedingungen aus einem realen Beispiel (Lineal über Kante) in Randbedingungen in ANSYS zu übertragen:

<figure style="text-align:center;">
  <img src="../images/Lagerungsbeispiel_Lineal.png" alt="Lineal" width="500" class="no-lightbox">
</figure>

## Gegeben

Es ist das gesamte Projektarchiv gegeben (Material,Geometrie,Netz und Belastung):

[:material-paperclip: Uebung-03.wbpz](assets/Uebung-03.wbpz)

## Aufgabenstellung

Nach dem Import der Archivdatei die Geometrie mit SpaceClaim öffnen und wie folgt ändern:

- [ ] Die Lagerung analog des gegebenen Bildes nur mit der Randbedingung `Displacement` einfügen

## Gesucht

Anschließend die folgenden Größen berechnen:

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="17.044" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt?">
</div>


<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-03-Loesung-Randbedingungen.png" alt="Lagerung Lösung" width="500">
  <figcaption>Randbedingung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-03-Loesung-disp.png" alt="Verschiebung Lösung" width="700">
  <figcaption>Gesamtverschiebung</figcaption>
</figure>

</div>

