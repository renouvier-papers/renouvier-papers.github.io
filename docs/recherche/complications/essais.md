---
title: "Compliquer les Essais pour les expliquer"
description: "Les quatre Essais de critique générale de Charles Renouvier, dépliés."
---

# Compliquer les Essais pour les expliquer

*Ex-pliquer*, c'est déplier. *Com-pliquer*, c'est plier ensemble. Expliquer un livre revient donc à le déplier, ce qui suppose d'admettre d'abord qu'il a été plié.

Cette page est un dépliant. Fermée, elle tient en trois mots ; chaque terme s'ouvre sur ce qu'il contient, qui s'ouvre à son tour. **Ouvrir un pli ne fait rien disparaître** : les voies écartées demeurent, repliées, à côté de celle que l'on suit. Entièrement ouvert, le dépliant livre le plan raisonné des quatre Essais et de quoi y entrer.

**Renouvier avait commencé ce travail.** Il a résumé ses deux premiers Essais dans des textes qu'il appelait des *Formulaires* et les a placés aux charnières de l'œuvre, à la fin d'un Essai ou en tête du suivant. Pour ces deux livres, les paliers intermédiaires du dépliant sont donc de sa main.

<div class="dp" id="dp">
<style>
/* ===================== LE DÉPLIANT — feuille de style locale =====================
   Sélecteurs préfixés par #dp : le dépliant l’emporte sur le style natif des details de
   Material sans recourir à !important, et n'affecte aucune autre page du site.
   ================================================================================= */

/* --- Remise à zéro du details de Material --- */
#dp details {
  display: block; margin: 0; padding: 0; border: 0; border-radius: 0;
  background: none; box-shadow: none; font-size: inherit;
}
#dp summary {
  display: block; margin: 0; padding: 0; border: 0; border-radius: 0;
  background: none; box-shadow: none; font-size: inherit; font-weight: inherit;
  list-style: none; cursor: pointer;
}
#dp summary::-webkit-details-marker { display: none; }

#dp {
  /* Le dépliant emprunte ses couleurs au thème du site : il vit en clair comme en sombre. */
  --dp-fg:      var(--md-typeset-color, #1c1c1c);
  --dp-bg:      var(--md-default-bg-color, #ffffff);
  --dp-accent:  var(--md-accent-fg-color, #37474f);
  --dp-muted:   var(--md-default-fg-color--light, rgba(0,0,0,.54));
  --dp-rule:    var(--md-default-fg-color--lighter, rgba(0,0,0,.24));
  --dp-faint:   var(--md-default-fg-color--lightest, rgba(0,0,0,.06));
  --dp-serif:   "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, "Times New Roman", serif;
  --dp-sans:    var(--md-text-font-family, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif);
  --dp-pas:     1.1rem;
  font-family: var(--dp-sans);
  color: var(--dp-fg);
  line-height: 1.62;
  margin: 2.2rem 0 3rem;
}
#dp *, #dp *::before, #dp *::after { box-sizing: border-box; }

/* --- Barre d'outils --- */
#dp .dp-outils {
  position: sticky; top: 0; z-index: 5;
  display: flex; flex-wrap: wrap; align-items: center; gap: .45rem;
  padding: .5rem 0 .55rem; margin-bottom: 1.3rem;
  border-bottom: 1px solid var(--dp-rule); background: var(--dp-bg);
}
#dp .dp-bouton {
  font: inherit; font-size: .7rem; letter-spacing: .04em;
  padding: .28rem .68rem; cursor: pointer;
  color: var(--dp-fg); background: none;
  border: 1px solid var(--dp-rule); border-radius: 2px;
}
#dp .dp-bouton:hover { border-color: var(--dp-accent); color: var(--dp-accent); }
#dp .dp-bouton:focus-visible { outline: 2px solid var(--dp-accent); outline-offset: 2px; }
#dp .dp-compteur {
  margin-left: auto; font-size: .68rem; color: var(--dp-muted);
  font-variant-numeric: tabular-nums; letter-spacing: .02em;
}

/* --- Le pli --- */
#dp .dp-pli { display: block; margin: .05rem 0; }
#dp .dp-pli + .dp-pli { margin-top: .2rem; }
#dp .dp-titre { display: flex; align-items: baseline; gap: .5rem; padding: .34rem 0; border-radius: 2px; }
#dp .dp-titre:hover .dp-texte { color: var(--dp-accent); }
#dp .dp-titre:focus-visible { outline: 2px solid var(--dp-accent); outline-offset: 2px; }

/* Le chevron du pli */
#dp .dp-titre::before {
  content: ""; flex: 0 0 auto; position: relative; top: -.14em;
  width: .32em; height: .32em;
  border-right: 1.5px solid var(--dp-muted); border-bottom: 1.5px solid var(--dp-muted);
  border-top: 0; border-left: 0; background: none;
  transform: rotate(-45deg); transform-origin: center;
  transition: transform .18s ease, border-color .18s ease;
}
#dp .dp-pli[open] > .dp-titre::before { transform: rotate(45deg); border-color: var(--dp-accent); }
#dp .dp-titre:hover::before { border-color: var(--dp-accent); }
#dp .dp-texte { font-weight: 600; transition: color .15s ease; }

/* La marque de lecture : pleine tant que le pli n'a jamais été ouvert, creuse ensuite.
   C'est la mémoire du parcours : d'un coup d'œil, on voit ce qu'on n'a pas encore vu. */
#dp .dp-titre::after {
  content: ""; flex: 0 0 auto; margin-left: auto; align-self: center;
  width: .4em; height: .4em; border-radius: 50%;
  background: var(--dp-accent); opacity: .5; border: 0;
  transition: background .2s ease, box-shadow .2s ease, opacity .2s ease;
}
#dp .dp-pli.dp-vu > .dp-titre::after {
  background: transparent; box-shadow: inset 0 0 0 1px var(--dp-rule); opacity: 1;
}

/* Le corps : chaque niveau ajoute un filet à gauche. Les filets s'empilent comme
   les plis d'un papier qu'on ouvre : la profondeur se compte à l'œil. */
#dp .dp-corps {
  margin: .05rem 0 .5rem .16rem;
  padding: .15rem 0 .15rem var(--dp-pas);
  border-left: 1px solid var(--dp-rule);
}
#dp .dp-pli[open] > .dp-corps { animation: dp-ouvre .22s ease both; }
@keyframes dp-ouvre { from { opacity: 0; transform: translateY(-2px); } to { opacity: 1; transform: none; } }
#dp .dp-corps > p { margin: .5rem 0; }
#dp .dp-corps > p:first-child { margin-top: .2rem; }

/* --- Rangs : le rang encode la nature du pli, il ne le décore pas --- */
#dp .dp-rang {
  flex: 0 0 auto; min-width: 5.4rem;
  font-size: .61rem; letter-spacing: .11em; text-transform: uppercase;
  color: var(--dp-muted); font-weight: 500; white-space: nowrap;
}
@media (max-width: 44rem) { #dp .dp-rang { min-width: 0; } }

/* Le titre du livre : trois mots empilés, en sérif, comme une page de titre de 1854.
   Ce sont les mots de Renouvier — ils prennent donc sa voix. */
#dp .dp-pli[data-rang="titre"] > .dp-titre .dp-texte {
  font-family: var(--dp-serif); font-size: 1.35rem; font-weight: 400; letter-spacing: .01em;
}
#dp .dp-pli[data-rang="titre"] > .dp-titre { padding: .1rem 0; }
#dp .dp-pli[data-rang="titre"] > .dp-titre .dp-rang { display: none; }
#dp .dp-pli[data-rang="titre"] > .dp-titre::before { top: -.3em; }
#dp .dp-pli[data-rang="titre"]:first-of-type { margin-top: .3rem; }
#dp .dp-pli[data-rang="titre"] + .dp-pli[data-rang="titre"] { margin-top: -.1rem; }
#dp .dp-pli[data-rang="titre"] > .dp-corps { margin-top: .3rem; margin-bottom: .9rem; }
#dp .dp-pli[data-rang="essai"] > .dp-titre .dp-texte { font-size: 1.05rem; }
#dp .dp-pli[data-rang="essai"] > .dp-corps { border-left-color: var(--dp-accent); }

/* --- La voix de Renouvier ---
   Sérif : Renouvier parle. Sans sérif : on parle de lui. La typographie dit qui parle. */
#dp .dp-cite {
  font-family: var(--dp-serif); font-size: .95rem; line-height: 1.72;
  margin: .75rem 0; padding: .5rem 0 .5rem .9rem;
  border-left: 2px solid var(--dp-rule); color: var(--dp-fg);
}
#dp .dp-cite p { margin: .5rem 0; }
#dp .dp-cite p:first-child { margin-top: 0; }
#dp .dp-cite p:last-child { margin-bottom: 0; }
#dp .dp-source {
  display: block; margin-top: .45rem; font-family: var(--dp-sans);
  font-size: .66rem; letter-spacing: .04em; color: var(--dp-muted); font-style: normal;
}

/* --- Les encarts didactiques --- */
#dp .dp-note {
  margin: .8rem 0; padding: .65rem .85rem;
  background: var(--dp-faint); border-radius: 2px;
  font-size: .87rem; line-height: 1.58;
}
#dp .dp-note p { margin: .4rem 0; }
#dp .dp-note p:first-of-type { margin-top: 0; }
#dp .dp-note p:last-child { margin-bottom: 0; }
#dp .dp-etiquette {
  display: block; margin-bottom: .32rem;
  font-size: .61rem; letter-spacing: .13em; text-transform: uppercase;
  font-weight: 700; color: var(--dp-accent);
}
#dp .dp-note--cle { box-shadow: inset 2px 0 0 var(--dp-accent); }

/* --- La charnière : la forme de toute catégorie ---
   Chaque catégorie de Renouvier a la même forme : deux contraires, et leur synthèse.
   C'est une machine. La montrer, c'est expliquer neuf chapitres d'un coup. */
#dp .dp-machine { margin: 1rem 0; display: grid; gap: .4rem; }
#dp .dp-charniere {
  display: grid; grid-template-columns: 1fr auto 1fr auto 1.05fr;
  align-items: center; gap: .45rem; padding: .48rem .7rem;
  border: 1px solid var(--dp-rule); border-radius: 2px; font-size: .82rem;
}
#dp .dp-terme { text-align: center; font-family: var(--dp-serif); }
#dp .dp-op { color: var(--dp-muted); font-size: .82em; text-align: center; }
#dp .dp-synthese { text-align: center; font-family: var(--dp-serif); font-weight: 700; color: var(--dp-accent); }
#dp .dp-nom { font-size: .61rem; letter-spacing: .1em; text-transform: uppercase; color: var(--dp-muted); text-align: right; }
@media (max-width: 44rem) {
  #dp .dp-charniere { grid-template-columns: 1fr auto 1fr; row-gap: .25rem; }
  #dp .dp-charniere .dp-op--fleche { display: none; }
  #dp .dp-synthese, #dp .dp-nom { grid-column: 1 / -1; text-align: center; }
  #dp .dp-synthese::before { content: "↓ "; color: var(--dp-muted); font-weight: 400; }
  #dp .dp-nom { order: -1; text-align: center; margin-bottom: .15rem; }
}

/* --- Le miroir III / IV --- */
#dp .dp-cadre { overflow-x: auto; margin: .85rem 0; -webkit-overflow-scrolling: touch; }
#dp .dp-miroir { width: 100%; min-width: 30rem; border-collapse: collapse; font-size: .79rem; display: table; }
#dp .dp-miroir th, #dp .dp-miroir td {
  padding: .38rem .5rem; text-align: left; vertical-align: top;
  border-bottom: 1px solid var(--dp-faint);
}
#dp .dp-miroir th {
  font-size: .61rem; letter-spacing: .09em; text-transform: uppercase;
  color: var(--dp-muted); font-weight: 600; border-bottom-color: var(--dp-rule);
}
#dp .dp-miroir td:first-child { font-family: var(--dp-serif); font-weight: 700; white-space: nowrap; }
#dp .dp-ch { font-size: .68rem; color: var(--dp-muted); letter-spacing: .03em; white-space: nowrap; }

/* --- La thèse : mise en avant, mais en linéale. C'est un commentaire, pas Renouvier. --- */
#dp .dp-these {
  font-size: 1.02rem; line-height: 1.55; font-weight: 500;
  margin: .4rem 0 1.3rem; padding: .6rem 0 .6rem .9rem;
  border-left: 2px solid var(--dp-accent);
}

/* --- Divers --- */
#dp .dp-chapo { font-size: .84rem; color: var(--dp-muted); margin: .1rem 0 .65rem; }
#dp .dp-epigraphe {
  font-family: var(--dp-serif); font-size: .76rem; letter-spacing: .06em;
  text-transform: uppercase; color: var(--dp-accent); margin: .25rem 0 .75rem;
}
#dp .dp-liste { margin: .55rem 0; padding-left: 1.05rem; }
#dp .dp-liste li { margin: .28rem 0; }
#dp .dp-legende {
  display: flex; flex-wrap: wrap; gap: 1rem;
  font-size: .68rem; color: var(--dp-muted);
  margin-top: 1.6rem; padding-top: .8rem; border-top: 1px solid var(--dp-faint);
}
#dp .dp-puce { display: inline-block; width: .4em; height: .4em; border-radius: 50%; background: var(--dp-accent); opacity: .5; margin-right: .35em; vertical-align: middle; }
#dp .dp-puce--vue { background: transparent; box-shadow: inset 0 0 0 1px var(--dp-rule); opacity: 1; }

@media (prefers-reduced-motion: reduce) {
  #dp *, #dp *::before, #dp *::after { animation: none !important; transition: none !important; }
}
/* --- Le double miroir : le même outil sur le monde, puis sur l'homme.
   À gauche il échoue (gris), à droite il réussit (accent). La couleur porte l'argument. --- */
#dp .dp-double td.dp-non { color: var(--dp-muted); }
#dp .dp-double td.dp-oui { color: var(--dp-accent); font-weight: 600; font-family: var(--dp-serif); }
#dp .dp-double th.dp-tete-non, #dp .dp-double th.dp-tete-oui { text-align: left; }
#dp .dp-double th.dp-tete-oui { color: var(--dp-accent); }

/* --- L'escalier des formulaires : quatre marches, un pli à chaque charnière --- */
#dp .dp-escalier { margin: 1rem 0; display: grid; gap: .3rem; }
#dp .dp-marche {
  display: grid; grid-template-columns: 4.6rem 1fr; gap: .7rem; align-items: baseline;
  padding: .45rem .7rem; border-left: 2px solid var(--dp-rule); font-size: .84rem;
}
#dp .dp-marche--pli {
  border-left-color: var(--dp-accent); background: var(--dp-faint);
  font-family: var(--dp-serif); font-size: .8rem;
}
#dp .dp-marche-num { font-size: .61rem; letter-spacing: .1em; text-transform: uppercase; color: var(--dp-muted); }
#dp .dp-marche--pli .dp-marche-num { color: var(--dp-accent); font-family: var(--dp-sans); }
@media (max-width: 44rem) {
  #dp .dp-marche { grid-template-columns: 1fr; gap: .15rem; }
}
#dp .dp-renvoi { margin: .95rem 0 0; font-size: .8rem; color: var(--dp-muted); }
#dp .dp-renvoi a { color: var(--dp-accent); }
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<p class="dp-chapo">Charles Renouvier — <em>Essais de critique générale</em>, 1854-1864 ; seconde édition, 1875-1896.</p>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">Essais</span></summary>
<div class="dp-corps">
<p>Le titre n'a rien d'une précaution modeste. Un <em>essai</em> est ici un examen qui ignore d'avance son résultat, à l'exact opposé d'un <em>système</em>. Renouvier reprochera sans relâche à Hegel et à Comte d'avoir connu la fin avant d'avoir commencé ; l'image par laquelle il les juge, celle des sphères de Ptolémée, figure au bout de cette page, dans le dernier pli du Quatrième Essai.</p>
<p>Les quatre essais sont donc quatre examens de quatre objets, menés avec un seul outil. Monté dans le premier livre, cet outil à neuf pièces ne changera plus.</p>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">de critique</span></summary>
<div class="dp-corps">
<p>Le mot vient de Kant, et Renouvier le revendique :</p>
<div class="dp-cite">
<p>J'avoue donc nettement que je continue Kant ; et, comme une ambition est bonne et nécessaire chez quiconque ose proposer ses pensées au public, la mienne serait de poursuivre sérieusement en France l'œuvre de la critique, manquée en Allemagne.</p>
<span class="dp-source">Premier Essai, préface de la première édition</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens du mot</span>
<p><em>Critique</em> ne signifie pas dénigrer, mais examiner de quel droit l'on parle du monde avant de dire ce qu'il est. Plutôt qu'une doctrine du monde, la critique est l'inventaire des titres de créance de la raison.</p>
</div>
<p>Les mots « manquée en Allemagne » signifient que Kant a ouvert le bon chantier sans l'achever. Renouvier passera un demi-siècle à le reprendre sur d'autres bases.</p>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">générale</span></summary>
<div class="dp-corps">
<p>Kant avait écrit trois <em>Critiques</em> séparées (raison pure, raison pratique, jugement). Renouvier n'en veut qu'une, mais qui aille partout, et applique une seule méthode à quatre terrains :</p>
<ul class="dp-liste">
<li><strong>La connaissance</strong> — que puis-je savoir, et jusqu'où ? <em>(Premier Essai)</em></li>
<li><strong>L'homme</strong> — qui sait ? suis-je libre ? de quel droit suis-je certain ? <em>(Deuxième Essai)</em></li>
<li><strong>La nature</strong> — que sont la matière, la vie, l'espèce, l'origine ? <em>(Troisième Essai)</em></li>
<li><strong>L'histoire</strong> — que fait l'humanité de sa propre expérience ? <em>(Quatrième Essai)</em></li>
</ul>
<p>Tel est tout le sens de « générale », et l'ambition est considérable, car rien n'y échappe, ni la géométrie, ni les passions, ni Darwin, ni les religions de l'Égypte.</p>
</div>
</details>

<p class="dp-epigraphe">— le livre en une phrase —</p>
<p class="dp-these">Un outil à neuf pièces s'applique quatre fois. Sur le monde pris comme un tout, il échoue à chaque catégorie (Renouvier compte huit échecs, l'étendue et la durée allant ensemble), ce qui marque la limite de la science ; sur l'homme, chaque catégorie donne une fonction, et la neuvième s'appelle la liberté.</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">↓ déplier</span><span class="dp-texte">Le livre en un paragraphe</span></summary>
<div class="dp-corps">
<p>Renouvier part d'une impossibilité qu'il tient pour démontrée, à savoir que <strong>le nombre ne peut pas être infini</strong>. Il en conclut que rien ne nous est donné <em>en soi</em>, mais seulement en <strong>représentation</strong>, et qu'on ne connaît des choses que leurs liaisons constantes, ou <strong>lois</strong>. Celles-ci se ramènent à <strong>neuf relations irréductibles</strong>, les catégories, toutes bâties sur le modèle de deux termes contraires et de leur synthèse. Ces neuf pièces forment le seul outil de toute l'œuvre, et <strong>les quatre Essais en sont les quatre applications</strong>. Appliqué au monde pris comme un tout, l'outil se brise à chaque catégorie (le Formulaire compte huit échecs, l'étendue et la durée allant ensemble), ce qui marque la <strong>limite extrême de la connaissance</strong>. Sur l'homme, il tient neuf fois, et la neuvième catégorie, la personnalité, donne la <strong>liberté</strong>. La science s'arrête, la liberté commence. Le champ ainsi demeuré libre est celui de la <strong>croyance</strong>, donc d'une morale, donc d'une <strong>histoire sans sens de l'Histoire</strong>. Aux deux premières charnières, enfin, Renouvier a glissé un <strong>formulaire</strong> qui replie l'Essai précédent.</p>
<p class="dp-chapo">Chacun des dix termes en gras s'ouvre ci-dessous. On peut s'arrêter à ce paragraphe, qui dit l'essentiel, ou tirer sur un fil.</p>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le pivot</span><span class="dp-texte">le nombre ne peut pas être infini</span></summary>
<div class="dp-corps">
<p>Le mot « pivot » est de Renouvier lui-même, qui écrit « pivotale » entre guillemets :</p>
<div class="dp-cite">
<p>[…] une doctrine dont l'idée « pivotale » a procédé chez moi d'une méditation prolongée sur le sens, et sur la seule justification rationnelle possible des méthodes transcendantes en géométrie.</p>
<span class="dp-source">Premier Essai, avant-propos de la seconde édition</span>
</div>
<p>L'idée directrice du système est donc née d'une réflexion sur les fondements du calcul infinitésimal. Le <em>Formulaire</em> par lequel Renouvier résume lui-même son premier livre en énonce la thèse :</p>
<div class="dp-cite">
<p>L'espace, le temps, la matière, le mouvement, s'ils étaient en soi, impliqueraient le continu en soi, et par suite un nombre infini de parties en soi de ce continu, ce qui est absurde, parce que l'infini et le nombre sont contradictoires entre eux.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">l'argument</span><span class="dp-texte">Pourquoi « l'infini et le nombre sont contradictoires »</span></summary>
<div class="dp-corps">
<p>L'argument tient en trois pas et ne suppose aucune mathématique.</p>
<ul class="dp-liste">
<li>Un <strong>nombre</strong> est un <em>tout</em>, la synthèse de l'un et du multiple. Dire « il y en a sept » revient à avoir fini de compter.</li>
<li>Un <strong>infini</strong> est ce dont on n'a jamais fini.</li>
<li>Un « nombre infini » est donc un tout qu'on ne peut pas achever, un tout qui n'est pas un tout. Le défaut d'une telle notion n'est pas d'être difficile à concevoir, mais de ne rien vouloir dire.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Un contresens à éviter</span>
<p>Renouvier ne prétend pas qu'on ne puisse <em>imaginer</em> l'infini, ni qu'il faille renoncer aux mathématiques. Il vise seulement l'infini <strong>donné en acte</strong>, achevé, réellement présent, et maintient l'autre infini, qu'il nomme l'<strong>indéfini</strong>, où l'on peut toujours ajouter un, toujours diviser encore. L'impossible est d'<em>avoir ajouté</em> une infinité de fois.</p>
<p>Toute la différence est entre <em>on peut toujours</em> (vrai) et <em>c'est déjà fait</em> (contradictoire).</p>
</div>
<p>Renouvier consacre un chapitre entier et plus de soixante-dix pages d'observations à refonder ainsi la fraction, l'incommensurable, la limite, les tangentes, les quadratures, soit le calcul infinitésimal, sans jamais admettre un infini en acte. Il en paie le prix <em>(Premier Essai, ch. XXXII)</em>.</p>
</div>
<p class="dp-renvoi">Ce raisonnement (deux définitions et leur incompatibilité) est décomposé pas à pas, en notation logique, sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">l'enjeu</span><span class="dp-texte">Ce qu'une querelle de mathématiciens vient faire dans une morale</span></summary>
<div class="dp-corps">
<p>La thèse sur le nombre devient ici déterminante, par l'enchaînement suivant :</p>
<ul class="dp-liste">
<li>Si tout nombre est fini, une série effective de choses passées ne peut être infinie.</li>
<li>Le monde a donc commencé, et la série des causes s'arrête à des <strong>causes premières</strong>.</li>
<li>Une cause première n'est pas causée, sans quoi elle ne serait pas première.</li>
<li>Quelque chose peut ainsi commencer sans être déterminé par ce qui précède.</li>
<li>Dès lors, le <strong>libre arbitre</strong> n'est pas une absurdité logique. Il devient possible ; restera à décider s'il est réel, ce que fera le Deuxième Essai en trois cents pages.</li>
</ul>
<p>La liberté, la morale, la République, la critique des religions, tout le personnalisme de Renouvier tient à ce fil, qui est une thèse sur le nombre. Ainsi s'expliquent son intransigeance sur ce point et l'attaque que ses critiques, Couturat notamment dans <em>De l'infini mathématique</em> (1896), y ont portée.</p>
<div class="dp-note">
<span class="dp-etiquette">L'état du débat</span>
<p>Le Premier Essai paraît vingt ans avant les premiers travaux de Cantor (1874), et Renouvier ne le nomme dans aucune des œuvres transcrites ici, même lorsqu'il vise, en 1903, « les partisans actuels de cet infini ». La théorie des ensembles donnera plus tard un sens mathématique cohérent à l'infini actuel, et l'on a souvent cru Renouvier réfuté par là. Les choses sont moins simples, car sa thèse porte non sur ce qu'une théorie peut définir sans contradiction, mais sur ce qui peut être <em>donné</em>, réellement, dans une série de phénomènes. Le débat, toujours ouvert, s'est déplacé des mathématiques vers cette question.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">représentation</span></summary>
<div class="dp-corps">
<p>« Représentation », principal faux ami, ne désigne pas ici une image dans une tête, mais la relation elle-même, dont le sujet et l'objet sont les deux faces.</p>
<div class="dp-cite">
<p>Les choses sont données à la connaissance, en qualité de <em>représentations</em>. Les choses comme représentations sont dites <em>phénomènes</em>. Toute représentation implique deux éléments : l'objectif, le subjectif, lesquels se trouvent encore dans chacun d'eux distingué de l'autre.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le renversement</span>
<p>On croit lire « il y a un moi, qui se représente des objets » ; c'est l'inverse. Il y a de la représentation, dont le « moi » et « le monde » sont les deux versants, sans privilège pour le moi :</p>
</div>
<div class="dp-cite">
<p>La chose appelée <em>moi</em>, aussi bien que tout autre objet de la connaissance, est donnée à la connaissance en une représentation, sous laquelle se groupent des phénomènes diversement composables et décomposables.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Piège de vocabulaire</span>
<p>Renouvier prévient lui-même en note que ses mots <em>objectif</em> et <em>subjectif</em> sont pris « dans un sens tout opposé à l'usage vulgaire ». Ils désignent les deux éléments internes de toute représentation, non deux mondes. Lus avec le sens courant, ils s'entendent à rebours, car la vérité « objective » est chez lui l'« accord de la pensée avec elle-même », la vérité « subjective » l'« accord de la pensée avec les phénomènes hors d'elle » (t. II, p. 246).</p>
</div>
<p>De là vient l'énoncé qui commande tout le reste, selon lequel <strong>il n'y a pas de chose en soi</strong>. Cette thèse est démontrée, non décrétée, par le pivot pour l'espace, le temps, la matière et le mouvement, qui seraient en soi des continus faits d'une infinité actuelle de parties <em>(ch. VIII à XI : le même argument quatre fois)</em>, et par l'analyse de la représentation pour le reste <em>(ch. XII à XIV)</em>.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">lois</span></summary>
<div class="dp-corps">
<p>Si tout est phénomène, il ne reste à connaître que les liaisons constantes entre phénomènes. Renouvier enchaîne alors quatre définitions, dont la dernière renverse l'ontologie.</p>
<div class="dp-cite">
<p>Une <em>loi</em> est un <em>phénomène complexe</em> constamment impliqué dans d'autres <em>phénomènes</em>. […] Une <em>fonction</em> est une <em>loi</em>, considérée en tant que les variations de certains phénomènes composants entraînent des variations déterminées de certains autres. Un <em>être</em> est une fonction.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens de la formule</span>
<p>« Un être est une fonction. » Cette phrase exclut tout socle sous les apparences, tout support caché sous les phénomènes. Une pierre n'est pas une substance qui aurait des propriétés, mais une régularité assez stable pour qu'on la traite comme une chose. <em>Un être</em>, chez Renouvier, est un ensemble de rapports dont la stabilité justifie un nom.</p>
<p>La formule reviendra. Le Formulaire du Deuxième Essai s'ouvrira sur « L'homme est une fonction particulière de toutes les fonctions données dans le monde », qui applique à l'homme la même définition, au sens strict.</p>
</div>
<p>L'opinion contraire, selon laquelle un mot abstrait désigne une chose existant à part, porte chez lui un nom polémique, <strong>le fétichisme en philosophie</strong>, titre du chapitre qui clôt la première partie <em>(ch. XV)</em>. La substance, l'absolu, l'infini, l'être en général sont autant de fétiches, des mots pris pour des dieux.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">la machine</span><span class="dp-texte">neuf relations irréductibles</span></summary>
<div class="dp-corps">
<p>Le cœur de l'œuvre entière tient sur une page. Renouvier appelle <strong>catégories</strong> les relations premières auxquelles tout se ramène et qui ne se ramènent à rien.</p>
<div class="dp-cite">
<p>La plus universelle des lois de la représentation est la <em>relation</em> en général. Toutes les autres sont des espèces de la relation.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Toutes les neuf ont la même forme, <strong>deux termes contraires, et leur synthèse.</strong> Elles composent une machine, dont Renouvier donne lui-même le plan complet, en une phrase, au premier chapitre du Deuxième Essai :</p>
<div class="dp-machine">
<div class="dp-charniere"><span class="dp-terme">distinct</span><span class="dp-op">+</span><span class="dp-terme">identique</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">déterminé</span><span class="dp-nom">Relation</span></div>
<div class="dp-charniere"><span class="dp-terme">un</span><span class="dp-op">+</span><span class="dp-terme">multiple</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">tout</span><span class="dp-nom">Nombre</span></div>
<div class="dp-charniere"><span class="dp-terme">point</span><span class="dp-op">+</span><span class="dp-terme">espace</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">étendue</span><span class="dp-nom">Position</span></div>
<div class="dp-charniere"><span class="dp-terme">instant</span><span class="dp-op">+</span><span class="dp-terme">temps</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">durée</span><span class="dp-nom">Succession</span></div>
<div class="dp-charniere"><span class="dp-terme">différence</span><span class="dp-op">+</span><span class="dp-terme">genre</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">espèce</span><span class="dp-nom">Qualité</span></div>
</div>
<p class="dp-chapo">— seuil : l'une de ces cinq ôtée, il ne reste rien de représenté —</p>
<div class="dp-machine">
<div class="dp-charniere"><span class="dp-terme">rapport</span><span class="dp-op">+</span><span class="dp-terme">non-rapport</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">changement</span><span class="dp-nom">Devenir</span></div>
<div class="dp-charniere"><span class="dp-terme">acte</span><span class="dp-op">+</span><span class="dp-terme">puissance</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">force</span><span class="dp-nom">Causalité</span></div>
<div class="dp-charniere"><span class="dp-terme">état</span><span class="dp-op">+</span><span class="dp-terme">tendance</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">passion</span><span class="dp-nom">Finalité</span></div>
<div class="dp-charniere"><span class="dp-terme">soi</span><span class="dp-op">+</span><span class="dp-terme">non-soi</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">conscience</span><span class="dp-nom">Personnalité</span></div>
</div>
<div class="dp-cite">
<p>Les catégories sont : la relation (trois formes : <em>distinct, identique, déterminé</em>) ; le nombre (<em>un, multiple, tout</em>) ; la position (<em>point, espace, étendue</em>) ; la succession (<em>instant, temps, durée</em>) ; la qualité (<em>différence, genre, espèce</em>) ; le devenir (<em>rapport, non-rapport, changement</em>) ; la causalité (<em>acte, puissance, force</em>) ; la finalité (<em>état, tendance, passion</em>) ; la personnalité (<em>soi, non-soi, conscience</em>).</p>
<span class="dp-source">Deuxième Essai, ch. I — De la nature humaine relativement aux catégories</span>
</div>
<p class="dp-chapo">Ces neuf lignes forment le squelette des chapitres XXVI à XL du Premier Essai et en condensent près de huit cents pages.</p>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">comment lire</span><span class="dp-texte">Ce que ces neuf lignes veulent dire</span></summary>
<div class="dp-corps">
<p>Chaque ligne signifie qu'aucun des deux termes de gauche ne peut être pensé tout seul. Rien n'est <em>un</em> sans être aussi multiple ; rien n'est purement multiple sans faire un. Ce qui existe pour la connaissance est toujours le troisième terme, le <em>tout</em>, qui est leur synthèse.</p>
<div class="dp-cite">
<p>[…] aucune chose n'est <em>une</em>, abstraction faite de toute multiplicité ; aucune n'est <em>multiple</em>, abstraction faite de toute unité ; mais toute chose est représentée comme un <em>tout</em>.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La conséquence pour la métaphysique</span>
<p>Les mots par lesquels la philosophie a toujours cru toucher le fond, <strong>l'un, le simple, l'infini, l'absolu</strong>, n'ont de sens que par corrélation à leurs contraires. Pris isolément, comme on le fait, ils ne désignent rien. Ce sont, non des objets difficiles, mais des moitiés de rapport privées de l'autre moitié.</p>
</div>
<div class="dp-cite">
<p>Les termes les plus généraux et les plus abstraits, à l'aide desquels on essaye de surmonter les rapports : l'un, le simple, l'infini, l'absolu, ne sont eux-mêmes représentés que par corrélation à des termes contraires, et séparément ne sont aucune chose et n'en qualifient aucune.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>D'où la formule qui tient lieu de devise à tout le criticisme français : <strong>« Tout phénomène est donné par rapport à d'autres phénomènes. »</strong></p>
</div>
<p class="dp-renvoi">Les neuf lignes se réduisent à une seule opération, la synthèse de deux contraires corrélatifs, mise en notation sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">le seuil</span><span class="dp-texte">Pourquoi cinq d'un côté et quatre de l'autre</span></summary>
<div class="dp-corps">
<p>Les neuf catégories ne sont pas à égalité, et Renouvier le dit dans un passage peu remarqué, qui place une coupure après la cinquième.</p>
<div class="dp-cite">
<p>Otée l'une quelconque des cinq premières catégories, rien de représenté ne subsiste. […] Les autres catégories, le Devenir, la Causalité, la Finalité, la Personnalité, ne s'appliquent pas toujours et d'une manière immédiate à tout sujet qu'on se représente ; mais il n'est pas de fonction représentative, objective, à laquelle elles ne soient inhérentes.</p>
<span class="dp-source">Deuxième Essai, ch. I</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La chose et l'acte</span>
<p>Les <strong>cinq premières</strong> constituent la chose, car sans relation, nombre, lieu, date ni genre, il n'y a pas d'objet du tout ; les <strong>quatre dernières</strong>, parfois absentes de l'objet (un caillou ne poursuit pas de fin), sont toujours dans <em>l'acte</em> de se le représenter, puisque penser quoi que ce soit exige de changer, d'agir, de viser et d'être quelqu'un.</p>
<p>Les cinq premières relèvent de ce qui est vu ; les quatre dernières, de celui qui voit. Aussi la personnalité est-elle la neuvième, comme le bout de cette pente et non comme un ajout.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">contre Kant</span><span class="dp-texte">Neuf, et non douze</span></summary>
<div class="dp-corps">
<p>Kant avait douze catégories, rangées en quatre groupes de trois, qu'il tirait de la table des jugements de la logique scolaire. Renouvier n'en compte que neuf, qu'il tire d'ailleurs. Trois différences les séparent, par ordre de gravité :</p>
<ul class="dp-liste">
<li><strong>L'origine.</strong> Kant lit ses catégories dans une table de logique héritée. Renouvier les obtient par analyse de la représentation et avoue sans fard le procédé : « J'arrive aux catégories empiriquement ; je les fixe par hypothèse, et je les propose pour être vérifiées. »</li>
<li><strong>L'unité.</strong> Kant juxtapose quatre familles hétérogènes ; Renouvier pose une seule racine, la relation, dont les huit autres sont des espèces.</li>
<li><strong>La nouveauté.</strong> Plusieurs de ses catégories manquent chez Kant (la position et la succession, qui étaient chez lui des formes de l'intuition, le devenir, la finalité), et la plus lourde de conséquences, <strong>la personnalité</strong>, n'est pas la dernière par hasard.</li>
</ul>
<div class="dp-cite">
<p>Sous un autre point de vue, celui de l'homme, nécessairement imposé à l'homme, la loi de <em>personnalité</em> est encore une loi universelle. Tout, pour nous, est relatif à la <em>conscience</em>.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">La portée de cette nouveauté</span>
<p>Deux catégories, et non une, sont donc universelles, la <em>relation</em> sous le point de vue des choses et la <em>personnalité</em> sous celui de l'homme ; les sept autres se rangent entre elles. En faisant de la conscience une catégorie, condition de toute représentation et non objet parmi d'autres, Renouvier pose la conclusion de toute son œuvre, le <strong>personnalisme</strong>. Le mot ne désignera la doctrine qu'en 1903 ; la chose figure ici, dans une liste de neuf.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le double miroir</span><span class="dp-texte">les quatre Essais en sont les quatre applications</span></summary>
<div class="dp-corps">
<p>Ce qui fait des quatre Essais un seul livre échappe à tout sommaire. Plutôt qu'un chapitre de l'œuvre, les neuf catégories en sont <strong>l'unique outil</strong>, qui ne changera plus une fois monté. Tout le reste consiste à l'appliquer, dans l'ordre, à quatre objets de plus en plus concrets.</p>
<ul class="dp-liste">
<li><strong>Au monde pris comme un tout</strong> — quatrième partie du Premier Essai. L'outil se brise à chaque catégorie.</li>
<li><strong>À l'homme</strong> — première partie du Deuxième Essai. L'outil tient, neuf fois.</li>
<li><strong>À la nature</strong> — Troisième Essai. L'être, la matière, la vie, l'espèce, l'origine.</li>
<li><strong>À l'histoire</strong> — Quatrième Essai. L'interdit logique y devient un interdit historiographique.</li>
</ul>
<p>Les deux premières applications se répondent catégorie par catégorie. Ce <strong>double miroir</strong> est reconstitué ici à partir des deux tables que Renouvier a laissées, celle des échecs, à la fin du Premier Essai (huit articles, l'étendue et la durée réunies), et celle des neuf fonctions, dans le <em>Formulaire</em> du Deuxième, selon un ordre un peu différent. Le tableau les aligne.</p>
<div class="dp-cadre">
<table class="dp-miroir dp-double">
<thead><tr><th>Catégorie</th><th class="dp-tete-non">Sur le monde, elle échoue</th><th class="dp-tete-oui">Sur l'homme, elle donne</th></tr></thead>
<tbody>
<tr><td>Relation</td><td class="dp-non">Le tout n'est le terme d'aucun rapport.</td><td class="dp-oui">Comparaison, Attention, Réflexion</td></tr>
<tr><td>Nombre</td><td class="dp-non">Les phénomènes font un nombre, que nul ne peut compter.</td><td class="dp-oui">Numération</td></tr>
<tr><td>Position</td><td class="dp-non">Le monde est mesuré, il n'est pas mesurable.</td><td class="dp-oui">Imagination</td></tr>
<tr><td>Succession</td><td class="dp-non">Traitée avec l'étendue : le monde est mesuré dans la durée, il n'est pas mesurable.</td><td class="dp-oui">Mémoire, Prévision</td></tr>
<tr><td>Qualité</td><td class="dp-non">Le tout enveloppe tous les genres : aucun ne le spécifie.</td><td class="dp-oui">Raison, Jugement, Raisonnement</td></tr>
<tr><td>Devenir</td><td class="dp-non">Le monde devient, mais on ne peut comparer le monde au monde ; il a commencé, et ce commencement est inexplicable.</td><td class="dp-oui">Pensée</td></tr>
<tr><td>Causalité</td><td class="dp-non">Il faut des causes premières ; on n'en peut rien dire.</td><td class="dp-oui">Volonté</td></tr>
<tr><td>Finalité</td><td class="dp-non">Ni premier but ni but dernier ne sont assignables.</td><td class="dp-oui">Passion, Instinct, Habitude</td></tr>
<tr><td>Personnalité</td><td class="dp-non">Une conscience du tout cesserait d'être une conscience.</td><td class="dp-oui">Liberté</td></tr>
</tbody>
</table>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La dernière ligne</span>
<p>La neuvième pièce du même outil interdit, sur le monde, toute conscience du tout, car une conscience qui envelopperait tout n'aurait plus de non-soi et cesserait donc d'en être une. Sur l'homme, elle donne la personnalité, c'est-à-dire la <strong>liberté</strong>.</p>
<p>Renouvier tient en une phrase, qui explique aussi l'unité des quatre Essais : <strong>la connaissance échoue sur le tout et réussit sur la personne.</strong> Le monde n'a pas de sommet ; il a des personnes. Ainsi le personnalisme n'est-il pas une doctrine ajoutée à sa logique, mais ce qui reste quand la logique a fini de démolir.</p>
</div>
<p class="dp-chapo">La colonne de gauche, en gris, énumère des impossibilités ; celle de droite, ce que l'analyse de l'homme établit.</p>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">la table</span><span class="dp-texte">D'où viennent ces deux colonnes</span></summary>
<div class="dp-corps">
<p>Les deux colonnes viennent chacune d'un <em>Formulaire</em>, et l'éditeur n'a eu qu'à les mettre côte à côte.</p>
<p>À gauche, la dernière section du <em>Formulaire du Traité de logique générale</em> énumère les huit échecs de la synthèse totale (l'étendue et la durée réunies au 3°), numérotés « 1° à l'égard de la relation… 2° à l'égard de la totalité… », dans l'ordre exact des chapitres XLII à LIII du tome III.</p>
<p>À droite, la section A du <em>Formulaire du Traité de Psychologie rationnelle</em> énumère les fonctions humaines, numérotées de 1 à 9, chacune sous le nom de sa catégorie, à deux nuances près. Le nombre y devient « Quantité », et l'ordre change (5. Devenir, 6. Qualité, 7. Finalité, 8. Causalité). On y lit textuellement « 1. Relation : <em>Comparaison, Attention, Réflexion</em> », « 3. Position : <em>Imagination</em> », « 4. Succession : <em>Mémoire</em> », et enfin « 9. Personnalité : <em>Liberté</em> ».</p>
<div class="dp-cite">
<p>La conscience des phénomènes comme limités, écartés d'espace et déterminés d'étendue, est l'<em>Imagination</em>.</p>
<span class="dp-source">Formulaire du Traité de Psychologie rationnelle, A, 3</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le prix de ce savoir</span>
<p>Cette correspondance est significative, car elle montre que la psychologie de Renouvier est une <em>déduction</em>. Au lieu d'observer l'esprit et de dresser la liste de ce que fait l'homme, il prend ses neuf catégories et demande, pour chacune, quelle fonction de conscience lui correspond. La mémoire n'est donc pas une faculté qu'on aurait trouvée, mais ce que devient la catégorie de succession quand un être s'en sert.</p>
<p>Le titre du premier chapitre du Deuxième Essai, <em>De la nature humaine relativement aux catégories</em>, vaut d'ailleurs programme.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">3ᵉ et 4ᵉ</span><span class="dp-texte">Les deux applications suivantes, et où elles s'arrêtent</span></summary>
<div class="dp-corps">
<p>Le même outil descend ensuite vers le concret, et chaque Essai s'achève en désignant le suivant. Renouvier noue lui-même cette chaîne explicite.</p>
<div class="dp-cite">
<p>[…] c'est à la critique de l'Homme qu'il appartiendra de les approfondir.</p>
<span class="dp-source">Premier Essai, dernières lignes du ch. LIV</span>
</div>
<div class="dp-cite">
<p>[…] en terminant le deuxième, je me suis trouvé, d'un côté, à l'entrée de la morale, de l'autre, sur la limite des religions, et j'ai senti la nécessité de donner une matière nouvelle à l'analyse : l'histoire.</p>
<span class="dp-source">Troisième Essai, ch. I — Résumé. Plan.</span>
</div>
<div class="dp-cite">
<p>Je m'arrête enfin en amenant l'homme sur la scène, c'est-à-dire au seuil même de l'histoire.</p>
<span class="dp-source">Troisième Essai, ch. I — Résumé. Plan.</span>
</div>
<div class="dp-cite">
<p>L'histoire est l'expérience que l'humanité a d'elle-même.</p>
<span class="dp-source">Quatrième Essai, § I — première phrase</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La soudure</span>
<p>Le Troisième Essai s'achève sur « L'origine de l'homme » et « Les origines premières et morales » ; le Quatrième, après un plan d'études (§ I), s'ouvre sur « Des commencements de l'humanité » (§ II). Sans couture, le troisième livre dépose l'homme au seuil, et le quatrième le fait entrer. Parus en dix ans, de 1854 à 1864, les quatre livres s'enchaînent exactement.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le miroir</span><span class="dp-texte">limite extrême de la connaissance</span></summary>
<div class="dp-corps">
<p>Ainsi s'intitule la quatrième et dernière partie du Premier Essai, dont Renouvier pose la question en sous-titre :</p>
<p class="dp-epigraphe">Une synthèse unique et totale des phénomènes est-elle possible ?</p>
<p><strong>La quatrième partie est le miroir de la troisième.</strong> Les neuf catégories, construites une par une dans la troisième, sont reprises par la quatrième <em>dans le même ordre</em> et appliquées au monde entier, sur lequel elles échouent l'une après l'autre.</p>
<div class="dp-cadre">
<table class="dp-miroir">
<thead><tr><th>Catégorie</th><th>Construite en III</th><th>Appliquée au monde en IV</th></tr></thead>
<tbody>
<tr><td>Relation</td><td class="dp-ch">ch. XXVII</td><td class="dp-ch">ch. XLII</td></tr>
<tr><td>Nombre</td><td class="dp-ch">ch. XXIX</td><td class="dp-ch">ch. XLIII</td></tr>
<tr><td>Position</td><td class="dp-ch">ch. XXX</td><td class="dp-ch">ch. XLIV, XLVI, XLVII</td></tr>
<tr><td>Succession</td><td class="dp-ch">ch. XXXI</td><td class="dp-ch">ch. XLV</td></tr>
<tr><td>Qualité</td><td class="dp-ch">ch. XXXIII</td><td class="dp-ch">ch. XLVIII</td></tr>
<tr><td>Devenir</td><td class="dp-ch">ch. XXXVI</td><td class="dp-ch">ch. XLIX, L</td></tr>
<tr><td>Causalité</td><td class="dp-ch">ch. XXXVII</td><td class="dp-ch">ch. LI</td></tr>
<tr><td>Finalité</td><td class="dp-ch">ch. XXXIX</td><td class="dp-ch">ch. LII</td></tr>
<tr><td>Personnalité</td><td class="dp-ch">ch. XL</td><td class="dp-ch">ch. LIII</td></tr>
</tbody>
</table>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'usage de la table</span>
<p>La table autorise à entrer dans le livre par n'importe quelle ligne. Qui s'intéresse au temps lira XXXI, puis XLV, où il trouvera la catégorie et sa ruine, et comprendra sur cet exemple la méthode entière. Le livre se lit en colonnes autant qu'en lignes, et son « architecture », selon le mot des commentateurs, ne désigne rien d'autre.</p>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">la rupture</span><span class="dp-texte">Là où Renouvier cesse de continuer Kant</span></summary>
<div class="dp-corps">
<p>Les antinomies de Kant sont quatre couples de propositions contraires (le monde a un commencement / il n'en a pas), dont Kant établit que <em>la thèse et l'antithèse sont également démontrables</em>. De cette égalité insoluble, il tire une preuve indirecte de l'idéalisme transcendantal.</p>
<p>Renouvier tient cette égalité pour une erreur, et rompt avec Kant sur ce point.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'antinomie tranchée</span>
<p>Thèse et antithèse sont inégales. La thèse (fini, commencement, nombre déterminé) est vraie, tout uniment ; l'antithèse (infini en acte), <strong>contradictoire</strong>, n'est pas une seconde démonstration mais un énoncé qui ne veut rien dire. En accordant à l'infini la même dignité logique qu'au fini, Kant s'est laissé prendre à un fétiche et a bâti son idéalisme sur une balance faussée.</p>
</div>
<p>Les Observations du chapitre XLII s'ouvrent sur un titre sans ambiguïté, <em>Réfutation des antinomies kantiennes</em>. Renouvier montre au passage que ses propres catégories ne produisent, elles, aucune antinomie, car leurs deux termes contraires, abstraits et corrélatifs, ne s'appliquent jamais séparément à rien et ne peuvent donc se contredire.</p>
<div class="dp-cite">
<p>[…] les catégories, par elles-mêmes, ne conduisent point à l'antinomie […]. D'autres antinomies semblent résulter de la tentative de détermination de la <em>chose en général</em> […]. Mais elles ne subsistent que parce qu'on se refuse à borner la science à la considération des relatifs.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Les antinomies sont donc la punition d'une ambition, non une fatalité de la raison. Elles ne surgissent que si l'on veut connaître le tout. Qu'on y renonce, et la raison redevient cohérente.</p>
</div>
<p class="dp-renvoi">Les échecs de la synthèse totale tiennent en un lemme (le Tout n'a pas de vis-à-vis), formalisé sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">liberté</span></summary>
<div class="dp-corps">
<p>Neuvième pièce de la machine, appliquée à l'homme, la liberté marque le sommet du Deuxième Essai et le premier endroit de l'œuvre où Renouvier doit décider au lieu de démontrer.</p>
<p>Car il commence par saborder l'argument que chacun attend :</p>
<div class="dp-cite">
<p>On voit à quel point se trompent les philosophes qui regardent la liberté humaine comme un fait d'expérience. Si cela était, en disputerait-on ? Qui jamais a contesté l'existence d'un fait sensible en le sentant ?</p>
<span class="dp-source">Deuxième Essai, ch. XIII — La liberté ; état de la question</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le nœud du problème</span>
<p>Si je suis libre, je juge librement que je le suis, et mon jugement ne prouve donc rien ; si je suis déterminé, je juge nécessairement, vrai ou faux, et il ne prouve rien non plus. Renouvier écrit sans détour que « c'est à la liberté qu'il appartient de déclarer si la liberté est ou non ».</p>
<p>Aucune preuve n'étant possible, ni pour ni contre, il faut <em>choisir</em>, et ce choix est lui-même un acte libre. La liberté s'affirme sans se démontrer, et l'affirmation en est déjà l'exercice.</p>
</div>
<p>De là le renversement du plan, qui fait de la certitude le terme de la philosophie et non son point de départ. Renouvier s'y engage dès la troisième page du Premier Essai ; le Deuxième, cinq ans plus tard, tiendra la promesse :</p>
<div class="dp-cite">
<p>Le chapitre de la certitude n'a pas sa place marquée dans ce <em>traité</em>. Il formera contre tout usage, mais en toute raison, la clef de voûte d'un édifice qu'il s'agit de fonder […] ; il n'en sera pas la première pierre.</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Même la statistique ne donne qu'une probabilité</span>
<p>Le chapitre s'adosse à une Observation entière, prélevée dans les <em>Observations et développements</em>, que cette page n'ouvre qu'exceptionnellement. Selon l'argument, le hasard a pour signature la loi des grands nombres, qui est l'<em>absence</em> de loi individuelle. Des actes libres la porteraient. Mais le verdict mérite d'être lu jusqu'au bout :</p>
<div class="dp-cite">
<p>[…] les applications du calcul des probabilités sont par elles-mêmes une vérification <em>probable</em> de l'existence effective de la liberté. La loi des grands nombres est la loi des faits qui ne reconnaissent point d'autre loi.</p>
<span class="dp-source">Deuxième Essai, ch. XIII, Observations et développements, A — De l'interprétation de la loi dite des <em>grands nombres</em></span>
</div>
<p>L'italique du mot <em>probable</em> est de Renouvier, qui refuse d'appeler preuve même son meilleur indice empirique. Le pari reste entier, à dessein.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">L'ordre cartésien renversé</span>
<p>Descartes commence par la certitude ; Renouvier finit par elle. Le motif est imparable, car chercher d'abord la certitude reviendrait à juger de la valeur de la raison avant de l'avoir examinée. La certitude est le toit, non le sol, et ce toit, une fois posé, s'appelle la liberté.</p>
</div>
<p>Dans les <em>Observations</em> du chapitre XIV, sous les titres « La philosophie de Jules Lequier » puis « Comment trouver, comment chercher une première vérité ? », et dans celles du chapitre XVII, Renouvier a publié les fragments de son ami Jules Lequier, mort en 1862, auquel il devait l'idée que la liberté doit être choisie. En 1859, ces pages tenaient dans une note ; la seconde édition leur fait place à la suite des chapitres.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">croyance</span></summary>
<div class="dp-corps">
<p>Ici revient toujours le même contresens, qui fait lire <em>la raison s'arrête, donc croyez ce qu'il vous plaît.</em> Le texte dit l'inverse.</p>
<div class="dp-cite">
<p>Les bornes de la connaissance ainsi reconnues, deux choses restent intactes. Ce sont d'abord les croyances, qui, sans prétendre dépasser ces bornes en s'obstinant dans l'affirmation d'objets que la raison a déclarés contradictoires, demeurent libres de s'étendre au delà et bien loin de ce que l'analyse peut ou pourra jamais atteindre.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le principe</span>
<p>La croyance est libre là où la raison <strong>ne démontre pas</strong> ; elle est interdite là où la raison <strong>démontre une contradiction</strong>.</p>
<p>La règle institue non un partage de territoire, mais une hiérarchie, où la raison, sans se retirer, trace la frontière et en garde un côté. Un Dieu infini en acte est proscrit parce qu'il ne veut rien dire, non parce qu'il déplaît. Une pluralité de consciences premières est en revanche permise, et Renouvier jugera d'abord qu'elle « semble » la seule hypothèse rationnelle, avant de l'abandonner en 1886.</p>
</div>
<p>Tel est tout le programme de la troisième partie du Deuxième Essai, dont le titre énumère ce qui reste debout, <em>Les probabilités touchant l'ordre moral du monde. L'immortalité, la liberté, la divinité.</em> Les trois postulats de Kant y sont repris un à un, mais sans chose en soi, sans infini, et en probabilités morales plutôt qu'en postulats nécessaires. Renouvier va jusqu'à intituler un chapitre entier <em>Examen des thèses de la raison pratique de Kant</em>, et un autre <em>Des hypothèses rationnelles sur la nature de Dieu</em>.</p>
<div class="dp-note">
<span class="dp-etiquette">Un Dieu fini</span>
<p>La conclusion, l'une des plus singulières du siècle, suit du pivot comme le reste. L'infini en acte étant contradictoire, un Dieu infini l'est aussi. Reste un Dieu fini, et « la personne divine est ainsi soustraite aux attributs infinis que la métaphysique appelait des <em>perfections</em> et qui la détruisaient. Mais la vraie <em>perfection</em> lui reste […] : la perfection de justice et de bonté ». Renouvier ajoute que rien alors ne prouve plus l'unité de Dieu plutôt que sa pluralité. Un traité de logique de 1854 aboutit, en 1875, à rendre le polythéisme rationnellement recevable.</p>
</div>
<p>Cette frontière dépasse l'exercice d'école. Elle est, dans la préface de 1854, ce que Renouvier attend de plus important pour son siècle :</p>
<div class="dp-cite">
<p>La limitation mutuelle et définitive de la science et des croyances est d'une importance majeure pour l'ordre et le progrès régulier des associations humaines. […] Le jour où la liberté serait connue, et l'homme désaccoutumé de vouloir forcer l'homme à croire ou à ne pas croire, on verrait des églises se former, s'unir, se dissoudre et se reconstituer, sans que la science ou l'État s'y trouvassent intéressés.</p>
<span class="dp-source">Premier Essai, préface de la première édition</span>
</div>
<p>Écrit six ans après 1848, un traité de logique de six cents pages sur les catégories et l'infini a pour conclusion politique la séparation des Églises et de l'État, votée cinquante et un ans plus tard, deux ans après la mort de Renouvier.</p>
<div class="dp-note">
<span class="dp-etiquette">Un chapitre inattendu</span>
<p>Le Deuxième Essai, traité de psychologie, comporte un chapitre XIX intitulé <em>Complément de la définition de la certitude. Du contrat personnel et du contrat social.</em> Ce passage de la certitude au contrat n'a rien d'une digression, car si la vérité est affirmée par une liberté, son lieu est un accord entre des libertés. Plutôt qu'une conséquence politique de la philosophie de Renouvier, la République est un chapitre de sa psychologie.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">l'interdit</span><span class="dp-texte">histoire sans sens de l'Histoire</span></summary>
<div class="dp-corps">
<p>La quatrième partie du Premier Essai a interdit la <strong>synthèse totale</strong>, la connaissance du tout. Or une philosophie de l'histoire, chez Bossuet, Vico, Hegel ou Comte, opère exactement la synthèse totale de l'histoire humaine, qu'elle dote d'un plan, d'un sens, d'une fin. Elle est donc interdite par la même démonstration, non par goût.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le titre est une conséquence</span>
<p>Le Quatrième Essai s'intitule <em>Introduction à la philosophie <strong>analytique</strong> de l'histoire</em>, et l'adjectif, nullement ornemental, est l'exact opposé de <em>synthétique</em>. Renouvier ne peut faire de philosophie synthétique de l'histoire, ayant démontré dans la quatrième partie du Premier Essai que la synthèse totale est impossible. L'interdit logique devient un interdit de méthode en histoire.</p>
</div>
<p>Il présente d'ailleurs sa méthode par ce qu'il refuse :</p>
<div class="dp-cite">
<p>Traitée dans un système apriorique, elle défigure les faits, ou elle les dédaigne ; elle en rejette et elle en interpole, afin de disposer plus commodément les autres en série.</p>
<span class="dp-source">Quatrième Essai, § I</span>
</div>
<p>On manque l'histoire de deux façons, sans critique ou avec un système fixé d'avance. Entre les deux, la voie étroite de l'analyse s'en tient aux faits établis et aux inductions tirées de ce que la personne humaine a de constant.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">l'escalier</span><span class="dp-texte">formulaire</span></summary>
<div class="dp-corps">
<p>La trouvaille est de Renouvier. Aux deux premières charnières de l'œuvre, il a placé un texte, qu'il appelle un <strong>formulaire</strong>, qui replie l'Essai précédent en propositions nues, sans preuves, sans exemples, sans polémique. Il a déplacé, réédité et corrigé ces textes pendant trente ans.</p>
<div class="dp-escalier">
<div class="dp-marche"><span class="dp-marche-num">Essai I</span><span>Traité de logique générale — 3 tomes, 54 chapitres</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">le pli</span><span>Formulaire du Traité de logique générale — 23 pages (t. III, p. 269-291). En tête du Deuxième Essai en 1859 ; déplacé à la fin du Premier en 1875.</span></div>
<div class="dp-marche"><span class="dp-marche-num">Essai II</span><span>Traité de psychologie rationnelle — 3 tomes, 25 chapitres</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">le pli</span><span>Formulaire du Traité de Psychologie rationnelle — sections A, B, C, D. Trois éditions : en tête du Troisième Essai en 1864 ; à la fin du Deuxième en 1875 ; <em>et</em> de nouveau en tête du Troisième en 1892, où Renouvier signale ses propres repentirs en note.</span></div>
<div class="dp-marche"><span class="dp-marche-num">Essai III</span><span>Les Principes de la nature — 2 tomes, 12 chapitres</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">le pli</span><span>« I. Résumé. Plan. » — ouverture du Troisième Essai, qui récapitule les deux premiers et présente le troisième jusqu'au « seuil même de l'histoire ». Ce chapitre n'est pas un formulaire, et le Quatrième n'en a pas.</span></div>
<div class="dp-marche"><span class="dp-marche-num">Essai IV</span><span>Introduction à la philosophie analytique de l'histoire — 32 paragraphes</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La conséquence pour cette page</span>
<p>Le niveau intermédiaire d'un dépliant, palier entre le titre et le livre, n'a pas eu à être inventé ici. <strong>Pour les deux premiers Essais, il est de la main de l'auteur.</strong> Renouvier a plié ses propres livres et rangé les plis aux charnières, là où on les cherche rarement, à la fin des tomes, avant les notes.</p>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">la preuve</span><span class="dp-texte">Renouvier raconte lui-même le déplacement</span></summary>
<div class="dp-corps">
<p>À la toute fin du Deuxième Essai, après le Formulaire, une <em>Note finale</em> explique le déplacement :</p>
<div class="dp-cite">
<p>Les lignes suivantes étaient jointes, dans la première édition du <em>Deuxième Essai de critique générale</em>, à un résumé du <em>Premier Essai</em>, portant le titre de : <em>Formulaire du Premier Essai</em>. Ce formulaire a été reproduit à la fin de la seconde édition du <em>Premier Essai</em>, où sa place se trouvait naturellement marquée.</p>
<span class="dp-source">Deuxième Essai, Note finale</span>
</div>
<p>« Où sa place se trouvait naturellement marquée ». En 1859, le résumé du premier livre servait de porte d'entrée au second ; en 1875, Renouvier le renvoie à la fin du premier. Sans changer de contenu, le pli a changé de charnière.</p>
<div class="dp-note">
<span class="dp-etiquette">Le pli suivant existe en trois états</span>
<p>Le <em>Formulaire du Traité de Psychologie rationnelle</em> ouvre le Troisième Essai en 1864, clôt le Deuxième en 1875 et rouvre le Troisième en 1892, sous le titre <em>Introduction — Résumé des principes de la psychologie rationnelle</em>, avec les mêmes quatre sections et la même première phrase. <strong>Ce texte connaît ainsi trois états sur vingt-huit ans.</strong> Les deux derniers concordent à 94,3 % au mot ; l'état de 1892 compte 599 mots de plus que celui de 1875 (16 811 contre 16 212). Renouvier signale aussi, en note, qu'il corrige là « cette troisième édition du résumé de mes <em>Essais</em> », qu'il a mis une conclusion « sous une forme dubitative » et en a ajouté une autre, « plus avancée dans le sens des postulats ».</p>
<p>En somme, <strong>le palier a une histoire, et elle est datée.</strong> Lu à trois âges, le même résumé montre un homme changer d'avis sur Dieu, en note. Une page voisine, <a href="../evolution/">Comment je suis arrivé à cette conclusion</a>, en fait son objet.</p>
</div>
</div>
</details>
</div>
</details>

</div>
</details>

<p class="dp-epigraphe">— les livres —</p>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai I · 1854 / 1875</span><span class="dp-texte">Traité de logique générale et de logique formelle</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trois tomes, cinquante-quatre chapitres, quatre parties. Les trois autres Essais dépendent de ce socle, qui ne dépend d'aucun d'eux.</p>

<details class="dp-pli" data-rang="entrée">
<summary class="dp-titre"><span class="dp-rang">ch. I</span><span class="dp-texte">L'aveu du départ : « il faut tomber droit au milieu de la raison »</span></summary>
<div class="dp-corps">
<p>Le livre s'ouvre sur trois questions en six mots, qui contiennent tout le problème :</p>
<div class="dp-cite">
<p>Tout langage et toute science procèdent par composition et décomposition. Mais que composons-nous ainsi, que décomposons-nous ? Des <em>mots</em> ? des <em>idées</em> ? des <em>choses</em> ?</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<p>Vient aussitôt un aveu d'une franchise rare :</p>
<div class="dp-cite">
<p>[…] la critique de la connaissance se meut dans un cercle inévitable. Quelque vérité, quelque rapport que j'entreprenne d'expliquer, de prouver, je suis contraint de proposer d'autres rapports que je n'explique pas. Comment expliquer en effet ce que supposerait une première explication quelconque ? et que ne supposé-je point dès mes premières lignes ? Ou le <em>procès à l'infini</em>, qui est impossible, ou le <em>cercle</em> qu'on nomme <em>vicieux</em> : lisez les sceptiques.</p>
<p>Donc il faut tomber droit au milieu de la raison et s'y livrer.</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La part du lecteur</span>
<p>Au lieu de promettre des fondations, Renouvier déclare qu'il n'y en a pas, qu'il n'y en aura jamais, et qu'il commence néanmoins. Sa seule garantie est offerte au lecteur, non au système :</p>
</div>
<div class="dp-cite">
<p>Quel est mon but, après tout ? D'être compris, d'être approuvé. J'écris l'histoire de mes pensées pour que d'autres la vérifient par l'histoire conforme des leurs, en me lisant. […] Je serai justifié si mon lecteur la possède avec moi, comme moi.</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<p>La preuve est le lecteur lui-même, et il n'en est pas d'autre. D'où la difficulté du livre, qui lui demande de refaire le chemin, non de se laisser convaincre.</p>
<div class="dp-note">
<span class="dp-etiquette">Un avertissement à prendre au sérieux</span>
<p>« Mais c'est en vain qu'on s'efforcerait d'épargner au lecteur l'attention ou même le travail. Un vice de la philosophie, dans quelques livres, est une certaine <em>fausse lucidité</em>. Je ne connais pas de science qui soit claire en ce sens-là. » (préface de la première édition). Cette page vise la lucidité vraie, qui fait entrer sans dispenser du travail.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie I">
<summary class="dp-titre"><span class="dp-rang">ch. II-XV</span><span class="dp-texte">De la représentation en général</span></summary>
<div class="dp-corps">
<p class="dp-epigraphe">Les phénomènes sont les éléments de la connaissance</p>
<p>Quatorze chapitres ont pour seule fin d'établir qu'<strong>il n'y a pas de chose en soi</strong>, par un mouvement d'une extrême simplicité.</p>
<ul class="dp-liste">
<li><strong>II-III</strong> — Définir la représentation, le fait, le phénomène ; première analyse.</li>
<li><strong>IV-V</strong> — Le dedans et le dehors ; « la représentation n'implique rien que ses propres éléments ».</li>
<li><strong>VI-VII</strong> — La thèse selon laquelle il n'existe pas de chose en soi pour la connaissance, et les principes de la preuve.</li>
<li><strong>VIII à XIV</strong> — La preuve, refaite une fois par objet : l'espace <em>(VIII)</em>, le temps <em>(IX)</em>, la matière <em>(X)</em>, le mouvement <em>(XI)</em>, les représentés quelconques <em>(XII)</em>, les faits représentatifs <em>(XIII)</em>, la somme totale des phénomènes <em>(XIV)</em>.</li>
<li><strong>XV</strong> — Récapitulation : <em>le fétichisme en philosophie</em>.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le schéma de la preuve</span>
<p>Les quatre premiers chapitres de « preuve » (VIII-XI) ne forment pas quatre arguments, mais <strong>un seul argument, appliqué quatre fois</strong>, le pivot qui tourne :</p>
<p><em>Si X était en soi, X serait un continu en soi ; un continu en soi a un nombre infini de parties en soi ; un nombre infini est contradictoire ; donc X n'est pas en soi.</em></p>
<p>X remplacé par l'espace, le temps, la matière, le mouvement, on obtient les chapitres VIII à XI. Les ch. XII à XIV prouvent autrement, par l'analyse de la représentation. Une fois le schéma compris, les chapitres VIII à XI, qui répètent quatre fois la même démonstration, se lisent plus vite.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le mot « fétichisme »</span>
<p>Le chapitre XV est un réquisitoire, et son titre le dit. Un fétichiste adore un morceau de bois parce qu'il a pris le signe pour la chose ; le philosophe qui parle de <em>la</em> Substance, de <em>l'</em>Absolu, de <em>l'</em>Être substantifie de même un adjectif avant de s'agenouiller devant lui. Le reste du livre ne fera que démonter des fétiches.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie II">
<summary class="dp-titre"><span class="dp-rang">ch. XVI-XXV</span><span class="dp-texte">Revue élémentaire des phénomènes</span></summary>
<div class="dp-corps">
<p class="dp-epigraphe">Les lois des phénomènes sont les fins de la connaissance</p>
<p>Les deux épigraphes se répondent, la première partie donnant les <em>éléments</em> (la matière), celle-ci les <em>fins</em> (le but). Le programme entier de la connaissance tient entre ces deux lignes en capitales, que Renouvier a mises en tête de ses parties comme des enseignes.</p>
<p>Les dix chapitres forment une seule chaîne de définitions, qui descend jusqu'à renverser l'ontologie :</p>
<ul class="dp-liste">
<li><strong>XVI-XVII</strong> — Réalité et vérité ; composition des phénomènes ; <em>principe du relatif</em>.</li>
<li><strong>XVIII-XIX</strong> — Ce qu'est une loi : ordre objectif, puis ordre subjectif.</li>
<li><strong>XX</strong> — Sujet, attribut, fonction.</li>
<li><strong>XXI</strong> — L'être et les êtres. <em>C'est le chapitre où tombe la substance.</em></li>
<li><strong>XXII-XXIV</strong> — Les êtres matériels, puis vitaux, puis représentatifs.</li>
<li><strong>XXV</strong> — La science et les sciences.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La chaîne, en quatre maillons</span>
<p><strong>phénomène → loi → fonction → être.</strong></p>
<p>Un phénomène est ce qui est donné ; une loi, un phénomène complexe constamment impliqué dans d'autres ; une fonction, une loi où la variation des uns entraîne celle des autres. Et un être <em>est</em> une fonction.</p>
<p>Le dernier maillon, à lire lentement, signifie que rien n'est sous les choses. Ce que nous appelons <em>un être</em> est un endroit du monde où les rapports sont assez réguliers pour recevoir un nom.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">La méthode sans l'école</span>
<p>Dans la préface de la première édition, Renouvier accepte publiquement une formule positiviste, « la réduction de la connaissance aux lois des phénomènes », tout en refusant l'école, à laquelle il reproche de ne pas analyser ses propres notions premières, de nier dogmatiquement ce qu'on peut croire et d'avoir gardé de Saint-Simon des ambitions d'organisation « chimériques à mon gré, et peu libérales ». Le partage est net, qui retient la méthode et rejette l'Église positiviste.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie III">
<summary class="dp-titre"><span class="dp-rang">ch. XXVI-XL</span><span class="dp-texte">Analyse des lois fondamentales — Catégories — Logique</span></summary>
<div class="dp-corps">
<p>La plus longue partie du livre occupe la fin du tome I et tout le tome II. Dans cet atelier, la machine est montée pièce par pièce. Deux séries de chapitres s'y entrelacent, et les distinguer épargne beaucoup de fatigue.</p>
<ul class="dp-liste">
<li><strong>Les neuf catégories</strong> — XXVII <em>(relation)</em>, XXIX <em>(nombre)</em>, XXX <em>(position)</em>, XXXI <em>(succession)</em>, XXXIII <em>(qualité)</em>, XXXVI <em>(devenir)</em>, XXXVII <em>(causalité)</em>, XXXIX <em>(finalité)</em>, XL <em>(personnalité)</em>. Précédées de XXVI, qui les définit et les distribue.</li>
<li><strong>La logique formelle qui en découle</strong> — XXVIII <em>(contradiction, alternative)</em>, XXXII <em>(mesure, valeurs négatives, l'infini)</em>, XXXIV <em>(le syllogisme)</em>, XXXV <em>(absurde, disjonction, induction, démonstration)</em>, XXXVIII <em>(nécessaire, possible, probable)</em>.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens du titre</span>
<p>Le titre « Logique <em>générale</em> et logique <em>formelle</em> », d'apparence redondante, énonce un ordre de dérivation. La logique générale se confond avec les catégories, lois de la représentation ; la logique formelle (syllogisme, contradiction, induction), loin d'être un art de raisonner posé à côté, en <strong>sort</strong>, et de deux seulement. « La <em>logique</em> est renfermée tout entière dans les lois générales de la relation et de la qualité. » Renouvier fait ainsi descendre la logique de sa théorie des catégories, au lieu d'en faire une technique.</p>
</div>

<details class="dp-pli" data-rang="ch. XXXII">
<summary class="dp-titre"><span class="dp-rang">le chapitre</span><span class="dp-texte">XXXII — là où se fixe le pivot</span></summary>
<div class="dp-corps">
<p>Titre complet : <em>Mesure de la position par le nombre. Valeurs positives et négatives. — Mesure du continu par le nombre : les fractions, les incommensurables, les limites. — Question de l'infini.</em></p>
<p>Le plus technique du livre, ce chapitre en est aussi le plus important. Renouvier doit y sauver toute la mathématique (fractions, incommensurables, tangentes, quadratures, calcul différentiel) <strong>sans jamais admettre un infini en acte</strong>, tâche difficile à laquelle ses <em>Observations et développements</em> consacrent plus de soixante-dix pages (t. I, p. 376-448), sous deux titres :</p>
<ul class="dp-liste">
<li><em>A. De la théorie des valeurs négatives</em> — le sens du symbole négatif, les imaginaires, les exposants négatifs.</li>
<li><em>B. Théorie de l'indéfini et des limites</em> — la fraction, l'incommensurable, la géométrie élémentaire, les tangentes, les rectifications et quadratures, les principes du calcul de l'indéfini, et pour finir Auguste Comte et la philosophie des mathématiques.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">S'il ne faut lire qu'un chapitre technique</span>
<p>Celui-là s'impose. Renouvier prévient dans son avant-propos qu'il a retranché des formules « en faveur du lecteur non mathématicien », mais qu'il ne pouvait aller plus loin « sans nuire au caractère d'une doctrine dont l'idée pivotale » vient de là. Ce chapitre est donc le seul dont il refuse de dispenser le lecteur.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="partie IV">
<summary class="dp-titre"><span class="dp-rang">ch. XLI-LIV</span><span class="dp-texte">De la limite extrême de la connaissance</span></summary>
<div class="dp-corps">
<p class="dp-epigraphe">Une synthèse unique et totale des phénomènes est-elle possible ?</p>
<p>Cette partie occupe tout le tome III et forme le miroir de la partie III, dont les neuf catégories, reprises dans l'ordre, sont appliquées au monde entier et brisées une à une. <em>(Voir la table, plus haut, sous « limite extrême de la connaissance » ; et le double miroir sous « les quatre applications ».)</em></p>
<ul class="dp-liste">
<li><strong>XLI-XLII</strong> — Les antinomies : celles du système des catégories, puis les autres. Définition du monde. <em>Réfutation des antinomies kantiennes.</em></li>
<li><strong>XLIII à LIII</strong> — La synthèse totale, éprouvée catégorie par catégorie : nombre <em>(XLIII)</em>, étendue <em>(XLIV)</em>, durée <em>(XLV)</em>, division interne <em>(XLVI)</em>, vide et plein <em>(XLVII)</em>, espèce <em>(XLVIII)</em>, devenir <em>(XLIX)</em>, évolution <em>(L)</em>, cause <em>(LI)</em>, fin <em>(LII)</em>, conscience <em>(LIII)</em>.</li>
<li><strong>LIV</strong> — Des problèmes en deçà de la connaissance possible. Conclusion.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le dernier échec est le plus lourd</span>
<p>Le chapitre LIII demande s'il peut y avoir une conscience du monde entier, et Renouvier répond non pour une raison purement logique. La conscience étant la synthèse du soi et du non-soi, une conscience qui envelopperait tout, privée de non-soi, cesserait d'en être une.</p>
<p>Il en tire une conséquence dont il vivra. Puisqu'une conscience unique et totale est contradictoire, « l'hypothèse d'une <strong>pluralité primitive de consciences distinctes</strong>, dans le monde, semble donc la seule rationnelle », comme l'écrit le Formulaire en résumant ce chapitre (t. III, p. 289). Le monde n'a pas de sommet ; il a des personnes. Le personnalisme trouve ici l'une de ses sources et naît, à la fin d'un traité de logique, comme le résidu d'une impossibilité.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le pli de Renouvier">
<summary class="dp-titre"><span class="dp-rang">fin du tome III</span><span class="dp-texte">Formulaire du Traité de logique générale</span></summary>
<div class="dp-corps">
<p>Ces vingt-trois pages (t. III, p. 269-291) figurent à la fin du dernier tome, après la mention « FIN DU PREMIER ESSAI ». Renouvier y récrit son livre entier en propositions nues, sans preuves, sans exemples, sans polémique, et commence ainsi :</p>
<div class="dp-cite">
<p>Les définitions, principes et conclusions qui suivent sont acquis pour nous à la suite d'une analyse de raison pure, sous la réserve d'un examen à faire de la nature et de la valeur de notre certitude.</p>
<span class="dp-source">Formulaire, première phrase</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Renouvier avait déjà fait ce dépliant</span>
<p>Le <em>Formulaire</em> est le livre plié, qui contient tout et énonce sans rien démontrer. Il suit l'ordre du traité, et sa dernière section énumère les huit échecs de la synthèse totale, numérotés « 1° à l'égard de la relation… 2° à l'égard de la totalité… », dans l'ordre exact des chapitres XLII à LIII.</p>
<p>Ainsi, <strong>sa dernière section est le plan de la quatrième partie</strong>, et l'ensemble révèle l'architecture entière. Renouvier l'a placé à la fin, où on le cherche rarement. Cette page ne fait, au fond, que le remettre au début.</p>
</div>
<p>S'il ne fallait qu'un conseil de lecture, ce serait de lire le <em>Formulaire</em> en premier, puis le traité, soit vingt-trois pages avant plus de douze cents. Renouvier a écrit son propre résumé et l'a rangé derrière la porte de sortie.</p>
</div>
</details>
</div>
</details>


<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai II · 1859 / 1875</span><span class="dp-texte">Traité de psychologie rationnelle d'après les principes du criticisme</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trois tomes, vingt-cinq chapitres, trois parties. Ce livre, où l'outil tient cette fois, est la clef de voûte promise dès la troisième page du Premier Essai, et il aura fallu cinq ans pour la poser.</p>

<details class="dp-pli" data-rang="partie I">
<summary class="dp-titre"><span class="dp-rang">ch. I-XIII</span><span class="dp-texte">L'homme et ses fonctions constituantes</span></summary>
<div class="dp-corps">
<p>Des treize chapitres, le premier donne la méthode dans son titre, <em>De la nature humaine relativement aux catégories</em>. Renouvier part, non de l'observation de l'esprit, mais de ses neuf catégories, et demande, pour chacune, quelle fonction humaine lui correspond.</p>
<ul class="dp-liste">
<li><strong>I</strong> — De la nature humaine relativement aux catégories.</li>
<li><strong>II-III</strong> — L'homme physique et organique ; l'homme comme sensibilité.</li>
<li><strong>IV-V</strong> — L'homme comme intelligence ; puis la raison, les signes, le langage.</li>
<li><strong>VI</strong> — De la conscience en général et des méthodes psychologiques.</li>
<li><strong>VII-VIII</strong> — L'homme comme passion ; la passion, l'instinct, l'habitude.</li>
<li><strong>IX-X</strong> — L'homme comme volonté ; <em>lois de dégradation de la conscience réfléchie</em>.</li>
<li><strong>XI-XII</strong> — Les rapports des fonctions passionnelles et volontaires avec l'organisme ; ceux de la passion avec la conscience.</li>
<li><strong>XIII</strong> — <em>La liberté ; état de la question ; solution provisoire.</em></li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le poids du mot « provisoire »</span>
<p>La première partie s'arrête sur une « solution provisoire » du problème de la liberté, Renouvier venant de montrer qu'aucune preuve n'est possible et que l'analyse rend la liberté <em>probable</em>, sans plus. Aller plus loin suppose de savoir d'abord ce qu'est croire, d'où la deuxième partie, sur la certitude. La liberté ne sera tranchée qu'au chapitre XVII, par un acte et non par un argument ; le chapitre XXII n'en résumera que les motifs.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le vertige</span>
<p>Les chapitres X à XII traitent du <em>vertige</em>, nom que Renouvier donne aux états où la conscience réfléchie se dégrade, où l'on fait ce qu'on ne veut pas, où la liberté s'efface sans qu'on ait cessé d'être conscient. Le Quatrième Essai renverra à cette contribution, la plus originale de Renouvier à la psychologie, pour excuser une part du mal historique. Il est rare qu'un philosophe de la liberté consacre trois chapitres aux moments où elle fait défaut.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie II">
<summary class="dp-titre"><span class="dp-rang">ch. XIV-XIX</span><span class="dp-texte">La certitude</span></summary>
<div class="dp-corps">
<p>Les six chapitres abordent enfin la question que Descartes mettait en premier, au quatorzième chapitre du Deuxième Essai, après les cinquante-quatre du Premier.</p>
<ul class="dp-liste">
<li><strong>XIV</strong> — Définition générale de la certitude dans une conscience. <em>(Ses Observations publient Jules Lequier.)</em></li>
<li><strong>XV</strong> — De quelques théories célèbres de la certitude.</li>
<li><strong>XVI</strong> — Du premier ordre de la certitude. — L'être de la conscience. L'être du monde.</li>
<li><strong>XVII</strong> — Du second ordre de la certitude. — La liberté eu égard à l'erreur et à la vérité. La raison pratique.</li>
<li><strong>XVIII</strong> — De la certitude des sciences et de leur classification rationnelle.</li>
<li><strong>XIX</strong> — Complément de la définition de la certitude. <em>Du contrat personnel et du contrat social.</em></li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Deux ordres de certitude, et une bascule entre les deux</span>
<p>Le <strong>premier ordre</strong> (ch. XVI) comprend ce qu'on ne peut pas ne pas affirmer, l'être de la conscience et celui du monde ; le <strong>second ordre</strong> (ch. XVII), tout le reste, qui dépend de la liberté, puisqu'y affirmer, c'est vouloir affirmer. D'où la phrase qui fait tourner le livre, « Le principe de ces principes est la liberté. »</p>
<p>Au second ordre, il n'est donc pas de certitude sans une volonté qui affirme. Sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>, ce joint est le premier des deux soulignés doubles. Comme il y a plusieurs personnes, la vérité passe par un accord, ce qui explique qu'un traité de psychologie finisse sur le <em>contrat social</em>.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie III">
<summary class="dp-titre"><span class="dp-rang">ch. XX-XXV</span><span class="dp-texte">Les probabilités touchant l'ordre moral du monde. L'immortalité, la liberté, la divinité</span></summary>
<div class="dp-corps">
<p>Le titre suffit à situer la manœuvre, qui reprend un par un les trois postulats de la raison pratique de Kant (liberté, immortalité, Dieu). Renouvier les traite cependant en <strong>probabilités morales</strong>, sans renoncer au mot de postulat, et consacre un chapitre entier à examiner les thèses de Kant.</p>
<ul class="dp-liste">
<li><strong>XX</strong> — De l'immortalité comme loi téléologique de la nature.</li>
<li><strong>XXI</strong> — <em>Examen des thèses de la raison pratique de Kant.</em></li>
<li><strong>XXII</strong> — De la liberté et de la destinée immortelle de l'homme.</li>
<li><strong>XXIII</strong> — De la croyance la plus large en la divinité.</li>
<li><strong>XXIV</strong> — Des moyens physiques de l'immortalité.</li>
<li><strong>XXV</strong> — Des hypothèses rationnelles sur la nature de Dieu.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Les dernières conséquences du pivot</span>
<p>Un Dieu infini en acte étant contradictoire, il ne reste qu'un Dieu <em>fini</em>, une personne à qui manquent les « perfections » de la métaphysique, mais à qui restent la justice et la bonté. Si Dieu est une personne parmi d'autres, rien ne prouve plus qu'il soit un seul, et Renouvier écrit noir sur blanc que « deux directions de l'esprit sont possibles, légitimes », l'unité et la pluralité.</p>
<p>Suivie depuis le début, la ligne montre qu'une thèse sur le nombre, en 1854, aboutit en 1875 à rendre le polythéisme rationnellement recevable. La même déduction court sur vingt et un ans et six tomes.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le pli de Renouvier">
<summary class="dp-titre"><span class="dp-rang">fin du tome III</span><span class="dp-texte">Formulaire du Traité de Psychologie rationnelle</span></summary>
<div class="dp-corps">
<p>Second grand pli de l'œuvre, ce formulaire est le plus utile de tous, parce qu'il est structuré. Ses quatre sections suivent l'ordre des trois parties du livre :</p>
<ul class="dp-liste">
<li><strong>A. L'analyse des fonctions humaines</strong> — les neuf catégories, chacune avec sa fonction : Relation → Comparaison ; Position → Imagination ; Succession → Mémoire ; … Personnalité → <em>Liberté</em>.</li>
<li><strong>B. La question de la certitude</strong> — les deux ordres, et la liberté comme principe des principes.</li>
<li><strong>C. La classification des sciences</strong> — avec un tableau qui range toute la connaissance sous les catégories, la logique et les mathématiques d'un côté (qualité, nombre), les sciences physiques de l'autre.</li>
<li><strong>D. Les probabilités morales</strong> — immortalité, liberté, divinité.</li>
</ul>
<div class="dp-cite">
<p>L'homme est une fonction particulière de toutes les fonctions données dans le monde, et qui tombent sous la connaissance : toutes les catégories sont impliquées dans la représentation de l'homme pour l'homme, aussi bien que dans la représentation du monde pour l'homme.</p>
<span class="dp-source">Formulaire du Traité de Psychologie rationnelle, première phrase</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">La même définition qu'au pli « lois »</span>
<p>« Un être est une fonction », disait le Formulaire du Premier Essai ; « L'homme est une fonction particulière », dit celui du Deuxième. La reprise, qui n'est pas affaire de style, applique la définition générale au cas de l'homme, et la suite de la phrase donne le programme du double miroir, les mêmes catégories pour l'homme et pour le monde.</p>
</div>
<p class="dp-chapo">Ce formulaire, qui ouvre aussi le Troisième Essai, existe ainsi à deux endroits de l'œuvre et en trois états (1864, 1875, 1892).</p>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai III · 1864 / 1892</span><span class="dp-texte">Les Principes de la nature</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Deux tomes, douze chapitres seulement, mais précédés de cent pages d'introduction qui sont le formulaire du livre précédent. Le plus court des Essais est aussi le plus singulier.</p>

<details class="dp-pli" data-rang="entrée">
<summary class="dp-titre"><span class="dp-rang">ch. I</span><span class="dp-texte">« Je m'arrête enfin […] au seuil même de l'histoire »</span></summary>
<div class="dp-corps">
<p>Le chapitre s'intitule <em>Résumé. Plan.</em> et fait exactement cela, récapitulant les deux Essais précédents avant de tracer le trajet du troisième. C'est l'endroit de l'œuvre où l'on comprend le mieux, d'un coup, pourquoi elle compte quatre livres.</p>
<div class="dp-cite">
<p>Ainsi, dans le <em>Premier Essai</em>, l'étude des principes de la raison pure et l'établissement des lois générales, ou catégories, aboutissaient à la reconnaissance des limites du savoir ; dans le <em>Deuxième Essai</em>, l'analyse des fonctions humaines a conclu à la croyance morale et aux fondements d'une raison pratique sérieuse […]. A la fin du premier se marquait le besoin de descendre des thèses les plus abstraites et des extrémités de la spéculation universelle à un sujet concret : l'Homme ; en terminant le deuxième, je me suis trouvé, d'un côté, à l'entrée de la morale, de l'autre, sur la limite des religions, et j'ai senti la nécessité de donner une matière nouvelle à l'analyse : l'histoire.</p>
<span class="dp-source">Troisième Essai, ch. I — Résumé. Plan.</span>
</div>
<p>Il expose ensuite le plan du présent volume, dont la dernière phrase est une porte :</p>
<div class="dp-cite">
<p>Je commence par traiter du fond et des modes premiers et universels de l'existence physique, en suivant la méthode exposée dans les <em>Essais</em> précédents. […] Je passe aux hypothèses cosmogoniques et au problème des espèces. […] Je m'arrête enfin en amenant l'homme sur la scène, c'est-à-dire au seuil même de l'histoire.</p>
<span class="dp-source">Troisième Essai, ch. I</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La descente</span>
<p>Les quatre Essais descendent continûment de l'abstrait au concret, des catégories à l'homme, à la nature, puis à l'histoire. Chaque livre finit là où le suivant commence, et Renouvier le dit chaque fois. Ils forment un seul mouvement en quatre paliers, publié en dix ans (1854-1864), et non une série d'ouvrages sur des sujets voisins.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="ch. II-VII">
<summary class="dp-titre"><span class="dp-rang">la nature</span><span class="dp-texte">L'être, l'atome, la matière, la vie</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>II</strong> — La nature de l'être sous l'aspect le plus général.</li>
<li><strong>III</strong> — Suite. — L'être physique. <em>L'atomisme.</em></li>
<li><strong>IV</strong> — Suite. — Vue générale du fond de la nature.</li>
<li><strong>V</strong> — Conjectures sur le fond des lois naturelles. — Physique spéciale.</li>
<li><strong>VI</strong> — Suite. — Phénomènes chimiques.</li>
<li><strong>VII</strong> — Suite. — Phénomènes biologiques.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La même machine, un degré plus bas</span>
<p>La section C du formulaire précédent avait rangé les sciences sous les catégories. Ces chapitres accomplissent ce travail. Les fonctions <em>mécaniques</em> n'impliquent que Nombre, Position, Succession et Devenir ; les <em>chimiques et physiques</em> y ajoutent la Qualité ; les <em>biologiques</em> apportent enfin la Causalité, la Finalité et la conscience.</p>
<p>Les neuf pièces dressent ainsi une échelle des êtres, chaque étage de la nature se définissant par le nombre de catégories requises pour le décrire. Un pur mouvement en demande quatre, outre la relation, présente partout ; un caillou, corps physique et chimique, y ajoute la qualité ; un vivant les demande toutes.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le sort de l'atome</span>
<p>L'atome change de sens. Renouvier rejette l'atome entendu comme « une espèce d'étendue concrétée », substrat indivisible où reviendraient le continu et l'infini, mais garde le mot pour les éléments derniers de la nature, en nombre fini (« Nommons-les librement des atomes, puisque nous avons écarté l'interprétation vicieuse de ce mot », t. I, ch. III, p. 30). Le pivot ne supprime pas l'atome ; il en exige un, bien entendu.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="ch. VIII-XII">
<summary class="dp-titre"><span class="dp-rang">les origines</span><span class="dp-texte">Darwin, les espèces, et une cosmogonie singulière</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>VIII</strong> — Critique des doctrines cosmogoniques physiques.</li>
<li><strong>IX</strong> — Suite. — <em>Question des espèces.</em></li>
<li><strong>X</strong> — Critique des systèmes de cosmogonie morale.</li>
<li><strong>XI</strong> — L'origine de l'homme.</li>
<li><strong>XII</strong> — Les origines premières et morales.</li>
</ul>
<p>Renouvier discute Darwin dans le texte, et sans mépris, ce qui est rare chez lui :</p>
<div class="dp-cite">
<p>On remarque dans la doctrine de Darwin, au moins avant qu'il eût été gagné à l'entraînement de ses disciples, cet heureux mélange de la spéculation libre avec les faits respectés et inaltérés, cet usage de l'induction à la fois mesurée et hardie […].</p>
<span class="dp-source">Troisième Essai, ch. IX</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le chapitre le plus singulier de l'œuvre</span>
<p>Dans la seconde édition (1892), au chapitre XII, Renouvier avance une hypothèse d'une grande audace, qu'il résume dans l'avant-propos de l'appendice B (t. II, p. 343). L'humanité et la nature auraient été créées à l'état d'« organisme universel et réellement parfait, laissant aux individus la liberté » ; cette liberté aurait causé la perversion de la société primitive, d'où « la ruine entière du monde, d'où la nature actuelle serait sortie en traversant la période occupée par la formation des nébuleuses et par la constitution des astres ».</p>
<p>La nébuleuse primitive de Laplace, les étoiles, les planètes, la mort, la lutte pour la vie seraient ainsi le <em>débris</em> d'une chute morale. Le cosmos est alors le résultat du drame, non son décor.</p>
<p>Renouvier, qui n'était pas homme à reculer, recule, et avoue que « chez moi, la haute conjecture s'arrête, intimidée ».</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Ce qui l'y contraint</span>
<p>Ni accès de mysticisme ni déduction, cette « haute conjecture », selon le mot de Renouvier, s'accorde pourtant avec ses thèses. Si tout nombre est fini, le monde a commencé ; s'il a commencé, il y a des causes premières ; et si, comme il le tient depuis 1886, ces causes remontent à un Dieu créateur et juste, la cause première du mal ne peut être Dieu. Il faut donc une liberté première, et une faute. La cosmogonie de 1892 est la plus cohérente avec l'interdit de l'infini <em>et</em> le refus de faire de Dieu l'auteur du mal.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai IV · 1864</span><span class="dp-texte">Introduction à la philosophie analytique de l'histoire</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trente-deux paragraphes, cinq parties. Seul des quatre Essais où l'on croise des dieux égyptiens, des tribus polynésiennes et des tablettes assyriennes, ce livre emploie pourtant le même outil que le premier.</p>

<details class="dp-pli" data-rang="§ I">
<summary class="dp-titre"><span class="dp-rang">le plan</span><span class="dp-texte">Ce que « analytique » interdit</span></summary>
<div class="dp-corps">
<p>Renouvier présente sa méthode par ses refus, dont la liste est la table des matières réelle :</p>
<div class="dp-cite">
<p>Abordée sans critique, l'histoire ne peut que multiplier, en les amplifiant, ces mêmes phénomènes incohérents que donne déjà l'expérience individuelle toute seule quand la loi morale ne règle pas la conduite et le jugement. Traitée dans un système apriorique, elle défigure les faits, ou elle les dédaigne ; elle en rejette et elle en interpole, afin de disposer plus commodément les autres en série.</p>
<span class="dp-source">Quatrième Essai, § I</span>
</div>
<p>On manque donc l'histoire de deux façons, sans critique ou avec un système fixé d'avance. Entre les deux passe la voie étroite de ce qu'il appelle l'analyse, qui s'en tient aux faits établis par les sciences historiques et aux inductions tirées de ce que la personne humaine a de constant.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Un livre qui suppose les trois autres</span>
<p>Ce livre est illisible seul. La quatrième partie du <strong>Premier Essai</strong> a démontré que la synthèse totale est impossible. Or une philosophie de l'histoire au sens de Hegel <em>est</em> une synthèse totale, donc interdite avant même d'être examinée sur pièces. Le <strong>Deuxième</strong> a fourni la seule chose qui reste pour juger, une personne libre, avec ses passions, sa mémoire et son vertige. Les renvois à cet Essai sont constants (§ V pour le langage, § XI et XII pour le vertige, § XXV pour Dieu, selon la numérotation du Deuxième Essai de 1859). Enfin, le <strong>Troisième</strong> a déposé l'homme au seuil.</p>
<p>Le Quatrième Essai est ce qui reste de la philosophie de l'histoire une fois retiré le droit de conclure sur le tout, soit des faits, des lois partielles et une conscience pour juger.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="I-V">
<summary class="dp-titre"><span class="dp-rang">le mouvement</span><span class="dp-texte">Les cinq parties</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>I. Les origines</strong> <em>(§ II-IX)</em> — Les commencements de l'humanité examinés à partir de la théorie de Kant, puis contre elle. Origine historique des vertus et des vices. Solidarité du bien et du mal. C'est la partie théorique, consacrée au problème du mal et du « premier manquement ».</li>
<li><strong>II. Les religions les plus basses, puis la Chine et l'Égypte</strong> <em>(§ X-XVII)</em> — Les lois de la critique appliquées aux religions ; le sentiment religieux dans l'état moral le plus bas ; religions de tribus ; origines chinoises ; religion patriarcale des Chinois et des Japonais ; religions locales de l'Égypte.</li>
<li><strong>III. Les Aryens</strong> <em>(§ XVIII-XXVI)</em> — L'esprit mythologique ; mythes et culte de l'Arye primitive ; anthropomorphisme et panthéisme ; origines helléniques ; l'esprit des races italiques ; la <em>Religio</em> des Romains ; Germains, Celtes.</li>
<li><strong>IV. Les Sémites</strong> <em>(§ XXVII-XXXI)</em> — Origines sémitiques, la partie la plus longue et la plus disputée.</li>
<li><strong>V. La reprise</strong> <em>(§ XXXII)</em> — Où Renouvier dit ce qu'il a fait, et pourquoi tant de faits dans un livre de philosophie.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Les raisons de cette érudition</span>
<p>Renouvier s'en explique lui-même à la fin. Les savants « manquent communément de philosophie », et les philosophes ignorent les résultats des savants. Il fallait donc quelqu'un pour tenir les deux bouts. « C'est à d'autres qu'eux-mêmes qu'il est donné de mettre leurs découvertes en place et de les utiliser. » Le Quatrième Essai tente ce travail en 1864, quand l'assyriologie et la mythologie comparée sortent à peine de terre.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le coup">
<summary class="dp-titre"><span class="dp-rang">§ XXXII</span><span class="dp-texte">Les sphères de Ptolémée</span></summary>
<div class="dp-corps">
<p>Le jugement le plus dur et le plus juste que Renouvier ait porté sur ses rivaux tient en une image, qu'il faut lire jusqu'au bout, car la pointe est à la fin :</p>
<div class="dp-cite">
<p>Hegel et Comte, aussi bien que Bossuet et Vico, traitent l'histoire comme Eudoxe et Ptolémée traitaient l'astronomie, avec leurs sphères idéales. Mais ces derniers satisfaisaient aux mouvements des corps célestes, tels qu'ils les constataient ; leurs théories permettaient la prévision dans une suffisante mesure, tandis que les philosophes écrivent leurs <em>équations</em> historiques en sacrifiant les faits […].</p>
<span class="dp-source">Quatrième Essai, § XXXII</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens de la pointe</span>
<p>Ptolémée se trompait, mais ses sphères fonctionnaient, puisqu'elles prédisaient les éclipses ; Hegel et Comte ont les sphères sans les prédictions. Ils sont donc <em>en dessous</em> de Ptolémée. La comparaison, loin de les reléguer parmi les anciens, leur refuse jusqu'au statut de mauvaise science.</p>
</div>
</div>
</details>
</div>
</details>


<div class="dp-legende">
<span><span class="dp-puce"></span> pli jamais ouvert</span>
<span><span class="dp-puce dp-puce--vue"></span> pli déjà ouvert</span>
<span>texte en sérif = Renouvier</span>
<span>texte en linéale = commentaire</span>
</div>
</div>

<script>
(function () {
  var racine = document.getElementById("dp");
  if (!racine) return;
  var plis = Array.prototype.slice.call(racine.querySelectorAll("details.dp-pli"));
  var compteur = document.getElementById("dp-compteur");

  function majCompteur() {
    if (!compteur) return;
    var ouverts = plis.filter(function (p) { return p.open; }).length;
    var vus = plis.filter(function (p) { return p.classList.contains("dp-vu"); }).length;
    var reste = plis.length - vus;
    compteur.textContent = ouverts + (ouverts > 1 ? " plis ouverts sur " : " pli ouvert sur ")
      + plis.length + " · " + reste + (reste > 1 ? " jamais ouverts" : " jamais ouvert");
  }

  plis.forEach(function (pli) {
    pli.addEventListener("toggle", function () {
      if (pli.open) pli.classList.add("dp-vu");
      majCompteur();
    });
  });

  racine.addEventListener("click", function (e) {
    var b = e.target.closest("[data-dp]");
    if (!b) return;
    var action = b.getAttribute("data-dp");
    if (action === "tout") {
      plis.forEach(function (p) { p.open = true; p.classList.add("dp-vu"); });
    } else if (action === "rien") {
      plis.forEach(function (p) { p.open = false; });
    } else if (action === "neufs") {
      var cible = plis.filter(function (p) { return !p.classList.contains("dp-vu"); })[0];
      if (!cible) return;
      var parent = cible.parentElement;
      while (parent && parent !== racine) {
        if (parent.tagName === "DETAILS") parent.open = true;
        parent = parent.parentElement;
      }
      cible.scrollIntoView({ behavior: "smooth", block: "center" });
      var t = cible.querySelector("summary");
      if (t) t.focus({ preventScroll: true });
    }
    majCompteur();
  });

  majCompteur();
})();
</script>

---

## Note de méthode

Ce dépliant obéit à six règles, notées ici pour que le lecteur sache à quoi il a affaire et que d'autres livres puissent être pliés de la même façon.

1. **Le pli conserve tout.** Déplier n'est pas résumer, mais ajouter de la résolution. Le sommet est la compression maximale, le fond le texte même. Rien n'est perdu en route, rien n'est ajouté qui ne soit vérifiable.
2. **Les sœurs restent.** Ouvrir une voie n'en referme aucune autre. Les chemins non pris demeurent visibles, repliés, à côté du chemin pris, et tiennent lieu de sommaire.
3. **La profondeur se voit.** Chaque niveau ajoute un filet à gauche, et l'on compte les filets comme les plis d'un papier ouvert.
4. **Le parcours se souvient.** Un pli jamais ouvert porte une pastille pleine, qui se creuse une fois le pli ouvert ; le compteur indique combien de plis restent inexplorés. Ce dispositif répond au seul problème sérieux du format, celui de savoir, une fois au fond, ce qu'on n'a pas vu.
5. **La typographie dit qui parle.** Le sérif signale Renouvier, cité verbatim avec sa référence ; la linéale, le commentaire. Aucun mot n'est prêté à Renouvier qu'il n'ait écrit.
6. **Les paliers sont de l'auteur quand ils existent.** Renouvier a résumé lui-même ses deux premiers Essais dans un *Formulaire*. Partout où c'était possible, le niveau intermédiaire est le sien, cité, et non une paraphrase.

**Ce qui reste à déplier.** Les *Observations et développements* de la seconde édition, ajouts de 1875, n'ont été ouverts qu'en passant (Premier Essai, ch. XXXII ; Deuxième Essai, ch. XIII et XIV). Renouvier, qui n'introduit dans son texte « aucun changement de quelque importance dans l'esprit ni dans les preuves ou les conclusions », y joint « des explications et des critiques relatives pour la plupart à l'état actuel de la philosophie ou des systèmes » (avant-propos, t. I, p. VI). Ces pages discutent Mill, Hamilton, Spencer, Comte, et publient Lequier, sans toucher à la charpente ; elles feront un étage supplémentaire.

**Sources.** Premier Essai : *Traité de logique générale et de logique formelle*, 2ᵉ éd., Au Bureau de la Critique philosophique, 1875, 3 t. — Deuxième Essai : *Traité de psychologie rationnelle d'après les principes du criticisme*, 2ᵉ éd. revue et considérablement augmentée, même éditeur, 1875, 3 t. — Troisième Essai : *Les Principes de la nature*, 2ᵉ éd. corrigée et augmentée, 1892, 2 t. — Quatrième Essai : *Introduction à la philosophie analytique de l'histoire*, Ladrange, 1864.
