---
icon: material/screw-lag
hide:
  - toc
sektion: Schrauben
title: Schrauben berechnen
order: 110
kurz: Vorspannkraft, Verspannungsschaubild und vier Arten, eine Schraube zu modellieren
thumb: images/Modellklassen.excalidraw.png
---

# :material-screw-lag: Schrauben berechnen

Eine Schraube wird beim Anziehen gedehnt und presst die Bauteile zusammen. Diese Vorspannkraft entscheidet darüber, wie die Verbindung auf eine Last im Betrieb reagiert. Zwei Dinge sind bei Schrauben anders als bei den bisherigen Bauteilen:

- Nachgewiesen wird eine Schraube mit Kräften und Nennspannungen nach der Richtlinie VDI 2230, nicht mit der Spannung aus dem Farbbild. Die FE-Rechnung liefert dafür die Kräfte.
- Vorspannen und Belasten sind zwei Schritte nacheinander. Die Reihenfolge zählt.

## Warum die Schraube so wenig abbekommt

<figure style="text-align:center;">
  <img src="../images/Verspannungsschaubild.excalidraw.png" alt="Verspannungsschaubild einer Schraube M10: Vorspannkraft 29,6 kN, von 10 kN Betriebskraft gehen 1,7 kN in die Schraube, 8,3 kN entlasten die Platten" width="800">
  <figcaption>Verspannungsschaubild für eine Schraube M10 mit zwei Stahlplatten von je 15 mm</figcaption>
</figure>

- Die Schraube ist eine weiche Zugfeder, die verspannten Platten sind eine steife Druckfeder.
- Eine Betriebskraft, die die Platten auseinanderzieht, teilt sich auf beide Federn auf. Der größere Teil entlastet die steifen Platten, nur der kleinere Teil kommt in der Schraube an.

$$
\Phi = n \cdot \frac{\delta_P}{\delta_S+\delta_P} \qquad F_{SA} = \Phi \cdot F_A \qquad F_{KR} = F_V - (1-\Phi) \cdot F_A
$$

- $\Phi$: Kraftverhältnis, ohne Einheit
- $n$: Krafteinleitungsfaktor zwischen 0 und 1. Bei 1 greift die Betriebskraft direkt unter Kopf und Mutter an.
- $\delta_S$: Nachgiebigkeit der Schraube in mm/N
- $\delta_P$: Nachgiebigkeit der verspannten Platten in mm/N
- $F_A$: Betriebskraft in Richtung der Schraubenachse in N
- $F_{SA}$: Zusatzkraft in der Schraube in N
- $F_V$: Vorspannkraft in N
- $F_{KR}$: Restklemmkraft in der Trennfuge in N

Zahlen im Bild:

- Vorspannkraft $F_V$ = 29,6 kN, Betriebskraft $F_A$ = 10 kN
- Kraftverhältnis $\Phi$ = 0,17 bei $n$ = 1
- Zusatzkraft in der Schraube $F_{SA}$ = 1,7 kN
- Restklemmkraft $F_{KR}$ = 21,3 kN

Wenn die Restklemmkraft null wird, dann klafft die Fuge, und die Schraube trägt die ganze Betriebskraft allein.

## Wie groß ist die Vorspannkraft?

Die Vorspannkraft steht in Tabellen der Schraubenhersteller, zusammen mit dem Anziehdrehmoment. Für die Festigkeitsklasse 8.8 und eine Reibungszahl von 0,12 in Gewinde und Kopfauflage:

| Schraube | Spannungsquerschnitt | Vorspannkraft | Anziehdrehmoment |
|---|---|---|---|
| M8 | 36,6 mm² | 18,6 kN | 24,6 Nm |
| M10 | 58,0 mm² | 29,6 kN | 48 Nm |

## Vier Arten, eine Schraube zu modellieren

<figure style="text-align:center;">
  <img src="../images/Modellklassen.excalidraw.png" alt="Vier Modellklassen: ohne Schraube mit Verbund, Schraube als Balken, Schraube als Volumenkörper ohne Gewinde, Schraube mit Gewinde" width="900">
  <figcaption>Die vier Modellklassen der VDI 2230 Blatt 2</figcaption>
</figure>

| Klasse | Im Modell | Die FE-Rechnung liefert |
|---|---|---|
| I | keine Schraube, die Platten sind durchgehend oder mit Verbund verklebt | Kräfte in der Fuge, die die Schraube tragen muss |
| II | Schraube als Balken (`Beam`) | Schraubenkraft und Biegemoment |
| III | Schraube als Volumenkörper ohne Gewinde, Reibung in der Trennfuge und unter dem Kopf | dazu Pressung, Klaffen und Rutschen |
| IV | Gewinde ausmodelliert | Spannungen im Gewinde |

- Wenn nur interessiert, wie sich die Baugruppe als Ganzes verformt, dann reicht Klasse I.
- Wenn die Schraubenkraft gesucht ist, dann Klasse II oder III. Beide können die Vorspannung abbilden.
- Wenn zusätzlich interessiert, ob die Fuge klafft oder rutscht, dann Klasse III.
- Klasse IV ist die Ausnahme: sehr feines Netz, lange Rechenzeit, und für den Nachweis nach der Richtlinie nicht nötig.

Das [geführte Beispiel](Beispiel.md) rechnet eine Schraube der Klasse III.

!!! warning "Spannungsspitzen an der Schraube sind kein Nachweis"
    Unter dem Kopf und am Übergang zum Gewinde zeigt das Farbbild hohe Spannungen, die vom Netz abhängen. Wenn eine Schraube nachgewiesen werden soll, dann mit der Schraubenkraft aus der FE-Rechnung und den Formeln der Richtlinie.
