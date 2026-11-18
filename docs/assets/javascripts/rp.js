/* =========================================================================
   RENOUVIER PAPERS : comportements du site
   - marqueurs de page [p. N] ;
   - sections pliables (clic sur un titre) et bouton « tout replier » de l'en-tête ;
   - carte d'une rubrique : groupes repliés à l'arrivée, dépliés d'un clic, retrouvés tels quels au retour ;
   - réglages d'affichage (4 thèmes, 4 polices de lecture), mémorisés sur l'appareil ;
   - tiroir mobile ouvert sur les grandes rubriques depuis l'accueil ; rubriques de l'accueil qui répondent au toucher ;
   - entrées du menu « à venir » (page pas encore créée) : sans lien ;
   - titre visé par un lien : maintenu à sa place pendant la mise en forme de la page.
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
    if (!zone || zone.querySelector('.rp-portail')) return 0;       // l'accueil se lit d'un seul tenant
    var titres = Array.prototype.filter.call(zone.querySelectorAll('h2, h3, h4'), function (h) {
      return !(h.closest && h.closest('.rp-sommaire'));             // la carte d'une rubrique a ses propres groupes
    });
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
    var groupe = cible.closest && cible.closest('.rp-groupe');
    if (groupe && carteCourante && !groupe.classList.contains('is-ouvert')) { carteCourante.ouvrir(groupe); ouvert = true; }
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

  /* ---- la carte d'une rubrique ----
     La page d'une rubrique (Œuvres, Revues, Autres auteurs…) présente ses groupes repliés quand la
     liste est longue : on voit d'abord l'ensemble, un clic sur un groupe déplie ses textes.
     hooks/renouvier.py pose la structure et l'état de départ (classe « is-ouvert ») ; ici : le bouton de
     chaque titre, le bouton « Tout déplier », l'ouverture du groupe visé par un lien ou par la recherche
     dans la page, et la mémoire de ce qui était déplié quand on revient par « page précédente ». */
  var carteCourante = null;
  var retourVers = null;            // adresse rejointe par « page précédente » ou « page suivante »
  var premierAffichage = true;
  window.addEventListener('popstate', function () { retourVers = location.pathname; });

  function session(cle, valeur) {
    try {
      if (valeur === undefined) return JSON.parse(sessionStorage.getItem(cle) || 'null');
      if (valeur === null) sessionStorage.removeItem(cle); else sessionStorage.setItem(cle, JSON.stringify(valeur));
    } catch (e) { /* mémoire indisponible : l'état de départ fera l'affaire */ }
    return null;
  }

  function carte(zone) {
    var sommaire = zone && zone.querySelector('.rp-sommaire');
    var groupes = sommaire ? Array.prototype.slice.call(sommaire.querySelectorAll('.rp-groupe')) : [];
    // de retour sur la page, ou page rechargée : on la retrouve comme on l'a laissée
    var retour = retourVers === location.pathname;
    if (premierAffichage) {
      try {
        var arrivee = performance.getEntriesByType('navigation')[0];
        retour = !!arrivee && (arrivee.type === 'back_forward' || arrivee.type === 'reload');
      } catch (e) { retour = false; }
    }
    premierAffichage = false; retourVers = null;
    if (!groupes.length) return null;
    var cle = 'rp-carte:' + location.pathname;
    var memo = retour ? session(cle) : null;
    if (!Array.isArray(memo)) memo = null;
    if (!retour) session(cle, null);
    var tout = null;

    function titreDe(g) { return g.querySelector('.rp-groupe__titre'); }
    function estOuvert(g) { return g.classList.contains('is-ouvert'); }
    function poser(g, ouvert) {
      var b = g.querySelector('.rp-groupe__bouton'), corps = g.querySelector('.rp-groupe__corps');
      g.classList.toggle('is-ouvert', ouvert);
      if (b) b.setAttribute('aria-expanded', ouvert ? 'true' : 'false');
      // « until-found » : replié, le texte reste trouvable par la recherche du navigateur, qui déplie alors le groupe
      if (corps) { if (ouvert) corps.removeAttribute('hidden'); else corps.setAttribute('hidden', 'until-found'); }
    }
    function toutOuvert() { return groupes.every(estOuvert); }
    function noter() {
      session(cle, groupes.filter(estOuvert).map(function (g) { var h = titreDe(g); return h ? h.id : ''; }));
      var ouvert = toutOuvert();
      if (tout) tout.textContent = ouvert ? 'Tout replier' : 'Tout déplier';
      var b = document.getElementById('rp-plier');
      if (b) etatPlier(b, !ouvert);
    }
    /* le groupe qu'on vient de déplier en bas de l'écran remonte, pour que sa liste se voie */
    function montrer(g) {
      var tete = g.querySelector('.rp-groupe__tete');
      if (!tete) return;
      var r = tete.getBoundingClientRect();
      if (r.bottom < window.innerHeight * 0.6) return;
      var marge = 3.5 * (parseFloat(getComputedStyle(racine).fontSize) || 20);
      var doux = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
      try { window.scrollTo({ top: window.scrollY + r.top - marge, behavior: doux ? 'smooth' : 'auto' }); }
      catch (e) { window.scrollTo(0, window.scrollY + r.top - marge); }
    }
    function basculerTout(ouvrir) { groupes.forEach(function (g) { poser(g, ouvrir); }); noter(); }

    groupes.forEach(function (g) {
      var h = titreDe(g), tete = g.querySelector('.rp-groupe__tete'), corps = g.querySelector('.rp-groupe__corps');
      if (!h || !tete || !corps) return;
      if (!g.dataset.rpPret) {
        g.dataset.rpPret = '1';
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'rp-groupe__bouton';
        while (h.firstChild) b.appendChild(h.firstChild);
        h.appendChild(b);
        if (!corps.id) corps.id = h.id + '--textes';
        b.setAttribute('aria-controls', corps.id);
        tete.addEventListener('click', function (e) {
          if (e.target.closest && e.target.closest('a')) return;      // un lien dans la notice reste un lien
          var ouvrir = !estOuvert(g);
          poser(g, ouvrir); noter();
          if (ouvrir) {
            corps.classList.add('rp-vient');
            setTimeout(function () { corps.classList.remove('rp-vient'); }, 400);
            montrer(g);
          }
        });
        // sur iPhone et iPad, le fond « appuyé » (:active) ne s'affiche que si l'élément écoute le toucher
        try { tete.addEventListener('touchstart', function () {}, { passive: true }); } catch (e) { /* tant pis */ }
        // la recherche du navigateur (Ctrl+F) a trouvé un mot dans un groupe replié : il se déplie
        corps.addEventListener('beforematch', function () { poser(g, true); noter(); });
      }
      poser(g, memo ? memo.indexOf(h.id) !== -1 : estOuvert(g));
    });

    if (sommaire.classList.contains('rp-sommaire--replie')) {
      tout = sommaire.querySelector('.rp-sommaire__tout');
      if (!tout) {
        var entete = sommaire.querySelector('.rp-sommaire__entete');
        if (!entete) {
          entete = document.createElement('div'); entete.className = 'rp-sommaire__entete';
          sommaire.insertBefore(entete, sommaire.firstChild);
        }
        tout = document.createElement('button');
        tout.type = 'button'; tout.className = 'rp-sommaire__tout';
        entete.appendChild(tout);
        tout.addEventListener('click', function () { basculerTout(!toutOuvert()); });
      }
    }
    return {
      retrouvee: !!memo,            // la carte vient d'être remise dans l'état où on l'avait laissée
      toutOuvert: toutOuvert,
      basculerTout: basculerTout,
      ouvrir: function (g) { poser(g, true); noter(); },
      noter: noter
    };
  }

  /* ---- bouton « replier / déplier toutes les sections » de l'en-tête ---- */
  function boutonPlier(nombre) {
    var b = document.getElementById('rp-plier');
    if (!b) return;
    b.hidden = !nombre && !carteCourante;
    etatPlier(b, carteCourante ? !carteCourante.toutOuvert() : false);
    if (b.dataset.rpPret) return; b.dataset.rpPret = '1';
    b.addEventListener('click', function () {
      var zone = document.querySelector('.md-content');
      if (!zone) return;
      var replier = b.getAttribute('aria-pressed') !== 'true';
      zone.querySelectorAll('.collapsible-content').forEach(function (s) { s.classList.toggle('collapsed', replier); });
      zone.querySelectorAll('.collapsible-heading').forEach(function (h) { h.classList.toggle('open', !replier); });
      etatPlier(b, replier);
      if (carteCourante) carteCourante.basculerTout(!replier);
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

  /* ---- accueil : les rubriques ----
     Sur iPhone et iPad, le fond « appuyé » d'un lien (:active) ne s'affiche que si l'élément écoute le
     toucher : sans cela, toucher une rubrique ne donnerait aucun retour avant le changement de page. */
  function rubriquesAccueil(zone) {
    if (!zone) return;
    Array.prototype.forEach.call(zone.querySelectorAll('.rp-portail .rp-carte'), function (a) {
      if (a.dataset.rpPret) return; a.dataset.rpPret = '1';
      try { a.addEventListener('touchstart', function () {}, { passive: true }); } catch (e) { /* tant pis */ }
    });
  }

  /* ---- entrées du menu dont la page n'existe pas encore ----
     mkdocs.yml annonce quelques textes dont le fichier manque : MkDocs en fait un lien vers
     « x.md », qui ne mène nulle part. Le menu les montre (mention « à venir », posée par
     hooks/renouvier.py) ; on leur retire ici leur lien. */
  function entreesAVenir() {
    document.querySelectorAll('a.md-nav__link[href$=".md"]').forEach(function (a) {
      if (a.origin && a.origin !== location.origin) return;       // lien vers un autre site : on n'y touche pas
      a.removeAttribute('href');
      a.setAttribute('aria-disabled', 'true');
      a.classList.add('rp-a-venir');
    });
  }

  /* ---- page calée sur un titre (lien vers une ancre) ----
     La mise en forme des marqueurs de page et des sections pliables change un peu la hauteur du
     texte : sur un long volume, le titre visé descendait de plusieurs centaines de pixels juste
     après l'arrivée, et la table des matières marquait une autre section. On note où est ce titre
     avant la mise en forme et on l'y remet après. On ne touche à rien quand la page n'est pas
     calée sur lui (retour en arrière : le lecteur retrouve l'endroit exact où il était). */
  function repereAncre() {
    var el = null, id = '';
    try { id = decodeURIComponent((location.hash || '').slice(1)); } catch (e) { return null; }
    if (id) el = document.getElementById(id);
    if (!el) return null;
    var marge = parseFloat(getComputedStyle(el).scrollMarginTop) || 0;
    var haut = el.getBoundingClientRect().top;
    return (marge > 0 && Math.abs(haut - marge) <= 4) ? { el: el, haut: haut } : null;
  }
  function recaler(repere) {
    if (!repere || !document.documentElement.contains(repere.el)) return;
    var ecart = repere.el.getBoundingClientRect().top - repere.haut;
    if (Math.abs(ecart) <= 1) return;
    try { window.scrollBy({ top: ecart, behavior: 'instant' }); } catch (e) { window.scrollBy(0, ecart); }
  }

  function init() {
    var contenu = document.querySelector('.md-content');
    reglages();
    entreesAVenir();
    var repere = repereAncre();
    marqueursDePage(contenu);
    var pliables = sectionsPliables(contenu);
    try { carteCourante = carte(contenu); }
    catch (e) { carteCourante = null; racine.classList.remove('rp-js'); }   // en cas d'imprévu : tout reste déplié
    boutonPlier(pliables);
    if (carteCourante) carteCourante.noter();
    recaler(repere);
    tiroirAccueil();
    rubriquesAccueil(contenu);
    // De retour sur une carte, on la retrouve telle quelle : l'adresse peut porter l'ancre de la section
    // où l'on s'était arrêté (Material la tient à jour au fil du défilement), ce n'est pas un lien suivi.
    if (!(carteCourante && carteCourante.retrouvee)) suivreAncre();
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
  window.rpPret = true;      // overrides/main.html s'en assure : sans ce fichier, rien ne reste replié
})();
