---
hide:
 - toc
---

# Netzeinstellungen und Konvergenz

Neben der Elementgröße sollten Sie vier weitere Einstellungen kennen, weil sie das Netz verändern, auch wenn die Elementgröße gleich bleibt:

- `Method`: mit welcher Elementform ANSYS vernetzt, Tetraeder oder Hexaeder
- `Defeature Size`: welche kleinen Details im Netz ankommen
- `Transition`: wie schnell die Elemente vom feinen zum groben Bereich wachsen
- `Inflation`: dünne Elementlagen an einer Oberfläche, zum Beispiel in einer Verrundung

`Method`, `Defeature Size` und `Transition` bleiben in den Übungen auf dem Standard, die Sollwerte gelten nur dafür. `Inflation` kommt dazu, wo die Spannung in einer Verrundung ausgewertet wird. Am Ende der Seite steht, wie Sie prüfen, ob das Netz reicht.

## Method: Tetraeder oder Hexaeder

<!-- ENTWURF 12.11.2026 (Felix): Method fehlte, vor allem Tetraeder, Sweep und MultiZone. Wann was, üben die Studierenden nicht.
     Beleg L-Profil: Felix 10. und 12.11.2026, lokal 0,5 mm, ohne Inflation. -->

**Was macht es?** `Method` legt fest, mit welcher Elementform ANSYS einen Körper vernetzt. Einfügen mit `Rechtsklick Strukturbaum Mesh → Insert → Method`, unter `Geometry` den Körper wählen.

- `Automatic` (Standard): Lässt sich der Körper sweepen, vernetzt ANSYS mit Hexaedern, sonst mit Tetraedern.
- `Tetrahedrons`: Tetraeder, passen auf jede Geometrie.
- `Sweep`: Hexaeder entlang eines Weges, für Körper mit gleichbleibendem Querschnitt, etwa gezogene oder gedrehte Teile.
- `MultiZone`: zerlegt einen Körper selbst in Bereiche, die sich sweepen lassen, und vernetzt diese mit Hexaedern.

**Wann benutzt man es?** Wenn ANSYS einen Körper nicht vernetzt oder Sie die Elementform bewusst wählen wollen. Hexaeder brauchen für dieselbe Elementgröße weniger Knoten, Tetraeder gehen immer.

**Worauf achten?**

- Die Elementform ändert das Ergebnis, auch bei gleicher Elementgröße. Beim L-Profil mit lokal 0,5&nbsp;mm ohne Inflation: Hexaeder (Sweep) 584,68&nbsp;MPa, Tetraeder 595,19&nbsp;MPa.
- Wenn eine Inflation am Körper liegt, vernetzt `Automatic` mit Tetraedern und Prismen.
- Mehr zu den Elementformen auf der Seite [Elementtypen](../01_Grundlagen/Elementtypen.md).

## Defeaturing: kleine Details weglassen

<!-- ENTWURF 12.11.2026: nach Felix gekürzt und je Einstellung gegliedert: Was macht es? Wann benutzt man es? Worauf achten? -->

**Was macht es?** Das Netz übergeht alle Details, die nicht größer sind als die `Defeature Size`. Die Geometrie bleibt unverändert, nur das Netz bildet das Detail nicht ab. Das ist standardmäßig aktiv, die `Defeature Size` richtet sich nach der Elementgröße.

<figure style="text-align:center;">
  <img src="../images/Netz_Defeaturing.excalidraw.png" alt="Platte mit kleiner Nut: Ist die Defeature Size kleiner als die Nut, folgt das Netz der Nut. Ist sie größer, fehlt die Nut im Netz." width="800" class="no-lightbox">
</figure>

**Wann benutzt man es?** Wenn kleine Details wie winzige Flächen oder kurze Kanten, oft aus dem CAD-Import, sehr kleine Elemente erzwingen oder die Vernetzung scheitern lassen.

**Worauf achten?**

- Das Netz ist dann nicht mehr genau das Bauteil. Das ist nur in Ordnung, wenn die weggelassenen Details für die Auswertung keine Rolle spielen.
- Wenn ein Radius im Netz fehlt, ist dort eine scharfe Kante und damit eine Singularität. Schauen Sie sich das Netz deshalb immer dort an, wo Sie die Spannung auswerten.

## Transition: vom feinen zum groben Netz

**Was macht es?** Nach einer lokalen Netzverfeinerung wachsen die Elemente wieder auf die globale Größe an. `Detailfenster → Transition` legt fest, wie schnell: Mit `Fast` (Standard) wird bei Volumenkörpern jede Elementlage rund 1,85-mal so lang wie die vorige, mit `Slow` wachsen die Elemente langsamer.

<figure style="text-align:center;">
  <img src="../images/Netz_Transition.excalidraw.png" alt="Elementlagen vom feinen zum groben Bereich: Mit Fast ist die globale Größe nach wenigen Lagen erreicht, mit Slow nach deutlich mehr Lagen." width="800" class="no-lightbox">
</figure>

**Wann benutzt man es?** Wenn sich die Spannung direkt neben der lokalen Verfeinerung noch stark ändert, kann der Übergang mit `Fast` zu abrupt sein. Dann helfen `Slow` oder ein größerer verfeinerter Bereich.

**Worauf achten?**

- Mit `Slow` bekommt das Netz mehr Elemente und rechnet länger.
- `Transition` wirkt nur, wenn `Detailfenster → Use Adaptive Sizing` auf `Yes` steht. Das ist der Standard.

## Inflation: dünne Lagen an der Verrundung

<!-- ENTWURF 10.11.2026 (Felix prüft), am 12.11. gegliedert wie die anderen Einstellungen. ANSYS-Bildpaar ohne und mit Inflation am 12.11. entfernt.
     Skizze (11.11.2026): bilder/P3_Vorgehen_excalidraw.py Netz_Inflation im Vault. -->

**Was macht es?** Eine lokale Netzgröße auf einer Fläche legt nur fest, wie lang die Elemente auf der Oberfläche sind. Wie tief sie reichen, entscheidet ANSYS. `Inflation` legt zusätzlich dünne Elementlagen parallel zur Oberfläche und damit die Elementgröße in die Tiefe fest.

<figure style="text-align:center;">
  <img src="../images/Netz_Inflation.excalidraw.png" alt="Schnitt durch die Verrundung, schematisch: Mit Face Sizing ist nur die Elementlänge h auf der Oberfläche fest, die erste Elementlage reicht mal flach, mal tief. Mit Inflation liegen fünf dünne Lagen parallel zur Oberfläche, zusammen etwa h dick, die dünnste an der Oberfläche." width="800" class="no-lightbox">
</figure>

**Wann benutzt man es?** Wenn die Spannung in einer Verrundung oder Kerbe ausgewertet wird. Dort fällt sie in die Tiefe steil ab, beim L-Profil auf den ersten 0,5&nbsp;mm um rund ein Drittel.

**Worauf achten?**

- Einfügen mit `Rechtsklick Strukturbaum Mesh → Insert → Inflation`: unter `Geometry` der Körper, unter `Boundary` die Fläche der Verrundung. Steht unter `Geometry` eine Fläche statt des Körpers, lassen sich bei `Boundary` nur Kanten wählen.
- Die Standardwerte lassen (`Smooth Transition`, 5 Lagen, `Growth Rate` 1,2). Dann sind die Lagen zusammen etwa so dick wie eine Elementkante, die dünnste liegt an der Oberfläche.
- Wenn Sie die Elementgröße auf der Fläche halbieren, werden auch die Lagen halb so dick. Für die Konvergenzstudie ändern Sie deshalb nur die Elementgröße im `Face Sizing`.
- Mit Inflation vernetzt ANSYS den Körper mit Tetraedern und Prismen statt mit Hexaedern.

!!! tip "Faustregeln für Spannungen in Verrundungen und Kerben"
    - Quadratische Elemente verwenden. Das ist in Mechanical der Standard für Volumenkörper.
    - In der Verrundung höchstens ein Viertel des Radius als Elementgröße (r/4), entlang der Oberfläche und in die Tiefe. So steht es in den [IIW-Empfehlungen für Schweißnähte](https://svv.cz/files/IIW182307FatigueRecomm20121017.pdf) (Abschnitt 2.2.4.2), die Regel gilt aber für jede Kerbe. Auf einem 90°-Bogen sind das mindestens 6 Elemente.
    - Die Tiefe mit `Inflation` festlegen.
    - Die Faustregel liefert nur den Startwert. Ob das Netz reicht, zeigt die Konvergenzstudie, siehe [Konvergenz prüfen](#konvergenz-prufen) unten.

Mehr dazu in der ANSYS-Hilfe: [Mesh Defeaturing](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/msh_auto_defeat.html), [Transition](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/msh_Trans.html) und [Inflation](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/ds_Inflation_Group.html).

## Konvergenz prüfen

<!-- ENTWURF 12.11.2026 (Felix): war die eigene Seite „Diskussion“, dann „Konvergenz prüfen“; jetzt Abschnitt dieser Seite.
     Nur die Empfehlung (mindestens drei Netze, immer halbieren, letzte Änderung unter 1 %), Felix prüft die Formulierung. -->

Ob das Netz an der Stelle reicht, an der Sie die Spannung auswerten, zeigt eine Netzstudie:

- Mit **mindestens drei Netzen** rechnen und die Elementgröße dabei **jedes Mal halbieren**.
- Wenn sich die Spannung beim letzten Halbieren um **weniger als 1&nbsp;%** ändert, gilt das Netz als konvergiert.
- Wenn die Änderung beim Halbieren nicht kleiner wird, liegt wahrscheinlich eine **Singularität** vor. Dann den Ort prüfen (scharfe Kante, feste Einspannung, Punktlast) und dort nicht auswerten.

**Warum mindestens drei Netze?** Zwei Netze reichen nicht: Ein großer Sprung kann auch von einem zu groben ersten Netz kommen, und ein kleiner Unterschied kann täuschen. Erst das dritte Netz zeigt, ob die Änderung kleiner wird.

So sah das beim L-Profil aus (mit Inflation, global 3&nbsp;mm):

| lokale Elementgröße | Spannung σ<sub>vM</sub> | Änderung zur vorigen Netzgröße |
| ------------------:| -----------------------:| ------------------------------:|
| 1&nbsp;mm          | 624,82&nbsp;MPa          |                                |
| 0,5&nbsp;mm        | 601,92&nbsp;MPa          | −3,7&nbsp;%                    |
| 0,25&nbsp;mm       | 597,67&nbsp;MPa          | <span style="color:green;">−0,7&nbsp;%</span> |

Die Änderung wird kleiner und liegt beim letzten Halbieren unter 1&nbsp;%: Das Netz mit 0,25&nbsp;mm ist konvergiert.
