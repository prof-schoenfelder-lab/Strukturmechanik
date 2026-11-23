---
title: Zusammenfassung
icon: material/head-snowflake
hide:
  - toc
---

# :material-head-snowflake: Zusammenfassung

In diesem Praktikum wurden Modelle so vereinfacht, dass sie weniger Rechenzeit brauchen: mit Symmetrie und mit Abstraktionen, die eine oder zwei Dimensionen weglassen.

<figure style="text-align:center;">
  <img src="../Praktikum04.excalidraw.png" alt="Abstraktionen: 2D ebener Spannungszustand, 2D Rotationssymmetrie, Linie mit Querschnitt (BEAM), Fläche mit Dicke (SHELL)" width="900">
</figure>

Hier noch mal die wichtigsten Kernaussagen des vierten Praktikums:

<div class="steps" markdown="1" data-spickzettel="ja">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Symmetrie</p>
    <p>Sind Geometrie und Randbedingungen (Lager und Lasten) symmetrisch, immer die Symmetrie nutzen und nur ein Halb- oder Viertelmodell rechnen.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">2D-Abstraktion</p>
    <p>Ist das Bauteil dünnwandig: <code>Plane Stress</code> (ebener Spannungszustand).</p>
    <p>Ist das Bauteil in der dritten Richtung sehr dick: <code>Plane Strain</code> (ebener Verzerrungszustand).</p>
    <p>Sind Geometrie, Lager und Lasten rotationssymmetrisch: <code>Axisymmetric</code> (Axialsymmetrie).</p>
    <p><strong>1. Skizze:</strong> in SpaceClaim in der x-y-Ebene zeichnen. Bei Axialsymmetrie ist die y-Achse die Rotationsachse, das Bauteil liegt rechts davon (x ist der Radius).</p>
    <p><strong>2. Workbench-Projektmenü:</strong> Geometrie auf 2D stellen, <code>Rechtsklick Geometry → Properties</code> und dort <code>Analysis Type = 2D</code>.</p>
    <p><strong>3. Mechanical:</strong> Art wählen, <code>Strukturbaum → Geometry</code> und dort <code>Detailfenster → 2D Behavior</code>: <code>Plane Stress</code>, <code>Plane Strain</code> oder <code>Axisymmetric</code>. Bei Plane Stress die Dicke eintragen, <code>Strukturbaum → Geometry → Fläche</code> und dort <code>Detailfenster → Thickness</code>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Linienabstraktion</p>
    <p>Ist ein Bauteil lang und schlank mit gleichbleibendem Querschnitt: als Linie mit Querschnitt modellieren, vernetzt mit Balkenelementen (<code>BEAM</code>).</p>
    <p><strong>1. Skizze:</strong> in SpaceClaim eine Linie zeichnen und ein Profil zuweisen, <code>Reiter Prepare → Profiles</code>. Oder einen Volumenkörper umwandeln, <code>Reiter Prepare → Extract</code>.</p>
    <p><strong>2. Mechanical:</strong> Maße des Querschnitts anpassen, <code>Strukturbaum → Cross Sections</code> und dort <code>Detailfenster → Dimensions</code>.</p>
    <p><strong>3. Lager:</strong> Balken können sich auch drehen. <code>Fixed Support</code> sperrt die Drehungen mit. Für ein Gelenk nur die Verschiebungen sperren (<code>Displacement</code>), gegen Drehen um die Längsachse <code>Fixed Rotation</code>.</p>
    <p><strong>4. Ergebnis:</strong> Spannungen im Querschnitt zeigen, <code>Strukturbaum → Solution</code> und dort <code>Detailfenster → Beam Section Results: Yes</code>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Schalenabstraktion</p>
    <p>Ist ein Bauteil dünn mit gleichbleibender Dicke, auch gekrümmt: als Fläche mit Dicke modellieren, vernetzt mit Schalenelementen (<code>SHELL</code>).</p>
    <p><strong>1. Skizze:</strong> in SpaceClaim eine Fläche zeichnen. Oder einen Volumenkörper umwandeln, <code>Reiter Prepare → Midsurface</code>. Der <code>Analysis Type</code> bleibt 3D.</p>
    <p><strong>2. Mechanical:</strong> Dicke eintragen (bei Midsurface schon gesetzt), <code>Strukturbaum → Geometry → Fläche</code> und dort <code>Detailfenster → Thickness</code>.</p>
    <p><strong>3. Lager:</strong> Wie bei Balken sperrt <code>Fixed Support</code> auch die Drehungen.</p>
  </div>

</div>
