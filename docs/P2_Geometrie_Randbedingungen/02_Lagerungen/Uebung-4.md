---
hide:
 - toc
sektion: Lagerungen
title: Übung 3
order: 140
kurz: Prüfstands-Dummies am Fahrradrahmen durch Remote Displacement ersetzen
thumb: images/Pruefstand_Rahmen.webp
---

# Prüfstands-Dummies durch Remote Displacement ersetzen

Im Rahmenprüfstand des bikelab der HTWK steht der Fahrradrahmen nicht auf Rädern, sondern auf zwei **Dummies**, also Ersatzteilen aus Stahl: Vorne steckt statt der Gabel der **Gabel-Dummy** im Steuerrohr, hinten sitzt statt des Hinterrads der **Hinterrad-Dummy** zwischen den Ausfallenden. Beide Dummies stehen unten in einem **Festlager**: Sie können sich dort um ihren Drehpunkt drehen, aber nicht verschieben.

<figure style="text-align:center;">
<svg viewBox="0 0 2000 1711" width="700" style="max-width:100%;height:auto" role="img" aria-label="Fahrradrahmen im Prüfstand mit Bezeichnungen: Satteldummy, Steuerrohr, Gabel-Dummy, Tretlager, Ausfallenden, Hinterrad-Dummy">
  <image href="../images/Pruefstand_Rahmen.webp" x="0" y="0" width="2000" height="1711"/>
  <g fill="#2f9e44" fill-opacity="0.45" stroke="#2f9e44" stroke-width="4" stroke-linejoin="round">
    <polygon points="1427,92 1457,82 1478,97 1478,112 1482,118 1490,160 1442,175 1430,133 1417,122 1415,112"/>
    <polygon points="1500,345 1545,345 1570,435 1520,440"/>
    <polygon points="1552,440 1605,432 1700,727 1652,737"/>
    <polygon points="1668,737 1700,730 1755,830 1720,840"/>
    <polygon points="440,785 470,760 498,760 497,1100 502,1122 502,1130 497,1140 497,1215 477,1215 477,1140 465,1130 465,1122 472,1100"/>
  </g>
  <g font-family="Source Sans Pro, sans-serif" font-size="46" font-weight="700" text-anchor="middle" dominant-baseline="central">
    <line x1="1640" y1="128" x2="1505" y2="290" stroke="#009EE3" stroke-width="5"/><circle cx="1505" cy="290" r="12" fill="#009EE3"/><rect x="1600" y="64" width="262" height="64" rx="8" fill="#ffffff" fill-opacity="0.9" stroke="#009EE3" stroke-width="3"/><text x="1731" y="96" fill="#022541">Steuerrohr</text>
    <line x1="595" y1="72" x2="730" y2="110" stroke="#009EE3" stroke-width="5"/><circle cx="730" cy="110" r="12" fill="#009EE3"/><rect x="280" y="40" width="315" height="64" rx="8" fill="#ffffff" fill-opacity="0.9" stroke="#009EE3" stroke-width="3"/><text x="437" y="72" fill="#022541">Satteldummy</text>
    <line x1="1720" y1="564" x2="1640" y2="620" stroke="#2f9e44" stroke-width="5"/><circle cx="1640" cy="620" r="12" fill="#2f9e44"/><rect x="1660" y="500" width="330" height="64" rx="8" fill="#ffffff" fill-opacity="0.9" stroke="#2f9e44" stroke-width="3"/><text x="1825" y="532" fill="#2f9e44">Gabel-Dummy</text>
    <line x1="1120" y1="940" x2="1000" y2="877" stroke="#009EE3" stroke-width="5"/><circle cx="1000" cy="877" r="12" fill="#009EE3"/><rect x="1100" y="940" width="226" height="64" rx="8" fill="#ffffff" fill-opacity="0.9" stroke="#009EE3" stroke-width="3"/><text x="1213" y="972" fill="#022541">Tretlager</text>
    <line x1="374" y1="660" x2="470" y2="780" stroke="#009EE3" stroke-width="5"/><circle cx="470" cy="780" r="12" fill="#009EE3"/><rect x="70" y="604" width="304" height="64" rx="8" fill="#ffffff" fill-opacity="0.9" stroke="#009EE3" stroke-width="3"/><text x="222" y="636" fill="#022541">Ausfallenden</text>
    <line x1="430" y1="900" x2="470" y2="950" stroke="#2f9e44" stroke-width="5"/><circle cx="470" cy="950" r="12" fill="#2f9e44"/><rect x="20" y="854" width="410" height="64" rx="8" fill="#ffffff" fill-opacity="0.9" stroke="#2f9e44" stroke-width="3"/><text x="225" y="886" fill="#2f9e44">Hinterrad-Dummy</text>
  </g>
</svg>
<figcaption>Der Rahmen aus der Übung im Rahmenprüfstand des bikelab. Auf dem Foto greift die Kraft am Satteldummy an, in der Übung am Tretlager.</figcaption>
</figure>

!!! info "Begriffe am Rahmen"
    - **Steuerrohr:** das kurze vordere Rohr, in dem sonst der Gabelschaft steckt
    - **Ausfallenden:** die beiden Platten am Ende des Hinterbaus, in die sonst die Hinterradachse eingespannt wird
    - **Sitzstreben:** die beiden Rohre vom Sitzrohr schräg nach unten zu den Ausfallenden
    - **Tretlager:** das quer liegende Rohr unten, in dem die Kurbel gelagert ist

Die Dummies sind extrem steif gegenüber dem Rahmen, daher können diese durch `Remote Displacement` ersetzt werden, um Rechenzeit zu sparen. In dieser Übung vergleichen Sie den Rahmen **mit** Dummies mit dem Rahmen, bei dem jeder Dummy durch ein `Remote Displacement` ersetzt ist. Der Vergleich zeigt eine Funktion von Remote Displacement: Übertragung von Freiheitsgraden von einem externen Punkt (die beiden Festlager) auf eine Geometrie (in diesem Fall am Ausfallende bzw. im Steuerrohr).

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Dummies.excalidraw.png" alt="Rahmen mit Dummies (A) und mit Remote Displacement statt Dummies (B)" width="700" class="no-lightbox">
</figure>

**So arbeitet Remote Displacement hier:** Die Verformung der gewählten Geometrie, zum Beispiel der Innenflächen des Steuerrohrs, wird auf einen externen Punkt bezogen, hier den Drehpunkt des Festlagers. Für diesen Punkt geben Sie dann die Randbedingung an: nicht verschiebbar, nur drehbar um eine Achse.

## Gegeben

### Archiv mit Rahmen, Dummies, Material, Netz und Belastung

[:material-paperclip: Rahmen_RemoteDisplacement.wbpz](assets/Rahmen_RemoteDisplacement.wbpz)

Wie das Archiv importiert wird, steht in [Übung 1](../01_Geometrie_anpassen/Uebung-1.md#archiv-importieren).

Im Archiv sind zwei Analysen vorbereitet:

- **A: `Rahmen mit Dummies`** ist fertig aufgebaut:
    - Rahmen aus Aluminium, Dummies aus Stahl (`Structural Steel`)
    - Dummies sind über `Joints` (Verbindung) mit dem Rahmen verbunden. Dabei können zwei Geometrien auch über feste Freiheitsgrade verbunden werden, um z.B. Drehbewegungen zu ermöglichen.
    - Die Festlager in den Dummies werden über `Cylindrical Support` festgelegt (drehbar in tangentialer Richtung, der Rest ist fest)
    - Kraft am Tretlager
- **B: `Rahmen mit Remote Displacement (Deformable)`** hat dieselbe Geometrie und dieselbe Kraft, aber:
    - die beiden Dummies sind unterdrückt (`Suppress`)
    - zwei Koordinatensysteme `Hinterrad-Drehpunkt` und `Gabel-Drehpunkt` liegen genau in den Drehachsen der Dummies
    - die Lagerung fehlt, die legen Sie an

## Aufgabenstellung

### 1. Rahmen mit Dummies rechnen

- [ ] Analyse A rechnen (`Solve`)
- [ ] Unter `Solution` das Ergebnis `Total Deformation - Rahmen` ansehen. Es wertet nur den Rahmen aus, nicht die Dummies.

### Die maximale Gesamtverformung des Rahmens mit Dummies in mm

<div class="numeric-question" data-answer="0.41554" data-tolerance="0.01" data-points="5" data-attempts="5" data-hints="Analyse A gerechnet? Total Deformation - Rahmen abgelesen, nicht Total Deformation mit Dummies? Einheit mm?">
</div>

### 2. Dummies durch Remote Displacement ersetzen

In Analyse B ersetzen Sie jeden Dummy durch ein `Remote Displacement`. Es sitzt auf denselben Flächen, an denen der Dummy mit dem Rahmen verbunden war, und sein Punkt liegt im Drehpunkt des Dummys.

Ein Bauteil durch `Remote Displacement` zu ersetzen, geht in vier Schritten. **In Analyse B sind die ersten drei schon erledigt**, die Bilder zeigen sie am Beispiel des Gabel-Dummys, damit Sie sehen, wie B entstanden ist.

<div class="steps" markdown="1" data-kategorie="Randbedingungen" data-titel="So ist Analyse B vorbereitet">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Koordinatensystem in den Drehpunkt legen (erledigt)</p>
    <p>Am Dummy die Fläche der Gelenkbohrung auswählen, dann <code>Rechtsklick Strukturbaum Coordinate Systems → Insert → Coordinate System</code>. Der Ursprung liegt damit auf der Drehachse.</p>
    <figure style="text-align:center;"><img src="../images/RD-Sequenz-01-KOS-einfuegen.webp" alt="Coordinate System an der Gelenkbohrung des Gabel-Dummys einfügen" width="700"></figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Bezug zur Geometrie lösen (erledigt)</p>
    <p>Im Detailfenster unter <code>Origin</code> bei <code>Define By</code> von <code>Geometry Selection</code> auf <code>Global Coordinates</code> umstellen. Der Ursprung bleibt, wo er ist, hängt aber nicht mehr an der Fläche des Dummys, der im nächsten Schritt unterdrückt wird. Die Achsen zeigen wie die globalen Achsen, die Drehachse der Dummies ist x.</p>
    <figure style="text-align:center;"><img src="../images/RD-Sequenz-02-KOS-Geometrie-Referenz-entfernen.webp" alt="Define By auf Global Coordinates umstellen" width="450"></figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Dummy unterdrücken (erledigt)</p>
    <p>Im Strukturbaum unter <code>Geometry</code> den Dummy anklicken, dann <code>Rechtsklick → Suppress Body</code>. Das Koordinatensystem bleibt erhalten, Lager und Joints am Dummy wirken danach nicht mehr.</p>
    <figure style="text-align:center;"><img src="../images/RD-Sequenz-03-Dummy-unterdruecken.webp" alt="Gabel-Dummy mit Suppress Body unterdrücken" width="450"></figure>
  </div>

</div>

**Schritt 4 ist Ihre Aufgabe:** je Dummy ein `Remote Displacement` anlegen.

!!! tip "Welche Flächen?"
    In Analyse A unter `Connections` die Joints anklicken: `General - SYS\Hinterrad-Dummy To SYS\Rahmen` markiert die Flächen an den **Ausfallenden**, `General - SYS\Gabel-Dummy To SYS\Rahmen` die Flächen im **Steuerrohr**. Genau diese Flächen am Rahmen wählen Sie in B für das Remote Displacement aus.

<div class="steps" markdown="1" data-kategorie="Randbedingungen" data-titel="Remote Displacement im Drehpunkt eines Dummys anlegen">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Remote Displacement einfügen</p>
    <p><code>Rechtsklick Strukturbaum Static Structural → Insert → Remote Displacement</code></p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Flächen zuweisen</p>
    <p>Die Flächen am Rahmen auswählen, an denen der Dummy angebunden war, und unter <code>Geometry</code> mit <code>Apply</code> bestätigen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Punkt in den Drehpunkt legen</p>
    <p>Unter <code>Coordinate System</code> das Koordinatensystem <code>Hinterrad-Drehpunkt</code> bzw. <code>Gabel-Drehpunkt</code> wählen, dann <code>X Coordinate</code>, <code>Y Coordinate</code> und <code>Z Coordinate</code> auf 0 setzen. Erst dann liegt der Punkt des Remote Displacements im Ursprung des Koordinatensystems, also im Drehpunkt.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Freiheitsgrade wie beim Cylindrical Support</p>
    <p><code>X Component</code>, <code>Y Component</code>, <code>Z Component</code> = 0, <code>Rotation X</code> = <code>Free</code> (die Drehachse der Dummies ist x), <code>Rotation Y</code> und <code>Rotation Z</code> = 0</p>
    <figure style="text-align:center;"><img src="../images/RD-Sequenz-04-RemoteDisplacement-Einstellungen.webp" alt="Remote Displacement im Steuerrohr mit dem Koordinatensystem im Drehpunkt" width="700"></figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Verhalten deformable lassen</p>
    <p>Unter <code>Behavior</code> bleibt zunächst die Standardeinstellung <code>Deformable</code></p>
  </div>

</div>

- [ ] Remote Displacement `Hinterrad` auf den Ausfallenden mit `Hinterrad-Drehpunkt` anlegen
- [ ] Remote Displacement `Gabel` im Steuerrohr mit `Gabel-Drehpunkt` anlegen
- [ ] Analyse B rechnen und die Gesamtverformung des Rahmens (`Total Deformation`) ansehen

### Die maximale Gesamtverformung des Rahmens mit Remote Displacement (deformable) in mm

<div class="numeric-question" data-answer="0.45212" data-tolerance="0.01" data-points="5" data-attempts="5" data-hints="Beide Remote Displacements auf den Flächen am Rahmen, mit den Koordinatensystemen Hinterrad-Drehpunkt und Gabel-Drehpunkt? X, Y und Z Coordinate auf 0? Nur Rotation X frei? Behavior Deformable?">
</div>

### Was passiert in Analyse B an den Ausfallenden?

Drehen Sie die Ansicht so, dass Sie von hinten auf die beiden Ausfallenden schauen, und vergleichen Sie mit Analyse A.

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q3aus_a" name="q3aus">
      <label for="q3aus_a">Die Ausfallenden biegen sich nach außen auseinander</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q3aus_b" name="q3aus">
      <label for="q3aus_b">Die Ausfallenden behalten ihren Abstand wie mit dem Hinterrad-Dummy</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q3aus_c" name="q3aus">
      <label for="q3aus_c">Die Ausfallenden werden zusammengedrückt</label>
    </div>
  </div>
</div>

### 3. Zum Vergleich: rigid

- [ ] In Analyse B: `Rechtsklick Strukturbaum Static Structural → Duplicate`. Die Kopie heißt C.
- [ ] In C bei beiden Remote Displacements `Behavior` = `Rigid` einstellen
- [ ] Analyse C rechnen

!!! question "Was ändert `rigid`?"
    Mit `deformable` dürfen sich die Flächen am Rahmen frei verformen, mit `rigid` bleiben sie in ihrer Form, als wäre dort ein unendlich steifes Bauteil angeschraubt. Mehr dazu auf der Seite [Externe Lager](RemoteDisplacement.md#starr-oder-verformbar).

### Die maximale Gesamtverformung des Rahmens mit Remote Displacement (rigid) in mm

<div class="numeric-question" data-answer="0.37357" data-tolerance="0.01" data-points="5" data-attempts="5" data-hints="In der Kopie C bei beiden Remote Displacements Behavior Rigid eingestellt und neu gerechnet?">
</div>

### Welche Einstellung bildet die Dummies besser ab?

Vergleichen Sie A, B und C: den Maximalwert, aber auch, **wo** das Maximum liegt und wie sich die Ausfallenden verformen.

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q3a" name="q3">
      <label for="q3a"><code>rigid</code>: Das Verformungsbild gleicht dem mit Dummies, das Maximum liegt an derselben Stelle</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q3b" name="q3">
      <label for="q3b"><code>deformable</code>: Der Maximalwert liegt näher am Wert mit Dummies</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="q3c" name="q3">
      <label for="q3c">Beide gleich gut, der Unterschied ist vernachlässigbar</label>
    </div>
  </div>
</div>

<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Loesung-Dummies.webp" alt="Gesamtverformung des Rahmens mit Dummies" width="700">
  <figcaption>A: mit Dummies, Maximum an den Sitzstreben</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Loesung-deformable.webp" alt="Gesamtverformung des Rahmens mit Remote Displacement deformable" width="700">
  <figcaption>B: Remote Displacement deformable, Maximum wandert ans Ausfallende</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung-04-Loesung-rigid.webp" alt="Gesamtverformung des Rahmens mit Remote Displacement rigid" width="700">
  <figcaption>C: Remote Displacement rigid, Verformungsbild wie mit Dummies</figcaption>
</figure>

| Analyse | max. Gesamtverformung | gegenüber A | Maximum liegt |
|---|---|---|---|
| A: mit Dummies | 0,416 mm | | an den Sitzstreben |
| B: deformable | 0,452 mm | +9 % | am Ausfallende |
| C: rigid | 0,374 mm | -10 % | an den Sitzstreben |

**Warum rigid, obwohl deformable beim Maximalwert näher liegt?**

- Beide Varianten liegen etwa 10 % neben A. Der Maximalwert allein entscheidet hier also nicht.
- Mit `deformable` hält nichts die Ausfallenden zusammen, sie biegen sich auseinander und das Maximum wandert dorthin. Im Prüfstand verbindet der Hinterrad-Dummy beide Seiten.
- Mit `rigid` bleibt die Form der Flächen erhalten, das Verformungsbild gleicht dem mit Dummies.
- Dass `rigid` etwas steifer rechnet, liegt daran, dass die Dummies in A selbst etwas nachgeben, das starre Remote Displacement aber nicht.

</div>

!!! question "Prüffrage für eigene Modelle"
    Was sitzt in Wirklichkeit an der Fläche, und hält es die Fläche in Form? Wenn ja: `rigid`. Wenn unklar: beide Varianten rechnen und das **Verformungsbild an der Fläche** vergleichen, nicht nur den Maximalwert.

Auf dem Foto vom Prüfstand greift die Kraft nicht am Tretlager an, sondern am Satteldummy, also oberhalb des Sitzrohrs und außerhalb der Rahmengeometrie. Wie man eine Kraft an einem Punkt außerhalb der Geometrie anbringt, zeigt [Übung 5](../03_Belastungen/Uebung-7.md) mit `Remote Force`.
