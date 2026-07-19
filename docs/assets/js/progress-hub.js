// "Mein Fortschritt": Fortschrittsringe pro Praktikum + Gesamtpunkte.
// Fragenkatalog kommt vom Backend (/api/questions, ohne Antworten);
// der eigene Stand aus dem localStorage (nach OPAL-Login serverseitig gemerged).
(function () {
  'use strict';

  var PRAKTIKA = [
    { prefix: '/P1_Einfuehrung/', name: 'Praktikum 1 · Einführung', href: 'P1_Einfuehrung/' },
    { prefix: '/P2_Geometrie_Randbedingungen/', name: 'Praktikum 2 · Geometrie & RB', href: 'P2_Geometrie_Randbedingungen/' },
    { prefix: '/P3_Vernetzung/', name: 'Praktikum 3 · Vernetzung', href: 'P3_Vernetzung/' },
    { prefix: '/P4_Abstraktionen/', name: 'Praktikum 4 · Abstraktionen', href: 'P4_Abstraktionen/' }
  ];

  function localBest(qid) {
    try {
      var rec = JSON.parse(localStorage.getItem('answer_best_' + qid));
      return rec && rec.points > 0 ? rec.points : 0;
    } catch (e) { return 0; }
  }

  function ring(pct, solved, total) {
    var r = 44, c = 2 * Math.PI * r;
    var off = c * (1 - pct);
    return '<svg viewBox="0 0 110 110" class="ph-ring">' +
      '<circle cx="55" cy="55" r="' + r + '" class="ph-ring-bg"/>' +
      '<circle cx="55" cy="55" r="' + r + '" class="ph-ring-fg" stroke-dasharray="' + c + '" stroke-dashoffset="' + off + '" transform="rotate(-90 55 55)"/>' +
      '<text x="55" y="52" class="ph-ring-num">' + solved + '/' + total + '</text>' +
      '<text x="55" y="70" class="ph-ring-sub">gelöst</text></svg>';
  }

  function localAttempts(qid) {
    try { return parseInt(localStorage.getItem('answer_attempts_' + qid), 10) || 0; } catch (e) { return 0; }
  }

  function render(hub, catalog) {
    var totalPoints = 0, totalSolved = 0, totalQ = 0;
    var firstTry = 0, comeback = false;
    var perP = {};
    var cards = PRAKTIKA.map(function (p) {
      var total = 0, solved = 0;
      Object.keys(catalog).forEach(function (qid) {
        if (qid.indexOf(p.prefix) === -1) return;
        total++;
        totalQ++;
        var best = localBest(qid);
        if (best > 0) {
          solved++; totalSolved++; totalPoints += best;
          if (best > (catalog[qid].points || 0)) firstTry++;      // Volltreffer-Bonus
          if (localAttempts(qid) >= 4) comeback = true;           // nach >=3 Fehlversuchen gelöst
        }
      });
      perP[p.prefix] = { solved: solved, total: total };
      var pct = total ? solved / total : 0;
      return '<a class="ph-card' + (pct >= 1 ? ' ph-done' : '') + '" href="../' + p.href + '">' +
        ring(pct, solved, total, p) +
        '<span class="ph-name">' + p.name + '</span>' +
        (pct >= 1 ? '<span class="ph-badge">✓ komplett</span>' : '') +
        '</a>';
    });

    function pDone(prefix) { var x = perP[prefix]; return x && x.total > 0 && x.solved >= x.total; }
    var badges = [
      { icon: '🚀', name: 'Erste Schritte', desc: 'Die erste Aufgabe gelöst', got: totalSolved >= 1 },
      { icon: '💪', name: 'Comeback', desc: 'Eine Aufgabe nach drei oder mehr Fehlversuchen doch noch geknackt', got: comeback },
      { icon: '🎯', name: 'Scharfschütze', desc: 'Fünf Aufgaben im ersten Versuch gelöst', got: firstTry >= 5 },
      { icon: '⏫', name: 'Halbzeit', desc: 'Die Hälfte aller Aufgaben gelöst', got: totalQ > 0 && totalSolved >= totalQ / 2 },
      { icon: '📥', name: 'Einführungs-Profi', desc: 'Praktikum 1 komplett gelöst', got: pDone('/P1_Einfuehrung/') },
      { icon: '📐', name: 'Geometrie-Meister', desc: 'Praktikum 2 komplett gelöst', got: pDone('/P2_Geometrie_Randbedingungen/') },
      { icon: '🔍', name: 'Singularitäten-Jäger', desc: 'Praktikum 3 komplett gelöst', got: pDone('/P3_Vernetzung/') },
      { icon: '🧩', name: 'Abstraktions-Künstler', desc: 'Praktikum 4 komplett gelöst', got: pDone('/P4_Abstraktionen/') },
      { icon: '🏆', name: 'FEM-Vollprofi', desc: 'Alle Aufgaben des Kurses gelöst', got: totalQ > 0 && totalSolved >= totalQ }
    ];
    var earned = badges.filter(function (b) { return b.got; }).length;
    var badgeHtml = badges.map(function (b) {
      return '<div class="ph-medal' + (b.got ? ' ph-earned' : '') + '" title="' + b.desc + '">' +
        '<span class="ph-medal-icon">' + b.icon + '</span>' +
        '<span class="ph-medal-name">' + b.name + '</span>' +
        '<span class="ph-medal-desc">' + b.desc + '</span></div>';
    }).join('');

    var levelHtml = '';
    try {
      if (window.acLevelInfo) {
        var li = window.acLevelInfo();
        levelHtml = '<div class="ph-level"><strong>Level ' + li.level + ' · ' + li.name + '</strong>' +
          (li.next !== null
            ? ' — noch ' + (li.next - li.solved) + ' Aufgabe(n) bis Level ' + (li.level + 1)
            : ' — Maximallevel erreicht!') + '</div>';
      }
    } catch (e) { }

    var token = null;
    try { token = localStorage.getItem('ac_backend_token'); } catch (e) { }
    hub.innerHTML =
      '<div class="ph-summary"><strong>' + totalPoints + ' Punkte</strong> · ' +
      totalSolved + ' von ' + totalQ + ' Aufgaben gelöst' +
      (token ? ' · <span class="ph-sync">✓ über OPAL gespeichert</span>'
             : ' · <span class="ph-sync ph-sync-off">nur lokal in diesem Browser</span>') +
      '</div>' + levelHtml +
      '<div class="ph-grid">' + cards.join('') + '</div>' +
      '<h2>Abzeichen <small>(' + earned + '/' + badges.length + ')</small></h2>' +
      '<div class="ph-medals">' + badgeHtml + '</div>';
  }

  function init() {
    var hub = document.getElementById('progress-hub');
    if (!hub) return;
    var BACKEND = (window.AC_BACKEND_URL || '').replace(/\/$/, '');
    if (!BACKEND) {
      hub.innerHTML = '<p class="progress-hub-loading">Fortschrittsdaten sind gerade nicht verfügbar.</p>';
      return;
    }
    fetch(BACKEND + '/api/questions')
      .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
      .then(function (catalog) { render(hub, catalog); })
      .catch(function () {
        hub.innerHTML = '<p class="progress-hub-loading">Fortschrittsdaten nicht erreichbar — dafür ist das HTWK-Netz oder VPN nötig.</p>';
      });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
