---
icon: material/clipboard-check-outline
hide:
  - toc
---

# Sensitivitätsanalyse

Ziel bei der Bestimmung der Netzgröße ist es, eine numerische `Konvergenz` zu erreichen. Dafür wird eine sogenannte `Sensitivitätsanalyse` verwendet.  

Dabei wird untersucht, wie empfindlich eine Ergebnisgröße (z. B. Verschiebung und/oder Spannung) auf eine Veränderung der Netzgröße reagiert. Typischerweise wird die Netzgröße schrittweise (z. B. durch Halbierung) verkleinert und die Ergebnisse werden miteinander verglichen.

Von einer Konvergenz spricht man, wenn sich die betrachtete Größe zwischen zwei aufeinanderfolgenden Vernetzungen nicht mehr signifikant ändert. Im Allgemeinen gilt eine Änderung von weniger als etwa 1 % als ausreichend klein.

<figure style="text-align:center;">
    <img src="../images/Netzverfeinerung.excalidraw.png" alt="Konvergenz und Singularität" width="600">
</figure>


# Singularitäten

Konvergiert die Spannung bei Netzverfeinerung nicht gegen einen Grenzwert, so handelt es sich wahrscheinlich um eine <code>Singularität</code>. Solche Spannungssingularitäten entstehen typischerweise durch idealisierte Randbedingungen oder Geometrien, zum Beispiel:

- feste Einspannungen
- Einzelkräfte (Punktlasten)
- scharfe innere Kanten (z. B. 90°-Innenkanten ohne Verrundung)

Bei <code>scharfen Kanten</code> kann man die Geometrie oft realitätsnäher mit einer Verrundung modellieren und anschließend an dieser verrundeten Stelle die Spannungen auswerten.

Bei <code>festen Einspannungen</code> und <code>Einzelkräften</code> können die direkt betroffenen Bereiche von der Spannungsauswertung ausgeschlossen werden. Stattdessen betrachtet man die Spannungen in einem gewissen Abstand im „unauffälligen“ Bereich des Bauteils.

Feste Einspannungen können außerdem durch andere Lagerungsbedingungen (z. B. Elastic Support oder Remote Displacement) ersetzt werden. Gerade bei Remote Displacement ist jedoch zu prüfen, ob die resultierende Verformungsform noch der realen Situation entspricht. 


!!! tip "Vertiefung: Lagerungen in Übung 6 aus Praktikum 2"

    In **Übung 6 / Praktikum 2** hatten wir die unterschiedliche Lagerungsarten (feste Einspannung, Elastic Support, Remote Displacement) am Beispiel des Inbus systematisch durchgespielt.

    <figure style="text-align:center;">
        <img src="../../../P2_Geometrie_Randbedingungen/02_Lagerungen/images/Uebung-06.png" alt="Lagerungen in Übung 6" width="700">
        <figcaption>Beispiel: Randbedingungen in Übung&nbsp;2 (Übung&nbsp;6)</figcaption>
    </figure>

    [Zu Übung6 vom Praktikum 2](../../P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-6.md){ .md-button .md-button--primary }


# Vorgehen zur Bestimmung der geeigneten Netzgröße

Ein mögliches allgemeines Vorgehen zur Bestimmung einer geeigneten Netzgröße ist hier schematisch dargestellt:

<figure style="text-align:center;">
    <img src="../images/Algorithmus.excalidraw.png" alt="Algorithmus zur Bestimmung der Netzgröße" width="900">
</figure>

!!! info "TL;DR:"

    1. Spannungen an Singularitäten nicht bewerten (oder nur mit großem Vorbehalt) – ggf. Geometrie/Randbedingungen realitätsnäher modellieren.
    2. Netzgröße so lange (insbesondere in kritischen Bereichen) verfeinern, bis sich die relevanten Spannungen nur noch maximal um etwa 1 % ändern.


