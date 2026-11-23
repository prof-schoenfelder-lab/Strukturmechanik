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
    <p>Dabei immer in der x-y-Ebene zeichnen (bei Axialsymmetrie ist die y-Achse die Drehachse) und die Geometrie im Workbench-Projektmenü auf 2D stellen: <code>Rechtsklick Geometry → Properties</code> und dort <code>Analysis Type = 2D</code>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Linienabstraktion</p>
    <p>Ist ein Bauteil lang und schlank mit gleichbleibendem Querschnitt: als Linie mit Querschnitt modellieren, vernetzt mit Balkenelementen (<code>BEAM</code>).</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Schalenabstraktion</p>
    <p>Ist ein Bauteil dünn mit gleichbleibender Dicke, auch gekrümmt: als Fläche mit Dicke modellieren, vernetzt mit Schalenelementen (<code>SHELL</code>).</p>
  </div>

</div>
