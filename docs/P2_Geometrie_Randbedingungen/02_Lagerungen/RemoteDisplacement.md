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

Ein Lager legt fest, wie sich ein Bauteil an einer Stelle bewegen darf. Im ersten Praktikum haben Sie den `Fixed Support` kennengelernt, der eine Fläche komplett festhält, und `Remote Displacement` als Mittel gegen `Singularitäten`. Hier schauen wir genauer hin: Was macht `Remote Displacement`, und wie ersetzt man damit Bauteile, die man nicht mitmodellieren will?

## Was macht Remote Displacement?

Ein Bauteil kann sich im Raum auf sechs Arten bewegen: in x, y und z **verschieben** und um x, y und z **drehen**. Das sind seine sechs **Freiheitsgrade**. Ein Lager sperrt einige davon (Wert `0`) und lässt die anderen frei (`Free`).

- **`Fixed Support`** sperrt die Verschiebung an **jedem Knoten** der gewählten Fläche. Die Fläche ist wie festgeklebt und kann sich nicht verformen. Die Knoten eines Volumennetzes haben nur die drei Verschiebungen, deshalb kann ein `Fixed Support` auch nur Verschiebungen sperren.
- **`Remote Displacement`** koppelt alle Knoten der Fläche an **einen einzigen Punkt**. Dieser Punkt hat alle sechs Freiheitsgrade, die Sie einzeln vorgeben. Die Fläche ist an den Punkt gebunden und macht seine Bewegung mit.

<figure style="text-align:center;">
    <img src="../images/FixedSupport_vs_RemoteDisplacement.excalidraw.png" alt="Fixed Suppor vs. Remote Displacement" width="700">
</figure>

Im Detailfenster stellen Sie für den Punkt jeden der sechs Freiheitsgrade einzeln ein:

<figure style="text-align:center;">
    <img src="../images/RemoteDisplacement_Freiheitsgrade.png" alt="FreiheitsgradeDetailfenster" width="250">
</figure>

## Wo liegt der Punkt?

**Standardmäßig im Schwerpunkt der gewählten Fläche.** Dann bezieht sich das Lager auf die Geometrie selbst, so wie in Praktikum 1.

Wichtig wird die Lage des Punkts, sobald ein Freiheitsgrad frei ist: Eine freie Drehung findet **um den Punkt** statt. Sind dagegen alle sechs Freiheitsgrade gesperrt, ist es egal, wo der Punkt liegt.

<figure style="text-align:center;">
<svg viewBox="0 0 660 250" width="660" style="max-width:100%;height:auto" role="img" aria-label="Drehung frei: Punkt im Schwerpunkt der Fläche und Punkt außerhalb im Vergleich">
  <defs>
    <marker id="rdpf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#E53009"/></marker>
  </defs>
  <g font-family="Source Sans Pro, sans-serif" font-size="14" fill="#2E3639" text-anchor="middle">
    <text x="160" y="22" font-weight="700" fill="#022541">Punkt im Schwerpunkt der Fläche</text>
    <g transform="rotate(14 90 110)"><rect x="90" y="95" width="150" height="30" fill="none" stroke="#BEC3C6" stroke-width="2" stroke-dasharray="6 4"/></g>
    <rect x="90" y="95" width="150" height="30" fill="#F2F6F9" stroke="#2E3639"/>
    <line x1="90" y1="95" x2="90" y2="125" stroke="#009EE3" stroke-width="5"/>
    <circle cx="90" cy="110" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <path d="M 255 108 A 165 165 0 0 1 248 150" fill="none" stroke="#E53009" stroke-width="2" marker-end="url(#rdpf)"/>
    <text x="160" y="200">Drehung frei: Das Bauteil dreht sich</text>
    <text x="160" y="218">um die Mitte der Fläche</text>

    <text x="500" y="22" font-weight="700" fill="#022541">Punkt außerhalb</text>
    <g transform="rotate(14 430 190)"><rect x="430" y="65" width="150" height="30" fill="none" stroke="#BEC3C6" stroke-width="2" stroke-dasharray="6 4"/></g>
    <rect x="430" y="65" width="150" height="30" fill="#F2F6F9" stroke="#2E3639"/>
    <line x1="430" y1="65" x2="430" y2="95" stroke="#009EE3" stroke-width="5"/>
    <g stroke="#009EE3" stroke-width="1.5" stroke-dasharray="4 4"><line x1="430" y1="65" x2="430" y2="190"/><line x1="430" y1="95" x2="430" y2="190"/></g>
    <circle cx="430" cy="190" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <path d="M 596 112 A 170 170 0 0 1 586 160" fill="none" stroke="#E53009" stroke-width="2" marker-end="url(#rdpf)"/>
    <text x="500" y="222">Drehung frei: Das Bauteil schwenkt</text>
    <text x="500" y="240">auf einem Kreisbogen um den Punkt</text>
  </g>
</svg>
</figure>

**Der Punkt darf aber auch außerhalb liegen.** Dann bildet er ein entferntes Lager ab: Die Freiheitsgrade dieses Punkts werden auf die gewählte Fläche übertragen, und das Bauteil dazwischen muss nicht modelliert werden.

!!! Info inline end

    Durch Remote Displacement können Lagerungsbedingungen angebracht werden ohne dass die notwendige Geometrie mit erstellt werden muss (hier am Beispiel also keine Fahrradgabel und kein Reifen).

<figure style="text-align:center;">
    <img src="../images/RemoteDisplacement_Fahrradbeispiel.excalidraw.png" alt="Remote Displacement am Fahrradrahmen" width="600">
</figure>

!!! question "Darf ich das Bauteil weglassen? Prüffrage"
    Zwischen Punkt und Fläche verformt sich im Modell nichts mehr: Das weggelassene Bauteil wirkt wie unendlich steif. Das ist nur sinnvoll, wenn es im Vergleich zum berechneten Bauteil **quasi starr** ist. Fragen Sie sich: Verformt sich das Bauteil, das ich weglasse, deutlich weniger als mein Bauteil? Wenn nicht, gehört es ins Modell.

    Auch seine Masse fehlt dann im Modell. Das spielt eine Rolle, sobald Eigengewicht oder [Beschleunigungen](../03_Belastungen/Beschleunigungen.md) wirken.

Eine Alternative mit demselben Gedanken: das Bauteil im Modell lassen und auf starr setzen (unter `Geometry` am Körper `Stiffness Behavior` = `Rigid`). Dann verformt es sich nicht mehr, Geometrie und Masse bleiben aber im Modell.

Wo der Punkt liegen soll, legen Sie in ANSYS über ein eigenes Koordinatensystem fest: im Remote Displacement unter `Coordinate System` auswählen und `X Coordinate`, `Y Coordinate`, `Z Coordinate` auf 0 setzen. Erst dann liegt der Punkt im Ursprung dieses Koordinatensystems. Wie das Schritt für Schritt geht, wenn das Bauteil im Modell ist, zeigt [Übung 3](Uebung-4.md#2-dummies-durch-remote-displacement-ersetzen) mit den Prüfstands-Dummies. Wie man den Punkt über einen Abstand festlegt, steht unten unter [Punkt über einen Abstand festlegen](#punkt-uber-einen-abstand-festlegen).

## Starr oder verformbar?

Unter `Behavior` legen Sie fest, wie sich die gekoppelte Fläche verhält. Im Praktikum nutzen wir `rigid (starr)` und `deformable (verformbar)`.

<figure style="text-align:center;">
    <img src="../images/Remote_Displacement_Verformungsverhalten.png" alt="FreiheitsgradeDetailfenster" width="250">
</figure>

<figure style="text-align:center;">
<svg viewBox="0 0 640 250" width="640" style="max-width:100%;height:auto" role="img" aria-label="Remote Displacement rigid und deformable im Vergleich">
  <g font-family="Source Sans Pro, sans-serif" font-size="14" fill="#2E3639" text-anchor="middle">
    <text x="160" y="22" font-weight="700" fill="#022541">rigid (starr)</text>
    <rect x="120" y="50" width="150" height="110" fill="#F2F6F9" stroke="#2E3639"/>
    <line x1="120" y1="50" x2="120" y2="160" stroke="#022541" stroke-width="5"/>
    <g stroke="#022541" stroke-width="2.5"><line x1="120" y1="55" x2="50" y2="105"/><line x1="120" y1="80" x2="50" y2="105"/><line x1="120" y1="105" x2="50" y2="105"/><line x1="120" y1="130" x2="50" y2="105"/><line x1="120" y1="155" x2="50" y2="105"/></g>
    <circle cx="50" cy="105" r="6" fill="#fff" stroke="#009EE3" stroke-width="3"/>
    <text x="160" y="190">Fläche behält ihre Form und bewegt sich</text>
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

- **`rigid`:** Die Fläche wird mit dem Punkt starr verbunden. Sie behält ihre Form und kann sich nur als Ganzes verschieben oder drehen, so weit die Freiheitsgrade es erlauben. Sind alle sechs gesperrt, wirkt das wie ein `Fixed Support`. Das Modell wird dort zusätzlich versteift, am Rand der Fläche kann wie beim `Fixed Support` eine Spannungsspitze entstehen.
- **`deformable`:** Festgelegt ist nur die Bewegung des Punkts, also im Mittel die der Fläche. Die Fläche selbst darf sich verformen, die Last verteilt sich weicher.

!!! question "Wann ist was sinnvoll? Prüffrage"
    Hält das, was in Wirklichkeit an dieser Fläche sitzt, die Fläche in Form?

    - **Ja**, ein steifes Teil ist fest mit der Fläche verbunden und hält sie in Form (Achse mit Schnellspanner in den Ausfallenden, Gabelschaft im Steuerrohr, eingepresster Bolzen): `rigid`.
    - **Nein** oder ähnlich steif, die Fläche verformt sich in Wirklichkeit mit (Schraubkopf auf dem Inbus, Einspannung ohne Singularität aus Praktikum 1): `deformable`.
    - **Unklar:** beide rechnen und vergleichen, nicht nur den Maximalwert, sondern auch das Verformungsbild an der Fläche (wie in Übung 3). Ändert sich dort kaum etwas, ist die Wahl unkritisch.

## Spart Remote Displacement Rechenzeit?

Nicht automatisch. Sicher ist: Das Modell wird einfacher, denn das ersetzte Bauteil braucht keine Geometrie, kein Netz und keine Verbindung zum Rest.

!!! danger "Viele gekoppelte Knoten kosten Rechenzeit"

    Pro Knoten der Fläche und gesperrtem Freiheitsgrad kommen zusätzliche Gleichungen dazu. Rechenzeit sparen Sie deshalb nur, wenn das weggelassene Bauteil viele Elemente gehabt hätte und die angekoppelte Fläche wenige Knoten hat. `rigid` ist dabei in der Regel günstiger als `deformable`.

## Punkt über einen Abstand festlegen

Ist das Bauteil gar nicht modelliert, zum Beispiel die Gabel am Fahrradrahmen, legen Sie das Koordinatensystem in die Fläche, an der das Bauteil angreifen würde (hier das Steuerrohr), und geben im Remote Displacement die Koordinaten des Lagerpunkts in diesem Koordinatensystem ein. So gehen Sie in [Übung 5](../03_Belastungen/Uebung-7.md) bei der `Remote Force` vor.

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
    <p><code>Rechtsklick Strukturbaum Coordinate Systems → Insert → New Coordinate System</code></p>
    <p>Neues Koordinatensystem mit <code>Rechtsklick → Rename</code> umbenennen.
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie erneut auswählen</p>
    <p>Je nach Geometrie das jeweilige <code>Selektionstool anklicken</code> (Punkt/Kante/Fläche/Körper) und die <code>Geometrie selektrieren</code></p>
    <p>Mehrere Geometrien mit <code>STRG</code> gedrückt halten auswählen</p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">Remote Displacement einfügen</p>
    <p><code>Rechtsklick Strukturbaum Static Structural → Insert → Remote Displacement</code></p>
  </div>

 <div class="step">
    <p class="step-title" role="heading" aria-level="2">Koordinatensystem auswählen</p>
    <p>Im Detailfenster: Unter <code>Coordinate System</code> das neue Koordinatensystem auswählen und die <code>Koordianten eingeben</code>.</p>
  </div>

</div>
