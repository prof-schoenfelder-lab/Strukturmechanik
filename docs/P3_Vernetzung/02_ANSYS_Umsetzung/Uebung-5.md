---
hide:
 - toc
---

# Übung 5: Schweißnaht am Fahrradrahmen

Im fünften Beispiel nehmen wir den Trekkingrahmen aus Praktikum 2 wieder auf und schauen uns die Schweißnaht zwischen Oberrohr und Steuerrohr an. Das Modell ist fertig aufgebaut, Sie kümmern sich nur um das Netz. Im Praktikum liegt der Rahmen aus, dort können Sie sich die Naht direkt ansehen.

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Rahmen.excalidraw.png" alt="Rahmen von der Seite und Nahaufnahme der Schweißnaht zwischen Oberrohr und Steuerrohr: Fase blau, die beiden Radien rot" width="900">
</figure>

## Gegeben

### Archiv mit Rahmen, Dummies, Material, Lagerung und Kraft

[:material-paperclip: Uebung-05-Rahmen.wbpz](assets/Uebung-05-Rahmen.wbpz)

Wie das Archiv importiert wird, steht auf der Seite [Globale Netzverfeinerung](Globale_Netzverfeinerung.md#import-der-archivdatei).

### Material

Rahmen aus Aluminium, Dummies aus Stahl (`Structural Steel`)

- Elastizitätsmodul Aluminium: \(E = 70\,\text{GPa}\)
- Querkontraktionszahl Aluminium: \(\nu = 0{,}34\)

### Randbedingungen

Lagerung und Kraft sind im Archiv gesetzt, hier ändern Sie nichts.

- Kraft \(F = 450\,\text{N}\) in Fahrtrichtung, wie bei der Rahmenprüfung mit horizontalen Kräften nach DIN EN ISO 4210-6 für City- und Trekkingräder

### So ist die Naht modelliert

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Naht.excalidraw.png" alt="Schnitt durch die Naht: am Rahmen wechseln Breite und Form, im Modell eine Fase von 7 mm mit rund 10 mm Breite und an beiden Übergängen ein Radius von 1 mm" width="800" class="no-lightbox">
</figure>

- Am Rahmen wechseln Breite und Form der Naht. Im Modell steht deshalb eine gleichmäßige Fase von 7 mm, das ergibt die am Rahmen gemessene Breite von rund 10 mm.
- Wenn am Übergang zwischen Fase und Rohr kein Radius modelliert ist, entsteht dort eine scharfe Kante und damit eine Singularität. Deshalb sitzt an beiden Übergängen ein Radius von 1 mm.
- Fase und Radius lehnen sich an die [IIW-Empfehlungen für Schweißnähte](https://svv.cz/files/IIW182307FatigueRecomm20121017.pdf) an. Dort ist der Radius erst ab 5 mm Wanddicke vorgesehen, hier ist die Wand 1,8 mm dick. Für diese Netzstudie ist das eine Modellannahme, die Spannung ist kein Festigkeitsnachweis.

## Aufgabenstellung

Die von-Mises-Vergleichsspannung in der Schweißnaht zwischen Oberrohr und Steuerrohr berechnen und das Netz dort verfeinern, bis es konvergiert ist. Die globale Elementgröße bleibt immer 5 mm, die lokale wird von 0,5 mm über 0,25 mm auf 0,125 mm halbiert.

- [ ] Globales Netz einstellen: `Strukturbaum → Mesh` auswählen und `Detailfenster → Element Size: 5 mm` eingeben (Einheit auf mm!). Mit dem Standardnetz lässt sich der Rahmen nicht vernetzen.
- [ ] Lokale Netzverfeinerung auf beide Radien setzen (rot im Bild oben): die Flächen mit `STRG` gedrückt halten auswählen, dann `Rechtsklick Strukturbaum Mesh → Insert → Sizing` und `Detailfenster → Element Size: 0,5 mm` eingeben. Die Radien sind schmal, dafür nah heranzoomen. Unter `Detailfenster → Geometry` steht dann `8 Faces`, eine winzige neunte Fläche können Sie weglassen.
- [ ] Spannung nur in der Naht auswerten: `Rechtsklick Strukturbaum Solution → Insert → Stress → Equivalent (von-Mises)`, dann unter `Detailfenster → Geometry` die Fase und beide Radien auswählen (blau und rot im Bild oben), zusammen `12 Faces`.
- [ ] Lösen und die maximale Spannung ablesen.
- [ ] Die lokale Elementgröße unter `Strukturbaum → Mesh → Face Sizing` auf 0,25 mm und dann auf 0,125 mm halbieren, jeweils lösen und ablesen.

## Gesucht

### Die maximale von-Mises-Vergleichsspannung \(\sigma_\text{von Mises}\) in der Naht in MPa, mit konvergiertem Netz

<div class="numeric-question" data-answer="43.68" data-tolerance="0.7" data-points="5" data-attempts="5" data-hints="Einheit auf mm gewechselt? Global 5 mm eingestellt? Face Sizing auf beiden Radien der Naht? Ergebnis nur auf der Naht zwischen Oberrohr und Steuerrohr ausgewertet? Lokal bis 0,125 mm verfeinert?" data-diagnose="35.68: Das ist der Wert für lokal 0,5 mm. Hier ist das Netz noch nicht konvergiert, die lokale Elementgröße weiter halbieren.">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Konvergenz.excalidraw.png" alt="Spannung in der Naht über der lokalen Elementgröße: 35,68 MPa bei 0,5 mm, 43,36 MPa bei 0,25 mm und 43,68 MPa bei 0,125 mm" width="700">
  <figcaption>Spannung in der Naht über der lokalen Elementgröße</figcaption>
</figure>

<table border="1">
  <tr>
    <th>lokale Elementgröße</th>
    <th>Spannung in der Naht</th>
    <th>Änderung zur vorigen Stufe</th>
  </tr>
  <tr>
    <td>0,5&nbsp;mm</td>
    <td>35,68&nbsp;MPa</td>
    <td></td>
  </tr>
  <tr>
    <td>0,25&nbsp;mm</td>
    <td>43,36&nbsp;MPa</td>
    <td>21,5&nbsp;%</td>
  </tr>
  <tr>
    <td>0,125&nbsp;mm</td>
    <td>43,68&nbsp;MPa</td>
    <td>0,7&nbsp;%</td>
  </tr>
</table>

<p>Von 0,25&nbsp;mm auf 0,125&nbsp;mm ändert sich die Spannung um weniger als 1&nbsp;%, damit gilt das Netz als konvergiert.</p>

<p>Die Radien sind im Mittel nur rund 0,5&nbsp;mm breit. Wenn die lokale Elementgröße ebenso groß ist, liegt nur ein Element auf dem Radius und das Netz bildet den Spannungsanstieg dort nicht ab.</p>

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Loesung.png" alt="Vergleichsspannung in der Naht bei lokal 0,125 mm: das Maximum liegt am Radius am Oberrohr, an der Unterseite des Rohrs" width="900">
  <figcaption>Spannungsverteilung bei lokal 0,125&nbsp;mm, das Maximum liegt am Radius am Oberrohr, an der Unterseite des Rohrs</figcaption>
</figure>

</div>
