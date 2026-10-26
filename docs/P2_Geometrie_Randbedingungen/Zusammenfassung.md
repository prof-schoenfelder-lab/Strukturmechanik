---
title: Zusammenfassung
icon: material/head-snowflake
hide:
  - toc
---

# :material-head-snowflake: Zusammenfassung

In diesem Praktikum wurden Geometrien in SpaceClaim für die Simulation vorbereitet und Lagerungen und Lasten in ANSYS Mechanical angebracht.

Hier noch mal die wichtigsten Kernaussagen des zweiten Praktikums:

<div class="steps" markdown="1" data-spickzettel="ja">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie in SpaceClaim anpassen</p>
    <p>Längen und Positionen ändern Sie mit <code>Move</code>, Radien und Wandstärken mit <code>Pull</code>. Soll eine Randbedingung nur auf einem Teil einer Fläche sitzen, teilen Sie die Fläche vorher mit <code>Split</code>.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Geometrie vereinfachen</p>
    <p>Kleinteile und Features wie Bohrungen oder kleine Radien kosten Elemente und Rechenzeit. Prüffrage vor dem Löschen: Liegt das Detail im Lastpfad oder dort, wo Sie auswerten? Dann bleibt es drin, sonst darf es weg. Gleiche Körper oder Flächen wählt <code>Select</code> in einem Schritt aus.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Körper zusammenfügen</p>
    <p>Sollen mehrere Körper fest miteinander verbunden sein, fügen Sie sie mit <code>Combine</code> zu einem Körper zusammen. Das Netz läuft dann über die früheren Grenzen hinweg.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Remote Displacement: Lager an einem Punkt außerhalb</p>
    <p>Die Knoten der gewählten Fläche werden auf einen Punkt bezogen: standardmäßig ihren Schwerpunkt, über ein eigenes Koordinatensystem auch einen Punkt außerhalb der Geometrie. Vorgegeben ist nur die Bewegung dieses Punkts, nicht die jedes Knotens. Mit <code>deformable</code> kann sich die Fläche dabei verformen, mit <code>rigid</code> bleibt sie starr. Sinnvoll, wenn das Lager außerhalb des Modells liegt (Achse, Gabel, Reifen) oder wenn eine Einspannung ohne die Singularität eines <code>Fixed Support</code> gebraucht wird. Bei sehr vielen Knoten steigt die Rechenzeit.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Remote Force: Kraft an einem Punkt außerhalb</p>
    <p>Wie Remote Displacement, nur mit einer Kraft: Sie greift an einem Punkt außerhalb der Geometrie an und wird auf die gewählte Fläche übertragen, samt dem Moment aus dem Hebelarm. Sinnvoll, wenn das Bauteil, über das die Last eingeleitet wird, nicht modelliert ist, etwa der Fahrer auf dem Sattel ohne Sattel und Sattelstütze.</p>
  </div>

</div>
