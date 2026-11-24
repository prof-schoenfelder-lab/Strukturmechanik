---
icon: material/link-variant
hide:
  - toc
sektion: Verbindungen und Kontakte
title: Bauteile verbinden
order: 10
kurz: Was Mechanical beim Import anlegt und welche Wege es gibt
thumb: images/Verbindungen.excalidraw.png
---

# :material-link-variant: Bauteile verbinden

Eine Baugruppe besteht aus mehreren Körpern. Jeder Körper bekommt sein eigenes Netz. Ohne Verbindung wissen die Körper nichts voneinander: Kräfte gehen nicht von einem zum anderen über, und ein Körper ohne Lager hat keinen Halt.

<figure style="text-align:center;">
  <img src="../images/Verbindungen.excalidraw.png" alt="Drei Wege, zwei Körper zu verbinden: gemeinsame Topologie mit durchgehendem Netz, Kontakt zwischen zwei Netzen, Gelenk zwischen zwei Punkten" width="900">
</figure>

## Was Mechanical beim Import tut

- Wenn sich zwei Körper an Flächen berühren, dann legt Mechanical dort beim Import selbst einen Kontakt an. Die Kontakte stehen unter `Strukturbaum → Connections → Contacts`.
- Die Kontaktart ist dabei immer Verbund (`Bonded`): Die Flächen sind wie verklebt.

!!! warning "Verbund hält auch auf Zug"
    - Mit Verbund kann eine Fuge weder aufgehen noch gleiten.
    - Wenn die Fuge das in Wirklichkeit kann, dann rechnet das Modell die Baugruppe zu steif.
    - Nach dem Import also jeden Kontakt ansehen und entscheiden, ob Verbund passt.

## Drei Wege, zwei Körper zu verbinden

| Weg | Was verbunden wird | Was man bekommt | In diesem Kurs |
|---|---|---|---|
| gemeinsame Topologie | Die Körper teilen sich an der Fuge die Knoten, das Netz läuft durch | ein Stück, ganz ohne Kontakt | Inbus und Schraubkopf in [Praktikum 2, Übung 4](../../P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-6.md) |
| Kontakt (`Contact Region`) | zwei Flächen, die Netze bleiben getrennt | Druck, Abheben und Gleiten in der Fuge, je nach Kontaktart | [Übung 1](Uebung-1.md) |
| Gelenk (`Joint`) | zwei Punkte, die Flächen hängen starr oder verformbar daran | Kräfte und Momente am Punkt, frei wählbare Freiheitsgrade | Dummies am Rahmen in [Praktikum 2, Übung 3](../../P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-4.md) |

- Außerdem gibt es die Feder (`Spring`) und den Balken (`Beam`). Beide verbinden wie das Gelenk zwei Punkte. Der Balken steht oft für eine Schraube, siehe [Schrauben berechnen](../02_Schraube/Schraube.md).
- Gemeinsame Topologie wird schon an der Geometrie eingestellt, in SpaceClaim über die Eigenschaft `Share Topology` der Komponente.

<!-- ENTWURF: Klickweg für Share Topology in SpaceClaim 2025 R2 im Pool prüfen (im Archiv aus P2 steht shareTopologyOption = Share an der Komponente „mit Schraube“). -->

## Welcher Weg passt?

- Wenn die Bauteile verschweißt oder verklebt sind, dann gemeinsame Topologie oder Kontakt mit Verbund.
- Wenn die Fuge aufgehen oder gleiten kann und genau das für das Ergebnis zählt, dann Kontakt mit einer Kontaktart, die das zulässt. Welche es gibt, steht auf der Seite [Kontaktarten](Kontakte.md).
- Wenn nur zählt, wie sich die Bauteile gegeneinander bewegen (Drehgelenk, Führung), dann ein Gelenk (`Joint`).
- Wenn eine Schraube nur Kräfte übertragen soll und ihre Umgebung nicht interessiert, dann ein Balken (`Beam`).

!!! info "Punkt statt Fläche"
    Gelenk, Feder und Balken brauchen deutlich weniger Rechenzeit als ein Kontakt. Dafür zeigen sie nicht, was in der Fuge passiert: keine Pressung, kein Abheben.
