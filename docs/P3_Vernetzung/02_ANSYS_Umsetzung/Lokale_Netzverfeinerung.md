---
hide:
---

# Globale Netzverfeinerung

Zunächst starten wir mit der globalen Netzverfeinerung, um den Unterschied besser zu erkennen. Als Beispiel verwenden wir das L-Profil aus dem zweiten Praktikum.

<figure style="text-align:center;">
    <img src="../../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/images/Uebung-01.png" alt="L-Profil" width="500">
</figure>

- [ ] Berechnen Sie die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine globale Netzgröße von <code>3&nbsp;mm</code>.

<div class="numeric-question" data-answer="436,89" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Netzgröße auf 3mm gestellt?">
</div>

- [ ] Berechnen Sie die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine globale Netzgröße von <code>1,5&nbsp;mm</code>.

<div class="numeric-question" data-answer="592,32" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Netzgröße auf 1,5mm gestellt?">
</div>


!!! failure "Wir haben nun zwei Probleme:"

    - Die Spannung ist um etwa 36&nbsp;% gestiegen, was auf eine Singularität hindeutet. Diese befindet sich in der <code>unendlich scharfen</code> Kante.  
      <br>→  Dies können wir mit der <code>Kantenverrundung</code> lösen.
    - Durch die globale Netzgröße hat die <code>Rechnung sehr lange gedauert</code>.  
      <br>→  Dies können wir mit der <code>lokalen Netzverfeinerung</code> lösen.

# Kantenverrundung

<figure style="text-align:center;">
    <img src="../images/LProfil_Radius.png" alt="Radius" width="400">
</figure>

- [ ] Erstellen Sie in SpaceClaim mit dem Pull-Tool an der Kante eine Kantenverrundung mit einem Radius von <code>3&nbsp;mm</code>. 

Wie im Praktikum&nbsp;2 zur Geometrieanpassung gezeigt, können innenliegende Kanten in <code>SpaceClaim</code> mit Hilfe des <code>Pull</code>-Tools verrundet werden (hier im Beispiel an einer Außenkante!):

<div class="steps" markdown="1">

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Pull-Tool starten</p>
    <p>In SpaceClaim im Reiter <code>Sketch</code> (oder <code>Design</code>) das <code>Pull-Tool</code> auswählen.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Verrundungskante wählen</p>
    <p>Die <code>Kante</code> anklicken, die verrundet werden soll.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Verrundung erstellen und bemaßen</p>
    <p>Mit <code>gedrückter linker Maustaste</code> von der Kante wegziehen, <code>Leertaste</code> drücken, den gewünschten <code>Radius</code> eingeben und mit zweimal <code>ESC</code> beenden.</p>
  </div>

  <div class="step" >
    <p class="step-title" role="heading" aria-level="2">Geometrie aktualisieren</p>
    <p>In Mechanical im Strukturbaum <code>Rechtsklick</code> auf <code>Geometry</code> und <code>Update Geometry from Source</code> auswählen.</p>
  </div>

</div>

# Lokale Netzverfeinerung

Bei der lokalen Netzverfeinerung stellen wir zunächst das <code>globale Netz wieder auf 3&nbsp;mm</code> und anschließend nur die <code>Verrundung auf 0,5&nbsp;mm</code>.

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Globale Netzgröße einstellen</p>
    <p>(1) Im Strukturbaum <code>Mesh</code> auswählen.</p>
    <p>(2) Im Detailfenster unter <code>Element Size</code> den Wert <code>3</code> eingeben (Einheit auf mm!).</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung1.png" alt="Lokale Netzverfeinerung" width="700">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lokale Netzverfeinerung einfügen</p>
    <p>(1) <code>Flächenauswahltool</code> auswählen.</p>
    <p>(2) Die <code>Fläche</code> der Verrundung auswählen.</p>
    <p>Im Strukturbaum (3) <code>Rechtsklick</code> auf <code>Mesh</code> und dann (4) <code>Insert</code> &gt; (5) <code>Sizing</code> auswählen.</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung2.png" alt="Lokale Netzverfeinerung" width="700">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lokale Netzgröße einstellen</p>
    <p>(1) Die lokale Netzverfeinerung (Sizing) auswählen.</p>
    <p>(2) Im Detailfenster unter <code>Sizing</code> den Wert <code>0,5</code> einstellen (Einheit auf mm!).</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung3.png" alt="Lokale Netzverfeinerung 2" width="300">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Netz generieren</p>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Mesh</code> und dann <code>Generate Mesh</code> auswählen.</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung4.png" alt="Lokale Netzverfeinerung 3" width="500">
    </figure>
  </div>

</div>

- [ ] Berechnen Sie die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,5&nbsp;mm</code> (globales Netz 3&nbsp;mm).

<div class="numeric-question" data-answer="586.0" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,5mm?">
</div>

- [ ] Berechnen Sie die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,25&nbsp;mm</code> (globales Netz 3&nbsp;mm).

<div class="numeric-question" data-answer="582.28" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,25mm?">
</div>

Wurde somit eine Konvergenz erreicht mit einer lokalen Netzgröße von 0,25&nbsp;mm?

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="3">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q1a" name="q1">
      <label for="q1a">Ja</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q1b" name="q1">
      <label for="q1b">Nein</label>
    </div>
  </div>
</div>


<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

🎯 <strong>Lösung</strong>

<table border="1">
  <tr>
    <th>Netzgröße</th>
    <th>&sigma;<sub>vM</sub> global ohne Verrundung [MPa]</th>
    <th>&sigma;<sub>vM</sub> lokal mit Verrundung [MPa]</th>
  </tr>
  <tr>
    <td>3&nbsp;mm</td>
    <td>436,89</td>
    <td>-</td>
  </tr>
  <tr>
    <td>1,5&nbsp;mm</td>
    <td>592,32&nbsp;(+35,6&nbsp;%)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>0,5&nbsp;mm</td>
    <td>&ndash;</td>
    <td>586,00&nbsp;</td>
  </tr>
  <tr>
    <td>0,25&nbsp;mm</td>
    <td>&ndash;</td>
    <td>582,28&nbsp;(−0,6&nbsp;%)</td>
  </tr>
</table>

<p>
  <small>
    Hinweis: Die prozentuale Änderung bezieht sich jeweils auf das vorherige Netz
    in derselben Spalte. Die lokalen Spannungen stammen aus dem Modell mit
    Kantenverrundung (Radius 3&nbsp;mm); bei 0,5&nbsp;mm und 0,25&nbsp;mm wurde zusätzlich
    eine lokale Netzverfeinerung in der Verrundung bei global 3&nbsp;mm verwendet.
  </small>
</p>

</div>