---
icon: material/alpha-a-box
hide:
  - toc
---

# Umsetzung von Rotationssymmetrie in ANSYS

Die Umsetzung ist im Prinzip analog zum `ebenen Spannungszustand`.  
Der Unterschied: In Mechanical muss das `2D Behavior` auf `Axissymmetric` gestellt werden und es wird **keine Dicke** eingetragen.

## Geometrie (SpaceClaim)

<!-- --8<-- [start:Geometrie] -->
In `SpaceClaim` eine Skizze in der `x-y`-Ebene zeichnen:

<figure style="text-align:left;">
    <img src="../../02_ESZ/images/SpaceClaim1.png" alt="Skizze in x-y Ebene" width="800">
</figure>

!!! danger "Die Rotationsachse muss immer die y-Achse sein"

    Für ein achsensymmetrisches Modell in Ansys gilt:  
    - x-Richtung = Radius  
    - y-Richtung = Achse der Rotation  
    Die Skizze wird also im x-y-Schnitt gezeichnet und um die y-Achse „gedreht“.

Darauf achten, dass die Skizze beendet wird und im Strukturbaum der Eintrag `Surface` erscheint.

<figure style="text-align:left;">
    <img src="../../02_ESZ/images/SpaceClaim2.png" alt="Auf Eintrag im Strukturbaum achten" width="200">
</figure>
<!-- --8<-- [end:Geometrie] -->

## ANSYS Workbench Projektmenü

<!-- --8<-- [start:WBProjektmenue] -->
Im Workbench-Projektmenü per Rechtsklick auf `Geometry` im Properties-Fenster `Analysis Type = 2D` einstellen:

<figure style="text-align:left;">
    <img src="../../02_ESZ/images/Geometry2D.png" alt="Einstellung WB Projektmenü für Geometry" width="800">
</figure>
<!-- --8<-- [end:WBProjektmenue] -->

## ANSYS Mechanical

<!-- --8<-- [start:Mechanical] -->
In Mechanical die `Geometry` auswählen und im Detailfenster `2D Behavior = Axissymmetric` einstellen:

<figure style="text-align:left;">
    <img src="../images/axissymmetric.png" alt="Einstellung Mechanical" width="400">
</figure>

Im 2D-Modell werden `Lagerungen`, `Lasten` sowie mögliche `Ergebnisauswertungen` auf Punkten und Linien angebracht:

- (3D) Fläche → (2D) Linie  
- (3D) Linie → (2D) Punkt
<!-- --8<-- [end:Mechanical] -->

<!-- --8<-- [start:Randbedingungen] -->
Die Mittelachse (y-Achse) muss nicht noch mal besonders gelagert werden.
<!-- --8<-- [end:Randbedingungen] -->


