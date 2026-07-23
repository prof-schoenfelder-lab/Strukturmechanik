---
icon: material/triangle-outline
hide:
  - toc
sektion: Lagerungen
title: externe Lager
order: 130
thumb: images/FixedSupport_vs_RemoteDisplacement.excalidraw.png
---

# Externe Lager mit `Remote Displacement`

Im ersten Praktikum haben wir `Remote Displacement` als Methode kennengelernt, um mit `Singularitäten` umzugehen. Dabei wurde es verwendet, um die durch ein Festlager entstehende Steifigkeit zu reduzieren.

## Grundprinzip von Remote Displacement

Jetzt schauen wir uns die Funktionsweise dahinter noch einmal genauer an:

<figure style="text-align:center;">
    <img src="../images/FixedSupport_vs_RemoteDisplacement.excalidraw.png" alt="Fixed Suppor vs. Remote Displacement" width="700">
</figure>

Beim Fixed Support wird die Verschiebung von jedem Knoten gleich Null gesetzt, die Geometrie kann sich also nicht verformen. Beim Remote Displacement kann sich die Geometrie hingegen verformen, weil nur die Summe der Knotenverschiebungen gleich Null sein muss. 

!!! danger "Rechenzeit kann sich stark vergrößern"

    Es werden pro Knoten und gesperrter Freiheitsgrad zusätzliche Gleichungen eingeführt, weshalb auch Remote Displacement mit vielen Knoten die Rechenzeit sich enorm erhöhen kann.

## Externer Punkt von Remote Displacement

Die Knoten auf der gewählten Geometrie werden über die Freiheitsgrade (`Verschiebung` und `Rotation`) auf einen Punkt reduziert. `Standardmäßig ist dies der Schwerpunkt der gewählten Geometrie`. Dies kann jedoch auch genutzt werden, um diesen Punkt gezielt an einen Ort zu legen der außerhalb der Geometrie liegt um zum Beispiel ein `entferntes Lager` abzubilden ohne die dafür nötige Geometrie zu erstellen.

!!! Info inline end

    Durch Remote Displacement können Lagerungsbedingungen angebracht werden ohne dass die notwendige Geometrie mit erstellt werden muss (hier am Beispiel also keine Fahrradgabel und kein Reifen).

<figure style="text-align:center;">
    <img src="../images/RemoteDisplacement_Fahrradbeispiel.excalidraw.png" alt="Remote Displacement am Fahrradrahmen" width="600">
</figure>

### Externer Punkt in ANSYS über neues Koordinatensystem einstellen

Der beste Weg die Entfernung des Punktes einzustellen ist über die Einführung ein neuen Koordinatensystems im Schwerpunkt der Geometrie:

<figure style="text-align:center;">
    <img src="../images/Remote_Displacement_Koordinatensystem.gif" alt="Koordinatensystem für Remote Displacement erstellen und anwenden" width="700">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie auswählen</p>
    <p>Je nach Geometrie das jeweilige <code>Selektionstool anklicken</code> (Punkt/Kante/Fläche/Körper) und die <code>Geometrie selektrieren</code></p>
    <p>Mehrere Geometrien mit <code>STRG</code> gedrückt halten auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Koordinatensystem einfügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Coordinate Systems</code> > <code>Insert</code> > <code>New Coordinate System</code> </p>
    <p>Neues Koordinatensystem mit <code>Rechtsklick</code> > <code>Rename</code> umbenennen.
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie erneut auswählen</p>
    <p>Je nach Geometrie das jeweilige <code>Selektionstool anklicken</code> (Punkt/Kante/Fläche/Körper) und die <code>Geometrie selektrieren</code></p>
    <p>Mehrere Geometrien mit <code>STRG</code> gedrückt halten auswählen</p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">Remote Displacement einfügen</p>
    <p>Im Strukturbaum: <code>Rechtsklick</code> auf <code>Static Structural</code> > <code>Insert</code> > <code>Remote Displacement</code> </p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">Koordinatensystem auswählen</p>
    <p>Im Detailfenster: Unter <code>Coordinate System</code> das neue Koordinatensystem auswählen und die <code>Koordianten eingeben</code>.</p>
  </div>

</div>

## Freiheitsgrade

Die Freiheitsgrade der Verschiebung und Rotation können im Detailfenster eingestellt werden:

!!! Info inline end

    Hier wurden Beispielhaft einige Freiheitsgrade Null gesetzt.


<figure style="text-align:center;">
    <img src="../images/RemoteDisplacement_Freiheitsgrade.png" alt="FreiheitsgradeDetailfenster" width="250">
</figure>

## Verformungsverhalten

Beim Verformungsverhalten gibt es mehrere Optionen. Wir beschränken uns in dem Praktikum jedoch nur auf `deformable (verformbar)` und `rigid (starr)`. Wird die Option `rigid (starr)` gewählt, so kann sich die Geometrie nur über die freigelassenen Freiheitsgrade (`Verschiebungen` oder `Rotationen`) Starrkörperbewegungen ausführen. Dies führt zu einem deutlich reduzierten Rechenaufwand im Vergleich zur Option `deformable (verformbar)`.

<figure style="text-align:center;">
    <img src="../images/Remote_Displacement_Verformungsverhalten.png" alt="FreiheitsgradeDetailfenster" width="250">
</figure>