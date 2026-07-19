// Scrollytelling-Hero der Startseite: ein Balken wird beim Scrollen
// modelliert, vernetzt, gelagert/belastet und gelöst (Biegelinie + "Spannungen").
// Läuft nur, wenn #fem-scrolly auf der Seite existiert. Kein Framework.
(function () {
  'use strict';

  function init() {
    var scrolly = document.getElementById('fem-scrolly');
    if (!scrolly) return;
    var svg = document.getElementById('fem-svg');
    var captionEl = document.getElementById('fem-caption');
    if (!svg || !captionEl) return;

    var NS = 'http://www.w3.org/2000/svg';
    // Geometrie des Balkens im viewBox-Koordinatensystem (800x320)
    var X0 = 100, Y0 = 115, L = 600, H = 70;
    var NX = 24, NY = 4;
    var WMAX = 46; // max. Durchbiegung in px

    var phases = [
      { until: 0.22, title: '1 · Geometrie', text: 'Das Bauteil wird als CAD-Geometrie beschrieben: ein Balken auf zwei Lagern.' },
      { until: 0.48, title: '2 · Vernetzung', text: 'Die Geometrie wird in finite Elemente zerlegt — aus einem Kontinuum werden viele einfache Teilprobleme.' },
      { until: 0.62, title: '3 · Randbedingungen', text: 'Lager fixieren das Modell, die Streckenlast bringt die Belastung auf.' },
      { until: 0.88, title: '4 · Lösung', text: 'Der Solver löst das Gleichungssystem: Verformung und Spannungen in jedem Element.' },
      { until: 1.01, title: 'Bereit?', text: 'Genau das lernst du in den Praktika — Schritt für Schritt in ANSYS.' }
    ];

    // --- SVG aufbauen ------------------------------------------------------
    function el(name, attrs, parent) {
      var e = document.createElementNS(NS, name);
      for (var k in attrs) e.setAttribute(k, attrs[k]);
      (parent || svg).appendChild(e);
      return e;
    }

    svg.setAttribute('viewBox', '0 0 800 320');

    // Umriss (Phase 1) — als Pfad mit Strichanimation
    var outline = el('path', {
      d: 'M ' + X0 + ' ' + Y0 + ' h ' + L + ' v ' + H + ' h ' + (-L) + ' Z',
      fill: 'none', 'stroke-width': 2.5, 'class': 'fem-outline'
    });
    var outlineLen = outline.getTotalLength();
    outline.style.strokeDasharray = outlineLen;

    // Netz (Phase 2): Elemente als Polygone, Knotenpositionen werden je Frame gesetzt
    var meshG = el('g', { 'class': 'fem-mesh' });
    var elems = [];
    for (var j = 0; j < NY; j++) {
      for (var i = 0; i < NX; i++) {
        elems.push({ i: i, j: j, poly: el('polygon', { 'class': 'fem-elem' }, meshG) });
      }
    }
    // Reihenfolge des Erscheinens: von links nach rechts, leicht versetzt je Zeile
    elems.forEach(function (q) { q.order = (q.i + q.j * 0.6) / (NX + NY * 0.6); });

    // Randbedingungen (Phase 3)
    var bcG = el('g', { 'class': 'fem-bc' });
    function support(x, y, roller) {
      var g = el('g', {}, bcG);
      el('polygon', { points: (x - 16) + ',' + (y + 26) + ' ' + (x + 16) + ',' + (y + 26) + ' ' + x + ',' + y, 'class': 'fem-support' }, g);
      if (roller) {
        el('circle', { cx: x - 9, cy: y + 31, r: 4, 'class': 'fem-support' }, g);
        el('circle', { cx: x + 9, cy: y + 31, r: 4, 'class': 'fem-support' }, g);
      } else {
        el('line', { x1: x - 20, y1: y + 34, x2: x + 20, y2: y + 34, 'class': 'fem-ground' }, g);
      }
      return g;
    }
    support(X0, Y0 + H, false);
    support(X0 + L, Y0 + H, true);
    var arrows = [];
    for (var a = 0; a <= 12; a++) {
      var ax = X0 + (L / 12) * a;
      var g2 = el('g', { 'class': 'fem-arrow' }, bcG);
      el('line', { x1: ax, y1: Y0 - 46, x2: ax, y2: Y0 - 10 }, g2);
      el('polygon', { points: ax + ',' + (Y0 - 4) + ' ' + (ax - 5) + ',' + (Y0 - 14) + ' ' + (ax + 5) + ',' + (Y0 - 14) }, g2);
      arrows.push(g2);
    }
    var loadLine = el('line', { x1: X0, y1: Y0 - 46, x2: X0 + L, y2: Y0 - 46, 'class': 'fem-loadline' }, bcG);

    // --- Physik/Farben -----------------------------------------------------
    function deflect(s) { // normierte Biegelinie, Gleichlast, gelenkig gelagert
      return (s * (1 - 2 * s * s + s * s * s)) / 0.3125;
    }
    function nodePos(i, j, bend) {
      var s = i / NX;
      var x = X0 + s * L;
      var y = Y0 + (j / NY) * H + WMAX * bend * deflect(s);
      return x + ',' + y;
    }
    function stressColor(i, j, amount) {
      var s = (i + 0.5) / NX;
      var yRel = Math.abs((j + 0.5) / NY - 0.5) * 2;   // Abstand von der neutralen Faser
      var v = Math.min(1, yRel * 4 * s * (1 - s) * 1.35) * amount;
      var hue = 225 - 225 * v;                          // blau -> rot
      return 'hsl(' + hue + ', 80%, ' + (60 - 12 * v) + '%)';
    }

    // --- Render pro Scroll-Fortschritt t in [0,1] --------------------------
    var currentPhase = -1;
    function render(t) {
      var p = 0;
      while (phases[p].until < t) p++;
      if (p !== currentPhase) {
        currentPhase = p;
        captionEl.innerHTML = '<strong>' + phases[p].title + '</strong><span>' + phases[p].text + '</span>';
        scrolly.setAttribute('data-phase', p);
      }
      var geomT = Math.min(1, t / 0.18);
      var meshT = Math.max(0, Math.min(1, (t - 0.22) / 0.24));
      var bcT = Math.max(0, Math.min(1, (t - 0.48) / 0.12));
      var solveT = Math.max(0, Math.min(1, (t - 0.62) / 0.22));
      var ease = solveT * solveT * (3 - 2 * solveT);

      outline.style.strokeDashoffset = outlineLen * (1 - geomT);
      outline.style.opacity = meshT >= 1 ? 0.25 : 1;

      elems.forEach(function (q) {
        var visible = meshT > 0 && q.order <= meshT;
        q.poly.style.opacity = visible ? 1 : 0;
        if (!visible) return;
        q.poly.setAttribute('points',
          nodePos(q.i, q.j, ease) + ' ' + nodePos(q.i + 1, q.j, ease) + ' ' +
          nodePos(q.i + 1, q.j + 1, ease) + ' ' + nodePos(q.i, q.j + 1, ease));
        q.poly.style.fill = ease > 0 ? stressColor(q.i, q.j, ease) : 'var(--fem-elem-fill)';
      });

      bcG.style.opacity = bcT;
      arrows.forEach(function (g, idx) {
        g.style.opacity = bcT > idx / arrows.length ? 1 : 0;
      });
      loadLine.style.opacity = bcT;
    }

    window.__femRender = render; // für Tests/Debugging von außen aufrufbar

    // --- Scroll-Kopplung ---------------------------------------------------
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced) { render(0.999); return; }

    // Höhen in px setzen statt sich auf CSS-vh zu verlassen (robust gegen
    // Viewport-Eigenheiten mobiler Browser / eingebetteter Webviews)
    function viewportH() {
      return window.innerHeight || document.documentElement.clientHeight ||
        (window.visualViewport && window.visualViewport.height) || 720;
    }
    var sticky = scrolly.querySelector('.fem-sticky');
    function layout() {
      var vh = viewportH();
      scrolly.style.height = Math.round(vh * 4.2) + 'px';
      if (sticky) sticky.style.height = Math.round(vh - 56) + 'px';
    }
    layout();

    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        ticking = false;
        var r = scrolly.getBoundingClientRect();
        var vh = window.innerHeight || document.documentElement.clientHeight;
        var total = r.height - vh;
        if (total <= 0) { render(1); return; }
        var t = Math.max(0, Math.min(1, -r.top / total));
        render(t);
      });
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () { layout(); onScroll(); });
    onScroll();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
