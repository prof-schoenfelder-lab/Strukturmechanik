---
hide:
 - toc
---

# Netzeinstellungen und Konvergenz

Neben der Elementgröße sollten Sie drei weitere Einstellungen kennen, weil sie das Netz verändern, auch wenn die Elementgröße gleich bleibt:

- `Defeature Size`: welche kleinen Details im Netz ankommen
- `Transition`: wie schnell die Elemente vom feinen zum groben Bereich wachsen
- `Inflation`: dünne Elementlagen an einer Oberfläche, zum Beispiel in einer Verrundung

`Defeature Size` und `Transition` bleiben in den Übungen auf dem Standardwert, die Sollwerte gelten nur dafür. `Inflation` kommt dazu, wo die Spannung in einer Verrundung ausgewertet wird. Am Ende der Seite steht, wie Sie prüfen, ob das Netz reicht.

## Defeaturing: kleine Details weglassen

Beim Vernetzen entfernt ANSYS kleine Details, damit sie das Netz nicht unnötig fein machen. Die Geometrie bleibt dabei unverändert, nur das Netz übergeht das Detail.

<figure style="text-align:center;">
  <img src="../images/Netz_Defeaturing.excalidraw.png" alt="Platte mit kleiner Nut: Ist die Defeature Size kleiner als die Nut, folgt das Netz der Nut. Ist sie größer, fehlt die Nut im Netz." width="800" class="no-lightbox">
</figure>

- Wenn ein Detail nicht größer ist als die `Defeature Size`, fehlt es im Netz.
- Wenn `Detailfenster → Mesh Defeaturing` auf `Yes` steht, ist das aktiv. Das ist der Standard.
- Wenn Sie die `Element Size` ändern, rechnet ANSYS die Standard-`Defeature Size` neu, denn sie hängt an der Elementgröße.
- Wenn eine lokale Netzverfeinerung die Elementgröße verändert, kann ANSYS die `Defeature Size` anpassen und meldet das als Warnung. Das ist kein Fehler.
- Wenn Sie unter `Detailfenster → Defeature Size` einen eigenen Wert eintragen, bleibt er fest, auch wenn sich die Elementgröße ändert.

!!! warning "Netz an der Auswertestelle ansehen"
    Wenn ein Radius im Netz fehlt, ist dort eine scharfe Kante und damit eine Singularität. Schauen Sie sich das Netz deshalb immer dort an, wo Sie die Spannung auswerten.

## Transition: vom feinen zum groben Netz

Nach einer lokalen Netzverfeinerung wachsen die Elemente wieder auf die globale Größe an. Wie schnell das geht, legt `Detailfenster → Transition` fest.

<figure style="text-align:center;">
  <img src="../images/Netz_Transition.excalidraw.png" alt="Elementlagen vom feinen zum groben Bereich: Mit Fast ist die globale Größe nach wenigen Lagen erreicht, mit Slow nach deutlich mehr Lagen." width="800" class="no-lightbox">
</figure>

- `Fast` ist der Standard: Bei Volumenkörpern wird jede Elementlage rund 1,85-mal so lang wie die vorige (`Growth Rate`).
- `Slow`: Die Elemente wachsen langsamer. Das Netz bekommt mehr Elemente und rechnet länger.
- Wenn sich die Spannung direkt neben der lokalen Verfeinerung noch stark ändert, kann der Übergang mit `Fast` zu abrupt sein. Dann helfen `Slow` oder ein größerer verfeinerter Bereich.
- `Transition` wirkt nur, wenn `Detailfenster → Use Adaptive Sizing` auf `Yes` steht. Das ist der Standard.

## Inflation: dünne Lagen an der Verrundung

<!-- ENTWURF 10.11.2026 (Felix prüft). ANSYS-Bildpaar ohne und mit Inflation am 12.11. entfernt (wirkte wie zwei Netzgrößen).
     Skizze (11.11.2026): bilder/P3_Vorgehen_excalidraw.py Netz_Inflation im Vault. -->

Eine lokale Netzgröße auf einer Fläche legt nur fest, wie lang die Elemente auf der Oberfläche sind. Wie tief sie in das Bauteil reichen, entscheidet ANSYS selbst. In einer Verrundung fällt die Spannung in die Tiefe aber steil ab, beim L-Profil auf den ersten 0,5&nbsp;mm um rund ein Drittel. `Inflation` legt dort dünne Elementlagen parallel zur Oberfläche.

<figure style="text-align:center;">
  <img src="../images/Netz_Inflation.excalidraw.png" alt="Schnitt durch die Verrundung, schematisch: Mit Face Sizing ist nur die Elementlänge h auf der Oberfläche fest, die erste Elementlage reicht mal flach, mal tief. Mit Inflation liegen fünf dünne Lagen parallel zur Oberfläche, zusammen etwa h dick, die dünnste an der Oberfläche." width="800" class="no-lightbox">
</figure>

- Einfügen mit `Rechtsklick Strukturbaum Mesh → Insert → Inflation`: unter `Geometry` der Körper, unter `Boundary` die Fläche der Verrundung.
- Wenn unter `Geometry` eine Fläche statt des Körpers steht, lassen sich bei `Boundary` nur Kanten wählen. Dann zuerst den Körper auswählen.
- Wenn `Inflation Option` auf `Smooth Transition` steht (Standard), richtet sich die Dicke der Lagen nach der Elementgröße auf der Fläche. Die Lage an der Oberfläche ist die dünnste, jede weitere ist 1,2-mal so dick wie die vorige (`Growth Rate`). Die letzte Lage, an die die Tetraeder anschließen, ist 0,272-mal so dick wie eine Elementkante (`Transition Ratio`). Die 5 Lagen (`Maximum Layers`) sind zusammen etwa so dick wie eine Elementkante.
- Wenn Sie die Elementgröße auf der Fläche halbieren, werden auch die Lagen halb so dick. Für die Konvergenzstudie ändern Sie deshalb nur die Elementgröße im `Face Sizing`.
- Wenn eine Inflation am Körper liegt, vernetzt ANSYS ihn mit Tetraedern und Prismen statt mit Hexaedern.

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
