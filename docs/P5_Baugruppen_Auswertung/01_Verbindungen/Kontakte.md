---
icon: material/layers-triple-outline
hide:
  - toc
sektion: Verbindungen und Kontakte
title: Kontaktarten
order: 20
kurz: Verbund, Reibung und was dazwischen liegt
thumb: images/Kontaktarten.excalidraw.png
---

# :material-layers-triple-outline: Kontaktarten

Ein Kontakt beschreibt, was zwei Flächen miteinander tun dürfen. Zwei Fragen genügen, um die fünf Kontaktarten von Mechanical zu unterscheiden: Darf die Fuge abheben? Darf sie gleiten?

<figure style="text-align:center;">
  <img src="../images/Kontaktarten.excalidraw.png" alt="Die fünf Kontaktarten: Verbund, kein Abheben, reibungsfrei, rau und Reibung, jeweils mit der Angabe, ob die Fuge abheben und gleiten darf" width="900">
</figure>

| Kontaktart | in ANSYS | abheben | gleiten | Rechnung | Vorstellung |
|---|---|---|---|---|---|
| Verbund | `Bonded` | nein | nein | linear | geklebt |
| kein Abheben | `No Separation` | nein | ja, ohne Reibung | linear | Schlitten in der Führung |
| reibungsfrei | `Frictionless` | ja | ja, ohne Reibung | nichtlinear | Eis |
| rau | `Rough` | ja | nein | nichtlinear | Schleifpapier |
| Reibung | `Frictional` | ja | ja, sobald die Reibung überwunden ist | nichtlinear | echte Fuge |

## Linear oder nichtlinear

- Wenn die Fuge nicht abheben kann (Verbund, kein Abheben), dann steht vor der Rechnung fest, welche Flächen tragen. Mechanical löst das Gleichungssystem einmal, wie in allen bisherigen Praktika.
- Wenn die Fuge abheben kann, dann hängt es von der Last ab, welche Flächen tragen. Mechanical muss das in mehreren Durchläufen (Iterationen) herausfinden.
    - Die Rechnung dauert länger.
    - Die Rechnung kann abbrechen, wenn Mechanical kein Gleichgewicht findet.
- Mehr dazu auf der Seite [Nichtlinearitäten](../04_Ausblick/Nichtlinearitaeten.md).

## Reibung

Bei der Kontaktart Reibung haftet die Fuge, solange die Kraft entlang der Fuge klein genug bleibt:

$$
F_R \le \mu \cdot F_N
$$

- $F_R$: Reibkraft entlang der Fuge in N
- $\mu$: Reibungszahl, ohne Einheit
- $F_N$: Kraft senkrecht auf die Fuge in N

In Tabellen für Schraubenverbindungen stehen für Stahl auf Stahl Reibungszahlen zwischen 0,1 und 0,2. In den Übungen ist die Reibungszahl vorgegeben.

## Welche Kontaktart passt?

- Wenn die Fuge im Betrieb weder aufgeht noch gleitet, dann Verbund.
- Wenn die Fuge gleiten, aber nicht abheben kann (Führung, Passung), dann kein Abheben.
- Wenn die Fuge abheben kann, dann Reibung mit einer Reibungszahl.
- Reibungsfrei nur dann, wenn etwas anderes das Bauteil hält: Ein Bauteil, das nur an reibungsfreien Kontakten hängt, kann wegrutschen, und die Rechnung bricht ab.

!!! warning "Jedes Bauteil braucht Halt"
    - Wenn ein Bauteil an keinem Lager und an keinem Kontakt hängt, dann bricht die Rechnung ab.
    - Dasselbe gilt, wenn zwischen den Kontaktflächen am Anfang ein Spalt ist: Der Kontakt greift dann nicht.
    - Wie man beides vor der Rechnung findet, steht auf der Seite [Umsetzung in ANSYS](Umsetzung.md).
