---
title: Zusammenfassung
icon: material/head-snowflake
hide:
  - toc
---

# :material-head-snowflake: Zusammenfassung

In diesem Praktikum wurde die geeignete Netzgröße bestimmt. Das vollständige Vorgehen:

<figure style="text-align:center;">
  <img src="../images/Vorgehen_Gesamt.excalidraw.png" alt="Vollständiges Vorgehen zur Bestimmung der Netzgröße" width="900">
</figure>

Hier noch mal die wichtigsten Kernaussagen des dritten Praktikums:

<div class="steps" markdown="1" data-spickzettel="ja">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Singularitäten</p>
    <p>Spannung an Singularitäten nicht auswerten.</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Konvergenz</p>
    <p>Außerhalb von Singularitäten die Netzgröße immer halbieren. Sobald der Unterschied zur vorigen Netzgröße kleiner als 1 % ist, gilt das Netz als konvergiert. Besonders sinnvoll ist dafür die lokale Netzverfeinerung.</p>
  </div>

</div>

## Quiz: Welcher Schritt kommt als Nächstes?

Gehen Sie für die folgenden Fälle die Grafik oben durch.

<figure style="text-align:center;">
  <img src="../images/Quiz_Verlauf.excalidraw.png" alt="Zwei Verläufe der Spannung über der Netzgröße. Verlauf A: 300, 340, 410 und 520 MPa bei 4, 2, 1 und 0,5 mm. Verlauf B: 300, 340, 348 und 349 MPa bei denselben Netzgrößen." width="800" class="no-lightbox">
</figure>

### Welcher Verlauf deutet auf eine Singularität hin?

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="zq1a" name="zq1">
      <label for="zq1a">Verlauf A</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="zq1b" name="zq1">
      <label for="zq1b">Verlauf B</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="zq1c" name="zq1">
      <label for="zq1c">Beide Verläufe</label>
    </div>
  </div>
</div>

### Die maximale Spannung liegt an einer scharfen Innenkante. Was ist der nächste Schritt?

<div class="multiple-choice-question" data-correct="B" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="zq2a" name="zq2">
      <label for="zq2a">Netzgröße weiter halbieren, bis der Unterschied unter 1 % liegt</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="zq2b" name="zq2">
      <label for="zq2b">Kante mit Radius verrunden</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="zq2c" name="zq2">
      <label for="zq2c">Lagerung durch eine alternative Lagerung ersetzen</label>
    </div>
  </div>
</div>

### Die maximale Spannung liegt an der festen Einspannung, ausgewertet wird weit davon entfernt. Welcher Schritt ist der Favorit?

<div class="multiple-choice-question" data-correct="C" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="zq3a" name="zq3">
      <label for="zq3a">Kante mit Radius verrunden</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="zq3b" name="zq3">
      <label for="zq3b">Netz an der Einspannung verfeinern, bis die Spannung dort konvergiert</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="zq3c" name="zq3">
      <label for="zq3c">Geometrie mit der Singularität aus der Spannungsauswertung herausnehmen</label>
    </div>
  </div>
</div>

### Ab welcher Netzgröße gilt das Netz in Verlauf B als konvergiert?

<div class="multiple-choice-question" data-correct="C" data-points="5" data-attempts="2">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="zq4a" name="zq4">
      <label for="zq4a">2 mm</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="zq4b" name="zq4">
      <label for="zq4b">1 mm</label>
    </div>
    <div class="mc-option" data-value="C">
      <input type="checkbox" id="zq4c" name="zq4">
      <label for="zq4c">0,5 mm</label>
    </div>
  </div>
</div>
