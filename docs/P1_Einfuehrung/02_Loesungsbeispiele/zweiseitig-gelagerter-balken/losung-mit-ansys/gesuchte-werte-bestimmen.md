---
icon: material/timeline-check-outline
hide:
    - toc
---

# Gesuchte Werte bestimmen

## Aufgabenstellung

--8<-- "P1_Einfuehrung/02_Loesungsbeispiele/zweiseitig-gelagerter-balken/Aufgabenstellung.md:Gesucht"

## Umsetzung

### maximale Verformung

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Maximale Verformung einfügen</p>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Solution</code> > <code>Insert</code> > <code>Deformation</code> > <code>Total</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../../images/Get_umax.png" alt="Aufgabenstellung" width="600" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ergebnis abrufen</p>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Total Deformation</code> > <code>Evaluate All Results</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../../images/Get_umax2.png" alt="Aufgabenstellung" width="430" class="no-lightbox">
    </figure>
  </div>

</div>

Als Ergebnis bekommen wir folgende Grafik mit dem maximalen Verschiebungswert von $u_{max}=0{,}922\,\mathrm{mm}$

<figure style="text-align:center;">
  <img src="../../images/u_max.png" alt="Get umax1" width="700" class="no-lightbox">
</figure>

### Spannung in y-Richtung

Die Spannung ergibt sich ähnlich, nur das wir hier zusätzlich die y-Richtung auswählen müssen.

<div class="steps" markdown="1">

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Normalspannung einfügen</p>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Solution</code> > <code>Insert</code> > <code>Stress</code> > <code>Normal</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../../images/Get_sy1.png" alt="Get sy1" width="650" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">y-Richtung einstellen</p>
    <p>Im Detailfenster bei <code>Orientation</code> auf <code>Y Axis</code> stellen</p>
    <figure style="text-align:center;">
    <img src="../../images/Get_sy2.png" alt="Get sy2" width="300" class="no-lightbox">
    </figure>
  </div>

  <div class="step">
    <p class="step-title" role="heading" aria-level="2">Ergebnis abrufen</p>
    <p>Im Strukturbaum <code>Rechtsklick</code> auf <code>Normal Stress</code> > <code>Evaluate All Results</code> auswählen</p>
    <figure style="text-align:center;">
    <img src="../../images/Get_sy3.png" alt="Get sy3" width="350" class="no-lightbox">
    </figure>
  </div>

</div>

Als Ergebnis bekommen wir folgende Grafik mit dem maximalen Wert der Spannung in y-Richtung von $\sigma_{y,max}=27{,}78\,\mathrm{MPa}$. 

<figure style="text-align:center;">
  <img src="../../images/sy.png" alt="Spannung in y-Richtung" width="700" class="no-lightbox">
</figure>