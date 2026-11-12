---
hide:
 - toc
---

# Netzeinstellungen und Konvergenz

Neben der Elementgröße verändern vier weitere Einstellungen das Netz:

- `Method`: mit welcher Elementform ANSYS vernetzt, Tetraeder oder Hexaeder
- `Transition`: wie schnell die Elemente vom feinen zum groben Bereich wachsen
- `Defeature Size`: welche kleinen Details im Netz ankommen
- `Inflation`: dünne Elementlagen an einer Oberfläche, zum Beispiel in einer Verrundung

In den Übungen bleiben `Method`, `Transition` und `Defeature Size` auf dem Standard. Nur dafür gelten die Sollwerte. Wenn Sie die Spannung in einer Verrundung auswerten, kommt `Inflation` dazu. Am Ende der Seite steht, wie Sie prüfen, ob das Netz reicht.

## Method: Tetraeder oder Hexaeder

<!-- ENTWURF 12.11.2026 (Felix): Method fehlte, vor allem Tetraeder, Sweep und MultiZone. Wann was, üben die Studierenden nicht.
     Beleg L-Profil: Felix 10. und 12.11.2026, lokal 0,5 mm, ohne Inflation. -->

**Was macht es?** `Method` legt fest, mit welcher Elementform ANSYS einen Körper vernetzt. Einfügen mit `Rechtsklick Strukturbaum Mesh → Insert → Method`, unter `Geometry` den Körper wählen. Zur Wahl stehen unter anderem:

- `Tetrahedrons`: Tetraeder, passen auf jede Geometrie.
- `Sweep`: Hexaeder entlang eines Weges. Für Körper mit gleichbleibendem Querschnitt, etwa gezogene oder gedrehte Teile.
- `MultiZone`: zerlegt einen Körper selbst in Bereiche, die sich sweepen lassen, und vernetzt diese mit Hexaedern.
- `Automatic` (Standard): Wenn sich der Körper sweepen lässt, vernetzt ANSYS mit Hexaedern, sonst mit Tetraedern.

<figure style="text-align:center;">
  <img src="../images/Netz_Method.png" alt="Drei Netze: links ein L-Profil mit Tetraedern, in der Mitte dasselbe L-Profil mit Sweep, der Querschnitt aus Vierecken entlang der Länge durchgezogen, rechts eine Platte mit Zapfen, mit MultiZone in zwei Bereiche zerlegt und mit Hexaedern vernetzt" width="900">
</figure>

**Wann benutzt man es?** Wenn ANSYS einen Körper nicht vernetzt oder Sie die Elementform bewusst wählen wollen.

!!! info "Wann Tetraeder, wann Hexaeder?"
    Hexaeder wären an sich besser:

    - Für dieselbe Elementgröße brauchen sie deutlich weniger Knoten.
    - Die Rechnung wird damit kürzer.

    Wenn nur eine kleine Stelle fein vernetzt werden soll, kommt man aber oft nicht um Tetraeder herum:

    - Hexaeder liegen in geordneten Lagen. Eine Verfeinerung lässt sich darin kaum auf eine kleine Stelle begrenzen.
    - Beim Sweep zieht sich die Verfeinerung zum Beispiel durch die ganze Länge.
    - Tetraeder können dagegen auf kurzem Weg von fein auf grob wachsen.

Mehr zu den Elementformen auf der Seite [Elementtypen](../01_Grundlagen/Elementtypen.md).

## Transition: vom feinen zum groben Netz

**Was macht es?** Nach einer lokalen Netzverfeinerung wachsen die Elemente wieder auf die globale Größe an. Wie schnell das geht, legt `Detailfenster → Transition` fest:

- `Fast` (Standard): Die Elemente wachsen schnell auf die globale Größe an.
- `Slow`: Die Elemente wachsen langsamer. Das ergibt mehr Elemente und eine längere Rechnung.

<figure style="text-align:center;">
  <img src="../images/Netz_Transition.excalidraw.png" alt="Elementlagen vom feinen zum groben Bereich: Mit Fast ist die globale Größe nach wenigen Lagen erreicht, mit Slow nach deutlich mehr Lagen." width="800" class="no-lightbox">
</figure>

**Wann benutzt man es?** Wenn sich die Spannung direkt neben der lokalen Verfeinerung noch stark ändert, kann der Übergang mit `Fast` zu abrupt sein. Dann helfen `Slow` oder ein größerer verfeinerter Bereich.

## Defeaturing: kleine Details weglassen

<!-- ENTWURF 12.11.2026: nach Felix gekürzt und je Einstellung gegliedert: Was macht es? Wann benutzt man es? Worauf achten? -->

**Was macht es?** Das Netz übergeht alle Details, die nicht größer sind als die `Defeature Size`. Die Geometrie selbst bleibt unverändert. Standardmäßig ist das aktiv, und die `Defeature Size` richtet sich nach der Elementgröße.

<figure style="text-align:center;">
  <img src="../images/Netz_Defeaturing.excalidraw.png" alt="Platte mit kleiner Nut: Ist die Defeature Size kleiner als die Nut, folgt das Netz der Nut. Ist sie größer, fehlt die Nut im Netz." width="800" class="no-lightbox">
</figure>

**Wann benutzt man es?** Wenn kleine Details sehr kleine Elemente erzwingen oder die Vernetzung scheitern lassen. Das sind zum Beispiel winzige Flächen oder kurze Kanten, oft aus dem CAD-Import.

**Worauf achten?**

- Das Netz ist dann nicht mehr genau das Bauteil. Das ist nur in Ordnung, wenn die weggelassenen Details für die Auswertung keine Rolle spielen.
- Wenn ein Radius im Netz fehlt, hat das Netz dort eine scharfe Kante und damit eine Singularität. Schauen Sie sich das Netz deshalb immer dort an, wo Sie die Spannung auswerten.

## Inflation: dünne Lagen an der Verrundung

<!-- ENTWURF 10.11.2026 (Felix prüft), am 12.11. gegliedert wie die anderen Einstellungen. ANSYS-Bildpaar ohne und mit Inflation am 12.11. entfernt.
     Skizze (11.11.2026): bilder/P3_Vorgehen_excalidraw.py Netz_Inflation im Vault. -->

**Was macht es?** Eine lokale Netzgröße auf einer Fläche (`Face Sizing`) legt nur fest, wie lang die Elemente auf der Oberfläche sind. Wie tief sie reichen, entscheidet ANSYS. `Inflation` erzeugt zusätzlich dünne Elementlagen parallel zur Oberfläche. Damit ist auch die Elementgröße in die Tiefe festgelegt.

<figure style="text-align:center;">
  <img src="../images/Netz_Inflation.excalidraw.png" alt="Schnitt durch die Verrundung, schematisch: Mit Face Sizing ist nur die Elementlänge h auf der Oberfläche fest, die erste Elementlage reicht mal flach, mal tief. Mit Inflation liegen fünf dünne Lagen parallel zur Oberfläche, zusammen etwa h dick, die dünnste an der Oberfläche." width="800" class="no-lightbox">
</figure>

**Wann benutzt man es?** Wenn Sie die Spannung in einer Verrundung oder Kerbe auswerten. Dort fällt sie in die Tiefe steil ab.

**Worauf achten?**

- Einfügen mit `Rechtsklick Strukturbaum Mesh → Insert → Inflation`: unter `Geometry` der Körper, unter `Boundary` die Fläche der Verrundung.
- Wenn unter `Geometry` eine Fläche statt des Körpers steht, lassen sich bei `Boundary` nur Kanten wählen.
- Die Standardwerte lassen: `Smooth Transition`, 5 Lagen, `Growth Rate` 1,2. Dann sind die Lagen zusammen etwa so dick wie eine Elementkante. Die dünnste Lage liegt an der Oberfläche.
- Wenn Sie die Elementgröße auf der Fläche halbieren, werden auch die Lagen halb so dick. Für die Konvergenzstudie ändern Sie deshalb nur die Elementgröße im `Face Sizing`.
- Mit Inflation vernetzt `Automatic` den Körper mit Tetraedern und Prismen statt mit Hexaedern.

Mehr dazu in der ANSYS-Hilfe: [Transition](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/msh_Trans.html), [Mesh Defeaturing](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/msh_auto_defeat.html) und [Inflation](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/ds_Inflation_Group.html).

## Faustregeln für Spannungen in Verrundungen und Kerben

- In der Verrundung höchstens ein Viertel des Radius als Elementgröße (r/4), entlang der Oberfläche und in die Tiefe. Auf einem 90°-Bogen sind das mindestens 7 Elemente.
- Diese Regel steht in den [IIW-Empfehlungen für Schweißnähte](https://doi.org/10.1007/978-3-319-23757-2) (Hobbacher, Springer 2016, Abschnitt 2.2.4) und lässt sich auf andere Kerben übertragen.
- Die Tiefe mit `Inflation` festlegen.
- Die Faustregel liefert nur den Startwert. Ob das Netz reicht, zeigt erst die Konvergenzstudie.

## Konvergenz prüfen

<!-- ENTWURF 12.11.2026 (Felix): war die eigene Seite „Diskussion“, dann „Konvergenz prüfen“; jetzt Abschnitt dieser Seite.
     Nur die Empfehlung (mindestens drei Netze, immer halbieren, letzte Änderung unter 1 %), Felix prüft die Formulierung. -->

Ob das Netz an der Stelle reicht, an der Sie die Spannung auswerten, zeigt eine Konvergenzstudie:

- Mit **mindestens drei Netzen** rechnen und die Elementgröße dabei **jedes Mal halbieren**.
- Wenn sich die Spannung beim letzten Halbieren um **weniger als 1&nbsp;%** ändert, gilt das Netz als konvergiert.
- Wenn die Änderung beim Halbieren nicht kleiner wird, liegt wahrscheinlich eine **Singularität** vor. Dann den Ort prüfen (scharfe Kante, feste Einspannung, Punktlast) und dort nicht auswerten.

**Warum mindestens drei Netze?** Zwei Netze reichen nicht:

- Ein großer Sprung kann auch von einem zu groben ersten Netz kommen.
- Ein kleiner Unterschied kann täuschen.
- Erst das dritte Netz zeigt, ob die Änderung kleiner wird.

So sah das beim L-Profil aus (mit Inflation, global 3&nbsp;mm):

| lokale Elementgröße | Spannung σ<sub>vM</sub> | Änderung zur vorigen Netzgröße |
| ------------------:| -----------------------:| ------------------------------:|
| 1&nbsp;mm          | 624,82&nbsp;MPa          |                                |
| 0,5&nbsp;mm        | 601,92&nbsp;MPa          | −3,7&nbsp;%                    |
| 0,25&nbsp;mm       | 597,67&nbsp;MPa          | <span style="color:green;">−0,7&nbsp;%</span> |

Die Änderung wird kleiner und liegt beim letzten Halbieren unter 1&nbsp;%: Das Netz mit 0,25&nbsp;mm ist konvergiert.
