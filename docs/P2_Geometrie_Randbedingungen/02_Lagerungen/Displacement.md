---
icon: material/triangle
hide:
  - toc
sektion: Lagerungen
title: Lager
order: 110
thumb: images/Lager.png
---

# Lager mit `Displacement` , `Fixed Support` und `Frictionless Support`

Grundsätzlich kann man die Standardlager in ANSYS Mechanical alle mit `Displacement` umsetzen und auf die jeweilige Geometrie und die jeweiligen Richtungen auf Null setzen. Für die Sperrung aller Freiheitsgrade gibt es jedoch `Fixed Support` und für die Bewegung nur innerhalb eine Ebene den `Frictionless Support`. 


Je nach Geometrie (Fläche oder Kante) und Freigabe einer Verschiebung (ja/nein) ergeben sich dabei folgende Lagerungen:

<figure style="text-align:center;">
    <img src="../images/Lager.png" alt="Übersicht über Standardlager und Umsetzung mit ANSYS" width="800">
</figure>

!!! info "Hinweis zum Loslager"

    Je nachdem ob man zusätzlich eine Starrkörperbewegung unterdrücken will kann beim Loslager auch eine zweite Bewegungsrichtung frei sein.