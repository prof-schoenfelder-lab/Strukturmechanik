---
icon: material/chat-question
hide:
  - toc
---

# Diskussion

Wir haben zu Beginn gelernt, dass bei einer `Sensitivitätsanalyse` die Netzgröße so lange (mindestens) halbiert wird, bis die Abweichung unter 1&nbsp;% liegt. Wenn wir uns dies jedoch für unser L-Profil-Beispiel anschauen, sehen wir, dass sich bereits nach der Verfeinerung von 3&nbsp;mm auf 1,5&nbsp;mm die Spannung nur um 0,2&nbsp;% verringert:

<figure style="text-align:center;">
    <img src="../images/Diskussion.excalidraw.png" alt="Diskussion" width="700">
</figure>

Somit ist **nicht nur die Netzgröße**, sondern auch der **Spannungsgradient innerhalb eines Elements** ein wichtiger Faktor. Dies kann man über den Wert `Nodal Fraction` in der `Display Option` des Spannungs-Plots ausgeben. 

`Nodal Fraction` ist die normierte prozentuale Abweichung der Knotenspannungen pro Element. Dieser Wert sollte im interessierenden Bereich **möglichst kleiner als 10&nbsp;%** sein.

<figure style="text-align:center;">
    <img src="../images/DisplayOption.png" alt="Display Option" width="400">
</figure>

??? info "Für Interessierte: Berechnung des Nodal-Fraction-Wertes (Klick auf den Pfeil rechts)"
    
    `Elemental Fraction` = `Elemental Difference` / `Elemental Mean`

    `Elemental Difference` =  
    \[
      \max\bigl(\lvert N1 - N2 \rvert,\; \lvert N2 - N3 \rvert,\; \lvert N3 - N4 \rvert,\; \lvert N4 - N1 \rvert \bigr)
    \]

    N1, N2, N3, N4 ... Knotenspannungen an den Knoten 1, 2, 3, 4

    `Elemental Mean` = Mittelwert aus den Knotenspannungen 

    <figure style="text-align:center;">
        <img src="../images/Nodal_Fraction.excalidraw.png" alt="Nodal Fraction" width="800">
    </figure>


Hier mal am Beispiel von 3mm und 0,25mm die normalen Spannungswerte (DisplayOption: averaged) und die Nodal Fraction:

<figure style="text-align:center;">
    <img src="../images/Averaged_vs_NodalFraction.excalidraw.png" alt="Averaged vs NodalFraction" width="1100">
</figure>

Hier nun alle Werte für unser Beispiel:

| Elementgröße [mm] | Spannung σ<sub>vM</sub> [MPa] | Spannungsdifferenz zur nächsten Verfeinerung                         | max. Nodal Fraction                             | Konvergenz?                                      |
| -----------------:| -----------------------------:| ---------------------------------------------------------------------:| -----------------------------------------------:|:------------------------------------------------|
| 3                 | 549,5                         | –                                                                     | <span style="color:red;">32&nbsp;%</span>       | <span style="color:red;">Nein</span>            |
| 1,5               | 548,2                         | <span style="color:green;">−0,2&nbsp;%</span>                        | <span style="color:red;">12&nbsp;%</span>       | <span style="color:red;">Nein</span>            |
| 0,5               | 586                           | <span style="color:red;">+6,9&nbsp;%</span>                          | <span style="color:green;">9&nbsp;%</span>      | <span style="color:red;">Nein</span>            |
| 0,25              | 582                           | <span style="color:green;">−0,6&nbsp;%</span>                        | <span style="color:green;">5&nbsp;%</span>      | <span style="color:green;">Ja</span>            |

!!! info "Vereinfacht kann man auch sagen:"

    Wenn sich die der rote Bereich der Spannung über mehrere Elemente erstreckt, ist der Spannungsgradient im Element meist klein genug.

    Die Darstellung der Elemente im Spannungsplot kann man einstellen, wenn im Strukturbaum ein Ergebnis ausgewählt ist: Im Reiter `Result` unter `Edges`:`Show Elements`

    <figure style="text-align:center;">
        <img src="../images/Show_Elements.png" alt="Averaged vs NodalFraction" width="800">
    </figure>
 