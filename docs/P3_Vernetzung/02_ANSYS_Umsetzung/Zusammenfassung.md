---
icon: material/lightbulb-on-outline
hide:
  - toc
---

# Zusammenfassung – wichtigste Take-aways

## 1. Netz, Elementtyp und Elementgröße

Das Wichtigste zum Netz:

- Das **Netz** ist die Gesamtheit aller Elemente, mit denen die Geometrie diskretisiert wird.
- Ein Netz wird im Wesentlichen bestimmt durch:
  - den **Elementtyp** (z. B. 3D-Volumenelement, 2D-Flächenelement)
  - die **Elementgröße** (Netzgröße)
- Quadratische Elemente (mit Mittelknoten) sind meist genauer, aber rechenaufwändiger als lineare Elemente.

!!! info "Merke"

    Die **Verschiebungen** werden direkt approximiert und konvergieren
    typischerweise schneller als die **Spannungen**, die aus den Ableitungen
    des Verschiebungsfeldes berechnet werden.

---

## 2. Sensitivitätsanalyse und Konvergenz

Bei der Sensitivitätsanalyse wird das Netz schrittweise verfeinert:

- Netzgröße reduzieren (oft etwa **halbieren**)
- Ergebnisse (z. B. σ<sub>vM</sub>, u<sub>max</sub>) zwischen den Netzen vergleichen

Praktisches Konvergenzkriterium:

- Die relative Änderung der interessierenden Größe zwischen zwei Netzen ist **kleiner als 1 %**  
  → Netz im betrachteten Bereich ausreichend fein.

---

## 3. Singularitäten richtig erkennen

Wenn Spannungen bei Netzverfeinerung **nicht** gegen einen Grenzwert konvergieren, liegt wahrscheinlich eine **Singularität** vor.

Typische Ursachen:

- feste Einspannungen
- Punktlasten (Einzelkräfte)
- unendlich scharfe Kanten (z. B. Innenkanten ohne Radius)

Typische Gegenmaßnahmen:

- Geometrie **realitätsnäher modellieren** (z. B. Kantenverrundung).
- Spannungen **nicht direkt an der Einspannung oder Lastangriffsfläche** bewerten,
  sondern in einem kleinen Abstand davon.
- Gegebenenfalls andere Lagerungen nutzen (z. B. Elastic Support, Remote Displacement),
  aber immer die Verformungsform auf **Plausibilität** prüfen.

---

## 4. Globale vs. lokale Netzverfeinerung

**Globale Netzverfeinerung**

- Netzgröße für das gesamte Bauteil verringern.
- Vorteil: einfach anzuwenden.
- Nachteil: Rechenzeit steigt stark, auch in unkritischen Bereichen.

**Lokale Netzverfeinerung**

- Nur in **kritischen Bereichen** (z. B. Kerben, Verrundungen, Hotspots) verfeinern.
- Vorteil: hohe Genauigkeit bei moderater Rechenzeit.

Typisches Vorgehen:

1. Grobes Startnetz wählen.
2. Kritische Bereiche (Spannungsspitzen) identifizieren.
3. Dort lokal verfeinern, bis sich die Spannungen kaum noch ändern.

---

## 5. Nodal Fraction als zusätzliches Qualitätsmerkmal

Neben der Spannungsänderung zwischen zwei Netzen ist der **Spannungsgradient innerhalb eines Elements** entscheidend.  
Dafür kann in Ansys Mechanical die Anzeigeoption **Nodal Fraction** genutzt werden.

- Nodal Fraction misst, wie stark sich die Knotenspannungen eines Elements unterscheiden.
- Kleine Werte → Spannungsfeld ist lokal „glatt“, Netz fein genug.
- Große Werte → starke Sprünge, eventuell Untervernetzung oder Singularität.

Praktischer Richtwert (für dieses Praktikum):

- **Nodal Fraction < 10 %** im interessierenden Bereich → Netzqualität dort **gut**.

In Kombination mit der Sensitivitätsanalyse bedeutet das:

- Spannungsänderung zwischen zwei Netzen < 1 %
- und Nodal Fraction im Hotspot < 10 %

→ Netz ist für die Spannungsbewertung gut geeignet.

---

## 6. Ergebnisse dokumentieren und vergleichen

Für eine saubere Sensitivitätsanalyse sollten die Ergebnisse immer dokumentiert werden.

Mögliche Vorgehensweisen:

- **Screenshots**
  - Ergebnis (z. B. von-Mises-Spannung) anzeigen
  - Image erzeugen und nach Netzgröße benennen (z. B. „σ<sub>vM</sub> – 0,5 mm“)
- **Solution History / Result Tracking**
  - Ansys speichert automatisch die letzten Läufe
  - z. B. Knotenanzahl, Elementanzahl, Rechenzeit, σ<sub>vM</sub>, u<sub>max</sub> etc.
  - Ergebnisse können als Kurve über den Rechenläufen visualisiert werden

Empfehlung:

- Ergebnisse in einer **Tabelle** oder einem **Diagramm** sammeln:
  - Netzgröße
  - σ<sub>vM</sub>, u<sub>max</sub>
  - Nodal Fraction (im Hotspot)
- So wird die Konvergenz der Ergebnisse schnell sichtbar.

---

!!! info "Kurzfassung"

    - Netzgröße schrittweise verfeinern, bis sich die relevanten Spannungen
      um weniger als etwa 1 % ändern.
    - Spannungen nicht direkt an offensichtlichen Singularitäten bewerten.
    - Globale und lokale Netzverfeinerung sinnvoll kombinieren.
    - Nodal Fraction als zusätzliches Qualitätskriterium nutzen
      (Ziel: < 10 % im kritischen Bereich).
    - Ergebnisse (σ<sub>vM</sub>, u<sub>max</sub>, Netzgröße, Nodal Fraction)
      systematisch dokumentieren (Screenshots, Tabellen, Result Tracking).
