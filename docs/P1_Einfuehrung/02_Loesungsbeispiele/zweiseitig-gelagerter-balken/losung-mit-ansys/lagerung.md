---
icon: material/timeline-check-outline
hide:
    - toc
---

# Lagerung

## Aufgabenstellung

<figure style="text-align:center;">
  <img src="../../images/Aufgabenstellung.png" alt="Aufgabenstellung" width="400" class="no-lightbox">
</figure>

--8<-- "P1_Einfuehrung/02_Loesungsbeispiele/zweiseitig-gelagerter-balken/Aufgabenstellung.md:Lagerung"

## Umsetzung

Wir beginnen mit dem Festlager auf der unteren Kante der linken Seite. Wir wollen hier die Verschiebungsfreiheitsgrade in x,y und z Richtung auf Null setzen (also eine Verschiebung verhindern). Dafür gibt es eine spezielle Randbedingungen die `Fixed Support` heißt.


<div class="tutorial-embed"
   data-tutorial="/assets/tutorials/Festlager_anbringen"
   style="width:800px">
</div>

Das Loslager ist Unterseite unten gegenüber. Hier sollen nur die Verschiebungsfreiheitsgrade in  x und z Richtung verhindert werden (also auf Null gesetzt). Dafür verwenden wir die Randbedingung `Displacement`.

<div class="tutorial-embed"
   data-tutorial="/assets/tutorials/Loslager_anbringen"
   style="width:800px">
</div>