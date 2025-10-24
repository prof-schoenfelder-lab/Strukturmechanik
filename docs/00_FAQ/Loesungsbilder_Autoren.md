# Lösungsbilder zu Übungen hinzufügen - Anleitung für Autoren

## Schnellstart

Um Lösungsbilder zu einer Übung hinzuzufügen, fügen Sie nach den `numeric-question` Elementen folgenden HTML-Block hinzu:

```markdown
<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

### 🎯 Lösung

Hier sehen Sie die Lösungsschritte für diese Übung:

<figure style="text-align:center;">
  <img src="../images/Loesung_Bild1.png" alt="Beschreibung" width="700">
  <figcaption>Schritt 1: Beschreibung des Bildes</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Loesung_Bild2.png" alt="Beschreibung" width="700">
  <figcaption>Schritt 2: Weitere Beschreibung</figcaption>
</figure>

**Wichtige Punkte:**
- Punkt 1
- Punkt 2

</div>
```

## Funktionsweise

1. **Automatische Anzeige**: Der `<div class="solution-images">` Block ist standardmäßig **unsichtbar**
2. **Trigger**: Sobald der Student **alle** Fragen auf der Seite beantwortet hat (entweder richtig oder alle Versuche aufgebraucht), wird der Block automatisch angezeigt
3. **Animation**: Die Einblendung erfolgt mit einem sanften Fade-in-Effekt
4. **Persistenz**: Bei erneutem Besuch der Seite bleiben die Lösungen sichtbar (falls bereits freigeschaltet)

## Struktur

### Container
```html
<div class="solution-images">
  <!-- Inhalt hier -->
</div>
```

### Überschrift (optional aber empfohlen)
```markdown
### 🎯 Lösung
```

### Bilder mit Beschreibung
```html
<figure style="text-align:center;">
  <img src="../images/Bildname.png" alt="Alt-Text" width="700">
  <figcaption>Beschreibung des Bildes</figcaption>
</figure>
```

### Zusätzliche Hinweise (optional)
```markdown
**Wichtige Punkte:**
- Punkt 1
- Punkt 2

**Häufige Fehler:**
- Fehler 1
- Fehler 2
```

## Best Practices

### 1. Bildauswahl
- ✅ Zeigen Sie **kritische Einstellungen** in ANSYS
- ✅ Zeigen Sie **Ergebnisdarstellungen** mit den erwarteten Werten
- ✅ Zeigen Sie **häufige Fehlerquellen** und deren Vermeidung
- ❌ Vermeiden Sie zu viele Bilder (3-5 sind ideal)

### 2. Bildbeschreibungen
- ✅ Nummerieren Sie die Schritte: "Schritt 1:", "Schritt 2:" etc.
- ✅ Seien Sie präzise: Nennen Sie konkrete Werte und Einstellungen
- ✅ Verwenden Sie die gleiche Terminologie wie in der Aufgabenstellung

### 3. Zusätzliche Hinweise
- ✅ Weisen Sie auf **häufige Fehler** hin
- ✅ Geben Sie **Tipps** zur Fehlersuche
- ✅ Verlinken Sie auf relevante **Tutorials** oder **Dokumentation**

### 4. Bildformate und -größen
- Bevorzugte Formate: PNG (Screenshots), JPG (Fotos)
- Empfohlene Breite: `width="700"` oder `width="800"` für große Detailbilder
- Speicherort: Immer im entsprechenden `images/` Unterordner

## Vollständiges Beispiel

```markdown
## Gesucht

### Die maximale Durchbiegung $u_{\max }$ in mm

<div class="numeric-question" data-answer="7.378" data-tolerance="0.1" data-points="5" data-attempts="5">
</div>

### Die maximale Spannung $\sigma_{\max }$ in MPa

<div class="numeric-question" data-answer="275.03" data-tolerance="0.5" data-points="5" data-attempts="5">
</div>

<!-- Lösungsbilder -->
<div class="solution-images">

### 🎯 Lösung

<figure style="text-align:center;">
  <img src="../images/Uebung_01_Setup.png" alt="Setup" width="700">
  <figcaption>Schritt 1: Korrekte Randbedingungen und Belastung</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung_01_Durchbiegung.png" alt="Durchbiegung" width="700">
  <figcaption>Schritt 2: Total Deformation - u_max = 7.378 mm</figcaption>
</figure>

<figure style="text-align:center;">
  <img src="../images/Uebung_01_Spannung.png" alt="Spannung" width="700">
  <figcaption>Schritt 3: Normal Stress Y - σ_max = 275.03 MPa</figcaption>
</figure>

**Wichtige Punkte:**
- Einheit auf mm umstellen!
- Kraft auf der Kante (nicht Fläche) applizieren
- Spannung in y-Richtung auswerten

**Häufige Fehler:**
- Falsche Kraftrichtung (muss negativ sein)
- Vergessene Einheitenumstellung
- Spannung in falscher Richtung ausgewertet

</div>
```

## CSS-Anpassungen

Die Styles sind in `/docs/assets/styles/answer-checker.css` definiert:

- `.solution-images`: Hauptcontainer (standardmäßig versteckt)
- `.solution-images.solution-shown`: Sichtbarer Zustand
- Dark-Mode Support ist integriert

## Testen

1. Öffnen Sie die Übungsseite im Browser
2. Beantworten Sie alle Fragen (oder erschöpfen Sie alle Versuche)
3. Die Lösungsbilder sollten automatisch erscheinen
4. Bei erneutem Laden bleiben die Bilder sichtbar

## Debugging

Falls die Lösungsbilder nicht erscheinen:

1. Prüfen Sie die Browser-Konsole auf JavaScript-Fehler
2. Stellen Sie sicher, dass alle `numeric-question` Elemente korrekt strukturiert sind
3. Prüfen Sie, ob die CSS-Datei korrekt eingebunden ist
4. Testen Sie mit `localStorage.clear()` in der Konsole, um alle gespeicherten Daten zu löschen

## Support für verschiedene Übungstypen

Das Feature funktioniert mit:
- ✅ Selbsttests (P1_Einfuehrung/03_Selbsttests)
- ✅ Übungen in P2 (P2_Geometrie_Randbedingunge)
- ✅ Allen Seiten mit `numeric-question` Elementen
