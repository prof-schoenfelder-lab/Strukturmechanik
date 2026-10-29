---
icon: material/arrow-expand-down
hide:
  - toc
sektion: Belastungen
title: Beschleunigungen
order: 240
thumb: images/Beschleunigungen.excalidraw.png
---

# Beschleunigungen

Beschleunigungen wirken nicht auf eine Fläche, sondern auf das ganze Volumen: Jedes Stück Material erfährt die Kraft $\mathrm{d}F = \mathrm{d}m \cdot a$. ANSYS rechnet diese Massenkräfte selbst aus der Dichte des Materials.

<figure style="text-align:center;">
<svg viewBox="0 0 660 230" width="660" style="max-width:100%;height:auto" role="img" aria-label="Eigengewicht, Beschleunigung und Drehung als Massenkräfte">
  <defs>
    <marker id="bpf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#009EE3"/></marker>
    <marker id="bpg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2E3639"/></marker>
  </defs>
  <g font-family="Source Sans Pro, sans-serif" font-size="14" fill="#2E3639" text-anchor="middle">
    <!-- Eigengewicht -->
    <text x="110" y="22" font-weight="700" fill="#022541">Eigengewicht</text>
    <rect x="50" y="50" width="120" height="70" rx="4" fill="#F2F6F9" stroke="#2E3639"/>
    <g stroke="#009EE3" stroke-width="2" marker-end="url(#bpf)">
      <line x1="75" y1="65" x2="75" y2="100"/><line x1="110" y1="65" x2="110" y2="100"/><line x1="145" y1="65" x2="145" y2="100"/>
    </g>
    <line x1="200" y1="55" x2="200" y2="115" stroke="#2E3639" stroke-width="2" marker-end="url(#bpg)"/>
    <text x="200" y="135">g</text>
    <text x="110" y="160">jedes Stück Material:</text>
    <text x="110" y="180" fill="#009EE3">dF = dm · g</text>
    <text x="110" y="210" font-size="13">Standard Earth Gravity</text>
    <!-- Beschleunigung -->
    <text x="330" y="22" font-weight="700" fill="#022541">Beschleunigung</text>
    <rect x="270" y="50" width="120" height="70" rx="4" fill="#F2F6F9" stroke="#2E3639"/>
    <line x1="400" y1="85" x2="440" y2="85" stroke="#2E3639" stroke-width="2" marker-end="url(#bpg)"/>
    <text x="420" y="75">a</text>
    <g stroke="#009EE3" stroke-width="2" marker-end="url(#bpf)">
      <line x1="345" y1="65" x2="295" y2="65"/><line x1="345" y1="85" x2="295" y2="85"/><line x1="345" y1="105" x2="295" y2="105"/>
    </g>
    <text x="330" y="160">Trägheitskraft gegen a:</text>
    <text x="330" y="180" fill="#009EE3">dF = dm · a</text>
    <text x="330" y="210" font-size="13">Acceleration</text>
    <!-- Drehung -->
    <text x="550" y="22" font-weight="700" fill="#022541">Drehung</text>
    <circle cx="550" cy="85" r="42" fill="#F2F6F9" stroke="#2E3639"/>
    <circle cx="550" cy="85" r="3" fill="#2E3639"/>
    <path d="M 518 52 A 46 46 0 0 1 582 52" fill="none" stroke="#2E3639" stroke-width="2" marker-end="url(#bpg)"/>
    <text x="598" y="50">ω</text>
    <g stroke="#009EE3" stroke-width="2" marker-end="url(#bpf)">
      <line x1="565" y1="85" x2="605" y2="85"/><line x1="535" y1="85" x2="495" y2="85"/><line x1="550" y1="100" x2="550" y2="140"/>
    </g>
    <text x="550" y="160">Fliehkraft nach außen:</text>
    <text x="550" y="180" fill="#009EE3">dF = dm · ω² · r</text>
    <text x="550" y="210" font-size="13">Rotational Velocity</text>
  </g>
</svg>
</figure>

!!! warning "Ohne Dichte keine Massenkräfte"
    Beschleunigungslasten brauchen die Dichte im Material (`Engineering Data` > `Density`). Fehlt sie oder stimmt sie nicht, stimmen auch die Kräfte nicht. Die Masse des Modells steht im Strukturbaum unter `Geometry` > Körper > `Properties` > `Mass`.

## Eigengewicht mit `Standard Earth Gravity`

Im Strukturbaum: `Rechtsklick` auf `Static Structural` > `Insert` > `Standard Earth Gravity`, dann im Detailfenster die Richtung wählen, zum Beispiel `-Y Direction`. ANSYS setzt $g = 9{,}81\,\mathrm{m/s^2}$ an, die Gewichtskraft ist $F = m \cdot g$.

Prüffrage: Spielt das Eigengewicht neben den äußeren Lasten überhaupt eine Rolle? Vergleichen Sie $m \cdot g$ mit den angreifenden Kräften. Ist es deutlich kleiner, ändert es das Ergebnis kaum.

## Beschleunigung mit `Acceleration`

Wird ein Bauteil beschleunigt, etwa beim Anfahren, Bremsen oder in einer Kurve, wirken auf jedes Stück Material Trägheitskräfte $F = m \cdot a$, und zwar **entgegen** der Beschleunigung: Ein Bauteil, das nach oben beschleunigt wird, wird nach unten gedrückt.

Im Strukturbaum: `Rechtsklick` auf `Static Structural` > `Insert` > `Acceleration`, dann Betrag und Richtung im Detailfenster eingeben.

Prüffrage nach der Rechnung: Zeigt die Verformung in die Richtung, in die die Trägheitskräfte wirken? Wenn nicht, ist das Vorzeichen der Beschleunigung vertauscht.

## Drehung mit `Rotational Velocity`

Dreht sich ein Bauteil, zum Beispiel ein Rad, eine Kurbel oder eine Scheibe, zieht die Fliehkraft $F = m \cdot \omega^2 \cdot r$ jedes Stück Material nach außen. Außen ist sie am größten.

Im Strukturbaum: `Rechtsklick` auf `Static Structural` > `Insert` > `Rotational Velocity`, dann die Drehachse und die Drehzahl angeben (in rad/s oder RPM).

## Beschleunigung oder Kraft?

Statt einer Beschleunigung ließe sich auch eine Kraft $F = m \cdot a$ anbringen. Das ist gleichwertig, wenn die Masse an einer Stelle sitzt, etwa ein schweres Bauteil, das als Punktmasse an einer Fläche hängt. Ist die Masse über das Bauteil verteilt, verteilt nur die Beschleunigung die Kraft richtig über das Volumen; eine Kraft auf eine Fläche würde dort eine Spannungsspitze erzeugen, die es in Wirklichkeit nicht gibt.

`Static Structural` rechnet die Beschleunigung als gleichbleibend (quasistatisch). Schwingungen und kurze Stöße bildet das nicht ab; dafür gibt es eigene dynamische Analysen.
