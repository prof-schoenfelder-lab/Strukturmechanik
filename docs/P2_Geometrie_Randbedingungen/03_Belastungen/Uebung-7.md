---
hide:
 - toc
sektion: Belastungen
title: Übung 5
order: 220
kurz: Lenkkopfsteifigkeit Fahrradrahmen
thumb: images/Uebung-07.excalidraw.png
---

# Lenkkopfsteifigkeit Fahrradrahmen

Im fünften Beispiel verwenden wir erneut den vereinfachten Fahrradrahmen. Wer dies in dem vorherigen Teil nicht gemacht hat, kann auch die gegebene Geometrie verwenden. 

So wird die Lenkkopfsteifigkeit gemessen, zum Beispiel in den Rahmentests von Fahrradmagazinen: Der Rahmen ist an den Ausfallenden eingespannt. Im Steuerrohr steckt ein Vollprofil, also eine massive Stange, die viel steifer ist als das Steuerrohr selbst. An ihrem Ende, 1000&nbsp;mm vom Mittelpunkt des Steuerrohrs entfernt, greift die Kraft quer zur Fahrtrichtung an.

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

- Kraft $F=100\,\mathrm{N}$ horizontal quer zur Fahrtrichtung am Ende des Vollprofils, 1000&nbsp;mm vom Mittelpunkt des Steuerrohrs (Remote Point)

## Hinweis

Für die Remote Force muss ein neues Koordinatensystem in das Steuerrohr gesetzt und gleichzeitig die y-Achse als Referenz ausgewählt werden damit die Richtung der y-Achse der Richtung des Steuerrohrs entspricht. Dadurch lässt sich der Abstand von 1000mm vom Mittelpunkt des Steuerrohrs genau einstellen.

<figure style="text-align:center;">
  <img src="../images/Uebung-07-Koordinatensystem.png" alt="Koordinatensystem" width="600" class="no-lightbox">
</figure>



## Gesucht

Anschließend die folgenden Größen berechnen:

### Die größte Verschiebung in Richtung der Kraft, als Betrag ohne Vorzeichen, in mm

Je nachdem, in welche Richtung die x-Achse zeigt, steht dieser Wert in ANSYS als Max oder als Min der Directional Deformation.

<div class="numeric-question" data-answer="3.1152" data-tolerance="0.25" data-points="5" data-attempts="5"  data-hints="Einheit auf mm gewechselt? Koordinatensystem eingefügt? Verschiebung in Kraftrichtung ausgewertet und als Betrag eingegeben? Netzgröße 10 mm eingestellt? Wie steif ist das Vollprofil im Steuerrohr?" data-diagnose="1.064: Dieser Wert entsteht mit dem Standardmaterial Structural Steel (E = 200 GPa) statt Aluminium 6061-T6 (E = 68,3 GPa). Ist das vorgegebene Material angelegt und dem Körper zugeordnet? | -3.1152: Richtiger Wert, aber mit Vorzeichen. Gefragt ist der Betrag. | 0.67617: Das ist die größte Verschiebung entgegen der Kraft. Gefragt ist die Verschiebung in Kraftrichtung, je nach Achsrichtung steht sie unter Min.">
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
  <figcaption>Verschiebung in x-Richtung (Directional Deformation), Kraft hier in positiver x-Richtung. Zeigt die Kraft in negative x-Richtung, steht derselbe Wert als Min: −3,1152&nbsp;mm.</figcaption>
</figure>

</div>

