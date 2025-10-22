---
icon: material/arrow-split-vertical
hide:
  - toc
---

# Flächen teilen zum Anbringen von Randbedingungen

Zum anbringen von Randbedingungen müssen oft Flächen auf Körpern erstellt werden.

# Flächen teilen mit `Split`

Im ersten Beispiel soll eine Fläche im Abstand von 40mm für eine Flächenlast erzeugt werden:

<figure style="text-align:center;">
    <img src="../images/Flaeche_erstellen.png" alt="Flächen erstellen mit Split" width="400">
</figure>


<figure style="text-align:center;">
    <img src="../images/Flaeche_erstellen.gif" alt="Flächen erstellen mit Split" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Split Tool auswählen und Fläche auswählen</p>
    <p>Im Reiter Design das <code>Split</code> Tool auswählen und auf die <code>Fläche</code> klicken die geteilt werden soll.</p>
    <p>Mit <code>STRG</code> gedrückt halten könnte man hier auch auch mehrere Flächen auswählen.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Splitfunktion UV Cutter Point auswählen</p>
    <p>Im Menü links <code>Select UV Cutter Point</code> auswählen <code>Maus auf Kante bewegen</code>.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Länge einstellen</p>
    <p>Mit <code>TAB</code> zur Längenbemaßung wechseln und <code>Wert</code> eingeben und mit <code>ENTER</code> bestätigen und den Modus mit 2x <code>ESC</code> beenden.</p>
  </div>

</div>


# Flächen teilen mit `Split` und `Ebenen`

Durch Ebenen kann man gleich mehrere Flächen auf einmal teilen (wie im Beispiel Inbus im ersten Praktikum).

Jetzt verwenden wir die Ebene um im Abstand von 80mm eine Fläche an einem Lenker zu erzeugen an dem eine Kraft angreifen soll. 

<figure style="text-align:center;">
    <img src="../images/Flaechen_erstellen_mit_Split.gif" alt="Flächen erstellen mit Split" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Ebene erstellen</p>
    <p>Im Reiter Design das <code>Ebenen</code> Tool auswählen und auf die <code>Fläche</code> klicken auf der die <code>Ebene</code> erzeugt werden soll.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Ebene mit Move verschieben</p>
    <p>Mit dem <code>Move</code> Tool die Ebene in die gewünschte Richtung und Abstand verschieben.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Mit dem Split Tool die Fläche mit der Ebene schneiden</p>
    <p>Mit dem <code>Split</code> Tool die <code>zu schneidenden Fläche</code> anklicken im Menü links das <code>Select Cutter Face</code> (Säge-Icon) auswählen und die <code>Ebene</code> mit der geschnitten werden soll anklicken. Den Modus mit 2x <code>ESC</code> beenden.</p>
  </div>

</div>

!!! info "Hinweis"

    Hier wird mit der Ebene nur eine Fläche auf dem Volumenkörper erzeugt. Im nachfolgenden Teil wird über ein sehr ähnlichen Workflow das gesamte Volumen mit der Ebene geschnitten.