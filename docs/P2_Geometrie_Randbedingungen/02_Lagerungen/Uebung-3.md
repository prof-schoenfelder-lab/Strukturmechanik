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

[:material-paperclip: Uebung-03.wbpz](../assets/Uebung-03.wbpz)

## Aufgabenstellung

Nach dem Import der Archivdatei öffnen Sie die Geometrie mit SpaceClaim und ändern die Geometrie wie folgt:

- [ ] Fügen Sie die Lagerung analog des gegebenen Bildes ein nur mit der Randbedingung `Displacement` ein

## Gesucht

Berechnen Sie anschließend die folgenden Größen:

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="17.044" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt?">
</div>

### Die maximale von-Mises Vergleichsspannung $\sigma_{Mises, \max }$ in MPa

<div class="numeric-question" data-answer="29.692" data-tolerance="0.5" data-points="5" data-attempts="5"  data-hints="Einheit auf mm (MPa) gewechselt?">
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

<figure style="text-align:center;">
  <img src="../images/Uebung-03-Loesung-stress.png" alt="Spannung Lösung" width="700">
  <figcaption>von-Mises Vergleichsspannung</figcaption>
</figure>

</div>

