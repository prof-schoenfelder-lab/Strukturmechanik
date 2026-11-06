---
hide:
 - toc
---

# Wichtige Netzeinstellungen

Bisher haben wir nur die Elementgröße vorgegeben. Zwei weitere Einstellungen unter `Strukturbaum → Mesh` im `Detailfenster` sollten Sie kennen, weil sie das Netz verändern, auch wenn die Elementgröße gleich bleibt:

- `Defeature Size`: welche kleinen Details im Netz ankommen
- `Transition`: wie schnell die Elemente vom feinen zum groben Bereich wachsen

In den Übungen bleiben beide auf dem Standardwert, die Sollwerte gelten nur dafür.

## Defeaturing: kleine Details weglassen

Beim Vernetzen entfernt ANSYS kleine Details, damit sie das Netz nicht unnötig fein machen. Die Geometrie bleibt dabei unverändert, nur das Netz übergeht das Detail.

<figure style="text-align:center;">
  <img src="../images/Netz_Defeaturing.excalidraw.png" alt="Platte mit kleiner Nut: Ist die Defeature Size kleiner als die Nut, folgt das Netz der Nut. Ist sie größer, fehlt die Nut im Netz." width="800" class="no-lightbox">
</figure>

- Wenn ein Detail nicht größer ist als die `Defeature Size`, fehlt es im Netz.
- Wenn `Detailfenster → Mesh Defeaturing` auf `Yes` steht, ist das aktiv. Das ist der Standard.
- Wenn Sie die `Element Size` ändern, rechnet ANSYS die Standard-`Defeature Size` neu, denn sie hängt an der Elementgröße.
- Wenn eine lokale Netzverfeinerung die Elementgröße verändert, kann ANSYS die `Defeature Size` anpassen und meldet das als Warnung. Das ist kein Fehler.
- Wenn Sie unter `Detailfenster → Defeature Size` einen eigenen Wert eintragen, bleibt er fest, auch wenn sich die Elementgröße ändert.

!!! warning "Netz an der Auswertestelle ansehen"
    Wenn ein Radius im Netz fehlt, ist dort eine scharfe Kante und damit eine Singularität. Schauen Sie sich das Netz deshalb immer dort an, wo Sie die Spannung auswerten.

## Transition: vom feinen zum groben Netz

Nach einer lokalen Netzverfeinerung wachsen die Elemente wieder auf die globale Größe an. Wie schnell das geht, legt `Detailfenster → Transition` fest.

<figure style="text-align:center;">
  <img src="../images/Netz_Transition.excalidraw.png" alt="Elementlagen vom feinen zum groben Bereich: Mit Fast ist die globale Größe nach wenigen Lagen erreicht, mit Slow nach deutlich mehr Lagen." width="800" class="no-lightbox">
</figure>

- `Fast` ist der Standard: Bei Volumenkörpern wird jede Elementlage rund 1,85-mal so lang wie die vorige (`Growth Rate`).
- `Slow`: Die Elemente wachsen langsamer. Das Netz bekommt mehr Elemente und rechnet länger.
- Wenn sich die Spannung direkt neben der lokalen Verfeinerung noch stark ändert, kann der Übergang mit `Fast` zu abrupt sein. Dann helfen `Slow` oder ein größerer verfeinerter Bereich.
- `Transition` wirkt nur, wenn `Detailfenster → Use Adaptive Sizing` auf `Yes` steht. Das ist der Standard.

Mehr dazu in der ANSYS-Hilfe: [Mesh Defeaturing](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/msh_auto_defeat.html) und [Transition](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_msh/msh_Trans.html).
