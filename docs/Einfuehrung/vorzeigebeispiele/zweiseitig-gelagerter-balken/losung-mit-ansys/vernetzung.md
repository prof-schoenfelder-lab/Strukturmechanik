# Vernetzung

### Aufgabenstellung

{% include "../../../.gitbook/includes/p1-bsp1-netz.md" %}

### Umsetzung

1. Mechanical öffnen (Doppelklick auf Model).
2. Knoten "Mesh" auswählen.
3. Im Detailfenster "Sizing" über Parameter "Resolution" auf 5 setzen (feineres Netz für Durchbiegung & Spannungen über Querschnitt).
4. Rechtsklick auf Mesh > Generate Mesh.

Erwartung: Mehrere Elemente (≥4) über die Höhe, gleichmäßige Hex-/Tetra-Mischung (Standard ist i.d.R. Tetra).

{% hint style="warning" %}
Zu grobes Netz unterschätzt i.d.R. Spannungsmaxima. Spätere Praktika behandeln systematische Konvergenzstudien.
{% endhint %}
