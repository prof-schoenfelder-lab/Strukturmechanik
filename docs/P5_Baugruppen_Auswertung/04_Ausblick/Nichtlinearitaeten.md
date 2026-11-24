---
icon: material/chart-bell-curve-cumulative
hide:
  - toc
sektion: Ausblick
title: Nichtlinearitäten
order: 310
kurz: Wann eine lineare Rechnung nicht mehr gilt
thumb: images/Nichtlinearitaeten.excalidraw.png
---

# :material-chart-bell-curve-cumulative: Nichtlinearitäten

Alle Rechnungen in diesem Kurs sind linear. Nichtlineare Rechnungen sind Stoff späterer Veranstaltungen. Hier geht es darum, zu erkennen, wann die lineare Rechnung an ihre Grenze kommt.

## Linear und nichtlinear

Linear heißt: Die Steifigkeit des Modells bleibt gleich, egal wie groß die Last ist.

- Doppelte Last ergibt doppelte Verformung und doppelte Spannung.
- Lastfälle lassen sich überlagern.
- Das Gleichungssystem wird einmal gelöst.

Nichtlinear heißt: Die Steifigkeit ändert sich mit der Last.

<figure style="text-align:center;">
  <img src="../images/Nichtlinearitaeten.excalidraw.png" alt="Drei Kraft-Weg-Kurven neben der linearen Geraden: Kontakt wird steifer, sobald sich ein Spalt schließt; ein dünnes Blech wird steifer, sobald es sich spannt; ein Werkstoff wird weicher, sobald er fließt" width="900">
  <figcaption>Drei Ursachen, drei Kennlinien: gestrichelt jeweils die lineare Rechnung</figcaption>
</figure>

## Drei Ursachen

| Ursache | Was passiert | Beispiel | Schalter in Mechanical |
|---|---|---|---|
| Kontakt | Eine Fuge geht auf oder zu, ein Bauteil legt sich an | Inbus im Schraubkopf, Trennfuge einer Schraube | Kontaktart, die abheben kann ([Kontaktarten](../01_Verbindungen/Kontakte.md)) |
| Geometrie | Die Verformung ist so groß, dass sie die Steifigkeit ändert | Angelrute, dünnes Blech | `Analysis Settings → Large Deflection` |
| Werkstoff | Spannung und Dehnung sind nicht mehr proportional | Fließen: Eine Büroklammer bleibt verbogen | Werkstoffmodell in den `Engineering Data` |

## Was sich dann ändert

- Mechanical rechnet in kleinen Lastschritten und wiederholt jeden so oft, bis das Gleichgewicht stimmt. Das dauert länger.
- Die Rechnung kann abbrechen, wenn Mechanical kein Gleichgewicht findet.
- Ergebnisse lassen sich nicht mehr hochrechnen: Doppelte Last heißt nicht doppelte Spannung.
- Lastfälle lassen sich nicht mehr überlagern, die Reihenfolge der Lasten zählt. Beispiel: erst vorspannen, dann belasten ([geführtes Beispiel](../02_Schraube/Beispiel.md)).

## Warnzeichen in einer linearen Rechnung

- Wenn die Vergleichsspannung über der Streckgrenze liegt, dann fließt der Werkstoff dort. Der Zahlenwert oberhalb der Streckgrenze ist kein echter Spannungswert.
- Wenn die Verformung groß gegen die Abmessungen des Bauteils ist, dann stimmt die lineare Rechnung nicht mehr. Mechanical meldet das selbst, sobald die Verschiebung ein Zehntel der Modellgröße übersteigt.
- Wenn sich ein dünnes Bauteil um mehr als ein Zehntel seiner Dicke durchbiegt, dann empfiehlt die ANSYS-Hilfe, mit `Large Deflection` zu rechnen.
- Wenn ein schlankes Bauteil unter Druck steht, dann kann es knicken oder beulen. Die lineare Rechnung zeigt das nicht.
- Wenn sich Bauteile im Verformungsbild im wahren Maßstab durchdringen, dann fehlt dort ein Kontakt.
- Wenn eine Fuge Zug überträgt, die in Wirklichkeit aufgehen würde, dann steht dort ein Kontakt mit Verbund.
