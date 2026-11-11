/* =========================================================================
   RENOUVIER PAPERS : comportements du site
   - marqueurs de page [p. N] ;
   - sections pliables (clic sur un titre) et bouton « tout replier » de l'en-tête ;
   - réglages d'affichage (4 thèmes, 4 polices de lecture), mémorisés sur l'appareil ;
   - tiroir mobile ouvert sur les grandes rubriques depuis l'accueil.
   Le thème et la police mémorisés sont appliqués avant le premier affichage par
   overrides/main.html (classes sur <html>) ; ce fichier-ci gère les changements.
   ========================================================================= */
(function () {
  var racine = document.documentElement;

  var THEMES = [
    { v: 'light',    nom: 'Clair',          c: ['#f1edf8', '#e63946', '#0096a8', '#e87800', '#06a870'] },
    { v: 'dark',     nom: 'Sombre',         c: ['#0a0e17', '#ff6b9d', '#00e5a0', '#ffa63d', '#50b0ff'] },
    { v: 'cb-light', nom: 'Daltonien jour', c: ['#f1edf8', '#0072B2', '#E69F00', '#CC79A7', '#009E73'] },
    { v: 'cb-dark',  nom: 'Daltonien nuit', c: ['#0a0e17', '#56B4E9', '#E69F00', '#CC79A7', '#009E73'] }
  ];
  var POLICES = [
    { v: 'default',      nom: 'Libertinus Serif',      note: 'par défaut',  f: "'Libertinus Serif', serif" },
    { v: 'solway',       nom: 'Solway',                note: '',            f: "'Solway', serif" },
    { v: 'hyperlegible', nom: 'Atkinson Hyperlegible', note: 'malvoyance',  f: "'Atkinson Hyperlegible', sans-serif" },
    { v: 'opendyslexic', nom: 'OpenDyslexic',          note: 'dyslexie',    f: "'OpenDyslexic', sans-serif" }
  ];

  function lire(cle, defaut) {
    try { return localStorage.getItem(cle) || defaut; } catch (e) { return defaut; }
  }
  function ecrire(cle, valeur) {
    try { localStorage.setItem(cle, valeur); } catch (e) { /* stockage indisponible : réglage valable pour la page */ }
  }

  /* ---- thème et police (mêmes clés de mémorisation qu'avant) ---- */
  function appliquerTheme(t) {
    racine.classList.remove('theme-dark', 'theme-cb-light', 'theme-cb-dark');
    if (t && t !== 'light') racine.classList.add('theme-' + t);
    var meta = document.querySelector('meta[name="theme-color"]');      // cadre du navigateur mobile
    if (meta) meta.setAttribute('content', (t === 'dark' || t === 'cb-dark') ? '#0f1520' : '#f1edf8');
  }
  function appliquerPolice(f) {
    racine.classList.remove('font-solway', 'font-hyperlegible', 'font-opendyslexic');
    if (f && f !== 'default') racine.classList.add('font-' + f);
  }
  appliquerTheme(lire('themeChoice', 'light'));
  appliquerPolice(lire('fontChoice', 'default'));

  /* ---- marqueurs de page [p. N] ---- */
  function marqueursDePage(zone) {
    if (!zone) return;
    var marcheur = document.createTreeWalker(zone, NodeFilter.SHOW_TEXT, null, false);
    var noeuds = []; while (marcheur.nextNode()) noeuds.push(marcheur.currentNode);
    noeuds.forEach(function (noeud) {
      var parent = noeud.parentNode;
      if (!parent || (parent.classList && parent.classList.contains('page-marker'))) return;
      if (parent.closest && parent.closest('pre, code, script, style')) return;
      if (!/\[p\.\s[^\]]+\]/.test(noeud.textContent)) return;
      var fragment = document.createDocumentFragment();
      noeud.textContent.split(/(\[p\.\s[^\]]+\])/g).forEach(function (part) {
        if (/^\[p\.\s[^\]]+\]$/.test(part)) {
          var s = document.createElement('span'); s.className = 'page-marker'; s.textContent = part; fragment.appendChild(s);
        } else { fragment.appendChild(document.createTextNode(part)); }
      });
      parent.replaceChild(fragment, noeud);
    });
  }

  /* ---- sections pliables ---- */
  function sectionsPliables(zone) {
    if (!zone) return 0;
    var titres = zone.querySelectorAll('h2, h3, h4');
    if (titres.length < 4) return 0;
    titres.forEach(function (h) {
      if (h.dataset.rpPli) return; h.dataset.rpPli = '1';
      h.classList.add('collapsible-heading', 'open');
      var niveau = parseInt(h.tagName.charAt(1), 10);
      var enveloppe = document.createElement('div'); enveloppe.className = 'collapsible-content';
      var frere = h.nextElementSibling;
      while (frere) {
        if (/^H[1-6]$/.test(frere.tagName) && parseInt(frere.tagName.charAt(1), 10) <= niveau) break;
        if (frere.classList.contains('footnote')) break;          // les notes restent visibles
        var suivant = frere.nextElementSibling; enveloppe.appendChild(frere); frere = suivant;
      }
      if (enveloppe.children.length) h.parentNode.insertBefore(enveloppe, h.nextSibling);
      h.addEventListener('click', function (e) {
        if (e.target.closest && e.target.closest('a')) return;    // un lien dans le titre reste un lien
        this.classList.toggle('open');
        var c = this.nextElementSibling;
        if (c && c.classList.contains('collapsible-content')) c.classList.toggle('collapsed');
      });
    });
    return titres.length;
  }

  /* une ancre visée dans une section repliée : on déplie ce qui la contient */
  function deplierVers(cible) {
    var n = cible, ouvert = false;
    while (n && n !== document.body) {
      if (n.classList && n.classList.contains('collapsible-content') && n.classList.contains('collapsed')) {
        n.classList.remove('collapsed');
        var t = n.previousElementSibling;
        if (t && t.classList.contains('collapsible-heading')) t.classList.add('open');
        ouvert = true;
      }
      n = n.parentNode;
    }
    return ouvert;
  }
  function suivreAncre() {
    var id = decodeURIComponent((location.hash || '').slice(1));
    if (!id) return;
    var cible = document.getElementById(id);
    if (cible && deplierVers(cible)) cible.scrollIntoView();
  }

  /* ---- bouton « replier / déplier toutes les sections » de l'en-tête ---- */
  function boutonPlier(nombre) {
    var b = document.getElementById('rp-plier');
    if (!b) return;
    b.hidden = !nombre;
    etatPlier(b, false);
    if (b.dataset.rpPret) return; b.dataset.rpPret = '1';
    b.addEventListener('click', function () {
      var zone = document.querySelector('.md-content');
      if (!zone) return;
      var replier = b.getAttribute('aria-pressed') !== 'true';
      zone.querySelectorAll('.collapsible-content').forEach(function (s) { s.classList.toggle('collapsed', replier); });
      zone.querySelectorAll('.collapsible-heading').forEach(function (h) { h.classList.toggle('open', !replier); });
      etatPlier(b, replier);
      if (replier) window.scrollTo(0, 0);
    });
  }
  function etatPlier(b, replie) {
    var texte = replie ? 'Déplier toutes les sections' : 'Replier toutes les sections';
    b.setAttribute('aria-pressed', replie ? 'true' : 'false');
    b.setAttribute('title', texte); b.setAttribute('aria-label', texte);
  }

  /* ---- réglages ---- */
  function reglages() {
    var bouton = document.getElementById('rp-reglages-bouton');
    if (!bouton || document.getElementById('rp-reglages')) return;
    var fond = document.createElement('div'); fond.id = 'rp-reglages-fond';
    var panneau = document.createElement('div'); panneau.id = 'rp-reglages';
    panneau.setAttribute('role', 'dialog'); panneau.setAttribute('aria-label', "Réglages d'affichage");

    var html = '<fieldset><legend>Apparence</legend><div class="rp-themes">';
    THEMES.forEach(function (t) {
      html += '<label class="rp-choix"><input type="radio" name="rp-theme" value="' + t.v + '">' +
        '<span class="rp-apercu" style="background:' + t.c[0] + '">' +
        '<i style="background:' + t.c[1] + '"></i><i style="background:' + t.c[2] + '"></i>' +
        '<i style="background:' + t.c[3] + '"></i><i style="background:' + t.c[4] + '"></i></span>' +
        '<span>' + t.nom + '</span></label>';
    });
    html += '</div></fieldset><fieldset><legend>Police de lecture</legend><div class="rp-polices">';
    POLICES.forEach(function (p) {
      html += '<label class="rp-choix"><input type="radio" name="rp-police" value="' + p.v + '">' +
        '<span style="font-family:' + p.f + '">' + p.nom + '</span>' +
        (p.note ? '<small>' + p.note + '</small>' : '') + '</label>';
    });
    html += '</div></fieldset>';
    panneau.innerHTML = html;
    document.body.appendChild(fond); document.body.appendChild(panneau);

    function cocher(nom, valeur) {
      var champ = panneau.querySelector('input[name="' + nom + '"][value="' + valeur + '"]') ||
                  panneau.querySelector('input[name="' + nom + '"]');
      if (champ) champ.checked = true;
    }
    cocher('rp-theme', lire('themeChoice', 'light'));
    cocher('rp-police', lire('fontChoice', 'default'));

    function ouvrir(oui) {
      panneau.classList.toggle('ouvert', oui); fond.classList.toggle('ouvert', oui);
      bouton.setAttribute('aria-expanded', oui ? 'true' : 'false');
      if (oui) { var c = panneau.querySelector('input:checked'); if (c) c.focus(); }
    }
    bouton.addEventListener('click', function (e) { e.stopPropagation(); ouvrir(!panneau.classList.contains('ouvert')); });
    fond.addEventListener('click', function () { ouvrir(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panneau.classList.contains('ouvert')) { ouvrir(false); bouton.focus(); }
    });
    panneau.addEventListener('change', function (e) {
      var c = e.target;
      if (c.name === 'rp-theme') { ecrire('themeChoice', c.value); appliquerTheme(c.value); }
      if (c.name === 'rp-police') { ecrire('fontChoice', c.value); appliquerPolice(c.value); }
    });
  }

  /* ---- tiroir mobile : sur l'accueil, ouvrir sur les grandes rubriques ----
     Material « zoome » le tiroir sur la rubrique de la page courante. Sur
     l'accueil (qui vit dans la rubrique « Accueil »), on n'y voyait donc que
     Contribuer et Licence. On remonte d'un cran, mais UNIQUEMENT à l'ouverture
     du tiroir et sur l'accueil : ailleurs, le tiroir garde son rôle (le menu
     de la rubrique où l'on se trouve). */
  function tiroirAccueil() {
    var tiroir = document.getElementById('__drawer');
    if (!tiroir || tiroir.dataset.rpAccueil) return;
    tiroir.dataset.rpAccueil = '1';
    tiroir.addEventListener('change', function () {
      if (!this.checked) return;
      if (!document.querySelector('.rp-portail')) return;           // seulement sur l'accueil
      var nav = document.querySelector('.md-nav--primary');
      if (!nav) return;
      nav.querySelectorAll('.md-nav__toggle').forEach(function (t) { t.checked = false; });
    });
  }

  function init() {
    var contenu = document.querySelector('.md-content');
    reglages();
    marqueursDePage(contenu);
    boutonPlier(sectionsPliables(contenu));
    tiroirAccueil();
    suivreAncre();
  }
  window.addEventListener('hashchange', suivreAncre);

  // navigation instantanée de Material si elle est là, sinon chargement classique
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(function () { init(); });
  } else if (document.readyState !== 'loading') {
    init();
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
