// "Mein Spickzettel": Bausteine aus dem Kurs (assets/spickzettel.json, scripts/spickzettel_hook.py) auswählen,
// eigene Notizen ergänzen, Füllstand für ein Blatt A4 vorne und hinten, Druck über ein unsichtbares iframe.
// Stand im localStorage ("spickzettel"), nach OPAL-Login zusätzlich auf dem Server (/api/spickzettel):
// der neuere Stand gewinnt. backend-sync.js meldet mit "kurs:angemeldet", wenn der Besitzer geprüft ist.
(function () {
  'use strict';

  var KEY = 'spickzettel';
  var s = document.currentScript || document.querySelector('script[src*="spickzettel.js"]');
  var BASE = new URL((s && s.getAttribute('src')) || '.', document.baseURI).href.replace(/assets\/js\/spickzettel\.js.*$/, '');
  var BACKEND = (window.AC_BACKEND_URL || '').replace(/\/$/, '');
  var PRAKTIKA = [
    ['P1', 'Praktikum 1 · Einführung'], ['P2', 'Praktikum 2 · Geometrie und Randbedingungen'],
    ['P3', 'Praktikum 3 · Vernetzung'], ['P4', 'Praktikum 4 · Abstraktionen']
  ];
  // Blatt: A4 mit 10 mm Rand, zwei Spalten mit 5 mm Abstand, vorne und hinten
  var MM = 96 / 25.4, SPALTE = 92.5, HOEHE = 277, SPALTEN = 4;
  var DRUCK_CSS =
    '@page{size:A4;margin:10mm}' +
    'body{margin:0;font:8pt/1.25 "Source Sans Pro","Source Sans 3",Arial,sans-serif;color:#000}' +
    '.blatt{column-count:2;column-gap:5mm;column-fill:auto}' +
    'h2{font-size:9pt;margin:0 0 1mm;break-after:avoid}' +
    'section{margin:0 0 2.5mm}' +
    'p,ul{margin:0 0 1mm}ul{padding-left:3.5mm}li{margin:0}' +
    'code{font:inherit;font-weight:600}' +
    '.notiz{white-space:pre-wrap}';

  var stand = laden(), daten = null, token = null, angemeldet = false, sendeTimer = null, messFrame = null;

  function laden() {
    try { return JSON.parse(localStorage.getItem(KEY)) || leer(); } catch (e) { return leer(); }
  }
  function leer() { return { stand: 0, kern: {}, check: {}, notizen: {} }; }
  function esc(t) { return String(t).replace(/[&<>"']/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }); }

  function speichern() {
    stand.stand = Date.now();
    try { localStorage.setItem(KEY, JSON.stringify(stand)); } catch (e) { }
    blattZeigen();
    if (angemeldet) {
      clearTimeout(sendeTimer);
      sendeTimer = setTimeout(senden, 1500);
    }
  }

  // ---- Bausteine ----------------------------------------------------------------------------------------
  var WAHL = [['', 'Nicht übernehmen'], ['kurz', 'Kurz'], ['lang', 'Ausführlich']];

  function kernZeile(k) {
    var w = stand.kern[k.id] || '';
    return '<li class="sz-kern">' +
      '<span class="sz-kern-text"><strong>' + esc(k.kurz) + '</strong>' +
      (k.lang ? '<span class="sz-kern-lang">' + esc(k.lang) + '</span>' : '') +
      ' <a href="' + BASE + k.url + '" class="sz-quelle">Zur Stelle</a></span>' +
      '<span class="sz-wahl" role="group" aria-label="' + esc(k.kurz) + '">' +
      WAHL.map(function (o) {
        return '<button type="button" data-kern="' + k.id + '" data-wert="' + o[0] + '"' +
          (o[0] === w ? ' class="sz-an" aria-pressed="true"' : ' aria-pressed="false"') + '>' +
          (o[0] ? o[1] : '–') + '</button>';
      }).join('') + '</span></li>';
  }

  function notizFeld(id, titel) {
    return '<label class="sz-notiz"><span>' + titel + '</span>' +
      '<textarea data-notiz="' + id + '" rows="3" placeholder="In eigenen Worten: was Sie sich merken wollen">' +
      esc(stand.notizen[id] || '') + '</textarea></label>';
  }

  function bausteine() {
    var html = PRAKTIKA.map(function (p) {
      var kern = daten.kernaussagen.filter(function (k) { return k.praktikum === p[0]; });
      return '<section class="sz-gruppe"><h2>' + p[1] + '</h2>' +
        (kern.length ? '<ul class="sz-kerne">' + kern.map(kernZeile).join('') + '</ul>'
          : '<p class="sz-hinweis">Für dieses Praktikum gibt es noch keine Kernaussagen.</p>') +
        notizFeld(p[0], 'Eigene Notizen') + '</section>';
    }).join('');
    html += '<section class="sz-gruppe"><h2>Fehlersuche</h2>' +
      '<p class="sz-hinweis">Punkte aus der <a href="' + BASE + '00_FAQ/Fehler_checkliste/">Fehler-Checkliste</a>, ' +
      'die auf Ihren Zettel sollen.</p><ul class="sz-checks">' +
      daten.checkliste.map(function (c) {
        return '<li><label><input type="checkbox" data-check="' + c.id + '"' + (stand.check[c.id] ? ' checked' : '') +
          '> <span>' + c.html + '</span></label></li>';
      }).join('') + '</ul></section>' +
      '<section class="sz-gruppe"><h2>Weitere Notizen</h2>' + notizFeld('weitere', 'Was sonst noch auf den Zettel soll') + '</section>';
    return html;
  }

  // ---- Blatt (Vorschau, Füllstand, Druck) ----------------------------------------------------------------
  function blattHtml() {
    var teile = [];
    PRAKTIKA.forEach(function (p) {
      var zeilen = daten.kernaussagen.filter(function (k) { return k.praktikum === p[0] && stand.kern[k.id]; })
        .map(function (k) {
          return '<li><strong>' + esc(k.kurz) + '</strong>' + (stand.kern[k.id] === 'lang' && k.lang ? ': ' + esc(k.lang) : '') + '</li>';
        });
      var notiz = (stand.notizen[p[0]] || '').trim();
      if (zeilen.length || notiz) {
        teile.push('<section><h2>' + p[1] + '</h2>' + (zeilen.length ? '<ul>' + zeilen.join('') + '</ul>' : '') +
          (notiz ? '<p class="notiz">' + esc(notiz) + '</p>' : '') + '</section>');
      }
    });
    var checks = daten.checkliste.filter(function (c) { return stand.check[c.id]; });
    if (checks.length) {
      teile.push('<section><h2>Fehlersuche</h2><ul>' + checks.map(function (c) { return '<li>' + c.html + '</li>'; }).join('') + '</ul></section>');
    }
    var weitere = (stand.notizen.weitere || '').trim();
    if (weitere) teile.push('<section><h2>Weitere Notizen</h2><p class="notiz">' + esc(weitere) + '</p></section>');
    return teile.join('');
  }

  function dokument(inhalt, mess) {
    return '<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Spickzettel</title><style>' + DRUCK_CSS +
      (mess ? '.blatt{column-count:1;width:' + SPALTE + 'mm}' : '') + '</style></head><body><div class="blatt">' +
      inhalt + '</div></body></html>';
  }

  // Höhe in einer Spalte messen (gleiche Schrift wie im Druck), Anteil an 2 Seiten × 2 Spalten
  function fuellstand(inhalt, fertig) {
    if (!messFrame) {
      messFrame = document.createElement('iframe');
      messFrame.setAttribute('aria-hidden', 'true');
      messFrame.tabIndex = -1;
      messFrame.style.cssText = 'position:absolute;left:-9999px;top:0;width:' + (SPALTE + 2) + 'mm;height:10px;border:0;visibility:hidden';
      document.body.appendChild(messFrame);
    }
    var d = messFrame.contentDocument;
    d.open(); d.write(dokument(inhalt, true)); d.close();
    var hoehe = d.querySelector('.blatt').scrollHeight;
    fertig(hoehe / (SPALTEN * HOEHE * MM));
  }

  function blattZeigen() {
    var inhalt = blattHtml();
    var blatt = document.getElementById('sz-blatt');
    blatt.innerHTML = inhalt || '<p class="sz-hinweis">Noch leer: Wählen Sie oben Kernaussagen und Punkte aus oder schreiben Sie eigene Notizen.</p>';
    fuellstand(inhalt, function (anteil) {
      var pct = Math.round(anteil * 100);
      var bar = document.getElementById('sz-balken');
      bar.style.width = Math.min(pct, 100) + '%';
      bar.parentNode.classList.toggle('sz-voll', pct > 100);
      document.getElementById('sz-pct').textContent = pct > 100
        ? pct + ' %: Das passt nicht mehr auf ein Blatt, bitte kürzen.'
        : pct + ' % des Blatts (A4 vorne und hinten)' + (pct > 50 ? ', die Rückseite ist angefangen' : '');
    });
  }

  function drucken() {
    var f = document.createElement('iframe');
    f.setAttribute('aria-hidden', 'true');
    f.style.cssText = 'position:fixed;right:0;bottom:0;width:0;height:0;border:0';
    document.body.appendChild(f);
    var d = f.contentDocument;
    d.open(); d.write(dokument(blattHtml(), false)); d.close();
    setTimeout(function () {
      f.contentWindow.focus();
      f.contentWindow.print();
      setTimeout(function () { f.remove(); }, 1000);
    }, 100);
  }

  // ---- Server ---------------------------------------------------------------------------------------------
  function senden() {
    fetch(BACKEND + '/api/spickzettel', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token },
      body: JSON.stringify({ daten: stand })
    }).catch(function () { });
  }

  function abgleichen() {
    fetch(BACKEND + '/api/spickzettel', { headers: { 'Authorization': 'Bearer ' + token } })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (srv) {
        if (!srv) return;
        angemeldet = true;
        var server = srv.daten;
        if (server && (server.stand || 0) > (stand.stand || 0)) {
          stand = { stand: server.stand, kern: server.kern || {}, check: server.check || {}, notizen: server.notizen || {} };
          try { localStorage.setItem(KEY, JSON.stringify(stand)); } catch (e) { }
          aufbauen();
        } else if ((stand.stand || 0) > ((server && server.stand) || 0)) {
          senden();
        }
      })
      .catch(function () { });
  }

  // ---- Seite -------------------------------------------------------------------------------------------
  function aufbauen() {
    var box = document.getElementById('spickzettel');
    box.innerHTML = bausteine() +
      '<section class="sz-gruppe sz-ergebnis"><h2>Mein Blatt</h2>' +
      '<div class="sz-fuell"><div class="sz-fuell-leiste"><div id="sz-balken"></div></div><span id="sz-pct"></span></div>' +
      '<p><button type="button" class="md-button md-button--primary" id="sz-drucken">Drucken</button> ' +
      '<span class="sz-hinweis">Ein Blatt A4, zwei Spalten. Wer von Hand schreibt, nimmt die Vorschau unten als Vorlage.</span></p>' +
      '<div id="sz-blatt" class="sz-blatt"></div></section>';
    blattZeigen();
  }

  function init() {
    var box = document.getElementById('spickzettel');
    if (!box) return;
    try { token = localStorage.getItem('ac_backend_token'); } catch (e) { }
    fetch(BASE + 'assets/spickzettel.json')
      .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
      .then(function (d) {
        daten = d;
        aufbauen();
        if (BACKEND && token) {
          if (window.AC_ANGEMELDET) abgleichen();
          else document.addEventListener('kurs:angemeldet', abgleichen);
        }
      })
      .catch(function () { box.innerHTML = '<p class="sz-laden">Spickzettel konnte nicht geladen werden.</p>'; });

    box.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-kern]');
      if (b) {
        if (b.dataset.wert) stand.kern[b.dataset.kern] = b.dataset.wert; else delete stand.kern[b.dataset.kern];
        b.parentNode.querySelectorAll('button').forEach(function (x) {
          var an = x === b;
          x.classList.toggle('sz-an', an);
          x.setAttribute('aria-pressed', an ? 'true' : 'false');
        });
        speichern();
      } else if (e.target.id === 'sz-drucken') {
        drucken();
      }
    });
    box.addEventListener('change', function (e) {
      var id = e.target.dataset && e.target.dataset.check;
      if (!id) return;
      if (e.target.checked) stand.check[id] = true; else delete stand.check[id];
      speichern();
    });
    var tippTimer = null;
    box.addEventListener('input', function (e) {
      var id = e.target.dataset && e.target.dataset.notiz;
      if (!id) return;
      stand.notizen[id] = e.target.value;
      clearTimeout(tippTimer);
      tippTimer = setTimeout(speichern, 400);
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
