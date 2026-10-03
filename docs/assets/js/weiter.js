// Weitermachen, wo man aufgehört hat. Jede Praktikumsseite merkt sich ihren Besuch
// (localStorage, nur in diesem Browser). Die Startseite wertet Besuche und bearbeitete
// Aufgaben aus (nach OPAL-Anmeldung vom Server übernommen, also auf jedem Gerät) und
// macht aus „Mit Praktikum 1 starten“ den passenden Weiter-Knopf; die Praktikumskarten
// zeigen, was abgeschlossen ist und wo es weitergeht.
// Maßgeblich ist das am weitesten begonnene Praktikum (Seite nach der Praktikums-Startseite
// besucht oder Aufgabe bearbeitet). Ist es abgeschlossen (letzte Seite erreicht oder alle
// Aufgaben gelöst bzw. ohne Versuche), geht es mit dem nächsten weiter, sonst auf der
// zuletzt besuchten oder der letzten Seite mit bearbeiteter Aufgabe, je nachdem welche
// in der Navigation weiter hinten liegt.
(function () {
  'use strict';

  var KEY = 'kurs_besucht';          // { Seitenpfad: Zeitpunkt des letzten Besuchs }
  var PRAKT = /\/P(\d+)_[^/]+\//;
  var HAKEN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>';

  function lesen(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
  function seitenpfad(p) { return p.replace(/index\.html$/, '').replace(/([^/])$/, '$1/'); }
  function span(cls, text) { var el = document.createElement('span'); el.className = cls; el.textContent = text; return el; }

  // Jede Praktikumsseite: Besuch merken
  var hier = seitenpfad(location.pathname);
  if (PRAKT.test(hier)) {
    var besucht = lesen(KEY) || {};
    besucht[hier] = Date.now();
    try { localStorage.setItem(KEY, JSON.stringify(besucht)); } catch (e) { }
  }

  // Startseite: Praktikumsseiten in Navigationsreihenfolge (partials/page-nav.html)
  var daten = document.getElementById('kurs-seiten');
  var knopf = document.querySelector('.kurs-hero a.kurs-btn--primary');
  if (!daten || !knopf) return;
  var liste;
  try { liste = JSON.parse(daten.textContent); } catch (e) { return; }
  var start = {}, letzte = {}, nachPfad = {};
  liste.forEach(function (s, i) {
    var pfad = new URL(s[0], location.href).pathname, m = pfad.match(PRAKT);
    if (!m) return;
    var seite = { href: s[0], titel: s[1], nr: +m[1], i: i };
    if (!start[seite.nr]) start[seite.nr] = seite;
    letzte[seite.nr] = seite;
    nachPfad[pfad] = seite;
  });

  // Aufgabe gelöst oder alle Versuche verbraucht (Lösung wird dann angezeigt)
  function erledigt(qid, q) {
    var best = lesen('answer_best_' + qid);
    if (best && best.points > 0) return true;
    try {
      if (localStorage.getItem('answer_done_' + qid) === '1') return true;
      return (parseInt(localStorage.getItem('answer_attempts_' + qid), 10) || 0) >= (q.attempts || 5);
    } catch (e) { return false; }
  }

  function auswerten() {
    var p = {};
    function stand(nr) { return p[nr] || (p[nr] = { begonnen: false, fertig: false, zuletzt: null, t: 0, aufgabe: null, n: 0, offen: 0 }); }

    // Besuche (die Startseite eines Praktikums zählt nicht als Position)
    var besucht = lesen(KEY) || {};
    Object.keys(besucht).forEach(function (pfad) {
      var s = nachPfad[pfad];
      if (!s || s === start[s.nr]) return;
      var x = stand(s.nr);
      x.begonnen = true;
      if (besucht[pfad] > x.t) { x.t = besucht[pfad]; x.zuletzt = s; }
      if (s === letzte[s.nr]) x.fertig = true;
    });

    // Bearbeitete Aufgaben; die Aufgaben-ID beginnt mit dem Pfad ihrer Seite
    for (var k = 0; k < localStorage.length; k++) {
      var m = (localStorage.key(k) || '').match(/^answer_(?:best|attempts|done)_(.+)$/);
      var s = m && nachPfad[seitenpfad(m[1].split(':')[0])];
      if (!s) continue;
      var x = stand(s.nr);
      x.begonnen = true;
      if (!x.aufgabe || s.i > x.aufgabe.i) x.aufgabe = s;
    }

    // Alle Aufgaben eines Praktikums erledigt? (Fragenkatalog vom Backend, siehe answer-checker.js)
    var katalog = (lesen('ac_qcatalog') || {}).data || {};
    Object.keys(katalog).forEach(function (qid) {
      var s = nachPfad[seitenpfad(qid.split(':')[0])];
      if (!s) return;
      var x = stand(s.nr);
      x.n++;
      if (!erledigt(qid, katalog[qid])) x.offen++;
    });
    Object.keys(p).forEach(function (nr) { if (p[nr].n && !p[nr].offen) p[nr].fertig = true; });

    var c = 0;
    Object.keys(p).forEach(function (nr) { if (p[nr].begonnen && +nr > c) c = +nr; });
    if (!c) return;                  // neu im Kurs: Knopf bleibt „Mit Praktikum 1 starten“

    var ziel = 0, text, sub, href;
    if (p[c].fertig && start[c + 1]) {
      var name = document.querySelector('.prakt-row[data-nr="' + (c + 1) + '"] .prakt-title');
      ziel = c + 1; text = 'Weiter mit Praktikum ' + ziel; sub = name ? name.textContent : start[ziel].titel; href = start[ziel].href;
    } else if (p[c].fertig) {
      text = 'Alle Praktika geschafft'; sub = 'Mein Fortschritt'; href = 'Fortschritt/';
      var doppelt = document.querySelector('.kurs-hero a.kurs-btn--in');
      if (doppelt) doppelt.remove();
    } else {
      var seite = p[c].zuletzt, a = p[c].aufgabe;
      if (!seite || (a && a.i > seite.i)) seite = a;
      ziel = c; text = 'Weiter in Praktikum ' + c; sub = seite.titel; href = seite.href;
    }
    // Zweizeilig: oben klein wohin, darunter die Seite (passt neben den OPAL-Knopf)
    knopf.href = href;
    knopf.title = text + ': ' + sub;
    knopf.setAttribute('aria-label', knopf.title);
    knopf.textContent = '';
    knopf.classList.add('kurs-btn--weiter');
    var zeilen = span('kurs-btn-zeilen', '');
    zeilen.appendChild(span('kurs-btn-kicker', text));
    zeilen.appendChild(span('kurs-btn-sub', sub));
    knopf.appendChild(zeilen);
    knopf.insertAdjacentHTML('beforeend', '<span aria-hidden="true">→</span>');

    // Karten: abgeschlossen, hier weiter, begonnen
    document.querySelectorAll('.prakt-row[data-nr]').forEach(function (row) {
      var nr = +row.getAttribute('data-nr'), x = p[nr] || {};
      var alt = row.querySelector('.prakt-status');
      if (alt) alt.remove();
      row.classList.toggle('prakt-row--weiter', nr === ziel);
      var art = nr === ziel ? 'weiter' : x.fertig ? 'fertig' : x.begonnen ? 'begonnen' : '';
      var label = row.querySelector('.prakt-label');
      if (!art || !label) return;
      label.insertAdjacentHTML('beforeend', '<span class="prakt-status prakt-status--' + art + '">' +
        (art === 'fertig' ? HAKEN + 'Abgeschlossen' : art === 'weiter' ? 'Hier weiter' : 'Begonnen') + '</span>');
    });
  }

  auswerten();
  // Der Fragenkatalog kommt beim ersten Besuch erst nach dem Laden (answer-checker.js)
  document.addEventListener('answer-checker:katalog', auswerten);
})();
