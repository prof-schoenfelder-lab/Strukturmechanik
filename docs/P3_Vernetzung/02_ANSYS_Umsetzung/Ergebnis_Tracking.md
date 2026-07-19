---
icon: material/note-text-outline
hide:
  - toc
---

# Ergebnisse für die Sensitivitätsanalyse speichern

Um zu jeder Netzgröße die Ergebnisse (meist Spannungen) zu dokumentieren, werden im Folgenden zwei Methoden vorgestellt.

## Methode 1: Screenshots der Ergebnisse

Mit Hilfe von Screenshots der Ergebnisse und einer Umbenennung entsprechend der jeweiligen Netzgröße kann man sich eine gute Übersicht erzeugen:

<figure style="text-align:center;">
    <img src="../images/Result_Image.png" alt="Result Image" width="1100">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ergebnis auswählen (z.&nbsp;B. von-Mises-Spannung)</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Reiter <code>Result</code> auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Images</code> auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Image</code> auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Image</code> umbenennen</p>
    <p>Mit <code>Rechtsklick</code> auf <code>Image</code> und <code>Rename</code> einen aussagekräftigen Namen vergeben, z.&nbsp;B. die verwendete Elementgröße.</p>
  </div>

</div>

## Methode 2: Solution History / Result Tracking

Ohne zusätzliche Einstellungen speichert ANSYS Mechanical automatisch die letzten 10 Ergebnisse in der `Solution History` bzw. dem `Result Tracking`. Dabei werden neben dem Ergebnis auch interessante Daten wie die Anzahl der Knoten und Elemente sowie die Rechenzeit ausgegeben.  

Ein Nachteil ist, dass keine individuelle Benennung (z.&nbsp;B. „Netz 1,5&nbsp;mm“) möglich ist, da die Ergebnisse einfach in der zeitlichen Reihenfolge der Berechnungen dargestellt werden.

<figure style="text-align:center;">
    <img src="../images/Solution_History.png" alt="Solution History" width="400">
</figure>

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Solution Information</code> im Strukturbaum auswählen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Im Detailfenster das Dropdown-Menü <code>Solution Output</code> öffnen</p>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2"><code>Solution History</code> auswählen</p>
  </div>

</div>

Standardmäßig wird zunächst die Solution History angezeigt, mit tabellarischen Daten der letzten 10 Simulationen bezüglich

- Anzahl der Knoten
- Anzahl der Elemente
- Zeit, die der Lösungsprozess benötigt hat
- verwendeter Arbeitsspeicher
- verwendeter CPU-Kerne
- belegtem Speicherplatz

Über die Häkchen können maximal zwei Größen gleichzeitig im Diagramm dargestellt werden.

<figure style="text-align:center;">
    <img src="../images/Solution_History2.png" alt="Solution History Diagramm" width="1100">
</figure>

Durch einen Klick auf `Result Tracking` können anschließend die Ergebnisse (z.&nbsp;B. Spannungen oder Verschiebungen) visualisiert werden.  
Dazu die Haken bei `Nodes`/`Elements` entfernen und stattdessen z.&nbsp;B. `Maximum Deformation` und `Maximum Equivalent Stress` aktivieren.

<figure style="text-align:center;">
    <img src="../images/Result_Tracking.png" alt="Result Tracking" width="1100">
</figure>
