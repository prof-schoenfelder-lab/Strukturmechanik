---
icon: material/alpha-a-box
hide:
  - toc
---

# Umsetzung vom Ebenen Spannungszustand in ANSYS

## Geometrie (SpaceClaim)

<!-- --8<-- [start:Geometrie] -->
In `SpaceClaim` eine Skizze immer in der `x-y` Ebene zeichnen:

<figure style="text-align:left;">
    <img src="../images/SpaceClaim1.png" alt="Skizze in x-y Ebene" width="800">
</figure>

Und darauf achten dass die Skizze beendet wird und im Strukturbaum der Eintrag `Surface` steht.

<figure style="text-align:left;">
    <img src="../images/SpaceClaim2.png" alt="Auf Eintrag im Strukturbaum achten" width="200">
</figure>
<!-- --8<-- [end:Geometrie] -->

## ANSYS Workbench Projektmenü

<!-- --8<-- [start:WBProjektmenue] -->
Im Workbench Projektmenü Rechtsklick auf `Geometry` und im Properties Fenster `Analysis Type=2D` einstellen: 

<figure style="text-align:left;">
    <img src="../images/Geometry2D.png" alt="Einstellung WB Projektmenü für Geometry" width="800">
</figure>
<!-- --8<-- [end:WBProjektmenue] -->

## ANSYS Mechanical

<!-- --8<-- [start:Mechanical] -->
Im Mechanical die `Geometry auswählen` und im Detailfenster `2D Behavior=Plane Stress` einstellen:  

<figure style="text-align:left;">
    <img src="../images/PlaneStress.png" alt="Einstellung Mechanical" width="400">
</figure>

Im Mechanical die `Fläche auswählen` und im Detailfenster über `thickness` die Dicke in die Richtung die reduziert wurde (z-Richtung) einstellen:  

<figure style="text-align:left;">
    <img src="../images/PlaneStress2.png" alt="Dicke einstellen" width="400">
</figure>

Im 2D werden `Lagerungen`, `Lasten` sowie mögliche `Ergebnisauswertungen` auf Punkten und Linien angebracht:

- (3D) Fläche > (2D) Linie
- (3D) Linie > (2D) Punkt
<!-- --8<-- [end:Mechanical] -->
