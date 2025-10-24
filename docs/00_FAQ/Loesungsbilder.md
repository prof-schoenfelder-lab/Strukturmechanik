# Lösungsbilder nach Aufgabenabschluss

## Übersicht

Bei den numerischen Übungsaufgaben werden automatisch **Lösungsbilder** angezeigt, sobald Sie alle Fragen einer Übung beantwortet haben. Dies geschieht unabhängig davon, ob Sie die Aufgaben korrekt gelöst oder alle Lösungsversuche aufgebraucht haben.

## Wann werden die Lösungsbilder angezeigt?

Die Lösungsbilder erscheinen automatisch, wenn eine der folgenden Bedingungen für **alle** Fragen einer Übung erfüllt ist:

- ✅ Sie haben die richtige Antwort eingegeben (und Punkte erhalten), **ODER**
- 🔴 Sie haben alle verfügbaren Lösungsversuche (standardmäßig 5) aufgebraucht

## Was wird in den Lösungsbildern gezeigt?

Die Lösungsbilder enthalten typischerweise:

1. **Screenshots der korrekten Konfiguration** in ANSYS
2. **Wichtige Einstellungen** und Parameter
3. **Erwartete Ergebnisse** mit den richtigen numerischen Werten
4. **Tipps und Hinweise** zu häufigen Fehlerquellen

## Beispiel

So sieht ein Lösungsbereich aus:

```markdown
<!-- Lösungsbilder - werden automatisch angezeigt, wenn alle Fragen beantwortet sind -->
<div class="solution-images">

### 🎯 Lösung

Hier sehen Sie die wichtigsten Lösungsschritte:

<figure style="text-align:center;">
  <img src="../images/Loesung_Schritt1.png" alt="Beschreibung" width="700">
  <figcaption>Schritt 1: Beschreibung des ersten Schritts</figcaption>
</figure>

**Wichtige Punkte:**
- Punkt 1
- Punkt 2

</div>
```

## Vorteile

- 🎓 **Lernen aus Fehlern**: Auch wenn Sie nicht zur richtigen Lösung gekommen sind, können Sie sehen, wie es richtig gemacht wird
- 🔍 **Selbstständige Fehleranalyse**: Vergleichen Sie Ihre Eingaben mit der Musterlösung
- 📚 **Nachschlagen**: Die Lösungen bleiben sichtbar, wenn Sie die Seite erneut besuchen

## Technische Details

- Die Lösungsbilder sind im HTML-Code bereits vorhanden, aber standardmäßig **ausgeblendet**
- Sobald alle Fragen beantwortet sind, werden sie per JavaScript **eingeblendet**
- Die Anzeige erfolgt mit einem sanften **Fade-in-Effekt**
- Die Entscheidung wird lokal im Browser gespeichert - ein erneuter Besuch der Seite zeigt die Lösungen weiterhin an

## Datenschutz

Alle Daten werden **ausschließlich lokal im Browser** gespeichert (localStorage). Es werden keine Daten an einen Server übertragen.
