---
hide:
---

# Lokale Netzverfeinerung

Zunächst starten wir mit der globalen Netzverfeinerung, um den Unterschied besser zu erkennen. Als Beispiel verwenden wir das L-Profil aus dem zweiten Praktikum

Es ist das gesamte Projektarchiv gegeben (Material,Geometrie,Netz und Belastung):

[:material-paperclip: Uebung-02-L-Profil.wbpz](assets/Uebung-02-L-Profil.wbpz)

<figure style="text-align:center;">
    <img src="../../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/images/Uebung-01.png" alt="L-Profil" width="500">
</figure>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine globale Netzgröße von <code>3&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="436.89" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Netzgröße auf 3mm gestellt?" data-diagnose="592.32: Das ist der Wert für 1,5 mm. Hier ist die globale Netzgröße 3 mm gefragt.">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa im <code>gesamten Bauteil</code> für eine globale Netzgröße von <code>1,5&nbsp;mm</code> berechnen.

<div class="numeric-question" data-answer="592.32" data-tolerance="1" data-points="5" data-attempts="5" data-hints="Netzgröße auf 1,5mm gestellt?" data-diagnose="436.89: Das ist der Wert für 3 mm. Globale Netzgröße auf 1,5 mm stellen.">
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

- [ ] In SpaceClaim mit dem Pull-Tool an der Kante eine Kantenverrundung mit einem Radius von <code>3&nbsp;mm</code> erstellen. 

??? tip "<code>HILFE</code>: Kurzanleitung Kantenverrundung (klicken zum aufklappen)"

    Wie im Praktikum&nbsp;2 zur Geometrieanpassung gezeigt, können innenliegende Kanten in <code>SpaceClaim</code> mit Hilfe des <code>Pull</code>-Tools verrundet werden (hier im Beispiel an einer Außenkante!):

    <figure style="text-align:center;">
        <img src="../../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/images/Verrundung_einfuegen.png" alt="Verrundungen einfügen mit Pull" width="500">
    </figure>

    <figure style="text-align:center;">
        <img src="../../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/images/Verrundung_einfuegen.gif" alt="Verrundungen einfügen mit Pull" width="800">
    </figure>

    1. In SpaceClaim: <code>Reiter Sketch</code> (oder <code>Reiter Design</code>): <code>Pull-Tool</code> auswählen.
    2. Die <code>Kante</code> anklicken, die verrundet werden soll.
    3. <code>Wert eingeben (3mm in diesem Fall)</code> mit <code>ENTER</code> bestätigen und mit zweimal <code>ESC</code> beenden.

- [ ] In Mechanical die Geometrie aktualisieren: <code>Rechtsklick Strukturbaum Geometry → Update Geometry from Source</code>

# Lokale Netzverfeinerung

Bei der lokalen Netzverfeinerung stellen wir zunächst das <code>globale Netz wieder auf 3&nbsp;mm</code> und anschließend nur die <code>Verrundung auf 0,5&nbsp;mm</code>.

<div class="steps" markdown="1" data-kategorie="Vernetzung">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Globale Netzgröße einstellen</p>
    <p>(1) <code>Strukturbaum → Mesh</code> auswählen.</p>
    <p>(2) <code>Detailfenster → Element Size: 3 mm</code> eingeben (Einheit auf mm!).</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung1.png" alt="Lokale Netzverfeinerung" width="700">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lokale Netzverfeinerung einfügen</p>
    <p>(1) <code>Flächenauswahltool</code> auswählen.</p>
    <p>(2) Die <code>Fläche</code> der Verrundung auswählen.</p>
    <p>(3) bis (5) <code>Rechtsklick Strukturbaum Mesh → Insert → Sizing</code></p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung2.png" alt="Lokale Netzverfeinerung" width="700">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Lokale Netzgröße einstellen</p>
    <p>(1) Die lokale Netzverfeinerung auswählen: <code>Strukturbaum → Mesh → Face Sizing</code></p>
    <p>(2) <code>Detailfenster → Element Size: 0,5 mm</code> einstellen (Einheit auf mm!).</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung3.png" alt="Lokale Netzverfeinerung 2" width="300">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Netz generieren</p>
    <p><code>Rechtsklick Strukturbaum Mesh → Generate Mesh</code></p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung4.png" alt="Lokale Netzverfeinerung 3" width="500">
    </figure>
  </div>

</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,5&nbsp;mm</code> (globales Netz 3&nbsp;mm) berechnen.

<div class="numeric-question" data-answer="584.68" data-tolerance="2" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,5mm?" data-diagnose="547.29: Das ist der Wert ohne lokale Verfeinerung. Sizing auf der Verrundung einfügen. | 595.76: Das ist der Wert für 0,25 mm. Lokale Netzgröße auf 0,5 mm stellen.">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,25&nbsp;mm</code> (globales Netz 3&nbsp;mm) berechnen.

<div class="numeric-question" data-answer="595.76" data-tolerance="2" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,25mm?" data-diagnose="584.68: Das ist der Wert für 0,5 mm. Lokale Netzgröße auf 0,25 mm stellen. | 599.55: Das ist der Wert für 0,125 mm. Lokale Netzgröße auf 0,25 mm stellen. | 582.28: Dieser Wert entsteht mit ANSYS 2024 R2. Im PC-Pool läuft 2025 R2, dort vernetzt ANSYS etwas anders.">
</div>

Wurde somit eine Konvergenz erreicht mit einer lokalen Netzgröße von 0,25&nbsp;mm?

<div class="multiple-choice-question" data-correct="B" data-points="5" data-attempts="3">
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

- [ ] Das lokale Netz noch einmal halbieren: Die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,125&nbsp;mm</code> (globales Netz 3&nbsp;mm) berechnen.

<div class="numeric-question" data-answer="599.55" data-tolerance="2" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,125mm?" data-diagnose="595.76: Das ist der Wert für 0,25 mm. Lokale Netzgröße auf 0,125 mm stellen.">
</div>

Unser Vorgehen wächst erneut: Wenn die maximale Spannung an einer scharfen Kante liegt, verrunden wir die Kante und verfeinern das Netz nur dort.

<figure style="text-align:center;">
  <img src="../images/Vorgehen_Stufe3.excalidraw.png" alt="Vorgehen mit Kantenverrundung und lokaler Netzgröße" width="800">
</figure>

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
    <td>584,68&nbsp;</td>
  </tr>
  <tr>
    <td>0,25&nbsp;mm</td>
    <td>&ndash;</td>
    <td>595,76&nbsp;(+1,9&nbsp;%)</td>
  </tr>
  <tr>
    <td>0,125&nbsp;mm</td>
    <td>&ndash;</td>
    <td>599,55&nbsp;(+0,6&nbsp;%)</td>
  </tr>
</table>

<p>Von 0,5&nbsp;mm auf 0,25&nbsp;mm ändert sich die Spannung noch um 1,9&nbsp;%, das ist noch keine Konvergenz. Erst von 0,25&nbsp;mm auf 0,125&nbsp;mm liegt die Änderung mit 0,6&nbsp;% unter 1&nbsp;%.</p>

<p>
  <small>
    Hinweis: Die prozentuale Änderung bezieht sich jeweils auf das vorherige Netz
    in derselben Spalte. Die lokalen Spannungen stammen aus dem Modell mit
    Kantenverrundung (Radius 3&nbsp;mm); bei 0,5&nbsp;mm, 0,25&nbsp;mm und 0,125&nbsp;mm wurde zusätzlich
    eine lokale Netzverfeinerung in der Verrundung bei global 3&nbsp;mm verwendet.
  </small>
</p>

</div>
