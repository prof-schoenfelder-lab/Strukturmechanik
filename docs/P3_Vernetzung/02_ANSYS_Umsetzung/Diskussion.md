---
icon: material/chat-question
hide:
  - toc
---

# Diskussion

Wir haben zu Beginn gelernt, dass bei einer `Sensitivitätsanalyse` die Netzgröße so lange (mindestens) halbiert wird, bis die Abweichung unter 1&nbsp;% liegt. Wenn wir uns dies jedoch für unser L-Profil-Beispiel anschauen, sehen wir, dass sich bereits nach der Verfeinerung von 3&nbsp;mm auf 1,5&nbsp;mm die Spannung nur um 0,04&nbsp;% ändert:

<figure style="text-align:center;">
    <img src="../images/Diskussion_2025R2.excalidraw.png" alt="Diskussion" width="700">
</figure>

Somit ist **nicht nur die Netzgröße**, sondern auch der **Spannungssprung zwischen benachbarten Elementen** ein wichtiger Faktor. Dies kann man über den Wert `Nodal Fraction` in der `Display Option` des Spannungs-Plots ausgeben. 

`Nodal Fraction` vergleicht an jedem Knoten die Spannungen der Elemente, die sich diesen Knoten teilen: größte Differenz geteilt durch den Mittelwert. Dieser Wert sollte im interessierenden Bereich **möglichst kleiner als 10&nbsp;%** sein.

<figure style="text-align:center;">
    <img src="../images/DisplayOption.png" alt="Display Option" width="400">
</figure>

??? info "Für Interessierte: Berechnung des Nodal-Fraction-Wertes (Klick auf den Pfeil rechts)"
    
    `Nodal Fraction` = `Nodal Difference` / `Nodal Average`

    `Nodal Difference` = größte Differenz der ungemittelten Spannungen am Knoten:

    \[
      \max(\sigma_1, \dots, \sigma_n) - \min(\sigma_1, \dots, \sigma_n)
    \]

    - \(\sigma_1, \dots, \sigma_n\): ungemittelte Spannungen am Knoten, je angrenzendem Element ein Wert
    - \(n\): Anzahl der Elemente, die sich den Knoten teilen

    `Nodal Average` = Mittelwert dieser Spannungen

    <figure style="text-align:center;">
        <img src="../images/Nodal_Fraction_Knoten.excalidraw.png" alt="Vier Elemente an einem Knoten mit 96, 104, 100 und 100 MPa: Nodal Difference 8 MPa, Nodal Average 100 MPa, Nodal Fraction 8 %" width="700">
    </figure>


Hier mal am Beispiel von 3&nbsp;mm und 0,25&nbsp;mm die normalen Spannungswerte (DisplayOption: averaged) und die Nodal Fraction:

<figure style="text-align:center;">
    <img src="../images/Averaged_ohneWerte.excalidraw.png" alt="Averaged vs NodalFraction" width="1100">
</figure>

Hier nun alle Werte für unser Beispiel:

| Elementgröße [mm] | Spannung σ<sub>vM</sub> [MPa] | Änderung zur vorigen Netzgröße                                       | max. Nodal Fraction                             | Konvergenz?                                      |
| -----------------:| -----------------------------:| ---------------------------------------------------------------------:| -----------------------------------------------:|:------------------------------------------------|
| 3                 | 547,3                         |                                                                       | <span style="color:red;">31&nbsp;%</span>       | <span style="color:red;">Nein</span>            |
| 1,5               | 547,5                         | <span style="color:green;">+0,04&nbsp;%</span>                       | <span style="color:red;">13&nbsp;%</span>       | <span style="color:red;">Nein</span>            |
| 0,5               | 584,7                         | <span style="color:red;">+6,8&nbsp;%</span>                          | <span style="color:green;">6&nbsp;%</span>      | <span style="color:red;">Nein</span>            |
| 0,25              | 595,8                         | <span style="color:red;">+1,9&nbsp;%</span>                          | <span style="color:green;">3&nbsp;%</span>      | <span style="color:red;">Nein</span>            |
| 0,125             | 599,6                         | <span style="color:green;">+0,6&nbsp;%</span>                        | <span style="color:green;">4&nbsp;%</span>      | <span style="color:green;">Ja</span>            |

!!! important "Wichtig"

    Bei 0,5 mm und 0,25 mm liegt die Nodal Fraction bereits unter 10 %,
    die Spannung ändert sich aber noch um mehr als 1 %.
    Erst bei 0,125 mm sind beide Kriterien erfüllt.
    Wenn nur eines der beiden Kriterien geprüft wird,
    kann das Netz also noch zu grob sein.


!!! info "Vereinfacht kann man auch sagen:"

    Wenn sich der rote Bereich der Spannung über mehrere Elemente erstreckt, ist der Spannungsgradient im Element meist klein genug.

    Die Darstellung der Elemente im Spannungsplot kann man einstellen, wenn im `Strukturbaum` ein Ergebnis ausgewählt ist: `Reiter Result → Edges → Show Elements`

    <figure style="text-align:center;">
        <img src="../images/Show_Elements.png" alt="Averaged vs NodalFraction" width="800">
    </figure>
 