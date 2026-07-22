---
title: Styleguide (intern)
hide:
  - navigation
---

# Styleguide — Bausteine des Kurses

Interne Beispielseite: alle Gestaltungs-Bausteine auf einen Blick
(nicht in der Navigation verlinkt).

## Typografie

Überschriften stehen in **Source Serif 4** (Serifen-Display), der
Lauftext in **Inter**. Die erste Zeile nach der H1 wird automatisch
zum Lead-Absatz. *Kursives* und **fettes** Inter für Betonungen im Text.

### Eine H3 sieht so aus

Normaler Absatz zur Kontrolle des Zeilenabstands: Die Wärmestromdichte
wird aus dem Temperaturgradienten berechnet und über die Fläche
integriert — so ergibt sich der gesamte Wärmestrom durch die Wand.

---

## Menüpfad-Chips

Rechtsklick mit Ziel dahinter (Aktion und Ziel getrennt):

`Rechtsklick Geometry → Properties → Analysis Type → 2D`

`Rechtsklick Solution → Insert → Thermal → Temperature`

Doppelklick und Linksklick funktionieren genauso — jede Klick-Art hat
ihr eigenes Maus-Icon (rechte Taste, Doppelklick-Wellen, linke Taste):

`Doppelklick Engineering Data`

`Linksklick Fläche → Reiter Environment → Temperature`

Orte mit Erkennungs-Icon:

`Reiter Environment → Temperature`

`Strukturbaum → Mesh → Detailfenster → Element Size: 1 mm`

`Grafikfenster → Fläche auswählen`

Einzelbegriffe als Chip: `Reiter Home` · `Detailfenster` · `Strukturbaum`

## Aufgaben-Kopfzeile

<div class="task-banner" markdown>
🎯 **Jetzt:** Temperaturen anbringen — **innen 100 °C, außen 20 °C**
</div>

## Boxen

Boxen sind typografisch: Kapitälchen-Label in der didaktischen Farbe,
feine Regel-Linie links, eingerückter Text — keine Farbflächen.

!!! question "Die Aufgabe"
    So sieht die Aufgabenstellung aus — blaues Label an blauer Regel-Linie.

!!! check "Checkpoint: So sollte es aussehen"
    Kontrollpunkt in grün — hier vergleichen Studierende ihren Stand.

!!! warning "Wichtige Änderung für 2D"
    Warnungen in amber: `Rechtsklick Geometry → Properties → Analysis Type → 2D`

!!! info
    Neutrale Zusatzinfo ohne didaktische Farbe.

??? tip "Kurzanleitung: Beispiel mit nummerierten Schritten"
    1. Mit dem **Flächenauswahltool** die Fläche wählen
    2. `Reiter Environment → Temperature` anklicken
    3. Im `Detailfenster` den Wert bei **Magnitude** eintragen
    4. `Rechtsklick Randbedingung → Rename` — sinnvoll benennen

## Buttons

[Primäre Aktion →](#){ .md-button .md-button--primary }
[KLICK-TUTORIAL: Sekundär](#){ .md-button }

## FollowMe-Konvertierung (Beispiel)

Mit `scripts/followme2md.py` aus einem FollowMe-Remote-Export erzeugt
(Schnelltest vom 22.07.2026 — die Schritt-Texte sind die Original-Hinweise
der Aufnahme, hier überall „Click here"):

??? tip "Kurzanleitung: Beispiel aus FollowMe Remote"

    1. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-0.png)

    2. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-1.png)

    3. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-2.png)

    4. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-3.png)

    5. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-4.png)

    6. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-5.png)

    7. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-6.png)

    8. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-7.png)

    9. Click here

        ![](../assets/tutorials/Beispiel_Remote/img/step-8.png)
