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

<div class="steps" markdown="1" data-kategorie="Lagerung">

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

### `rigid` oder `deformable`: Was ist der Unterschied?

<figure style="text-align:center;">
<svg viewBox="0 0 640 250" width="640" style="max-width:100%;height:auto" role="img" aria-label="Remote Displacement rigid und deformable im Vergleich">
  <g font-family="Source Sans Pro, sans-serif" font-size="14" fill="#2E3639" text-anchor="middle">
    <text x="160" y="22" font-weight="700" fill="#022541">rigid (starr)</text>
    <rect x="120" y="50" width="150" height="110" fill="#F2F6F9" stroke="#2E3639"/>
    <line x1="120" y1="50" x2="120" y2="160" stroke="#022541" stroke-width="5"/>
    <g stroke="#022541" stroke-width="2.5"><line x1="120" y1="55" x2="50" y2="105"/><line x1="120" y1="80" x2="50" y2="105"/><line x1="120" y1="105" x2="50" y2="105"/><line x1="120" y1="130" x2="50" y2="105"/><line x1="120" y1="155" x2="50" y2="105"/></g>
    <circle cx="50" cy="105" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <text x="160" y="190">Fläche bleibt eben und bewegt sich</text>
    <text x="160" y="208">nur als Ganzes, wie ein starres Teil</text>
    <text x="160" y="232" fill="#009EE3">z. B. Achse im Ausfallende, Gabelschaft</text>
    <text x="480" y="22" font-weight="700" fill="#022541">deformable (verformbar)</text>
    <rect x="440" y="50" width="150" height="110" fill="#F2F6F9" stroke="#2E3639"/>
    <path d="M440,50 C455,85 455,125 440,160" fill="none" stroke="#009EE3" stroke-width="3" stroke-dasharray="6 4"/>
    <g stroke="#2E3639" stroke-width="1.2" stroke-dasharray="3 3"><line x1="440" y1="55" x2="370" y2="105"/><line x1="447" y1="80" x2="370" y2="105"/><line x1="451" y1="105" x2="370" y2="105"/><line x1="447" y1="130" x2="370" y2="105"/><line x1="440" y1="155" x2="370" y2="105"/></g>
    <circle cx="370" cy="105" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <text x="480" y="190">Fläche darf sich verformen, festgelegt</text>
    <text x="480" y="208">ist nur die Bewegung des Punkts (Mittel)</text>
    <text x="480" y="232" fill="#009EE3">z. B. Schraubkopf am Inbus (Übung 4)</text>
  </g>
</svg>
</figure>

- **`rigid`:** Die Fläche wird mit dem Punkt starr verbunden. Sie bleibt eben und kann sich nur als Ganzes verschieben oder drehen, so weit die Freiheitsgrade es erlauben. Das Modell wird dort zusätzlich versteift, am Rand der Fläche kann wie beim `Fixed Support` eine Spannungsspitze entstehen.
- **`deformable`:** Festgelegt ist nur die Bewegung des Punkts, also im Mittel die der Fläche. Die Fläche selbst darf sich verformen, die Last verteilt sich weicher.

!!! question "Wann ist was sinnvoll? Prüffrage"
    Was sitzt in Wirklichkeit an dieser Fläche, und ist es deutlich steifer als das Bauteil?

    - **Ja**, ein steifes Teil hält die Fläche in Form (Achse mit Schnellspanner in den Ausfallenden, Gabelschaft im Steuerrohr, eingepresster Bolzen): `rigid`.
    - **Nein** oder ähnlich steif, die Fläche verformt sich in Wirklichkeit mit (Schraubkopf auf dem Inbus, Einspannung ohne Singularität aus Praktikum 1): `deformable`.
    - **Unklar:** beide rechnen und an der Stelle vergleichen, die ausgewertet wird. Ändert sich dort kaum etwas, ist die Wahl unkritisch.
