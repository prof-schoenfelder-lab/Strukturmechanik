---
title: Zusammenfassung
icon: material/head-snowflake
hide:
  - toc
---

# :material-head-snowflake: Zusammenfassung

In diesem Praktikum wurden die ersten strukturmechanischen Analysen mit ANSYS Workbench durchgeführt. Mit SpaceClaim wurden einfache Geometrien erstellt und bearbeitet.

Hier noch mal die wichtigsten Kernaussagen des ersten Praktikums:

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ablauf in ANSYS</p>
    <p>Material → Geometrie → Materialzuordnung → Netz → Lagerung und Lasten → Lösen und Ergebnis (Spannungen, Verschiebungen)</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Simulationen validieren</p>
    <p>Analytische Lösungen (wenn vorhanden) und Experimente (wenn möglich) sind essenziell, um Simulationen zu validieren.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Fixed Support kann Singularitäten verursachen</p>
    <p>An den Rändern der fixierten Fläche steigt die Spannung mit immer feinerem Netz immer weiter an. Die Spannung an dieser Stelle ist nicht real und darf nicht ausgewertet werden, in ausreichendem Abstand davon schon.</p>
  </div>

</div>

Wie man eine Lagerung ohne Singularität abbildet, hängt vom Fall ab. Eine Möglichkeit haben Sie in [Übung 2](03_Selbsttests/Uebung-2.md#alternative-randbedingungen-fur-feste-einspannung-ohne-singularitat) gesehen. Welche Lagerung wann passt, ist Thema im nächsten Praktikum, ebenso die Möglichkeiten von `SpaceClaim` zur Geometrieaufbereitung.
