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

<!-- ENTWURF 12.11.2026 (Felix: „Ja, zum 16.11.“): Übung 5 mit Inflation wie das L-Profil.
     Sollwert 0,125 mm mit Inflation: 107,15 MPa (Felix 11.11., 1000 N, global 5 mm) mal 0,45 = 48,22 MPa.
     Mit Inflation bei global 5 mm und 450 N (Felix 12.11.): lokal 0,5 mm 38,028, 0,25 mm 46,891 MPa, also +23,3 % und +2,8 %.
     Felix 12.11.: Die Studierenden hören bei 0,125 mm auf, die Lösung nennt die 2,8 % und die Kontrollrechnung.
     Bild Uebung-05-Konvergenz: bilder/P3_Vorgehen_excalidraw.py Uebung-05-Konvergenz im Vault (KURS_REPO=…-entwurf).
     Ohne Inflation (Netzstudie 06.11., global 5 mm): 35,68, 43,36, 43,68 MPa; global 2,5 mm, lokal 0,075 mm: 46,246 MPa (Felix 12.11.),
     mit Inflation dort 48,693 MPa (Felix 11.11.); mit global 5 mm vernetzt ANSYS lokal 0,075 mm nicht.
     Boundary der Inflation: die Radiusflächen wie beim Sizing (Felix, 12.11.). -->

## Aufgabenstellung

Die von-Mises-Vergleichsspannung in der Schweißnaht zwischen Oberrohr und Steuerrohr berechnen und das Netz dort in drei Stufen verfeinern. Die globale Elementgröße bleibt immer 5 mm, die lokale wird von 0,5 mm über 0,25 mm auf 0,125 mm halbiert. Auf beiden Radien liegt dabei eine Inflation, wie beim L-Profil auf der Seite [Lokale Netzverfeinerung](Lokale_Netzverfeinerung.md).

- [ ] Globales Netz einstellen: `Strukturbaum → Mesh` auswählen und `Detailfenster → Element Size: 5 mm` eingeben (Einheit auf mm!). Mit dem Standardnetz lässt sich der Rahmen nicht vernetzen.
- [ ] Lokale Netzverfeinerung auf beide Radien setzen (rot im Bild oben): die Flächen mit `STRG` gedrückt halten auswählen, dann `Rechtsklick Strukturbaum Mesh → Insert → Sizing` und `Detailfenster → Element Size: 0,5 mm` eingeben. Die Radien sind schmal, dafür nah heranzoomen. Unter `Detailfenster → Geometry` steht dann `8 Faces`, eine winzige neunte Fläche können Sie weglassen.
- [ ] Inflation auf beide Radien setzen, wie beim L-Profil: `Rechtsklick Strukturbaum Mesh → Insert → Inflation`. Unter `Detailfenster → Geometry` mit dem `Körperauswahltool` den Rahmen auswählen (`1 Body`), unter `Detailfenster → Boundary` mit dem `Flächenauswahltool` dieselben 8 Flächen wie beim Sizing. Alles andere bleibt auf dem Standard.
- [ ] Spannung nur in der Naht auswerten: `Rechtsklick Strukturbaum Solution → Insert → Stress → Equivalent (von-Mises)`, dann unter `Detailfenster → Geometry` die Fase und beide Radien auswählen (blau und rot im Bild oben), zusammen `12 Faces`.
- [ ] Lösen und die maximale Spannung ablesen.
- [ ] Die lokale Elementgröße unter `Strukturbaum → Mesh → Face Sizing` auf 0,25 mm und dann auf 0,125 mm halbieren, jeweils lösen und ablesen. Die Inflation bleibt, wie sie ist, ihre Lagen werden mit der Elementgröße von selbst dünner.

## Gesucht

### Die maximale von-Mises-Vergleichsspannung \(\sigma_\text{von Mises}\) in der Naht in MPa, bei lokal 0,125 mm

<div class="numeric-question" data-answer="48.22" data-tolerance="0.7" data-points="5" data-attempts="5" data-hints="Einheit auf mm gewechselt? Global 5 mm eingestellt? Face Sizing und Inflation auf beiden Radien der Naht? Ergebnis nur auf der Naht zwischen Oberrohr und Steuerrohr ausgewertet? Lokal bis 0,125 mm verfeinert?" data-diagnose="46.89: Das ist der Wert für lokal 0,25 mm. Noch einmal auf 0,125 mm halbieren. | 38.03: Das ist der Wert für lokal 0,5 mm. Die lokale Elementgröße bis 0,125 mm halbieren. | 43.68: Dieser Wert entsteht ohne Inflation. Inflation auf beide Radien einfügen: Geometry der Rahmen, Boundary die 8 Radiusflächen. | 35.68: Das ist der Wert für lokal 0,5 mm ohne Inflation. Inflation einfügen und die lokale Elementgröße bis 0,125 mm halbieren.">
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-05-Konvergenz.excalidraw.png" alt="Spannung in der Naht über der lokalen Elementgröße mit Inflation: 38,03 MPa bei 0,5 mm, 46,89 MPa bei 0,25 mm und 48,22 MPa bei 0,125 mm, Kontrolle mit global 2,5 mm und lokal 0,075 mm 48,69 MPa; hell dieselbe Reihe ohne Inflation" width="700">
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
    <td>38,03&nbsp;MPa</td>
    <td></td>
  </tr>
  <tr>
    <td>0,25&nbsp;mm</td>
    <td>46,89&nbsp;MPa</td>
    <td>23,3&nbsp;%</td>
  </tr>
  <tr>
    <td>0,125&nbsp;mm</td>
    <td>48,22&nbsp;MPa</td>
    <td>2,8&nbsp;%</td>
  </tr>
</table>

<p>Von 0,25&nbsp;mm auf 0,125&nbsp;mm ändert sich die Spannung noch um 2,8&nbsp;%. Nach der 1-%-Regel wäre noch einmal zu halbieren, mit global 5&nbsp;mm vernetzt ANSYS den Rahmen dann aber nicht mehr. Eine Kontrollrechnung mit global 2,5&nbsp;mm und lokal 0,075&nbsp;mm ergibt 48,69&nbsp;MPa, nur 1&nbsp;% mehr. Der Wert bei 0,125&nbsp;mm liegt also nah genug am konvergierten Wert.</p>

<!-- ENTWURF: Absatz zur Inflation von Claude, Felix formuliert die Aussage. Werte: Felix 06., 11. und 12.11.2026. -->
<p>Ohne Inflation sieht die Reihe dagegen schon konvergiert aus (hell im Bild): 35,68, 43,36 und 43,68&nbsp;MPa, von 0,25 auf 0,125&nbsp;mm nur 0,7&nbsp;%. Mit dem Netz der Kontrollrechnung steigt sie aber auf 46,25&nbsp;MPa. Wenn nur die Elementgröße auf der Fläche halbiert wird und die Tiefe offen bleibt, kann die Konvergenzstudie eine Konvergenz vortäuschen.</p>

<p>Die Radien sind im Mittel nur rund 0,5&nbsp;mm breit. Wenn die lokale Elementgröße ebenso groß ist, liegt nur ein Element auf dem Radius und das Netz bildet den Spannungsanstieg dort nicht ab.</p>

<!-- ENTWURF: Lösungsbild noch ohne Inflation (1000 N, Legende unkenntlich); ein Bild mit Inflation bei 0,125 mm von Felix wäre besser. -->
<figure style="text-align:center;">
  <img src="../images/Uebung-05-Loesung.png" alt="Vergleichsspannung in der Naht bei lokal 0,125 mm: das Maximum liegt am Radius am Oberrohr, an der Unterseite des Rohrs" width="900">
  <figcaption>Spannungsverteilung bei lokal 0,125&nbsp;mm, das Maximum liegt am Radius am Oberrohr, an der Unterseite des Rohrs</figcaption>
</figure>

</div>
