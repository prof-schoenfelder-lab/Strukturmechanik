---
icon: material/check-circle-outline
hide:
  - toc
---

# Konvergenz prüfen

<!-- ENTWURF 12.11.2026 (Felix): Die Seite hieß „Diskussion“ und zeigte die Reihe ohne Inflation mit Nodal Fraction.
     Jetzt nur die Empfehlung: mindestens drei Netze, immer halbieren, letzte Änderung unter 1 %. Felix prüft die Formulierung.
     Datei bleibt Diskussion.md, damit Adresse und Verweise gleich bleiben. -->

Ob das Netz an der Stelle reicht, an der Sie die Spannung auswerten, zeigt eine Netzstudie:

- Mit **mindestens drei Netzen** rechnen und die Elementgröße dabei **jedes Mal halbieren**.
- Wenn sich die Spannung beim letzten Halbieren um **weniger als 1&nbsp;%** ändert, gilt das Netz als konvergiert.
- Wenn die Änderung beim Halbieren nicht kleiner wird, liegt wahrscheinlich eine **Singularität** vor. Dann den Ort prüfen (scharfe Kante, feste Einspannung, Punktlast) und dort nicht auswerten.

**Warum mindestens drei Netze?** Zwei Netze reichen nicht: Ein großer Sprung kann auch von einem zu groben ersten Netz kommen, und ein kleiner Unterschied kann täuschen. Erst das dritte Netz zeigt, ob die Änderung kleiner wird.

So sah das beim L-Profil aus (mit Inflation, global 3&nbsp;mm):

| lokale Elementgröße | Spannung σ<sub>vM</sub> | Änderung zur vorigen Netzgröße |
| ------------------:| -----------------------:| ------------------------------:|
| 1&nbsp;mm          | 624,82&nbsp;MPa          |                                |
| 0,5&nbsp;mm        | 601,92&nbsp;MPa          | −3,7&nbsp;%                    |
| 0,25&nbsp;mm       | 597,67&nbsp;MPa          | <span style="color:green;">−0,7&nbsp;%</span> |

Die Änderung wird kleiner und liegt beim letzten Halbieren unter 1&nbsp;%: Das Netz mit 0,25&nbsp;mm ist konvergiert.

Wie Sie das Netz in Verrundungen und Kerben einstellen (Elementgröße, Inflation), steht auf der Seite [Netzeinstellungen](Netzeinstellungen.md).
