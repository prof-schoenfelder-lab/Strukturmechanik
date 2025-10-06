# Lagerung und Lasten

### Aufgabenstellung

{% include "../../../.gitbook/includes/p1-bsp1.md" %}

{% include "../../../.gitbook/includes/p1-bsp1-randbedingungen.md" %}

### Umsetzung

1. Festlager links unten:
   - Ansicht drehen, untere Kante bei y=0 wählen.
   - Rechtsklick > Insert > Fixed Support.
2. Loslager rechts unten:
   - Untere Kante bei y = 1000 mm wählen.
   - Rechtsklick > Insert > Displacement.
   - DOF X=0, Z=0 setzen, Y leer (frei).
3. Linienlast (vereinfachte Flächenlast) oben:
   - Obere Fläche wählen.
   - Rechtsklick > Insert > Pressure; Wert q0 = 1000 N / (Fläche). Alternativ direkt als "Force" auf obere Fläche wenn konsistent mit Aufgabenstellung.

Kontrolle: Unter "Static Structural" alle Randbedingungen sichtbar machen; ikonische Pfeile & Symbole prüfen.

{% hint style="info" %}
Loslager korrekt? Prüfen indem temporär Gesamtkraft lösen – eine Warnung zu starren Körperbewegungen würde auf fehlende Fixierung hinweisen.
{% endhint %}
