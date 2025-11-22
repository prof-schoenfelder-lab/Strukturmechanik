---
icon: material/blur
hide:
  - toc
---

# Definition Netz

Unter einem <code>Netz</code> verstehen wir die Gesamtheit aller Elemente, mit denen eine Geometrie in der Finite-Elemente-Methode diskretisiert wird. Das Netz ist im Wesentlichen durch den gewählten <code>Elementtyp</code> und die <code>Elementgröße</code> definiert. 

<figure style="text-align:center;">
    <img src="../images/Netz.excalidraw.png" alt="Definition Netz" width="500">
</figure>

# Elementtypen 

Bisher haben wir uns nur mit 3D-Elementen (Volumenelementen) beschäftigt. Diese werden von Workbench (ANSYS Mechanical) standardmäßig mit quadratischer Ansatzfunktion gewählt. Das bedeutet, dass diese Elemente zwischen den Eckknoten zusätzliche, sogenannte Mittelknoten besitzen. Durch die größere Anzahl an Freiheitsgraden sind sie in der Regel genauer, aber auch mit höherem Rechenaufwand verbunden.

<figure style="text-align:center;">
    <img src="../images/3D-Elemente.excalidraw.png" alt="3D-Elemente" width="600">
</figure>

Daneben gibt es noch 2D-Elemente (Flächenelemente), mit denen wir uns im nächsten Praktikum zum Thema Abstraktionen beschäftigen werden.

<figure style="text-align:center;">
    <img src="../images/2D-Elemente.excalidraw.png" alt="2D-Elemente" width="600">
</figure>

# Elementgröße

Die Elementgröße (auch Netzgröße genannt) gibt eine charakteristische Kantenlänge der Elemente zu Beginn der Vernetzung vor. Je mehr Elemente man hat, desto besser kann man z. B. die Durchbiegung abbilden – hier stark vereinfacht an einer Balkenbiegung dargestellt:

<figure style="text-align:center;">
    <img src="../images/Netzgroesse_einfach.excalidraw.png" alt="vereinfachte Darstellung Netzgröße" width="300">
</figure>

Zur adäquaten Abbildung der Verformungsform ist eine gewisse Netzfeinheit erforderlich. Mit zunehmender Netzverfeinerung konvergiert die FEM-Lösung im Allgemeinen gegen die exakte Lösung (vorausgesetzt, der Elementtyp ist geeignet und Randbedingungen sowie Materialmodell sind korrekt).

Die Verschiebungen werden in der FEM direkt approximiert und konvergieren typischerweise schneller als die Spannungen, da letztere aus den Ableitungen des Verschiebungsfeldes berechnet werden.

!!! info "Merke:"

    Bei Netzverfeinerung konvergieren die Verschiebungen in der FEM in der Regel schneller als die Spannungen.
