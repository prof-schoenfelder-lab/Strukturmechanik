// Startseite: Weiter-Knopf und Stand je Praktikum. Grundlage sind nur die bearbeiteten
// Aufgaben (nach OPAL-Anmeldung vom Server übernommen, also auf jedem Rechner gleich).
// Bearbeitet heißt gelöst oder alle Versuche verbraucht; die Karten zeigen den Anteil je
// Praktikum, bei 100 % ist es abgeschlossen. Der Knopf führt in das am weitesten begonnene
// Praktikum: ist es abgeschlossen, zum nächsten, sonst zur Seite nach der weitesten
// bearbeiteten Übung (oder zu ihr selbst, wenn dort noch etwas offen ist).
(function () {
  'use strict';

  var PRAKT = /\/P(\d+)_[^/]+\//;
  var HAKEN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>';

  function lesen(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
  function span(cls, text) { var el = document.createElement('span'); el.className = cls; el.textContent = text; return el; }

  // Zweizeilig: oben klein wohin, darunter die Seite (passt neben den OPAL-Knopf); neu: im neuen Tab
  function setze(text, sub, href, neu) {
    knopf.href = href;
    knopf.title = text + ': ' + sub;
    knopf.setAttribute('aria-label', knopf.title);
    knopf.target = neu ? '_blank' : ''; knopf.rel = neu ? 'noopener' : '';
    // „Mein Fortschritt“ (angemeldet) nicht doppelt, wenn der Knopf selbst dorthin führt
    var zweiter = document.querySelector('.kurs-hero a.kurs-btn--in');
    if (zweiter) zweiter.style.display = href === 'Fortschritt/' ? 'none' : '';
    knopf.textContent = '';
    knopf.classList.add('kurs-btn--weiter');
    var zeilen = span('kurs-btn-zeilen', '');
    zeilen.appendChild(span('kurs-btn-kicker', text));
    zeilen.appendChild(span('kurs-btn-sub', sub));
    knopf.appendChild(zeilen);
    knopf.insertAdjacentHTML('beforeend', '<span aria-hidden="true">→</span>');
  }

  // Alle Praktika abgeschlossen: Das Backend prüft die gespeicherten Ergebnisse und gibt den Link samt Ticket
  // fürs ganze Spiel Knackpunkt. Erst nach dem Laden, dann steht AC_BACKEND_URL (backend-config.js) fest.
  function knackpunkt() {
    var token = null;
    try { token = localStorage.getItem('ac_backend_token'); } catch (e) { }
    if (!token || !window.fetch) return;
    var holen = function () {
      var base = (window.AC_BACKEND_URL || '').replace(/\/$/, '');
      if (!base) return;
      fetch(base + '/api/kp/freigabe', { headers: { Authorization: 'Bearer ' + token } })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (d) { if (d && d.frei && d.link) setze('Knackpunkt freigeschaltet', 'Jetzt spielen', d.link, true); })
        .catch(function () { });
    };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', holen); else holen();
  }

  // Kollegen-Link (#lehrende=…, aus dem Dashboard) auf jeder Seite merken: Lehrenden-Ticket fürs ganze Spiel,
  // damit sind auch alle Knackpunkt-Runden im Kurs frei (answer-checker.js). Hier zählt nur die Frist,
  // die Signatur prüft das Spiel; abgelaufene Tickets fliegen raus.
  function lehrendenTicket() {
    var t = null, exp = 0;
    try {
      t = localStorage.getItem('kurs_lehrende');
      if (t) exp = JSON.parse(atob(t.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'))).exp;
    } catch (e) { }
    if (t && exp > Date.now() / 1000) return { ticket: t, exp: exp };
    try { localStorage.removeItem('kurs_lehrende'); } catch (e) { }
    return null;
  }
  var linkLehrende = /^#lehrende=([\w-]+\.[\w-]+\.[\w-]+)$/.exec(location.hash);
  if (linkLehrende) {
    try { localStorage.setItem('kurs_lehrende', linkLehrende[1]); } catch (e) { }
    try { history.replaceState(null, '', location.pathname + location.search); } catch (e) { }
  }
  var lehrende = lehrendenTicket();

  // Praktikumsseiten in Navigationsreihenfolge (partials/page-nav.html)
  var daten = document.getElementById('kurs-seiten');
  var knopf = document.querySelector('.kurs-hero a.kurs-btn--primary');
  if (!daten || !knopf) return;

  // Lehrenden-Zugang: in der OPAL-Karte ein Hinweis mit dem ganzen Spiel (Spiel-Adresse aus backend-config.js)
  document.documentElement.classList.toggle('kurs-lehrende', !!lehrende);
  if (lehrende) {
    var bis = document.getElementById('kurs-lehrende-bis'), kpLink = document.getElementById('kurs-kp-lehrende');
    if (bis) bis.textContent = new Date(lehrende.exp * 1000).toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit', year: 'numeric' });
    var spielLink = function () { if (kpLink) kpLink.href = (window.AC_KNACKPUNKT_URL || 'https://fkaule.github.io/Knackpunkt/') + '#ticket=' + lehrende.ticket; };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', spielLink); else spielLink();
  }
  var liste;
  try { liste = JSON.parse(daten.textContent); } catch (e) { return; }
  var seiten = [], start = {}, nachPfad = {};
  liste.forEach(function (s) {
    var pfad = new URL(s[0], location.href).pathname, m = pfad.match(PRAKT);
    if (!m) return;
    var seite = { href: s[0], titel: s[1], nr: +m[1], i: seiten.length };
    if (!start[seite.nr]) start[seite.nr] = seite;
    nachPfad[pfad] = seite;
    seiten.push(seite);
  });
  // Die Aufgaben-ID beginnt mit dem Pfad ihrer Seite
  function seiteVon(qid) { return nachPfad[qid.split(':')[0].replace(/([^/])$/, '$1/')]; }

  function bearbeitet(qid, versuche) {
    var best = lesen('answer_best_' + qid);
    if (best && best.points > 0) return true;
    try {
      if (localStorage.getItem('answer_done_' + qid) === '1') return true;
      return (parseInt(localStorage.getItem('answer_attempts_' + qid), 10) || 0) >= versuche;
    } catch (e) { return false; }
  }

  function auswerten() {
    // Weiteste Seite mit angefangener Aufgabe je Praktikum
    var weiteste = {}, c = 0;
    for (var k = 0; k < localStorage.length; k++) {
      var m = (localStorage.key(k) || '').match(/^answer_(?:best|attempts|done)_(.+)$/);
      var s = m && seiteVon(m[1]);
      if (!s) continue;
      if (!weiteste[s.nr] || s.i > weiteste[s.nr].i) weiteste[s.nr] = s;
      if (s.nr > c) c = s.nr;
    }
    if (!c) return;                  // neu im Kurs: Knopf bleibt „Mit Praktikum 1 starten“

    // Bearbeitet je Praktikum und offene Aufgaben je Seite (Fragenkatalog, answer-checker.js)
    var katalog = (lesen('ac_qcatalog') || {}).data || {};
    var n = {}, fertig = {}, aufSeite = {}, offenAuf = {};
    Object.keys(katalog).forEach(function (qid) {
      var s = seiteVon(qid);
      if (!s) return;
      n[s.nr] = (n[s.nr] || 0) + 1;
      aufSeite[s.i] = (aufSeite[s.i] || 0) + 1;
      if (bearbeitet(qid, katalog[qid].attempts || 5)) fertig[s.nr] = (fertig[s.nr] || 0) + 1;
      else offenAuf[s.i] = (offenAuf[s.i] || 0) + 1;
    });
    function abgeschlossen(nr) { return n[nr] > 0 && fertig[nr] >= n[nr]; }

    var ziel = 0, text, sub, href;
    if (abgeschlossen(c) && start[c + 1]) {
      var name = document.querySelector('.prakt-row[data-nr="' + (c + 1) + '"] .prakt-title');
      ziel = c + 1; text = 'Weiter mit Praktikum ' + ziel; sub = name ? name.textContent : start[ziel].titel; href = start[ziel].href;
    } else if (abgeschlossen(c)) {
      text = 'Alle Praktika geschafft'; sub = 'Mein Fortschritt'; href = 'Fortschritt/';
      knackpunkt();
    } else {
      // Ist auf der weitesten Seite alles bearbeitet, geht es auf der nächsten weiter;
      // liegt dahinter nichts mehr im Praktikum, bei der ersten Seite mit offenen Aufgaben
      var seite = weiteste[c];
      if (aufSeite[seite.i] && !offenAuf[seite.i]) {
        var danach = seiten[seite.i + 1];
        if (danach && danach.nr === c) seite = danach;
        else seiten.some(function (s) { return s.nr === c && offenAuf[s.i] && (seite = s); });
      }
      ziel = c; text = 'Weiter in Praktikum ' + c; sub = seite.titel; href = seite.href;
    }
    setze(text, sub, href);

    // Karten: Anteil bearbeiteter Aufgaben, Haken bei 100 %, Marke für hier weiter
    document.querySelectorAll('.prakt-row[data-nr]').forEach(function (row) {
      var nr = +row.getAttribute('data-nr'), label = row.querySelector('.prakt-label');
      row.querySelectorAll('.prakt-status, .prakt-stand').forEach(function (el) { el.remove(); });
      row.classList.toggle('prakt-row--weiter', nr === ziel);
      row.classList.toggle('prakt-row--fertig', abgeschlossen(nr));
      if (label && nr === ziel) label.insertAdjacentHTML('beforeend', '<span class="prakt-status prakt-status--weiter">Hier weiter</span>');
      else if (label && abgeschlossen(nr)) label.insertAdjacentHTML('beforeend', '<span class="prakt-status prakt-status--fertig">' + HAKEN + 'Abgeschlossen</span>');
      if (!n[nr]) return;
      var f = fertig[nr] || 0, pct = Math.floor(100 * f / n[nr]);
      row.querySelector('.prakt-body').insertAdjacentHTML('beforeend',
        '<span class="prakt-stand" title="' + f + ' von ' + n[nr] + ' Aufgaben bearbeitet (gelöst oder alle Versuche verbraucht)">' +
        '<span class="prakt-stand-text"><span>' + f + ' von ' + n[nr] + ' Aufgaben</span><b>' + pct + ' %</b></span>' +
        '<span class="prakt-stand-bar"><i style="width:' + pct + '%"></i></span></span>');
    });
  }

  auswerten();
  // Der Fragenkatalog kommt beim ersten Besuch erst nach dem Laden (answer-checker.js)
  document.addEventListener('answer-checker:katalog', auswerten);
})();
