---
icon: material/help-box
---

# zweiseitig gelagerter Balken

Als einfaches Beispiel starten wir mit einem zweiseitig gelagerten Balken mit Linienlast. Dieser ist in der Geometrie leicht zu erstellen und wir können die Lösungen leicht mit analytischen Gleichungen überprüfen.

<!-- --8<-- [start:Aufgabenstellung] -->
<figure style="text-align:center;">
  <img src="../images/Aufgabenstellung.png" alt="Aufgabenstellung" width="400" class="no-lightbox">
</figure>
<!-- --8<-- [end:Aufgabenstellung] -->

## Gesucht

1. Die maximale Durchbiegung $u_{\max }$
2. Die maximale Spannung in y-Richtung $\sigma_{y, \max }$

## Gegeben

### Material

<!-- --8<-- [start:Material] -->
Stahl

- Elastizitätsmodul $E=200 \mathrm{GPa}$
- Querkontraktionszahl $\nu=0,3$
<!-- --8<-- [end:Material] -->

### Geometrie

<!-- --8<-- [start:Geometrie] -->
Balken mit rechteckigem Querschnitt

- Länge $L=1000 \mathrm{~mm}$
- Breite $b=30 \mathrm{~mm}$
- Breite $h=30 \mathrm{~mm}$
<!-- --8<-- [end:Geometrie] -->

### Vernetzung

<!-- --8<-- [start:Vernetzung] -->
- Netzgröße global: 15 mm
<!-- --8<-- [end:Vernetzung] -->


### Randbedingungen (Lagerung und Belastung)

<!-- --8<-- [start:Randbedingungen] -->
- Loslager auf der linken Seite
- Festlager auf der rechten Seite
- Flächenlast $q_0=1000 \mathrm{~N}$
<!-- --8<-- [end:Randbedingungen] -->
