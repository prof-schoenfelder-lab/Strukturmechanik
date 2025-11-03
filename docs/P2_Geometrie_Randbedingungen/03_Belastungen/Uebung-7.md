---
hide:
 - toc
---

# Lenkkopfsteifigkeit Fahrradrahmen

Im siebten Beispiel verwenden wir erneut den vereinfachten Fahrradrahmen. Wer dies in dem vorherigen Teil nicht gemacht hat, kann auch die gegebene Geometrie verwenden. 

<figure style="text-align:center;">
  <img src="../images/Uebung-07.excalidraw.png" alt="Fahrradrahmen mit externen Kräften" width="700" class="no-lightbox">
</figure>

## Gegeben

### Material

Aluminiumlegierung 6061-T6

- Elastizitätsmodul $E=68{,}3 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0{,}33$

### Geometrie

Selbstvereinfachte Rahmengeometrie oder diese fertig aufbereitete:

[:material-paperclip: TrekkingRahmen_vereinfacht.scdoc](assets/TrekkingRahmen_vereinfacht.scdoc)

### Vernetzung

- Netzgröße global: 10 mm

### Randbedingungen

Lagerung:

- Feste Einspannung im Bereich der hinteren Achslagerung

Belastung:

- Kraft $F_{x}=100\,\mathrm{N}$ horizontal quer zur Fahrtrichtung auf den Remote Point

## Hinweis

Für die Remote Force müssen Sie ein neues Koordinatensystem in das Steuerrohr setzen und gleichzeitig die y-Achse als Referenz auswählen damit die Richtung der y-Achse der Richtung des Steuerrohrs entspricht. Dadurch können Sie den Abstand von 1000mm vom Mittelpunkt des Steuerrohrs genau einstellen.

<figure style="text-align:center;">
  <img src="../images/Uebung-07-Koordinatensystem.png" alt="Koordinatensystem" width="600" class="no-lightbox">
</figure>



## Gesucht

Berechnen Sie anschließend die folgenden Größen:

### Die maximale Verschiebung in x-Richtung $u_{x,max}$ in mm

<div class="numeric-question" data-answer="3.1152" data-tolerance="0.25" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Koordinatensystem eingefügt? Kraft in richtige Richtung? Richtige Verschiebungsrichtung ausgewertet?">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-07-Loesung-RB.png" alt="Lagerung Lösung" width="500">
  <figcaption>Randbedingung (Fixiertes Lager im Bereich der Achsauflage)</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-07-Loesung-disp.png" alt="Verschiebung Lösung" width="700">
  <figcaption>Gesamtverschiebung</figcaption>
</figure>

</div>

