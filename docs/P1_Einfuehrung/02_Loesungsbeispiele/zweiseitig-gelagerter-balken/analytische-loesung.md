---
icon: material/calculator-variant
---

# Analytische Lösung

Prüfen wir nun also die Ergebnisse mit Hilfe der analytischen Gleichungen für die bekannten Biegefälle.

Das Flächenträgheitsmoment ergibt sich zu

$$
I=\frac{b\,h^3}{12}=\frac{30\,\mathrm{mm}\,(30\,\mathrm{mm})^3}{12}=67500\,\mathrm{mm}^4
$$

## Durchbiegung

Für den Fall des zweiseitig gelagerten Balkens mit Linienlast können wir die Durchbiegung berechnen nach:

$$
u_{max}=\frac{5\,q\,L^3}{384\,E\,I}=\frac{5\cdot1000\,\mathrm{N}\,(1000\,\mathrm{mm})^3}{384\cdot210000\,\mathrm{MPa}\cdot67500\,\mathrm{mm}^4}=0{,}9185773075\,\mathrm{mm}
$$
!!! success

    Dieser Wert stimmt gut mit dem Wert aus unserer Simulation mit $u_{max,Simulation}=0{,}922\,\mathrm{mm}$ überein. Bei einer Verschiebung von $\approx 1 \mathrm{mm}$ ist eine Abweichung von $1 \mathrm{\mu m}$ akzeptabel, da es ein Tausendstel der Ergebnisgröße ist.

## Maximale Spannung

Die maximale Biegespannung kann folgend berechnet werden:

$$
\sigma_{max}=M_{Max}\frac{\frac{h}{2}}{I}
$$

Mit dem maximalen Biegemoment zu:

$$
M_{Max}=\frac{q\,L}{8}=\frac{1000N\cdot1000\,\mathrm{mm}}{8}=125000\,\mathrm{Nmm}
$$

Kann die maximale Biegespannung berechnet werden:

$$
\sigma_{max}=M_{Max}\frac{\frac{h}{2}}{I}=125000\,\mathrm{mm}\frac{(30\,\mathrm{mm})/2}{67500\,\mathrm{mm}^4}=27{,}78\,\mathrm{MPa}
$$

!!! success

    Auch dieser Wert stimmt gut mit Wert aus unserer Simulation mit $\sigma_{max,Simulation}=27{,}789\,\mathrm{MPa}$ überein.
