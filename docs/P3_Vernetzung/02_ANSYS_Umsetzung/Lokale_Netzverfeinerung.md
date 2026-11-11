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

    Wie im Praktikum&nbsp;2 zur Geometrieanpassung gezeigt, können Kanten in <code>SpaceClaim</code> mit Hilfe des <code>Pull</code>-Tools verrundet werden. Die Bilder zeigen eine Außenkante, die Innenkante am L-Profil verrunden Sie genauso:

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

Bei der lokalen Netzverfeinerung stellen wir zunächst das <code>globale Netz wieder auf 3&nbsp;mm</code> und anschließend nur die <code>Verrundung auf 1&nbsp;mm</code>. Dazu kommt eine <code>Inflation</code> auf der Verrundung.

<!-- ENTWURF 10.11.2026 (Felix prüft): Die Wenn-dann-Sätze sind ein Vorschlag, Kernaussagen formuliert Felix. Bild:
     ANSYS 2025 R2 von Felix, lokal 0,5 mm ohne und mit Inflation (bilder/P3_LProfil_ANSYS_Vergleich.py im Vault). -->

??? info "Warum Inflation?"

    Eine lokale Netzgröße auf der Verrundung legt nur fest, wie lang die Elemente auf der Oberfläche sind. Wie tief sie in das Bauteil reichen, entscheidet ANSYS selbst, und das kann auf zwei Rechnern verschieden ausfallen.

    <figure style="text-align:center;">
        <img src="../images/LProfil_Inflation_Netz.png" alt="ANSYS-Netz an der Verrundung bei lokal 0,5 mm: ohne Inflation Vierecke, die an der Ecke unregelmäßig in die Tiefe wachsen; mit Inflation Tetraeder und dünne Lagen entlang des Bogens" width="800">
    </figure>

    - Wenn die Spannung an einer Verrundung ausgewertet wird, fällt sie in die Tiefe steil ab: beim L-Profil auf den ersten 0,5&nbsp;mm um rund ein Drittel. Dann hängt der Wert davon ab, wie dick die erste Elementlage ist.
    - Wenn eine Inflation auf der Verrundung liegt, baut ANSYS dort dünne Elementlagen parallel zur Oberfläche. Dann bekommt jeder Rechner an der Verrundung dasselbe Netz und denselben Wert.

<!-- ENTWURF 11.11.2026 (Felix' Idee, Felix prüft): Die Wenn-dann-Sätze sind ein Vorschlag. Skizze im Vault:
     bilder/P3_Vorgehen_excalidraw.py Netz_Global. Belege: Inbus als Sweep mit Hexaedern (Bild Inbus_2mm_einstellen),
     mit globalem Netz gleiche Werte im Pool (L-Profil global 1,5 mm: 592,32 MPa bei Felix und beim Studenten). -->

??? info "Warum ging es beim Inbus ohne Inflation?"

    Beim Inbus haben Sie die Elementgröße global eingestellt, also für das ganze Bauteil. ANSYS vernetzt ihn mit Hexaedern, die überall gleich groß sind.

    <figure style="text-align:center;">
        <img src="../images/Netz_Global.excalidraw.png" alt="Schnitt durch eine Verrundung, schematisch: Mit globaler Elementgröße sind die Elemente überall gleich groß, auch in der Tiefe. Mit Face Sizing ist nur an der Oberfläche h klein, die erste Elementlage reicht mal flach, mal tief." width="800" class="no-lightbox">
    </figure>

    - Wenn die Elementgröße global eingestellt ist, sind die Elemente in der Tiefe genauso klein wie an der Oberfläche. Dann ist auch der Abfall der Spannung in die Tiefe fein aufgelöst, und jeder Rechner bekommt dasselbe Netz.
    - Wenn nur die Fläche der Verrundung verfeinert ist, sind nur die Elemente an der Oberfläche klein. Dahinter wachsen sie bis auf die globale Größe von 3&nbsp;mm, und wie tief die erste Lage reicht, entscheidet ANSYS. Diese Tiefe legt die Inflation fest.

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
    <p>(2) <code>Detailfenster → Element Size: 1 mm</code> einstellen (Einheit auf mm!).</p>
    <figure style="text-align:center;">
        <img src="../images/Lokale_Netzverfeinerung3.png" alt="Lokale Netzverfeinerung 2" width="300">
    </figure>
  </div>

  <!-- ENTWURF: Klickweg Variante 1 (Inflation am Körper, Boundary die Fläche der Verrundung), so von Felix am 10.11.2026
       in ANSYS gerechnet. Bild vom Dialog von Felix (11.11.2026), Nummern: bilder/P3_LProfil_ANSYS_Vergleich.py dialog im Vault.
       Skizze (11.11.2026): bilder/P3_Vorgehen_excalidraw.py Netz_Inflation im Vault. -->

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Inflation auf der Verrundung einfügen</p>
    <p>(1) <code>Rechtsklick Strukturbaum Mesh → Insert → Inflation</code></p>
    <p>(2) <code>Körperauswahltool</code> wählen, den Körper anklicken und unter <code>Detailfenster → Geometry</code> mit <code>Apply</code> bestätigen. Unter Geometry muss <code>1 Body</code> stehen. Steht dort <code>1 Face</code>, hat ANSYS die Verrundung aus dem vorigen Schritt übernommen, und bei Boundary lassen sich nur Kanten wählen.</p>
    <p>(3) <code>Flächenauswahltool</code> wählen, die Fläche der Verrundung anklicken und unter <code>Detailfenster → Boundary</code> mit <code>Apply</code> bestätigen. Von dieser Fläche aus wachsen die dünnen Lagen in das Bauteil.</p>
    <p>(4) Alles andere bleibt auf dem Standard: <code>Inflation Option: Smooth Transition</code>, <code>Maximum Layers: 5</code>, <code>Growth Rate: 1.2</code>.</p>
    <figure style="text-align:center;">
        <img src="../images/LProfil_Inflation_Dialog.png" alt="Inflation im Strukturbaum unter Mesh, Detailfenster mit Geometry 1 Body, Boundary 1 Face und den Standardwerten Smooth Transition, 5 Lagen, Growth Rate 1,2; im Grafikfenster der Körper blau und die Fläche der Verrundung rot" width="700">
    </figure>
    <p>Das Face Sizing aus dem vorigen Schritt legt nur die Elementlänge auf der Oberfläche fest, die Inflation zusätzlich die Tiefe:</p>
    <figure style="text-align:center;">
        <img src="../images/Netz_Inflation.excalidraw.png" alt="Schnitt durch die Verrundung, schematisch: Mit Face Sizing ist nur die Elementlänge h auf der Oberfläche fest, die erste Elementlage reicht mal flach, mal tief. Mit Inflation liegen fünf dünne Lagen parallel zur Oberfläche, zusammen etwa h dick, die dünnste an der Oberfläche." width="700" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Netz generieren</p>
    <p><code>Rechtsklick Strukturbaum Mesh → Generate Mesh</code></p>
    <figure style="flex-wrap:wrap; gap:12px 16px; align-items:flex-end;">
        <img src="../images/LProfil_Netz_Inflation_1mm.png" alt="Netz an der Verrundung mit lokal 1 mm und Inflation: Tetraeder und dünne Lagen entlang des Bogens" width="500">
        <img src="../images/LProfil_Inflation_Lagen_0-25mm.png" alt="Ausschnitt am Bogen bei lokal 0,25 mm: die dünnen Lagen der Inflation als dunkles Band entlang der Verrundung" width="180">
        <figcaption style="flex-basis:100%;">Rechts ein Ausschnitt am Bogen bei lokal 0,25&nbsp;mm: Die dünnen Lagen liegen als Band entlang der Verrundung.</figcaption>
    </figure>
  </div>

</div>

<!-- ENTWURF: Sollwerte von Felix (ANSYS 2025 R2, 10.11.2026, Inflation am Körper, Smooth Transition, Standardwerte):
     1 mm 624,82, 0,5 mm 601,92, 0,25 mm 597,67, 0,125 mm 597,88 MPa (−3,7 %, −0,7 %, +0,04 %).
     Ohne Inflation (nur Face Sizing): 552,84, 584,68, 595,76, 599,55 MPa; ganz ohne lokale Verfeinerung 547,29.
     Das Backend ordnet Diagnosen bis 3 % Abstand zu. Die Nachbarwerte der Reihe liegen nur 0,7 bis 4 % auseinander
     und sind deshalb keine Diagnosen; bei 1 mm liegen „ohne Inflation“ und „ohne lokale Verfeinerung“ 1 % auseinander
     und teilen sich eine Diagnose; Werte ohne Inflation bei 0,25 mm (595,76 und 600,95) liegen im Sollband.
     Fragen-IDs hängen an der Position: q2 bis q4 und mc0 bekommen eine neue Bedeutung, mc1 ist neu. -->

- [ ] Die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>1&nbsp;mm</code> (globales Netz 3&nbsp;mm, Inflation auf der Verrundung) berechnen.

<div class="numeric-question" data-answer="624.82" data-tolerance="2" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 1mm, Inflation auf der Verrundung?" data-diagnose="552.84: Dieser Wert entsteht ohne Inflation, ganz ohne lokale Verfeinerung kommt fast dasselbe heraus. Face Sizing 1 mm und Inflation auf der Verrundung prüfen: Geometry der Körper, Boundary die Fläche der Verrundung.">
</div>

- [ ] Die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,5&nbsp;mm</code> (globales Netz 3&nbsp;mm, Inflation auf der Verrundung) berechnen.

<div class="numeric-question" data-answer="601.92" data-tolerance="2" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,5mm, Inflation auf der Verrundung?" data-diagnose="584.68: Das ist der Wert ohne Inflation. Inflation einfügen: Geometry der Körper, Boundary die Fläche der Verrundung. | 547.29: Das ist der Wert ohne lokale Verfeinerung. Face Sizing und Inflation auf der Verrundung einfügen.">
</div>

Wurde somit eine Konvergenz erreicht mit einer lokalen Netzgröße von 0,5&nbsp;mm?

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

- [ ] Das lokale Netz noch einmal halbieren: Die von-Mises-Vergleichsspannung in MPa in der Verrundung mit einem dortigen lokalen Netz von <code>0,25&nbsp;mm</code> (globales Netz 3&nbsp;mm, Inflation auf der Verrundung) berechnen.

<div class="numeric-question" data-answer="597.67" data-tolerance="2" data-points="5" data-attempts="5" data-hints="Globales Netz 3mm, lokales Netz 0,25mm, Inflation auf der Verrundung?" data-diagnose="547.29: Das ist der Wert ohne lokale Verfeinerung. Face Sizing und Inflation auf der Verrundung einfügen.">
</div>

Wurde jetzt eine Konvergenz erreicht mit einer lokalen Netzgröße von 0,25&nbsp;mm?

<div class="multiple-choice-question" data-correct="A" data-points="5" data-attempts="3">
  <div class="mc-options">
    <div class="mc-option" data-value="A">
      <input type="checkbox" id="q2a" name="q2">
      <label for="q2a">Ja</label>
    </div>
    <div class="mc-option" data-value="B">
      <input type="checkbox" id="q2b" name="q2">
      <label for="q2b">Nein</label>
    </div>
  </div>
</div>

Unser Vorgehen wächst erneut: Wenn die maximale Spannung an einer scharfen Kante liegt, verrunden wir die Kante, verfeinern das Netz nur dort und legen mit einer Inflation die Elementlagen in die Tiefe fest.

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
    <td>1&nbsp;mm</td>
    <td>&ndash;</td>
    <td>624,82&nbsp;</td>
  </tr>
  <tr>
    <td>0,5&nbsp;mm</td>
    <td>&ndash;</td>
    <td>601,92&nbsp;(&minus;3,7&nbsp;%)</td>
  </tr>
  <tr>
    <td>0,25&nbsp;mm</td>
    <td>&ndash;</td>
    <td>597,67&nbsp;(&minus;0,7&nbsp;%)</td>
  </tr>
</table>

<figure style="text-align:center;">
  <img src="../images/LProfil_Spannung_Inflation_0-25mm.png" alt="Vergleichsspannung an der Verrundung mit lokal 0,25 mm und Inflation, Maximum 597,67 MPa in Bauteilmitte" width="800">
</figure>

<p>Von 1&nbsp;mm auf 0,5&nbsp;mm ändert sich die Spannung noch um 3,7&nbsp;%, das ist noch keine Konvergenz. Von 0,5&nbsp;mm auf 0,25&nbsp;mm liegt die Änderung mit 0,7&nbsp;% unter 1&nbsp;%: Das Netz ist konvergiert.</p>

<p>
  <small>
    Hinweis: Die prozentuale Änderung bezieht sich jeweils auf das vorherige Netz
    in derselben Spalte. Die lokalen Spannungen stammen aus dem Modell mit
    Kantenverrundung (Radius 3&nbsp;mm); bei 1&nbsp;mm, 0,5&nbsp;mm und 0,25&nbsp;mm wurde zusätzlich
    eine lokale Netzverfeinerung mit Inflation in der Verrundung bei global 3&nbsp;mm verwendet.
  </small>
</p>

</div>
