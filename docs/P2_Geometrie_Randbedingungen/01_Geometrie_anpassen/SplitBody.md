---
icon: material/rhombus-split
hide:
  - toc
---

# Körper teilen mit `Split Body`

Körper werden vorrangig geteilt für die folgenden Zwecke:

1. Um Körpern unterschiedliche Materialien zuzuordnen
2. Für eine bessere Vernetzung (kommt im Praktikum 3)
3. Um Bereiche zu entfernen

Durch das <code>Split Body</code> Tool werden Körper aufgeteilt, es entstehen also mehrere Körper im Strukturbaum.

## Körper teilen mit `Split Body` und vorhandenen `Geometrien`

Zum Trennen der Körper ist eine Trennebene notwendig. Dies kann eine bereits vorhandene Fläche sein, aber auch Linien die in einer Ebene verlaufen (z.B. auf einem Zylinder).

Hier wird dies beispielhaft gezeigt:

<figure style="text-align:center;">
    <img src="../images/Koerper_teilen.gif" alt="Körper erstellen mit Split Body" width="800">
</figure>

<div class="steps" markdown="1">

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Split Body Tool auswählen und Körper auswählen</p>
    <p>Im Reiter Design das <code>Split Body</code> Tool auswählen und auf den <code>Körper</code> klicken der geteilt werden soll.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Trennebene auswählen</p>
    <p>Die Ebene anklicken die den Körper trennen soll und den Modus mit 2x <code>ESC</code> beenden.</p>
  </div>

</div>


## Körper teilen mit `Split Body` und `Ebenen`

Als Beispiel verwenden wir ein Bimetall das in der Mitte geteilt werden soll um dem oberen und unteren ein unterschiedliches Material zuzuordnen:

<figure style="text-align:center;">
    <img src="../images/Koerper_teilen_Ebene.png" alt="Körper erstellen mit Split Body" width="400">
</figure>


<figure style="text-align:center;">
    <img src="../images/Koerper_teilen_Ebene.gif" alt="Körper erstellen mit Split Body" width="800">
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
    <p class="step-title" role="heading" aria-level="2">Mit dem Split Body Tool den Körper mit der Ebene schneiden</p>
    <p>Mit dem <code>Split Body</code> Tool den <code>zu schneidenden Körper</code> anklicken im Menü links das <code>Select Cutter</code> (Säge-Icon) auswählen und die <code>Ebene</code> mit der geschnitten werden soll anklicken. Den Modus mit 2x <code>ESC</code> beenden.</p>
    <p>Hinweis: Man könnte auch hier wieder mehrere Körper schneiden die vorher mit <code>STRG</code> selektieren worden und diese dann auch gleich an mehreren Ebenen schneiden.</p>
  </div>

</div>