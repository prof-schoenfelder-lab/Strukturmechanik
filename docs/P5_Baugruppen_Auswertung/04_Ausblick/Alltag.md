---
icon: material/message-alert-outline
hide:
  - toc
sektion: Ausblick
title: Meldungen und große Modelle
order: 320
kurz: Die häufigsten Meldungen lesen, Rechenzeit sparen, Projekte sichern
thumb: images/Nichtlinearitaeten.excalidraw.png
---

# :material-message-alert-outline: Meldungen und große Modelle

## Meldungen lesen

Mechanical schreibt Warnungen und Fehler ins Fenster `Messages`. Die Meldung nennt meist schon die Ursache. Die häufigsten:

| Meldung | Was sie bedeutet | Was tun |
|---|---|---|
| „One or more parts may be underconstrained and experiencing rigid body motion“ | Ein Bauteil hat keinen Halt | Lager und Kontakte prüfen: Hängt jedes Bauteil an etwas? |
| „An internal solution magnitude limit was exceeded“ | Meist dasselbe: Ein Bauteil ist nicht gehalten, oder eine Last ist um Größenordnungen zu groß | Lager, Kontakte und Einheiten der Lasten prüfen |
| „The deformation is large compared to the model bounding box“ | Die Verschiebung ist größer als ein Zehntel des Modells | Lasten, Einheiten und Dicken prüfen |
| „One or more contact regions may not be in initial contact“ | Zwischen zwei Kontaktflächen ist am Anfang ein Spalt | Kontakt vor der Rechnung prüfen ([Umsetzung in ANSYS](../01_Verbindungen/Umsetzung.md)) |
| „The solver engine was unable to converge“ | Eine nichtlineare Rechnung findet kein Gleichgewicht | Lagerung, Höhe der Last und Kontaktart prüfen |
| „The solver has found conflicting DOF constraints“ | Zwei Lager verlangen am selben Knoten Verschiedenes | überlappende Lager suchen |

Wenn ein Bauteil keinen Halt hat, dann bricht die Rechnung in der Regel ab. Weitere Fehlerquellen stehen in der [Fehler-Checkliste](../../00_FAQ/Fehler_checkliste.md).

## Große Modelle

Mit der Zahl der Bauteile wachsen Rechenzeit und Fehlerquellen.

- Wenn eine Fuge im Betrieb weder aufgeht noch gleitet, dann reicht Verbund oder gemeinsame Topologie. Jeder Kontakt, der abheben kann, macht die Rechnung nichtlinear und damit um ein Vielfaches länger.
- Wenn ein Detail für die gesuchte Stelle nichts ändert, dann weglassen: kleine Bohrungen, Fasen, Schriftzüge ([Praktikum 2, Vereinfachungen](../../P2_Geometrie_Randbedingungen/01_Geometrie_anpassen/Vereinfachungen.md)).
- Wenn Geometrie, Lager und Lasten symmetrisch sind, dann nur einen Teil rechnen. Wenn ein Bauteil dünn oder schlank ist, dann als Schale oder Balken ([Praktikum 4](../../P4_Abstraktionen/index.md)).
- Wenn ein Bauteil viel steifer ist als der Rest und selbst nicht interessiert, dann durch ein Lager ersetzen, wie die Dummies in [Praktikum 2, Übung 3](../../P2_Geometrie_Randbedingungen/02_Lagerungen/Uebung-4.md).

## Projekte sichern und weitergeben

- Zum Weitergeben das Projekt als Archiv speichern (`.wbpz`), wie in [Praktikum 1](../../P1_Einfuehrung/abspeichern.md).
- Von den Dateien einer Rechnung ist nur die Ergebnisdatei groß. Wenn das Archiv klein bleiben soll, dann vorher die Ergebnisse löschen: `Rechtsklick Strukturbaum Solution → Clear Generated Data`. Die Rechnung lässt sich jederzeit wiederholen.
- Wenn Geometrie oder Netz eines gerechneten Projekts geändert werden, dann löscht Mechanical die alten Ergebnisse. Wer einen Stand behalten will, speichert vorher eine Kopie.
- Ein Projekt aus einer neueren ANSYS-Version lässt sich in einer älteren nicht öffnen.
