---
title: "Compliquer les Essais pour les expliquer"
description: "Les quatre Essais de critique générale de Charles Renouvier, dépliés."
---

# Compliquer les Essais pour les expliquer

*Ex-pliquer*, c'est déplier. *Com-pliquer*, c'est plier ensemble. On n'explique jamais un livre : on le déplie — et pour le déplier, il faut d'abord admettre qu'il a été plié.

Cette page est un dépliant. Fermée, elle tient en trois mots. Chaque terme s'ouvre sur ce qu'il contient ; ce qu'il contient s'ouvre encore. **Rien ne disparaît quand vous ouvrez** : les voies que vous n'avez pas prises restent là, repliées, à côté de celle que vous avez prise. Tout ouvert, vous avez les quatre Essais.

Une précision, qui est aussi une découverte : **Renouvier avait commencé ce travail.** Il a résumé chacun de ses Essais dans un texte qu'il appelait un *Formulaire*, et il a placé ces formulaires aux charnières de l'œuvre — à la fin d'un Essai, en tête du suivant. Les paliers intermédiaires de ce dépliant ne sont donc pas inventés : ils sont de sa main.

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

<p class="dp-chapo">Charles Renouvier — <em>Essais de critique générale</em>, 1854-1864 ; seconde édition, 1875-1892.</p>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">Essais</span></summary>
<div class="dp-corps">
<p>Le mot n'est pas de la modestie. Un <em>essai</em>, ici, c'est un examen qui ne connaît pas son résultat d'avance — l'exact contraire d'un <em>système</em>. Renouvier passera sa vie à reprocher à Hegel et à Comte d'avoir su la fin avant d'avoir commencé — et l'image qui règle leur compte, celle des sphères de Ptolémée, attend au bout de cette page, dans le dernier pli du Quatrième Essai.</p>
<p>Quatre essais, donc : quatre examens, sur quatre objets, avec un seul outil. Cet outil a neuf pièces, il est monté dans le premier livre, et il ne changera plus jamais.</p>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">de critique</span></summary>
<div class="dp-corps">
<p>Le mot vient de Kant, et Renouvier ne s'en cache pas une seconde :</p>
<div class="dp-cite">
<p>J'avoue donc nettement que je continue Kant ; et, comme une ambition est bonne et nécessaire chez quiconque ose proposer ses pensées au public, la mienne serait de poursuivre sérieusement en France l'œuvre de la critique, manquée en Allemagne.</p>
<span class="dp-source">Premier Essai, préface de la première édition</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">En clair</span>
<p><em>Critique</em> ne veut pas dire dénigrer. Cela veut dire : avant de dire ce qu'est le monde, examiner de quel droit on en parle. La critique n'est pas une doctrine du monde, c'est l'inventaire des titres de créance de la raison.</p>
</div>
<p>Reste ce « manquée en Allemagne », qui est une déclaration de guerre polie. Renouvier tient que Kant a ouvert le bon chantier et l'a mal fermé — et il passera quarante ans à le fermer autrement.</p>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">générale</span></summary>
<div class="dp-corps">
<p>Kant avait écrit trois <em>Critiques</em> séparées : la raison pure, la raison pratique, le jugement. Renouvier n'en veut qu'une, mais qui aille partout. Quatre terrains, une seule méthode :</p>
<ul class="dp-liste">
<li><strong>La connaissance</strong> — que puis-je savoir, et jusqu'où ? <em>(Premier Essai)</em></li>
<li><strong>L'homme</strong> — qui sait ? suis-je libre ? de quel droit suis-je certain ? <em>(Deuxième Essai)</em></li>
<li><strong>La nature</strong> — que sont la matière, la vie, l'espèce, l'origine ? <em>(Troisième Essai)</em></li>
<li><strong>L'histoire</strong> — que fait l'humanité de sa propre expérience ? <em>(Quatrième Essai)</em></li>
</ul>
<p>C'est tout ce que « générale » veut dire — et c'est énorme : rien n'y échappe, ni la géométrie, ni les passions, ni Darwin, ni les religions de l'Égypte.</p>
</div>
</details>

<p class="dp-epigraphe">— le livre en une phrase —</p>
<p class="dp-these">Un outil à neuf pièces, appliqué quatre fois. Sur le monde entier, il échoue neuf fois : c'est la limite de la science. Sur l'homme, il réussit neuf fois, et la neuvième s'appelle la liberté.</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">↓ déplier</span><span class="dp-texte">Le livre en un paragraphe</span></summary>
<div class="dp-corps">
<p>Renouvier part d'une impossibilité qu'il tient pour démontrée : <strong>le nombre ne peut pas être infini</strong>. Il en tire que rien ne nous est donné <em>en soi</em> : les choses ne nous sont données qu'en <strong>représentation</strong>, et ce qu'il y a à connaître en elles, ce sont leurs liaisons constantes — des <strong>lois</strong>. Ces lois se ramènent à <strong>neuf relations irréductibles</strong>, les catégories, toutes bâties sur le même modèle : deux termes contraires, et leur synthèse. Ces neuf pièces sont le seul outil de toute l'œuvre, et <strong>les quatre Essais en sont les quatre applications</strong>. Appliqué au monde pris comme un tout, l'outil casse — neuf fois, une fois par catégorie : c'est la <strong>limite extrême de la connaissance</strong>. Appliqué à l'homme, il tient — neuf fois, et la neuvième catégorie, la personnalité, donne la <strong>liberté</strong>. Une science qui s'arrête, une liberté qui commence : le champ demeuré libre est celui de la <strong>croyance</strong>, donc d'une morale, donc d'une <strong>histoire sans sens de l'Histoire</strong>. Et d'un Essai à l'autre, aux charnières, Renouvier a glissé un <strong>formulaire</strong> qui replie le précédent.</p>
<p class="dp-chapo">Chacun des neuf termes en gras s'ouvre ci-dessous. Vous pouvez vous arrêter ici : ce paragraphe est vrai. Vous pouvez aussi tirer sur un fil.</p>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le pivot</span><span class="dp-texte">le nombre ne peut pas être infini</span></summary>
<div class="dp-corps">
<p>C'est Renouvier lui-même qui emploie le mot, et il le met entre guillemets comme s'il en mesurait le poids :</p>
<div class="dp-cite">
<p>[…] une doctrine dont l'idée « pivotale » a procédé chez moi d'une méditation prolongée sur le sens, et sur la seule justification rationnelle possible des méthodes transcendantes en géométrie.</p>
<span class="dp-source">Premier Essai, avant-propos de la seconde édition</span>
</div>
<p>Traduction : tout ce système est né d'un problème de mathématiques. Voici la thèse, dans les termes du <em>Formulaire</em> par lequel Renouvier résume lui-même son premier livre :</p>
<div class="dp-cite">
<p>L'espace, le temps, la matière, le mouvement, s'ils étaient en soi, impliqueraient le continu en soi, et par suite un nombre infini de parties en soi de ce continu, ce qui est absurde, parce que l'infini et le nombre sont contradictoires entre eux.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">l'argument</span><span class="dp-texte">Pourquoi « l'infini et le nombre sont contradictoires »</span></summary>
<div class="dp-corps">
<p>L'argument tient en trois pas, et il ne suppose aucune mathématique.</p>
<ul class="dp-liste">
<li>Un <strong>nombre</strong>, c'est un <em>tout</em> : la synthèse de l'un et du multiple. Dire « il y en a sept », c'est avoir fini de compter.</li>
<li>Un <strong>infini</strong>, c'est ce dont on n'a jamais fini.</li>
<li>Donc un « nombre infini », c'est un tout qu'on ne peut pas achever : un tout qui n'est pas un tout. Ce n'est pas une chose difficile à concevoir — c'est une chose qui ne veut rien dire.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Attention au contresens</span>
<p>Renouvier ne dit pas qu'on ne peut pas <em>imaginer</em> l'infini, ni qu'il faut cesser de faire des mathématiques. Il vise une chose précise : l'infini <strong>donné en acte</strong>, achevé, réellement là. Il maintient l'autre infini, qu'il appelle l'<strong>indéfini</strong> : on peut toujours ajouter un, toujours diviser encore. Ce qu'on ne peut pas, c'est <em>avoir ajouté</em> une infinité de fois.</p>
<p>Toute la différence est entre <em>on peut toujours</em> (vrai) et <em>c'est déjà fait</em> (contradictoire).</p>
</div>
<p>Renouvier consacre un chapitre entier et une centaine de pages d'observations à refonder là-dessus la fraction, l'incommensurable, la limite, les tangentes, les quadratures — c'est-à-dire le calcul infinitésimal — sans jamais admettre un infini en acte. C'est le prix à payer, et il le paie <em>(Premier Essai, ch. XXXII)</em>.</p>
</div>
<p class="dp-renvoi">Ce raisonnement — deux définitions, un choc — est démonté jeton par jeton sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">l'enjeu</span><span class="dp-texte">Ce qu'une querelle de mathématiciens vient faire dans une morale</span></summary>
<div class="dp-corps">
<p>C'est ici que le pivot pivote. Suivez la chaîne :</p>
<ul class="dp-liste">
<li>Si le nombre est fini, une série effective de choses passées ne peut pas être infinie.</li>
<li>Donc le monde a commencé, et la série des causes s'arrête : il y a des <strong>causes premières</strong>.</li>
<li>Une cause première n'est pas causée — sans quoi elle ne serait pas première.</li>
<li>Donc quelque chose peut commencer sans être déterminé par ce qui précède.</li>
<li>Donc le <strong>libre arbitre</strong> n'est pas une absurdité logique. Il devient possible ; restera à décider s'il est réel — ce sera l'affaire du Deuxième Essai, et il faudra trois cents pages.</li>
</ul>
<p>Tout le personnalisme de Renouvier — la liberté, la morale, la République, la critique des religions — pend à ce fil, et le fil est une thèse sur le nombre. Voilà pourquoi il ne cède pas d'un pouce là-dessus, et pourquoi ses adversaires ont toujours attaqué à cet endroit.</p>
<div class="dp-note">
<span class="dp-etiquette">Le rapport de force</span>
<p>Renouvier écrit avant Cantor. La théorie des ensembles donnera plus tard un sens mathématique cohérent à l'infini actuel, et l'on a souvent cru que cela réglait son compte à Renouvier. Ce n'est pas si simple : sa thèse ne porte pas sur ce qu'on peut définir sans contradiction dans une théorie, mais sur ce qui peut être <em>donné</em>, réellement, dans une série de phénomènes. Le débat n'est pas clos — il a seulement changé de camp.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">représentation</span></summary>
<div class="dp-corps">
<p>Faux ami numéro un. « Représentation » ne désigne pas ici une image dans une tête. C'est le nom de la relation elle-même, dont le sujet et l'objet sont les deux faces.</p>
<div class="dp-cite">
<p>Les choses sont données à la connaissance, en qualité de <em>représentations</em>. Les choses comme représentations sont dites <em>phénomènes</em>. Toute représentation implique deux éléments : l'objectif, le subjectif, lesquels se trouvent encore dans chacun d'eux distingué de l'autre.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le renversement</span>
<p>On croit lire : « il y a un moi, qui se représente des objets ». C'est l'inverse. Il y a de la représentation ; le « moi » et « le monde » en sont les deux versants, et le moi n'a aucun privilège :</p>
</div>
<div class="dp-cite">
<p>La chose appelée <em>moi</em>, aussi bien que tout autre objet de la connaissance, est donnée à la connaissance en une représentation, sous laquelle se groupent des phénomènes diversement composables et décomposables.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Piège de vocabulaire</span>
<p>Renouvier prévient lui-même en note : ses mots <em>objectif</em> et <em>subjectif</em> sont pris « dans un sens tout opposé à l'usage vulgaire ». Chez lui, ce sont les deux éléments internes de toute représentation, pas deux mondes. Si vous lisez avec le lexique kantien en tête, vous ne comprendrez rien — c'est le premier obstacle du livre, et il est purement lexical.</p>
</div>
<p>De là vient l'énoncé qui commande tout le reste : <strong>il n'y a pas de chose en soi</strong>. Non par décret, mais par le pivot : une chose en soi serait un continu en soi, donc un nombre infini de parties en soi. Renouvier refait cette démonstration quatre fois de suite — pour l'espace, le temps, la matière, le mouvement <em>(ch. VIII à XI)</em>. C'est le même argument qui tourne quatre fois.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">lois</span></summary>
<div class="dp-corps">
<p>Si tout est phénomène, que reste-t-il à connaître ? Les liaisons constantes entre phénomènes. Renouvier enchaîne alors quatre définitions, et la quatrième est une bombe.</p>
<div class="dp-cite">
<p>Une <em>loi</em> est un <em>phénomène complexe</em> constamment impliqué dans d'autres <em>phénomènes</em>. […] Une <em>fonction</em> est une <em>loi</em>, considérée en tant que les variations de certains phénomènes composants entraînent des variations déterminées de certains autres. Un <em>être</em> est une fonction.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">En clair</span>
<p>« Un être est une fonction. » Autrement dit : il n'y a pas de socle sous les apparences. Une pierre n'est pas une substance qui aurait des propriétés — c'est une régularité assez stable pour qu'on la traite comme une chose. <em>Être</em>, chez Renouvier, ce n'est pas un verbe d'existence : c'est le nom d'un nœud de rapports qui tient.</p>
<p>Retenez la formule : elle vous attend au tournant. Le Deuxième Essai s'ouvrira sur « L'homme est une fonction particulière de toutes les fonctions données dans le monde ». Ce n'est pas une image. C'est la même définition, appliquée à vous.</p>
</div>
<p>Croire le contraire — croire qu'un mot abstrait désigne une chose qui existe à part — porte un nom chez lui, et le nom est méchant : <strong>le fétichisme en philosophie</strong>. C'est le titre du chapitre qui clôt la première partie <em>(ch. XV)</em>. La substance, l'absolu, l'infini, l'être en général : autant de fétiches, des mots qu'on a pris pour des dieux.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">la machine</span><span class="dp-texte">neuf relations irréductibles</span></summary>
<div class="dp-corps">
<p>Voici le cœur de l'œuvre entière, et la bonne nouvelle : il tient sur une page. Renouvier appelle <strong>catégories</strong> les relations premières auxquelles tout se ramène et qui ne se ramènent à rien.</p>
<div class="dp-cite">
<p>La plus universelle des lois de la représentation est la <em>relation</em> en général. Toutes les autres sont des espèces de la relation.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Et toutes ont la même forme : <strong>deux termes contraires, et leur synthèse.</strong> Neuf fois. C'est une machine, et Renouvier en donne lui-même le plan complet, en une phrase, au premier chapitre du Deuxième Essai :</p>
<div class="dp-machine">
<div class="dp-charniere"><span class="dp-terme">distinct</span><span class="dp-op">+</span><span class="dp-terme">identique</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">déterminé</span><span class="dp-nom">Relation</span></div>
<div class="dp-charniere"><span class="dp-terme">un</span><span class="dp-op">+</span><span class="dp-terme">multiple</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">tout</span><span class="dp-nom">Nombre</span></div>
<div class="dp-charniere"><span class="dp-terme">point</span><span class="dp-op">+</span><span class="dp-terme">espace</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">étendue</span><span class="dp-nom">Position</span></div>
<div class="dp-charniere"><span class="dp-terme">instant</span><span class="dp-op">+</span><span class="dp-terme">temps</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">durée</span><span class="dp-nom">Succession</span></div>
<div class="dp-charniere"><span class="dp-terme">différence</span><span class="dp-op">+</span><span class="dp-terme">genre</span><span class="dp-op dp-op--fleche">→</span><span class="dp-synthese">espèce</span><span class="dp-nom">Qualité</span></div>
</div>
<p class="dp-chapo">— seuil : ôtez l'une de ces cinq, et il ne reste rien de représenté —</p>
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
<p class="dp-chapo">Ces neuf lignes sont le squelette des chapitres XXVI à XL du Premier Essai. Vous venez de lire trois cents pages.</p>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">comment lire</span><span class="dp-texte">Ce que ces neuf lignes veulent dire</span></summary>
<div class="dp-corps">
<p>Chaque ligne se lit ainsi : on ne peut penser aucun des deux termes de gauche tout seul. Rien n'est <em>un</em> sans être aussi multiple ; rien n'est purement multiple sans faire un. Ce qui existe pour la connaissance, c'est toujours le troisième terme — le <em>tout</em>, qui est leur synthèse.</p>
<div class="dp-cite">
<p>[…] aucune chose n'est <em>une</em>, abstraction faite de toute multiplicité ; aucune n'est <em>multiple</em>, abstraction faite de toute unité ; mais toute chose est représentée comme un <em>tout</em>.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La conséquence, qui est terrible pour la métaphysique</span>
<p>Les mots par lesquels la philosophie a toujours cru toucher le fond — <strong>l'un, le simple, l'infini, l'absolu</strong> — sont des termes de gauche isolés de leur contraire. Pris seuls, ils ne désignent rien. Ce ne sont pas des objets difficiles : ce sont des moitiés de rapport à qui l'on a coupé l'autre moitié.</p>
</div>
<div class="dp-cite">
<p>Les termes les plus généraux et les plus abstraits, à l'aide desquels on essaye de surmonter les rapports : l'un, le simple, l'infini, l'absolu, ne sont eux-mêmes représentés que par corrélation à des termes contraires, et séparément ne sont aucune chose et n'en qualifient aucune.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>D'où la formule qui tient lieu de devise à tout le criticisme français : <strong>« Tout phénomène est donné par rapport à d'autres phénomènes. »</strong></p>
</div>
<p class="dp-renvoi">Les neuf lignes se réduisent à une seule opération — la synthèse de deux contraires corrélatifs —, mise en notation sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">le seuil</span><span class="dp-texte">Pourquoi cinq d'un côté et quatre de l'autre</span></summary>
<div class="dp-corps">
<p>Les neuf catégories ne sont pas à égalité, et Renouvier le dit dans un passage que personne ne cite. Il y a une coupure après la cinquième.</p>
<div class="dp-cite">
<p>Otée l'une quelconque des cinq premières catégories, rien de représenté ne subsiste. […] Les autres catégories, le Devenir, la Causalité, la Finalité, la Personnalité, ne s'appliquent pas toujours et d'une manière immédiate à tout sujet qu'on se représente ; mais il n'est pas de fonction représentative, objective, à laquelle elles ne soient inhérentes.</p>
<span class="dp-source">Deuxième Essai, ch. I</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">En clair</span>
<p>Les <strong>cinq premières</strong> font la chose : sans relation, sans nombre, sans lieu, sans date, sans genre, il n'y a pas d'objet du tout. Les <strong>quatre dernières</strong> ne sont pas toujours dans l'objet — un caillou ne poursuit pas de fin — mais elles sont toujours dans <em>l'acte</em> de se le représenter : pour penser quoi que ce soit, il faut durer, vouloir, viser, et être quelqu'un.</p>
<p>Les cinq premières sont du côté de ce qui est vu. Les quatre dernières sont du côté de celui qui voit. C'est pourquoi la personnalité est la neuvième : elle est le bout de cette pente, et non un ajout.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">contre Kant</span><span class="dp-texte">Neuf, et non douze</span></summary>
<div class="dp-corps">
<p>Kant avait douze catégories, rangées en quatre groupes de trois, et il les tirait de la table des jugements de la logique scolaire. Renouvier n'en a que neuf, et les tire d'ailleurs. Trois différences, par ordre de gravité :</p>
<ul class="dp-liste">
<li><strong>L'origine.</strong> Kant lit ses catégories dans une table de logique héritée. Renouvier les obtient par analyse de la représentation, et il avoue le procédé sans fard : « J'arrive aux catégories empiriquement ; je les fixe par hypothèse, et je les propose pour être vérifiées. »</li>
<li><strong>L'unité.</strong> Chez Kant, quatre familles hétérogènes. Chez Renouvier, une seule racine — la relation — dont les huit autres sont des espèces.</li>
<li><strong>L'ajout.</strong> Renouvier en a une que Kant n'a pas : <strong>la personnalité</strong>. Elle n'est pas la dernière par hasard.</li>
</ul>
<div class="dp-cite">
<p>Sous un autre point de vue, celui de l'homme, nécessairement imposé à l'homme, la loi de <em>personnalité</em> est encore une loi universelle. Tout, pour nous, est relatif à la <em>conscience</em>.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Pourquoi c'est décisif</span>
<p>Il y a donc deux catégories universelles, pas une : la <em>relation</em>, sous le point de vue des choses ; la <em>personnalité</em>, sous le point de vue de l'homme. Les sept autres se rangent entre elles. En faisant de la conscience une catégorie — une condition de toute représentation, et non un objet parmi d'autres — Renouvier a déjà écrit la conclusion de son œuvre entière : le <strong>personnalisme</strong>. Le mot viendra quarante ans plus tard ; la chose est ici, dans une liste de neuf.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le double miroir</span><span class="dp-texte">les quatre Essais en sont les quatre applications</span></summary>
<div class="dp-corps">
<p>Voici ce qu'aucun sommaire ne montre, et qui fait des quatre Essais un seul livre. Les neuf catégories ne sont pas un chapitre de l'œuvre : elles en sont <strong>l'unique outil</strong>. Une fois monté, il ne changera plus. Tout le reste consiste à l'appliquer, dans l'ordre, à quatre objets de plus en plus concrets.</p>
<ul class="dp-liste">
<li><strong>Au monde pris comme un tout</strong> — quatrième partie du Premier Essai. L'outil casse. Neuf fois.</li>
<li><strong>À l'homme</strong> — première partie du Deuxième Essai. L'outil tient. Neuf fois.</li>
<li><strong>À la nature</strong> — Troisième Essai. L'être, la matière, la vie, l'espèce, l'origine.</li>
<li><strong>À l'histoire</strong> — Quatrième Essai. Là où l'interdit logique devient un interdit historiographique.</li>
</ul>
<p>Les deux premières applications se répondent ligne à ligne. C'est le <strong>double miroir</strong>, et il est reconstitué ici pour la première fois à partir des deux tables que Renouvier a laissées : celle des neuf échecs, à la fin du Premier Essai ; celle des neuf fonctions, dans le <em>Formulaire</em> du Deuxième.</p>
<div class="dp-cadre">
<table class="dp-miroir dp-double">
<thead><tr><th>Catégorie</th><th class="dp-tete-non">Sur le monde, elle échoue</th><th class="dp-tete-oui">Sur l'homme, elle donne</th></tr></thead>
<tbody>
<tr><td>Relation</td><td class="dp-non">Le tout n'est le terme d'aucun rapport.</td><td class="dp-oui">Comparaison, Attention, Réflexion</td></tr>
<tr><td>Nombre</td><td class="dp-non">Les phénomènes font un nombre, que nul ne peut compter.</td><td class="dp-oui">Numération</td></tr>
<tr><td>Position</td><td class="dp-non">Le monde est mesuré, il n'est pas mesurable.</td><td class="dp-oui">Imagination</td></tr>
<tr><td>Succession</td><td class="dp-non">Un passé infini est contradictoire : il y eut un commencement, et il est inexplicable.</td><td class="dp-oui">Mémoire, Prévision</td></tr>
<tr><td>Qualité</td><td class="dp-non">Le tout enveloppe tous les genres : aucun ne le spécifie.</td><td class="dp-oui">Raison, Jugement, Raisonnement</td></tr>
<tr><td>Devenir</td><td class="dp-non">Le monde devient, mais on ne peut comparer le monde au monde.</td><td class="dp-oui">Pensée</td></tr>
<tr><td>Causalité</td><td class="dp-non">Il faut des causes premières ; on n'en peut rien dire.</td><td class="dp-oui">Volonté</td></tr>
<tr><td>Finalité</td><td class="dp-non">Ni premier but ni but dernier ne sont assignables.</td><td class="dp-oui">Passion, Instinct, Habitude</td></tr>
<tr><td>Personnalité</td><td class="dp-non">Une conscience du tout cesserait d'être une conscience.</td><td class="dp-oui">Liberté</td></tr>
</tbody>
</table>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Lisez la dernière ligne deux fois</span>
<p>Le même outil, la même neuvième pièce. Sur le monde, elle interdit : il ne peut pas y avoir de conscience du tout, car une conscience qui envelopperait tout n'aurait plus de non-soi, et cesserait donc d'être une conscience. Sur l'homme, elle donne : la personnalité, c'est-à-dire la <strong>liberté</strong>.</p>
<p>Voilà Renouvier en une phrase, et voilà pourquoi les quatre Essais forment un tout : <strong>la connaissance échoue sur le tout et réussit sur la personne.</strong> Le monde n'a pas de sommet ; il a des personnes. Le personnalisme n'est pas une doctrine que Renouvier aurait ajoutée à sa logique — c'est ce qui reste quand la logique a fini de démolir.</p>
</div>
<p class="dp-chapo">La colonne de gauche est en gris parce qu'elle dit non. Celle de droite est la seule chose que Renouvier ait jamais eu à gagner.</p>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">la table</span><span class="dp-texte">D'où viennent ces deux colonnes</span></summary>
<div class="dp-corps">
<p>Aucune des deux n'est de moi. Elles sont chacune dans un <em>Formulaire</em>, et il suffisait de les mettre côte à côte.</p>
<p>À gauche : la dernière section du <em>Formulaire du Traité de logique générale</em> énumère les échecs de la synthèse totale, numérotés « 1° à l'égard de la relation… 2° à l'égard de la totalité… », dans l'ordre exact des chapitres XLII à LIII du tome III.</p>
<p>À droite : la section A du <em>Formulaire du Traité de Psychologie rationnelle</em> énumère les fonctions humaines, numérotées de 1 à 9, chacune sous le nom de sa catégorie. On y lit textuellement « 1. Relation : <em>Comparaison, Attention, Réflexion</em> », « 3. Position : <em>Imagination</em> », « 4. Succession : <em>Mémoire</em> », et pour finir « 9. Personnalité : <em>Liberté</em> ».</p>
<div class="dp-cite">
<p>La conscience des phénomènes comme limités, écartés d'espace et déterminés d'étendue, est l'<em>Imagination</em>.</p>
<span class="dp-source">Formulaire du Traité de Psychologie rationnelle, A, 3</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Ce que ça coûte de le savoir</span>
<p>Cette correspondance n'est pas une curiosité. Elle dit que la psychologie de Renouvier n'est pas une observation de l'esprit : c'est une <em>déduction</em>. Il ne regarde pas ce que fait l'homme pour en dresser la liste — il prend ses neuf catégories et demande, pour chacune, quelle fonction de conscience lui correspond. La mémoire n'est pas une faculté qu'on aurait trouvée : c'est ce que devient la catégorie de succession quand un être s'en sert.</p>
<p>Et le premier chapitre du Deuxième Essai s'appelle, en toutes lettres : <em>De la nature humaine relativement aux catégories</em>. Le titre est le programme.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">3ᵉ et 4ᵉ</span><span class="dp-texte">Les deux applications suivantes, et où elles s'arrêtent</span></summary>
<div class="dp-corps">
<p>Le même outil descend ensuite vers le concret, et chaque Essai s'achève en désignant le suivant. La chaîne est explicite, et c'est Renouvier qui la noue.</p>
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
<p>Le Troisième Essai s'achève sur « L'origine de l'homme » et « Les origines premières et morales ». Le Quatrième s'ouvre sur « Des commencements de l'humanité ». Il n'y a pas de couture : le troisième livre dépose l'homme au seuil, le quatrième le fait entrer. Quatre volumes séparés de dix à quarante ans, et pas un centimètre de jeu.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le miroir</span><span class="dp-texte">limite extrême de la connaissance</span></summary>
<div class="dp-corps">
<p>C'est le titre de la quatrième et dernière partie du Premier Essai, et Renouvier y met sa question en sous-titre, comme on pose un couteau sur une table :</p>
<p class="dp-epigraphe">Une synthèse unique et totale des phénomènes est-elle possible ?</p>
<p><strong>La quatrième partie est le miroir de la troisième.</strong> La troisième construit les neuf catégories, une par une. La quatrième les reprend <em>dans le même ordre</em> et les applique au monde entier. Neuf fois, neuf échecs.</p>
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
<span class="dp-etiquette">Ce que la table vous donne</span>
<p>Le droit d'entrer dans le livre par n'importe quelle ligne. Le temps vous intéresse ? Lisez XXXI, puis XLV : vous aurez la catégorie et sa ruine, et vous aurez compris la méthode entière sur un exemple. Le livre se lit en colonnes autant qu'en lignes — c'est ce que les commentateurs appellent son « architecture », et c'est simplement cela.</p>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">le coup</span><span class="dp-texte">Là où Renouvier cesse de continuer Kant</span></summary>
<div class="dp-corps">
<p>Tout le monde connaît les antinomies de Kant : quatre couples de propositions contraires — le monde a un commencement / il n'en a pas — dont Kant établit que <em>la thèse et l'antithèse sont également démontrables</em>. De cette égalité insoluble, il tire l'idéalisme transcendantal.</p>
<p>Renouvier tient cette égalité pour une erreur. C'est son seul coup de force, mais il porte :</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'antinomie se tranche</span>
<p>Thèse et antithèse ne sont pas à égalité. La thèse (fini, commencement, nombre déterminé) est simplement vraie. L'antithèse (infini en acte) est <strong>contradictoire</strong> — ce n'est pas une seconde démonstration, c'est un énoncé qui ne veut rien dire. En accordant à l'infini la même dignité logique qu'au fini, Kant s'est laissé prendre à un fétiche, et il a bâti son idéalisme sur une balance faussée.</p>
</div>
<p>Le chapitre XLII et ses observations portent un titre sans ambiguïté : <em>Réfutation des antinomies kantiennes</em>. Renouvier montre au passage que ses propres catégories ne produisent, elles, aucune antinomie : leurs deux termes contraires étant abstraits et corrélatifs, ils ne s'appliquent jamais séparément à rien, et ne peuvent donc pas se contredire.</p>
<div class="dp-cite">
<p>[…] les catégories, par elles-mêmes, ne conduisent point à l'antinomie […]. Mais elles ne subsistent que parce qu'on se refuse à borner la science à la considération des relatifs.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Voilà toute l'affaire : les antinomies ne sont pas une fatalité de la raison, elles sont la punition d'une ambition. Elles ne surgissent que si l'on veut connaître le tout. Renoncez à cela, et la raison redevient cohérente.</p>
</div>
<p class="dp-renvoi">Les neuf échecs tiennent en un lemme — le Tout n'a pas de vis-à-vis — formalisé sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>.</p>
</details>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">liberté</span></summary>
<div class="dp-corps">
<p>La neuvième pièce de la machine, appliquée à l'homme. C'est le sommet du Deuxième Essai, et le seul endroit de l'œuvre où Renouvier doit décider au lieu de démontrer.</p>
<p>Car il commence par saborder l'argument que tout le monde attend :</p>
<div class="dp-cite">
<p>On voit à quel point se trompent les philosophes qui regardent la liberté humaine comme un fait d'expérience. Si cela était, en disputerait-on ? Qui jamais a contesté l'existence d'un fait sensible en le sentant ?</p>
<span class="dp-source">Deuxième Essai, ch. XIII — La liberté ; état de la question</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le nœud, qui est vertigineux</span>
<p>Si je suis libre, c'est librement que je juge être libre — donc mon jugement ne prouve rien. Si je suis déterminé, c'est nécessairement que je juge, vrai ou faux — donc mon jugement ne prouve rien non plus. Renouvier l'écrit sans ciller : « c'est à la liberté qu'il appartient de déclarer si la liberté est ou non ».</p>
<p>Aucune preuve n'est possible, ni pour, ni contre. Il faut donc <em>choisir</em> — et ce choix est le premier acte libre, celui qui fonde tous les autres. La liberté ne se démontre pas : elle s'affirme, et l'affirmation est déjà son exercice.</p>
</div>
<p>De là le renversement du plan : la certitude n'est pas le point de départ de la philosophie, c'en est le terme. Renouvier l'annonce dès la troisième page du Premier Essai, vingt ans avant d'y arriver :</p>
<div class="dp-cite">
<p>Le chapitre de la certitude n'a pas sa place marquée dans ce <em>traité</em>. Il formera contre tout usage, mais en toute raison, la clef de voûte d'un édifice qu'il s'agit de fonder […] ; il n'en sera pas la première pierre.</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et même la statistique ne donne qu'une probabilité — il le dit</span>
<p>Le chapitre s'adosse à une Observation entière — première pièce que cette page prélève dans les <em>Observations et développements</em>, comme promis. L'argument : le hasard a une signature, la loi des grands nombres, et cette signature est précisément l'<em>absence</em> de loi individuelle. Des actes libres la porteraient. Mais lisez le verdict jusqu'au bout :</p>
<div class="dp-cite">
<p>[…] les applications du calcul des probabilités sont par elles-mêmes une vérification <em>probable</em> de l'existence effective de la liberté. La loi des grands nombres est la loi des faits qui ne reconnaissent point d'autre loi.</p>
<span class="dp-source">Deuxième Essai, ch. XIII, Observations et développements, A — De l'interprétation de la loi dite des <em>grands nombres</em></span>
</div>
<p>Une vérification <em>probable</em> — l'italique est de lui. Même son meilleur indice empirique, Renouvier refuse de l'appeler preuve. Le pari reste entier, et c'est voulu.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Descartes à l'envers</span>
<p>Descartes commence par la certitude ; Renouvier finit par elle. Sa raison est imparable : chercher d'abord la certitude, ce serait juger de la valeur de la raison avant d'avoir examiné la raison. La certitude n'est pas le sol : c'est le toit. Et le toit, une fois posé, s'appelle la liberté.</p>
</div>
<p>Et c'est ici, dans les <em>Observations</em> du chapitre XIV — sous les titres « La philosophie de Jules Lequier » puis « Comment trouver, comment chercher une première vérité ? » —, que Renouvier a publié les fragments de son ami noyé, à qui il devait l'idée que la liberté doit être choisie. Le texte le plus abrupt du siècle sur la liberté a été sauvé de l'oubli dans les notes de bas de page d'un traité de psychologie.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">croyance</span></summary>
<div class="dp-corps">
<p>Ici, presque tous les lecteurs se trompent, et dans le même sens. On croit lire : <em>la raison s'arrête, donc croyez ce qu'il vous plaît.</em> C'est le contraire.</p>
<div class="dp-cite">
<p>Les bornes de la connaissance ainsi reconnues, deux choses restent intactes. Ce sont d'abord les croyances, qui, sans prétendre dépasser ces bornes en s'obstinant dans l'affirmation d'objets que la raison a déclarés contradictoires, demeurent libres de s'étendre au delà et bien loin de ce que l'analyse peut ou pourra jamais atteindre.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La règle, en une ligne</span>
<p>La croyance est libre là où la raison <strong>ne démontre pas</strong>. Elle est interdite là où la raison <strong>démontre une contradiction</strong>.</p>
<p>Ce n'est pas un partage de territoire, c'est une hiérarchie. La raison ne se retire pas : elle trace la frontière, et elle en garde un côté. Un Dieu infini en acte est proscrit — non parce qu'il déplaît, parce qu'il ne veut rien dire. Une pluralité de consciences premières, en revanche, est permise, et Renouvier y croira.</p>
</div>
<p>C'est tout le programme de la troisième partie du Deuxième Essai, dont le titre énumère ce qui reste debout : <em>Les probabilités touchant l'ordre moral du monde. L'immortalité, la liberté, la divinité.</em> Les trois postulats de Kant, repris un à un — mais cette fois sans chose en soi, sans infini, et par des probabilités morales au lieu d'une raison pratique posée d'autorité. Renouvier va jusqu'à écrire un chapitre entier intitulé <em>Examen des thèses de la raison pratique de Kant</em>, et un autre <em>Des hypothèses rationnelles sur la nature de Dieu</em>.</p>
<div class="dp-note">
<span class="dp-etiquette">Un Dieu qui n'est pas infini</span>
<p>La conclusion est parmi les plus étranges du siècle, et elle suit du pivot comme le reste : puisque l'infini en acte est contradictoire, un Dieu infini est contradictoire. Reste un Dieu fini — « la personne divine est ainsi soustraite aux attributs infinis que la métaphysique appelait des <em>perfections</em> et qui la détruisaient. Mais la vraie <em>perfection</em> lui reste […] : la perfection de justice et de bonté ». Renouvier ajoute que rien alors ne prouve plus l'unité de Dieu plutôt que sa pluralité. Un traité de logique de 1854 aboutit, en 1875, à rendre le polythéisme rationnellement recevable.</p>
</div>
<p>Et cette frontière n'est pas un exercice d'école. Elle est, dans la préface de 1854, ce que Renouvier attend de plus important pour son siècle :</p>
<div class="dp-cite">
<p>La limitation mutuelle et définitive de la science et des croyances est d'une importance majeure pour l'ordre et le progrès régulier des associations humaines. […] Le jour où la liberté serait connue, et l'homme désaccoutumé de vouloir forcer l'homme à croire ou à ne pas croire, on verrait des églises se former, s'unir, se dissoudre et se reconstituer, sans que la science ou l'État s'y trouvassent intéressés.</p>
<span class="dp-source">Premier Essai, préface de la première édition</span>
</div>
<p>Un traité de logique de six cents pages sur les catégories et l'infini, écrit six ans après 1848 — et sa conclusion politique est la séparation des Églises et de l'État. Il faudra cinquante et un ans pour qu'elle soit votée. Renouvier meurt deux ans avant.</p>
<div class="dp-note">
<span class="dp-etiquette">Le chapitre que personne n'attend</span>
<p>Le Deuxième Essai, traité de psychologie, comporte un chapitre XIX intitulé <em>Complément de la définition de la certitude. Du contrat personnel et du contrat social.</em> La certitude débouche sur le contrat. Ce n'est pas une digression : si la vérité est affirmée par une liberté, alors le lieu de la vérité est un accord entre des libertés. La République n'est pas une conséquence politique de la philosophie de Renouvier — c'est un chapitre de sa psychologie.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">la clé</span><span class="dp-texte">histoire sans sens de l'Histoire</span></summary>
<div class="dp-corps">
<p>La quatrième partie du Premier Essai a interdit la <strong>synthèse totale</strong> : on ne peut pas connaître le tout. Or que fait une philosophie de l'histoire, chez Bossuet, chez Vico, chez Hegel, chez Comte ? Elle fait exactement la synthèse totale de l'histoire humaine : un plan, un sens, une fin. Elle est donc interdite — non par goût, par la même démonstration.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le titre est une conséquence</span>
<p>Le Quatrième Essai s'appelle <em>Introduction à la philosophie <strong>analytique</strong> de l'histoire</em>. Ce mot n'est pas un ornement : il est l'exact opposé de <em>synthétique</em>. Renouvier ne peut pas faire de philosophie synthétique de l'histoire, puisqu'il a démontré au tome III du Premier Essai que la synthèse totale est impossible. L'interdit logique est devenu, mot pour mot, un interdit historiographique.</p>
</div>
<p>Il annonce d'ailleurs sa méthode par ce qu'il refuse, et la liste des refus est la vraie table des matières :</p>
<div class="dp-cite">
<p>Traitée dans un système apriorique, elle défigure les faits, ou elle les dédaigne ; elle en rejette et elle en interpole, afin de disposer plus commodément les autres en série.</p>
<span class="dp-source">Quatrième Essai, § I</span>
</div>
<p>Deux façons de manquer l'histoire : sans idée, ou avec une idée d'avance. La voie étroite entre les deux, c'est l'analyse — des faits établis, des inductions tirées de ce que la personne humaine a de constant, et rien de plus.</p>
</div>
</details>

<details class="dp-pli" data-rang="terme">
<summary class="dp-titre"><span class="dp-rang">l'escalier</span><span class="dp-texte">formulaire</span></summary>
<div class="dp-corps">
<p>Voici la trouvaille, et elle est de Renouvier. À la charnière de chaque Essai, il a placé un texte qui replie le précédent en propositions nues — sans preuves, sans exemples, sans polémique. Il appelle cela un <strong>formulaire</strong>. Et il les a déplacés, réédités, corrigés pendant trente ans.</p>
<div class="dp-escalier">
<div class="dp-marche"><span class="dp-marche-num">Essai I</span><span>Traité de logique générale — 3 tomes, 54 chapitres</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">le pli</span><span>Formulaire du Traité de logique générale — 30 pages. En tête du Deuxième Essai en 1859 ; déplacé à la fin du Premier en 1875.</span></div>
<div class="dp-marche"><span class="dp-marche-num">Essai II</span><span>Traité de psychologie rationnelle — 3 tomes, 25 chapitres</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">le pli</span><span>Formulaire du Traité de Psychologie rationnelle — sections A, B, C, D. Trois éditions : en tête du Troisième Essai en 1864 ; à la fin du Deuxième en 1875 ; <em>et</em> de nouveau en tête du Troisième en 1892, où Renouvier signale ses propres repentirs en note.</span></div>
<div class="dp-marche"><span class="dp-marche-num">Essai III</span><span>Les Principes de la nature — 2 tomes, 12 chapitres</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">le pli</span><span>« I. Résumé. Plan. » — où les trois premiers Essais sont récapitulés et l'homme déposé au seuil de l'histoire.</span></div>
<div class="dp-marche"><span class="dp-marche-num">Essai IV</span><span>Introduction à la philosophie analytique de l'histoire — 32 paragraphes</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que ça veut dire pour cette page</span>
<p>Le niveau intermédiaire d'un dépliant — le palier entre le titre et le livre — n'a pas eu à être inventé ici. <strong>Il existe, verbatim, de la main de l'auteur.</strong> Renouvier a plié ses propres livres, et il a rangé les plis aux charnières, là où l'on ne va jamais : à la fin des tomes, avant les notes.</p>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">la preuve</span><span class="dp-texte">Renouvier raconte lui-même le déménagement</span></summary>
<div class="dp-corps">
<p>À la toute fin du Deuxième Essai, après le Formulaire, une <em>Note finale</em> explique l'affaire :</p>
<div class="dp-cite">
<p>Les lignes suivantes étaient jointes, dans la première édition du <em>Deuxième Essai de critique générale</em>, à un résumé du <em>Premier Essai</em>, portant le titre de : <em>Formulaire du Premier Essai</em>. Ce formulaire a été reproduit à la fin de la seconde édition du <em>Premier Essai</em>, où sa place se trouvait naturellement marquée.</p>
<span class="dp-source">Deuxième Essai, Note finale</span>
</div>
<p>« Où sa place se trouvait naturellement marquée ». En 1859, le résumé du premier livre servait de porte d'entrée au second. En 1875, Renouvier le renvoie à la fin du premier. Le pli n'a pas changé de contenu : il a changé de charnière.</p>
<div class="dp-note">
<span class="dp-etiquette">Et le pli suivant existe en deux états</span>
<p>Le <em>Formulaire du Traité de Psychologie rationnelle</em> ouvrait le Troisième Essai en 1864 ; il clôt le Deuxième en 1875 ; il rouvre le Troisième en 1892, sous le titre <em>Introduction — Résumé des principes de la psychologie rationnelle</em>, avec les mêmes quatre sections et la même première phrase. <strong>Trois états du même texte, sur vingt-huit ans.</strong> Les deux derniers sont identiques à 94,3 % au mot — l'écart tient en 599 mots, soit 3,7 %. Et Renouvier signale en note qu'il corrige là « cette troisième édition du résumé de mes <em>Essais</em> », qu'il a mis une conclusion « sous une forme dubitative » et en a ajouté une autre, « plus avancée dans le sens des postulats ».</p>
<p>Autrement dit : <strong>le palier a une histoire, et elle est datée.</strong> On peut lire le même résumé à trois âges et voir un homme changer d'avis sur Dieu, en note. C'est l'objet d'une page voisine, <a href="../evolution/">Comment je suis arrivé à cette conclusion</a>.</p>
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
<p class="dp-chapo">Trois tomes, cinquante-quatre chapitres, quatre parties. C'est le socle : les trois autres Essais en dépendent, et lui ne dépend de rien.</p>

<details class="dp-pli" data-rang="entrée">
<summary class="dp-titre"><span class="dp-rang">ch. I</span><span class="dp-texte">L'aveu du départ : « il faut tomber droit au milieu de la raison »</span></summary>
<div class="dp-corps">
<p>Le livre s'ouvre sur trois questions de six mots, qui sont déjà tout le problème :</p>
<div class="dp-cite">
<p>Tout langage et toute science procèdent par composition et décomposition. Mais que composons-nous ainsi, que décomposons-nous ? Des <em>mots</em> ? des <em>idées</em> ? des <em>choses</em> ?</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<p>Puis, aussitôt, l'aveu — et c'est peut-être le plus beau moment d'honnêteté de tout le XIX<sup>e</sup> siècle philosophique :</p>
<div class="dp-cite">
<p>[…] la critique de la connaissance se meut dans un cercle inévitable. Quelque vérité, quelque rapport que j'entreprenne d'expliquer, de prouver, je suis contraint de proposer d'autres rapports que je n'explique pas. Comment expliquer en effet ce que supposerait une première explication quelconque ? et que ne supposé-je point dès mes premières lignes ? Ou le <em>procès à l'infini</em>, qui est impossible, ou le <em>cercle</em> qu'on nomme <em>vicieux</em> : lisez les sceptiques.</p>
<p>Donc il faut tomber droit au milieu de la raison et s'y livrer.</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que cela vous autorise</span>
<p>Renouvier ne promet pas des fondations. Il déclare qu'il n'y en a pas, qu'il n'y en aura jamais, et qu'il commence quand même. Sa seule garantie est offerte au lecteur, pas au système :</p>
</div>
<div class="dp-cite">
<p>Quel est mon but, après tout ? D'être compris, d'être approuvé. J'écris l'histoire de mes pensées pour que d'autres la vérifient par l'histoire conforme des leurs, en me lisant. […] Je serai justifié si mon lecteur la possède avec moi, comme moi.</p>
<span class="dp-source">Premier Essai, ch. I</span>
</div>
<p>La preuve, c'est vous. Il n'y en a pas d'autre. Cela dit aussi pourquoi ce livre est si dur : il ne s'agit pas de vous convaincre, il s'agit que vous refassiez le chemin.</p>
<div class="dp-note">
<span class="dp-etiquette">Et un avertissement, qu'il faut prendre au sérieux</span>
<p>« Mais c'est en vain qu'on s'efforcerait d'épargner au lecteur l'attention ou même le travail. Un vice de la philosophie, dans quelques livres, est une certaine <em>fausse lucidité</em>. Je ne connais pas de science qui soit claire en ce sens-là. » — Cette page-ci vise la lucidité vraie : elle vous fait entrer, elle ne vous dispense pas.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie I">
<summary class="dp-titre"><span class="dp-rang">ch. II-XV</span><span class="dp-texte">De la représentation en général</span></summary>
<div class="dp-corps">
<p class="dp-epigraphe">Les phénomènes sont les éléments de la connaissance</p>
<p>Quatorze chapitres pour établir une seule chose : <strong>il n'y a pas de chose en soi</strong>. Le mouvement est d'une simplicité brutale.</p>
<ul class="dp-liste">
<li><strong>II-III</strong> — Définir la représentation, le fait, le phénomène ; première analyse.</li>
<li><strong>IV-V</strong> — Le dedans et le dehors ; « la représentation n'implique rien que ses propres éléments ».</li>
<li><strong>VI-VII</strong> — La thèse : il n'existe pas de chose en soi pour la connaissance. Et les principes de la preuve.</li>
<li><strong>VIII à XIV</strong> — La preuve, refaite une fois par objet : l'espace <em>(VIII)</em>, le temps <em>(IX)</em>, la matière <em>(X)</em>, le mouvement <em>(XI)</em>, les représentés quelconques <em>(XII)</em>, les faits représentatifs <em>(XIII)</em>, la somme totale des phénomènes <em>(XIV)</em>.</li>
<li><strong>XV</strong> — Récapitulation : <em>le fétichisme en philosophie</em>.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le truc, une fois pour toutes</span>
<p>Les sept chapitres de « preuve » ne sont pas sept arguments. C'est <strong>un seul argument, appliqué sept fois</strong> — le pivot qui tourne :</p>
<p><em>Si X était en soi, X serait un continu en soi ; un continu en soi a un nombre infini de parties en soi ; un nombre infini est contradictoire ; donc X n'est pas en soi.</em></p>
<p>Remplacez X par : l'espace, le temps, la matière, le mouvement. Vous avez les chapitres VIII à XI. Une fois que vous tenez le schéma, ces cent pages se lisent en diagonale — et c'est le bon usage : on ne lit pas sept fois une démonstration qu'on a comprise une fois.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le mot « fétichisme »</span>
<p>Le chapitre XV est un règlement de comptes, et son titre le dit. Le fétichiste adore un morceau de bois parce qu'il a pris le signe pour la chose. Le philosophe qui parle de <em>la</em> Substance, de <em>l'</em>Absolu, de <em>l'</em>Être, fait exactement pareil : il a substantifié un adjectif, puis il s'est agenouillé devant. Le reste du livre ne fera que démonter des fétiches.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie II">
<summary class="dp-titre"><span class="dp-rang">ch. XVI-XXV</span><span class="dp-texte">Revue élémentaire des phénomènes</span></summary>
<div class="dp-corps">
<p class="dp-epigraphe">Les lois des phénomènes sont les fins de la connaissance</p>
<p>Les deux épigraphes se répondent : la première partie donnait les <em>éléments</em>, celle-ci donne les <em>fins</em>. Éléments et fins : matière et but. Le programme entier de la connaissance tient entre ces deux lignes en capitales, et Renouvier les a mises en tête de ses parties comme des enseignes.</p>
<p>Dix chapitres, une seule chaîne de définitions, qui descend jusqu'à faire sauter l'ontologie :</p>
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
<p>Un phénomène est ce qui est donné. Une loi est un phénomène complexe constamment impliqué dans d'autres. Une fonction est une loi où la variation des uns entraîne celle des autres. Et un être <em>est</em> une fonction.</p>
<p>Lisez le dernier maillon lentement. Il dit que rien n'est sous les choses. Ce que nous appelons <em>un être</em>, c'est un endroit du monde où les rapports sont assez réguliers pour qu'on leur donne un nom.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le rapport de force</span>
<p>C'est aussi ici que Renouvier accepte publiquement une formule positiviste — « la réduction de la connaissance aux lois des phénomènes » — tout en refusant l'école : il lui reproche de ne pas analyser ses propres notions premières, de nier dogmatiquement ce qu'on peut croire, et d'avoir gardé de Saint-Simon des ambitions d'organisation « chimériques à mon gré, et peu libérales ». Le partage est net : la méthode, oui ; l'Église positiviste, non.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie III">
<summary class="dp-titre"><span class="dp-rang">ch. XXVI-XL</span><span class="dp-texte">Analyse des lois fondamentales — Catégories — Logique</span></summary>
<div class="dp-corps">
<p>La plus longue partie du livre : elle occupe la fin du tome I et tout le tome II. C'est l'atelier où la machine est montée pièce par pièce. Deux séries de chapitres s'y entrelacent, et savoir les distinguer épargne beaucoup de fatigue.</p>
<ul class="dp-liste">
<li><strong>Les neuf catégories</strong> — XXVII <em>(relation)</em>, XXIX <em>(nombre)</em>, XXX <em>(position)</em>, XXXI <em>(succession)</em>, XXXIII <em>(qualité)</em>, XXXVI <em>(devenir)</em>, XXXVII <em>(causalité)</em>, XXXIX <em>(finalité)</em>, XL <em>(personnalité)</em>. Précédées de XXVI, qui les définit et les distribue.</li>
<li><strong>La logique formelle qui en découle</strong> — XXVIII <em>(contradiction, alternative)</em>, XXXII <em>(mesure, valeurs négatives, l'infini)</em>, XXXIV <em>(le syllogisme)</em>, XXXV <em>(absurde, disjonction, induction, démonstration)</em>, XXXVIII <em>(nécessaire, possible, probable)</em>.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens du titre</span>
<p>« Logique <em>générale</em> et logique <em>formelle</em> » : ce n'est pas une redondance, c'est l'ordre de dérivation. La logique générale, ce sont les catégories — les lois de ce qui est. La logique formelle — syllogisme, contradiction, induction — n'est pas un art de raisonner posé à côté : elle <strong>sort</strong> des catégories, et de deux seulement. « La <em>logique</em> est renfermée tout entière dans les lois générales de la relation et de la qualité. » Renouvier ne fait pas de la logique une technique : il la fait descendre de sa métaphysique.</p>
</div>

<details class="dp-pli" data-rang="ch. XXXII">
<summary class="dp-titre"><span class="dp-rang">le chapitre</span><span class="dp-texte">XXXII — là où le pivot est vissé</span></summary>
<div class="dp-corps">
<p>Titre complet : <em>Mesure de la position par le nombre. Valeurs positives et négatives. — Mesure du continu par le nombre : les fractions, les incommensurables, les limites. — Question de l'infini.</em></p>
<p>C'est le chapitre le plus technique du livre et le plus important. Renouvier y doit faire une chose difficile : sauver toute la mathématique — les fractions, les incommensurables, les tangentes, les quadratures, le calcul différentiel — <strong>sans jamais admettre un infini en acte</strong>. Ses <em>Observations et développements</em> y consacrent une centaine de pages, sous deux titres :</p>
<ul class="dp-liste">
<li><em>A. De la théorie des valeurs négatives</em> — le sens du symbole négatif, les imaginaires, les exposants négatifs.</li>
<li><em>B. Théorie de l'indéfini et des limites</em> — la fraction, l'incommensurable, la géométrie élémentaire, les tangentes, les rectifications et quadratures, les principes du calcul de l'indéfini, et pour finir Auguste Comte et la philosophie des mathématiques.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Si vous ne lisez qu'un chapitre technique</span>
<p>Lisez celui-là. Renouvier prévient dans son avant-propos qu'il a retranché des formules « en faveur du lecteur non mathématicien », mais qu'il ne pouvait pas aller plus loin « sans nuire au caractère d'une doctrine dont l'idée pivotale » vient de là. Traduction : ce chapitre est le seul dont il refuse de vous dispenser.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="partie IV">
<summary class="dp-titre"><span class="dp-rang">ch. XLI-LIV</span><span class="dp-texte">De la limite extrême de la connaissance</span></summary>
<div class="dp-corps">
<p class="dp-epigraphe">Une synthèse unique et totale des phénomènes est-elle possible ?</p>
<p>Tout le tome III. C'est le miroir de la partie III : les neuf catégories, reprises dans l'ordre, appliquées au monde entier, et brisées une à une. <em>(Voir la table, plus haut, sous « limite extrême de la connaissance » ; et le double miroir sous « les quatre applications ».)</em></p>
<ul class="dp-liste">
<li><strong>XLI-XLII</strong> — Les antinomies : celles du système des catégories, puis les autres. Définition du monde. <em>Réfutation des antinomies kantiennes.</em></li>
<li><strong>XLIII à LIII</strong> — La synthèse totale, éprouvée neuf fois : nombre <em>(XLIII)</em>, étendue <em>(XLIV)</em>, durée <em>(XLV)</em>, division interne <em>(XLVI)</em>, vide et plein <em>(XLVII)</em>, espèce <em>(XLVIII)</em>, devenir <em>(XLIX)</em>, évolution <em>(L)</em>, cause <em>(LI)</em>, fin <em>(LII)</em>, conscience <em>(LIII)</em>.</li>
<li><strong>LIV</strong> — Des problèmes en deçà de la connaissance possible. Conclusion.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le dernier échec est le plus lourd</span>
<p>Le chapitre LIII demande s'il peut y avoir une conscience du monde entier. Renouvier répond non, et sa raison est purement logique : la conscience est la synthèse du soi et du non-soi ; une conscience qui envelopperait tout n'aurait pas de non-soi ; elle cesserait donc d'être une conscience.</p>
<p>Et il en tire une conséquence dont il vivra : puisqu'une conscience unique et totale est contradictoire, « l'hypothèse d'une <strong>pluralité primitive de consciences distinctes</strong>, dans le monde, semble donc la seule rationnelle ». Le monde n'a pas de sommet. Il a des personnes. Tout le personnalisme est né dans ce chapitre, à la fin d'un traité de logique, comme le résidu d'une impossibilité.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le pli de Renouvier">
<summary class="dp-titre"><span class="dp-rang">fin du tome III</span><span class="dp-texte">Formulaire du Traité de logique générale</span></summary>
<div class="dp-corps">
<p>Une trentaine de pages, à la fin du dernier tome, après la mention « FIN DU PREMIER ESSAI ». Renouvier y récrit son livre entier en propositions nues, sans preuves, sans exemples, sans polémique. Il ouvre ainsi :</p>
<div class="dp-cite">
<p>Les définitions, principes et conclusions qui suivent sont acquis pour nous à la suite d'une analyse de raison pure, sous la réserve d'un examen à faire de la nature et de la valeur de notre certitude.</p>
<span class="dp-source">Formulaire, première phrase</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Renouvier avait déjà fait ce dépliant</span>
<p>Le <em>Formulaire</em> est le livre plié. Il contient tout et il ne démontre rien — il énonce. Il suit l'ordre du traité, et sa dernière section énumère les huit échecs de la synthèse totale, numérotés « 1° à l'égard de la relation… 2° à l'égard de la totalité… », dans l'ordre exact des chapitres XLII à LIII.</p>
<p>Autrement dit : <strong>le Formulaire est le plan de la quatrième partie</strong>, et il donne la clé de l'architecture entière. Renouvier l'a mis à la fin, où presque personne ne va. Cette page-ci ne fait, au fond, que le remettre au début.</p>
</div>
<p>Conseil de lecture, s'il n'en fallait qu'un : lisez le <em>Formulaire</em> en premier, puis le traité. Trente pages avant six cents. Renouvier a écrit son propre résumé et l'a rangé derrière la porte de sortie.</p>
</div>
</details>
</div>
</details>


<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai II · 1859 / 1875</span><span class="dp-texte">Traité de psychologie rationnelle d'après les principes du criticisme</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trois tomes, vingt-cinq chapitres, trois parties. Le livre où l'outil, cette fois, tient. C'est la clef de voûte annoncée dès la troisième page du Premier Essai — et il aura fallu cinq ans pour la poser.</p>

<details class="dp-pli" data-rang="partie I">
<summary class="dp-titre"><span class="dp-rang">ch. I-XIII</span><span class="dp-texte">L'homme et ses fonctions constituantes</span></summary>
<div class="dp-corps">
<p>Treize chapitres, et le premier donne la méthode dans son titre : <em>De la nature humaine relativement aux catégories</em>. Renouvier ne va pas observer l'esprit pour en dresser l'inventaire. Il prend ses neuf catégories et demande, pour chacune, quelle fonction humaine lui correspond.</p>
<ul class="dp-liste">
<li><strong>I</strong> — De la nature humaine relativement aux catégories.</li>
<li><strong>II-III</strong> — L'homme physique et organique ; l'homme comme sensibilité.</li>
<li><strong>IV-V</strong> — L'homme comme intelligence ; puis la raison, les signes, le langage.</li>
<li><strong>VI</strong> — De la conscience en général et des méthodes psychologiques.</li>
<li><strong>VII-VIII</strong> — L'homme comme passion ; la passion, l'instinct, l'habitude.</li>
<li><strong>IX-X</strong> — L'homme comme volonté ; <em>lois de dégradation de la conscience réfléchie</em>.</li>
<li><strong>XI-XII</strong> — Les rapports des fonctions volontaires avec l'organisme, puis avec la conscience.</li>
<li><strong>XIII</strong> — <em>La liberté ; état de la question ; solution provisoire.</em></li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le mot « provisoire » est à prendre au sérieux</span>
<p>La première partie s'arrête sur une « solution provisoire » du problème de la liberté. Provisoire, parce que Renouvier vient de montrer qu'aucune preuve n'est possible : l'analyse rend la liberté <em>probable</em>, rien de plus. Pour aller plus loin il faut d'abord savoir ce qu'est croire — d'où la deuxième partie, sur la certitude. La liberté ne sera tranchée qu'après, au chapitre XXII, et par un acte, pas par un argument.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le vertige</span>
<p>Les chapitres X à XII contiennent ce que Renouvier appelle le <em>vertige</em> : ces états où la conscience réfléchie se dégrade, où l'on fait ce qu'on ne veut pas, où la liberté s'efface sans qu'on ait cessé d'être conscient. C'est sa contribution la plus originale à la psychologie, et le Quatrième Essai y renverra pour excuser une part du mal historique. Il est rare qu'un philosophe de la liberté consacre trois chapitres aux moments où elle n'est pas là.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie II">
<summary class="dp-titre"><span class="dp-rang">ch. XIV-XIX</span><span class="dp-texte">La certitude</span></summary>
<div class="dp-corps">
<p>Six chapitres, et la question que Descartes mettait en premier arrive ici en vingt-quatrième position du parcours total.</p>
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
<p>Le <strong>premier ordre</strong> (ch. XVI) est ce qu'on ne peut pas ne pas affirmer : l'être de la conscience, l'être du monde. Le <strong>second ordre</strong> (ch. XVII) est tout le reste — et il dépend de la liberté, parce qu'y affirmer, c'est vouloir affirmer. D'où la phrase qui fait tourner le livre : « Le principe de ces principes est la liberté. »</p>
<p>Conséquence : il n'y a pas de vérité sans quelqu'un qui la veuille. Sur <a href="/recherche/logique-philosophique/systeme-en-formules/">Le système en formules</a>, ce joint est le seul souligné double de toute la charpente. Et comme il y a plusieurs personnes, la vérité passe par un accord — ce qui explique qu'un traité de psychologie finisse sur le <em>contrat social</em>.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="partie III">
<summary class="dp-titre"><span class="dp-rang">ch. XX-XXV</span><span class="dp-texte">Les probabilités touchant l'ordre moral du monde. L'immortalité, la liberté, la divinité</span></summary>
<div class="dp-corps">
<p>Le titre suffit à situer la manœuvre : ce sont les trois postulats de la raison pratique de Kant — liberté, immortalité, Dieu — repris un par un. Mais Renouvier n'en fait pas des postulats : il en fait des <strong>probabilités morales</strong>, et il ose leur consacrer un chapitre de réfutation frontale.</p>
<ul class="dp-liste">
<li><strong>XX</strong> — De l'immortalité comme loi téléologique de la nature.</li>
<li><strong>XXI</strong> — <em>Examen des thèses de la raison pratique de Kant.</em></li>
<li><strong>XXII</strong> — De la liberté et de la destinée immortelle de l'homme.</li>
<li><strong>XXIII</strong> — De la croyance la plus large en la divinité.</li>
<li><strong>XXIV</strong> — Des moyens physiques de l'immortalité.</li>
<li><strong>XXV</strong> — Des hypothèses rationnelles sur la nature de Dieu.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Où mène le pivot, tout au bout</span>
<p>Un Dieu infini en acte étant contradictoire, il ne reste qu'un Dieu <em>fini</em> — une personne, à qui manquent les « perfections » de la métaphysique mais à qui restent la justice et la bonté. Et si Dieu est une personne parmi d'autres, alors rien ne prouve plus qu'il soit un seul : Renouvier écrit noir sur blanc que « deux directions de l'esprit sont possibles, légitimes », l'unité et la pluralité.</p>
<p>Suivez la ligne depuis le début : une thèse sur le nombre, en 1854, aboutit en 1875 à rendre le polythéisme rationnellement recevable. C'est la même déduction qui court sur vingt et un ans et huit tomes.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le pli de Renouvier">
<summary class="dp-titre"><span class="dp-rang">fin du tome III</span><span class="dp-texte">Formulaire du Traité de Psychologie rationnelle</span></summary>
<div class="dp-corps">
<p>Le second grand pli de l'œuvre, et le plus utile de tous, parce qu'il est structuré. Quatre sections, dans l'ordre des trois parties du livre :</p>
<ul class="dp-liste">
<li><strong>A. L'analyse des fonctions humaines</strong> — les neuf catégories, chacune avec sa fonction : Relation → Comparaison ; Position → Imagination ; Succession → Mémoire ; … Personnalité → <em>Liberté</em>.</li>
<li><strong>B. La question de la certitude</strong> — les deux ordres, et la liberté comme principe des principes.</li>
<li><strong>C. La classification des sciences</strong> — avec un tableau qui range toute la connaissance sous les catégories : la logique et les mathématiques d'un côté (qualité, nombre), les sciences physiques de l'autre.</li>
<li><strong>D. Les probabilités morales</strong> — immortalité, liberté, divinité.</li>
</ul>
<div class="dp-cite">
<p>L'homme est une fonction particulière de toutes les fonctions données dans le monde, et qui tombent sous la connaissance : toutes les catégories sont impliquées dans la représentation de l'homme pour l'homme, aussi bien que dans la représentation du monde pour l'homme.</p>
<span class="dp-source">Formulaire du Traité de Psychologie rationnelle, première phrase</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Relisez cette phrase après « lois »</span>
<p>« Un être est une fonction », disait le Formulaire du Premier Essai. « L'homme est une fonction particulière », dit celui du Deuxième. Ce n'est pas une variation de style : c'est la définition générale, appliquée au cas de l'homme. Et la suite de la phrase donne le programme du double miroir — les mêmes catégories pour l'homme et pour le monde.</p>
</div>
<p class="dp-chapo">Ce formulaire est aussi l'ouverture du Troisième Essai. C'est le seul texte de Renouvier qui existe à deux endroits et en deux âges.</p>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai III · 1864 / 1892</span><span class="dp-texte">Les Principes de la nature</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Deux tomes, douze chapitres seulement — mais précédés de cent pages d'introduction qui sont le formulaire du livre précédent. Le plus court des Essais, et le plus étrange.</p>

<details class="dp-pli" data-rang="entrée">
<summary class="dp-titre"><span class="dp-rang">ch. I</span><span class="dp-texte">« Je m'arrête au seuil même de l'histoire »</span></summary>
<div class="dp-corps">
<p>Le chapitre s'appelle <em>Résumé. Plan.</em> et il fait exactement cela : il récapitule les deux Essais précédents, puis trace le trajet du troisième. C'est le meilleur endroit de l'œuvre pour comprendre d'un coup pourquoi il y a quatre livres.</p>
<div class="dp-cite">
<p>Ainsi, dans le <em>Premier Essai</em>, l'étude des principes de la raison pure et l'établissement des lois générales, ou catégories, aboutissaient à la reconnaissance des limites du savoir ; dans le <em>Deuxième Essai</em>, l'analyse des fonctions humaines a conclu à la croyance morale et aux fondements d'une raison pratique sérieuse […]. A la fin du premier se marquait le besoin de descendre des thèses les plus abstraites et des extrémités de la spéculation universelle à un sujet concret : l'Homme ; en terminant le deuxième, je me suis trouvé, d'un côté, à l'entrée de la morale, de l'autre, sur la limite des religions, et j'ai senti la nécessité de donner une matière nouvelle à l'analyse : l'histoire.</p>
<span class="dp-source">Troisième Essai, ch. I — Résumé. Plan.</span>
</div>
<p>Puis il annonce le plan du présent volume, et sa dernière phrase est une porte :</p>
<div class="dp-cite">
<p>Je commence par traiter du fond et des modes premiers et universels de l'existence physique, en suivant la méthode exposée dans les <em>Essais</em> précédents. […] Je passe aux hypothèses cosmogoniques et au problème des espèces. […] Je m'arrête enfin en amenant l'homme sur la scène, c'est-à-dire au seuil même de l'histoire.</p>
<span class="dp-source">Troisième Essai, ch. I</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La descente</span>
<p>Les quatre Essais forment une descente continue de l'abstrait au concret : les catégories, puis l'homme, puis la nature, puis l'histoire. Chaque livre finit là où le suivant commence, et Renouvier le dit à chaque fois. Ce n'est pas une série d'ouvrages sur des sujets voisins : c'est un seul mouvement, en quatre paliers, qui met vingt-cinq ans à descendre.</p>
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
<span class="dp-etiquette">La même machine, un cran plus bas</span>
<p>La section C du formulaire précédent avait rangé les sciences sous les catégories. Ces chapitres font le travail : les fonctions <em>mécaniques</em> n'impliquent que Nombre, Position, Succession et Devenir ; les fonctions <em>chimiques et physiques</em> ajoutent la Qualité ; les fonctions <em>biologiques</em> apportent enfin la Causalité, la Finalité et la conscience.</p>
<p>C'est une échelle des êtres construite avec les neuf pièces : chaque étage de la nature se définit par le nombre de catégories qu'il faut pour le décrire. Un caillou en demande quatre. Un vivant les demande toutes.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et l'atome ?</span>
<p>Il tombe, évidemment. Un atome au sens strict serait un simple, un indivisible en soi — donc un terme de gauche sans son contraire, donc un fétiche. Renouvier ne peut pas plus admettre l'atome que l'infini : ce sont les deux bouts de la même erreur, le trop petit absolu et le trop grand absolu.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="ch. VIII-XII">
<summary class="dp-titre"><span class="dp-rang">les origines</span><span class="dp-texte">Darwin, les espèces, et une cosmogonie très étrange</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>VIII</strong> — Critique des doctrines cosmogoniques physiques.</li>
<li><strong>IX</strong> — Suite. — <em>Question des espèces.</em></li>
<li><strong>X</strong> — Critique des systèmes de cosmogonie morale.</li>
<li><strong>XI</strong> — L'origine de l'homme.</li>
<li><strong>XII</strong> — Les origines premières et morales.</li>
</ul>
<p>Renouvier discute Darwin dans le texte, et sans mépris — ce qui est rare chez lui :</p>
<div class="dp-cite">
<p>On remarque dans la doctrine de Darwin, au moins avant qu'il eût été gagné à l'entraînement de ses disciples, cet heureux mélange de la spéculation libre avec les faits respectés et inaltérés, cet usage de l'induction à la fois mesurée et hardie […].</p>
<span class="dp-source">Troisième Essai, ch. IX</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le chapitre le plus étrange de toute l'œuvre</span>
<p>Au chapitre XII, Renouvier avance une hypothèse dont il faut mesurer l'audace : l'humanité et la nature auraient été créées à l'état d'« organisme universel et réellement parfait, laissant aux individus la liberté » ; cette liberté aurait causé la perversion de la société primitive ; d'où « la ruine entière du monde, d'où la nature actuelle serait sortie en traversant la période occupée par la formation des nébuleuses et par la constitution des astres ».</p>
<p>Traduisez : la nébuleuse primitive de Laplace, les étoiles, les planètes, la mort, la lutte pour la vie — tout cela serait le <em>débris</em> d'une chute morale. Le cosmos n'est pas le décor du drame : il en est le résultat.</p>
<p>Et Renouvier, qui n'était pas homme à reculer, recule : « chez moi, la haute conjecture s'arrête, intimidée ».</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Pourquoi il y est obligé</span>
<p>Ce n'est pas un accès de mysticisme. C'est une contrainte. Si le nombre est fini, le monde a commencé. S'il a commencé, il y a des causes premières. Si le mal existe et que Dieu est bon, la cause première du mal ne peut pas être Dieu : il faut donc une liberté première, et une faute. La cosmogonie de Renouvier est la seule qui reste debout quand on a interdit l'infini <em>et</em> refusé de faire de Dieu l'auteur du mal.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">Essai IV · 1864</span><span class="dp-texte">Introduction à la philosophie analytique de l'histoire</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Trente-deux paragraphes, cinq parties. Le seul des quatre Essais où l'on croise des dieux égyptiens, des tribus polynésiennes et des tablettes assyriennes — et c'est le même livre que le premier.</p>

<details class="dp-pli" data-rang="§ I">
<summary class="dp-titre"><span class="dp-rang">le plan</span><span class="dp-texte">Ce que « analytique » interdit</span></summary>
<div class="dp-corps">
<p>Renouvier annonce sa méthode par ce qu'il refuse, et la liste des refus est la vraie table des matières :</p>
<div class="dp-cite">
<p>Abordée sans critique, l'histoire ne peut que multiplier, en les amplifiant, ces mêmes phénomènes incohérents que donne déjà l'expérience individuelle toute seule quand la loi morale ne règle pas la conduite et le jugement. Traitée dans un système apriorique, elle défigure les faits, ou elle les dédaigne ; elle en rejette et elle en interpole, afin de disposer plus commodément les autres en série.</p>
<span class="dp-source">Quatrième Essai, § I</span>
</div>
<p>Deux façons de manquer l'histoire, donc : sans idée, ou avec une idée d'avance. La voie étroite entre les deux, c'est ce qu'il appelle l'analyse : des faits établis par les sciences historiques, des inductions tirées de ce que la personne humaine a de constant, et rien de plus.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Il faut avoir lu les trois autres</span>
<p>Ce livre est illisible seul, et voici pourquoi. La quatrième partie du <strong>Premier Essai</strong> a démontré que la synthèse totale est impossible : une philosophie de l'histoire au sens de Hegel <em>est</em> une synthèse totale, donc elle est interdite avant même d'être examinée sur pièces. Le <strong>Deuxième</strong> a fourni la seule chose qui reste pour juger — une personne libre, avec ses passions, sa mémoire et son vertige : les renvois y sont constants (§ V pour le langage, § XI et XII pour le vertige, § XXV pour Dieu). Le <strong>Troisième</strong> a déposé l'homme au seuil.</p>
<p>Le Quatrième Essai est ce qui reste de la philosophie de l'histoire quand on a retiré le droit de conclure sur le tout : des faits, des lois partielles, et une conscience pour juger.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="I-V">
<summary class="dp-titre"><span class="dp-rang">le mouvement</span><span class="dp-texte">Les cinq parties</span></summary>
<div class="dp-corps">
<ul class="dp-liste">
<li><strong>I. Les origines</strong> <em>(§ II-IX)</em> — Les commencements de l'humanité examinés à partir de la théorie de Kant, puis contre elle. Origine historique des vertus et des vices. Solidarité du bien et du mal. C'est la partie théorique : le problème du mal et du « premier manquement ».</li>
<li><strong>II. Les religions les plus basses, puis la Chine et l'Égypte</strong> <em>(§ X-XVII)</em> — Les lois de la critique appliquées aux religions ; le sentiment religieux dans l'état moral le plus bas ; religions de tribus ; origines chinoises ; religion patriarcale des Chinois et des Japonais ; religions locales de l'Égypte.</li>
<li><strong>III. Les Aryens</strong> <em>(§ XVIII-XXVI)</em> — L'esprit mythologique ; mythes et culte de l'Arye primitive ; anthropomorphisme et panthéisme ; origines helléniques ; l'esprit des races italiques ; la <em>Religio</em> des Romains ; Germains, Celtes.</li>
<li><strong>IV. Les Sémites</strong> <em>(§ XXVII-XXXI)</em> — Origines sémitiques, la partie la plus longue et la plus disputée.</li>
<li><strong>V. La reprise</strong> <em>(§ XXXII)</em> — Où Renouvier dit ce qu'il a fait, et pourquoi tant de faits dans un livre de philosophie.</li>
</ul>
<div class="dp-note">
<span class="dp-etiquette">Pourquoi tant d'érudition</span>
<p>Il s'en explique lui-même à la fin : les savants « manquent communément de philosophie », et les philosophes ignorent les résultats des savants. Il fallait donc quelqu'un pour tenir les deux bouts. « C'est à d'autres qu'eux-mêmes qu'il est donné de mettre leurs découvertes en place et de les utiliser. » Le Quatrième Essai est une tentative pour faire ce travail — en 1864, quand l'assyriologie et la mythologie comparée sortent à peine de terre.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="le coup">
<summary class="dp-titre"><span class="dp-rang">§ XXXII</span><span class="dp-texte">Les sphères de Ptolémée</span></summary>
<div class="dp-corps">
<p>Le jugement le plus dur et le plus juste que Renouvier ait porté sur ses rivaux tient en une image, et il faut la lire jusqu'au bout car le venin est dans la queue :</p>
<div class="dp-cite">
<p>Hegel et Comte, aussi bien que Bossuet et Vico, traitent l'histoire comme Eudoxe et Ptolémée traitaient l'astronomie, avec leurs sphères idéales. Mais ces derniers satisfaisaient aux mouvements des corps célestes, tels qu'ils les constataient ; leurs théories permettaient la prévision dans une suffisante mesure, tandis que les philosophes écrivent leurs <em>équations</em> historiques en sacrifiant les faits […].</p>
<span class="dp-source">Quatrième Essai, § XXXII</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le sens de la pointe</span>
<p>Ptolémée se trompait, mais ses sphères marchaient : elles prédisaient les éclipses. Hegel et Comte, eux, ont les sphères sans les prédictions. Ils sont donc <em>en dessous</em> de Ptolémée. Ce n'est pas les traiter d'anciens : c'est leur refuser jusqu'au statut de mauvaise science.</p>
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

Ce dépliant obéit à six règles. Elles sont notées ici pour que le lecteur sache à quoi il a affaire, et pour que d'autres livres puissent être pliés de la même façon.

1. **Le pli conserve tout.** Déplier n'est pas résumer : c'est ajouter de la résolution. Le sommet est la compression maximale, le fond est le texte même. Rien n'est perdu en route, rien n'est ajouté qui ne soit vérifiable.
2. **Les sœurs restent.** Ouvrir une voie n'en referme aucune autre. Les chemins non pris demeurent visibles, repliés, à côté du chemin pris. C'est ce qui remplace le sommaire.
3. **La profondeur se voit.** Chaque niveau ajoute un filet à gauche. On compte les filets comme on compte les plis d'un papier ouvert.
4. **Le parcours se souvient.** Un pli jamais ouvert porte une pastille pleine ; une fois ouvert, elle se creuse. Le compteur dit combien de plis restent inexplorés. C'est la réponse au seul problème sérieux de ce format : savoir, une fois au fond, ce qu'on n'a pas vu.
5. **La typographie dit qui parle.** Sérif : Renouvier, verbatim, avec sa référence. Linéale : le commentaire. Aucun mot n'est prêté à Renouvier qu'il n'ait écrit.
6. **Les paliers sont de l'auteur quand ils existent.** Renouvier a résumé lui-même chacun de ses Essais dans un *Formulaire*. Partout où c'était possible, le niveau intermédiaire est le sien, cité, et non une paraphrase.

**Ce qui reste à déplier.** Les *Observations et développements* de la seconde édition n'ont pas été ouverts : Renouvier avertit qu'il n'y « introduit aucun changement de quelque importance dans l'esprit ni dans les preuves ni dans les conclusions ». Ils discutent Mill, Hamilton, Spencer, Comte, et publient Lequier ; ils ne touchent pas la charpente. Ils feront un étage supplémentaire.

**Sources.** Premier Essai : *Traité de logique générale et de logique formelle*, 2ᵉ éd., Au Bureau de la Critique philosophique, 1875, 3 t. — Deuxième Essai : *Traité de psychologie rationnelle d'après les principes du criticisme*, 2ᵉ éd. revue et considérablement augmentée, même éditeur, 1875, 3 t. — Troisième Essai : *Les Principes de la nature*, 2ᵉ éd. corrigée et augmentée, 1892, 2 t. — Quatrième Essai : *Introduction à la philosophie analytique de l'histoire*, Ladrange, 1864.
