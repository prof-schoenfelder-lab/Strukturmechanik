---
hide:
 - toc
sektion: Lagerungen
title: Übung 3
order: 120
kurz: Lagerungsbeispiel Lineal über Kante belastet
thumb: images/Lagerungsbeispiel_Lineal.png
---

# Lagerungsbeispiel Lineal über Kante belastet

Im dritten Beispiel versuchen wir Lagerungsbedingungen aus einem realen Beispiel (Lineal über Kante) in Randbedingungen in ANSYS zu übertragen:

<figure style="text-align:center;">
  <img src="../images/Lagerungsbeispiel_Lineal.png" alt="Lineal" width="500" class="no-lightbox">
</figure>

## Gegeben

Es ist das gesamte Projektarchiv gegeben (Material,Geometrie,Netz und Belastung):

[:material-paperclip: Uebung-03.wbpz](assets/Uebung-03.wbpz)

Wie das Archiv importiert wird, steht in [Übung 1](../01_Geometrie_anpassen/Uebung-1.md#archiv-importieren).

## Aufgabenstellung

Nach dem Import der Archivdatei in Mechanical die Lagerung wie folgt ergänzen:

- [ ] Die Lagerung analog des gegebenen Bildes nur mit der Randbedingung `Displacement` einfügen

<div class="hotspot-frage" data-fall="p2-lineal" data-points="3" data-attempts="2"></div>

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

<div class="zwischenspiel" data-seite="/P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/Uebung-1,/P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/Uebung-2,/P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-3" data-voraussetzung="Übung 1 bis 3" data-name="Lineal (Übung 3)" data-teil="bau-2l4.______________.lB601fTk31.T031628">
<h2>Zwischenspiel: Knackpunkt</h2>
<p>Das Lineal aus dieser Übung: 210 mm lang, es liegt 60 mm vom freien Ende auf der Tischkante auf und ist am anderen Ende geklemmt. Die Tischkante ist ein Loslager, das nur nach oben drückt, die Klemmung ein Festlager. Im Spiel ist das Lineal 40 mm hoch und eine 10 mm dicke Platte aus Stahl S235, am freien Ende drücken 8 kN. Nehmen Sie so viel Material weg wie möglich, ohne dass es versagt.</p>
</div>
