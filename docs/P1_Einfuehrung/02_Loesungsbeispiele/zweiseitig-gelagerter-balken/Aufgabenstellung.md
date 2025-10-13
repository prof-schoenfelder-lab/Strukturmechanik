---
icon: material/help-box
---

# zweiseitig gelagerter Balken mit Flächenlast

Als einfaches Beispiel starten wir mit einem zweiseitig gelagerten Balken mit Flächenlast. Dieser ist in der Geometrie leicht zu erstellen und wir können die Lösungen leicht mit analytischen Gleichungen überprüfen.

<figure style="text-align:center;">
  <img src="../images/Aufgabenstellung.png" alt="Aufgabenstellung" width="400" class="no-lightbox">
</figure>

## Gesucht

<!-- --8<-- [start:Gesucht] -->
1. Die maximale Durchbiegung $u_{\max }$
2. Die maximale Spannung in y-Richtung $\sigma_{y, \max }$
<!-- --8<-- [end:Gesucht] -->

## Gegeben

### Material

<!-- --8<-- [start:Material] -->
Stahl

- Elastizitätsmodul $E=210 \mathrm{GPa}$
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


### Randbedingungen

Lagerung:

<!-- --8<-- [start:Lagerung] -->
- Loslager auf der linken Seite
- Festlager auf der rechten Seite
<!-- --8<-- [end:Lagerung] -->

Belastung:

<!-- --8<-- [start:Belastung] -->
- Flächenlast $q_0=1000 \mathrm{~N}$
<!-- --8<-- [end:Belastung] -->
