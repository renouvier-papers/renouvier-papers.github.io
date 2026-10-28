---
title: "Comment je suis arrivé à cette conclusion"
description: "Ce que Renouvier a changé entre 1854 et 1903, ce qu'il en a dit et ce que les textes en montrent."
---

# Comment je suis arrivé à cette conclusion

Renouvier a donné ce titre au dernier chapitre de son *Esquisse d'une classification systématique des doctrines philosophiques*, tome II, 1886, où il raconte en vingt-cinq mille mots comment il a changé d'avis.

Dix-sept ans plus tard, dans la préface du dernier livre paru de son vivant, il fait remonter sa doctrine à son premier livre, **« dès son origine »**, et ne présente plus le changement que comme un complément tardif.

Cette page tient les deux bouts. Sans chercher à prendre un vieil homme en défaut, elle se sert de ce qu'il a laissé (un aveu daté, un résumé publié trois fois dont la dernière édition signale ses repentirs, une préface qui n'y voit plus qu'un complément) pour mesurer ce qu'on ne mesure presque jamais, **de combien une pensée bouge, et par où.**

Fermée, la page tient en quatre mots ; chaque terme s'ouvre sur ce qu'il contient. **Ouvrir un pli ne fait rien disparaître.**

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
/* --- L'appareil critique ---
   Deux états d'une même phrase, l'un sous l'autre, la variante seule en relief.
   C'est la figure de cette page : tout le reste du texte est identique, et c'est
   précisément ce qui rend le mot changé lisible. */
#dp .dp-variante {
  margin: 1rem 0; border: 1px solid var(--dp-rule); border-radius: 2px; overflow: hidden;
}
#dp .dp-var-ligne {
  display: grid; grid-template-columns: 3.2rem 1fr; gap: .7rem; align-items: baseline;
  padding: .6rem .8rem; font-family: var(--dp-serif); font-size: .92rem; line-height: 1.55;
}
#dp .dp-var-ligne + .dp-var-ligne { border-top: 1px solid var(--dp-faint); }
#dp .dp-var-an {
  font-family: var(--dp-sans); font-size: .63rem; letter-spacing: .09em;
  color: var(--dp-muted); font-variant-numeric: tabular-nums; white-space: nowrap;
}
#dp .dp-var-ligne--neuf { background: var(--dp-faint); }
#dp .dp-var-ligne--neuf .dp-var-an { color: var(--dp-accent); font-weight: 700; }
#dp .dp-avant { text-decoration: line-through; text-decoration-thickness: 1px; opacity: .55; }
#dp .dp-apres { color: var(--dp-accent); font-weight: 700; }
#dp .dp-ajout {
  color: var(--dp-accent); box-shadow: inset 0 -.5em 0 -.1em var(--dp-faint);
}
@media (max-width: 44rem) {
  #dp .dp-var-ligne { grid-template-columns: 1fr; gap: .1rem; }
}

/* --- La balance : ce qui entre, ce qui sort, ce qui ne bouge pas --- */
#dp .dp-balance { display: grid; gap: .35rem; margin: 1rem 0; }
#dp .dp-poste {
  display: grid; grid-template-columns: 1.5rem 1fr; gap: .6rem; align-items: baseline;
  padding: .42rem .7rem; border-left: 2px solid var(--dp-rule); font-size: .85rem;
}
#dp .dp-poste--plus { border-left-color: var(--dp-accent); }
#dp .dp-poste--socle { border-left-style: dotted; }
#dp .dp-signe { font-family: var(--dp-serif); font-weight: 700; text-align: center; color: var(--dp-muted); }
#dp .dp-poste--plus .dp-signe { color: var(--dp-accent); }
#dp .dp-renvoi { margin: .95rem 0 0; font-size: .8rem; color: var(--dp-muted); }
#dp .dp-renvoi a { color: var(--dp-accent); }
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<p class="dp-chapo">Charles Renouvier — <em>Esquisse d'une classification systématique des doctrines philosophiques</em>, tome II, 1886, dernier chapitre. Le titre est de lui ; les quatre mots ci-dessous sont les siens.</p>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">Comment</span></summary>
<div class="dp-corps">
<p>Le premier mot signale une question de méthode que Renouvier se pose à lui-même. Ce chapitre s'ouvre sur la thèse que tout système est une affaire personnelle :</p>
<div class="dp-cite">
<p>[…] chacun d'eux est l'œuvre personnelle, ou du moins l'affirmation personnelle d'un penseur, placé sous l'influence d'un certain tempérament intellectuel et passionnel, d'une certaine éducation, d'un certain milieu […].</p>
<span class="dp-source">Esquisse, t. II, ch. « Comment je suis arrivé à cette conclusion »</span>
</div>
<p>Il en tire lui-même, et non nous, la règle qui commande cette page-ci :</p>
<div class="dp-cite">
<p>[…] on trouvera presque toujours que c'est une considération de sentiment, ou d'ordre pratique, au fond, qui a été le mobile.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que « comment » exclut</span>
<p>La question est « par quel chemin suis-je venu », non « pourquoi ai-je raison ». Renouvier réclame pour l'histoire de la philosophie ce qui n'existe pas, non des <em>confessions</em>, dit-il, mais « des monographies de la marche de la réflexion et de l'enchaînement des idées systématiques ». Il sait pourquoi elles manquent :</p>
</div>
<div class="dp-cite">
<p>[…] les philosophes […] veulent autant que possible dérober à autrui leurs variations et leurs erreurs, et se les dissimuler à eux-mêmes. […] On dirait qu'ils se croient immuables, ou qu'ils jugent absurde de le paraître. Et tout naturellement l'infaillibilité accompagne l'immutabilité.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<p>Cette phrase sera, dix-sept ans plus tard, la mesure du récit qu'il fera de sa propre variation.</p>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">je</span></summary>
<div class="dp-corps">
<p>Écrire « je » dans un traité de classification des doctrines déroge à l'usage. Renouvier reproche pourtant aux autres de ne jamais le faire :</p>
<div class="dp-cite">
<p>Chaque penseur dogmatique, en vertu d'une fiction dont il est dupe et dont le public a pris l'habitude, […] enseigne et décrète en se targuant de l'autorité d'une raison impersonnelle et d'une expérience commune à tous les hommes.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">La cohérence de ce « je »</span>
<p>Ce choix est une conséquence, non une coquetterie d'auteur. Si la vérité est affirmée par une liberté (le Deuxième Essai pose que « le principe de ces principes est la liberté »), aucune raison impersonnelle ne parle toute seule. Un philosophe qui écrirait sans « je » mentirait sur sa propre doctrine. Le personnalisme oblige à l'autobiographie.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">suis arrivé</span></summary>
<div class="dp-corps">
<p>Ce mot décide de tout. <strong>Arriver, c'est avoir bougé.</strong></p>
<p>En 1886, un titre de chapitre dit que l'auteur est <em>arrivé</em> à cette conclusion, donc qu'il n'y était pas. La préface du dernier livre, en 1903, fait remonter l'essentiel à l'origine :</p>
<div class="dp-cite">
<p>Le néocriticisme, <em>dès son origine</em> (<em>Essais de critique générale, Premier essai</em>, 1854. — <em>Deuxième essai</em>, 1859) est en opposition décisive avec tous les points caractéristiques de la doctrine kantienne, un relativisme net, qui est en même temps le personnalisme.</p>
<span class="dp-source">Le Personnalisme, 1903, préface</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'écart qui résume la page</span>
<p>Le <em>je suis arrivé</em> de 1886 et le <em>dès son origine</em> de 1903 ne se contredisent pas terme à terme, puisque la préface reconnaît, quatre paragraphes plus loin, que la doctrine « a été plus tardive à se compléter » par l'unité de la personne première. Les deux racontent pourtant des histoires différentes, un chemin en 1886, un achèvement en 1903. Renouvier avait écrit, dans le chapitre de 1886, que les philosophes dérobent leurs variations ; en 1903, sans dérober la sienne, il l'appelle un complément.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">à cette conclusion</span></summary>
<div class="dp-corps">
<p>Le chapitre s'appuie sur le précédent (<em>Optimisme et pessimisme. — Le monde moral. — Le fait moral.</em>), mais la conclusion à laquelle Renouvier est arrivé, et qu'il n'avait pas au départ, tient en cinq mots :</p>
<p class="dp-epigraphe">l'unité de la conscience première</p>
<p>La formule désigne un Dieu unique, créateur, et fini. Si le dernier trait était acquis de longue date, les deux premiers sont nouveaux. Le Premier Essai inclinait vers une pluralité de consciences premières, et le résumé de 1875 tenait encore la question pour indécise.</p>
</div>
</details>

<p class="dp-epigraphe">— la page en une phrase —</p>
<p class="dp-these">En 1886, Renouvier écrit que les philosophes dissimulent leurs variations et se croient immuables, puis raconte les siennes sur vingt-cinq mille mots. Il consigne le changement en 1892 dans un résumé, en signalant ses propres repentirs. En 1903, il fait remonter sa doctrine à 1854 et ne voit plus dans ce changement qu'un complément.</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">↓ déplier</span><span class="dp-texte">La page en un paragraphe</span></summary>
<div class="dp-corps">
<p>En 1854, le Premier Essai conclut qu'une conscience du tout est contradictoire ; son Formulaire en tire que <strong>la pluralité des consciences premières</strong> « semble donc la seule rationnelle ». Trente ans plus tard, Renouvier applique au monde entier sa propre thèse de jeunesse, pas de loi sans phénomène, pas de phénomène sans conscience, et <strong>elle produit Dieu</strong>, car des lois partout les mêmes exigent une conscience une qui les ait posées. Il l'écrit en 1886, dans un chapitre autobiographique où il avoue <strong>le mobile</strong>, à savoir que les postulats de la raison pratique ont besoin de garanties que la pluralité ne donne pas. En 1892, il <strong>réédite son propre résumé</strong> et y consigne le changement par deux opérations mesurables au mot, qu'il signale en note. Puis, en 1903, il <strong>n'y voit plus qu'un complément</strong>. Le compte de ce qui est entré, de ce qui est sorti et de <strong>ce qui n'a jamais bougé</strong> reste pourtant faisable. Sur le socle, il a raison ; mais ce qu'il appelle un complément est un renversement, qui rendra possible, à la dernière page de son dernier livre, <strong>l'harmonie préétablie</strong>.</p>
<p class="dp-chapo">Chacun des sept termes en gras s'ouvre ci-dessous. On peut s'arrêter à ce paragraphe, qui dit l'essentiel, ou tirer sur un fil.</p>

<details class="dp-pli" data-rang="1854">
<summary class="dp-titre"><span class="dp-rang">le départ</span><span class="dp-texte">la pluralité des consciences premières</span></summary>
<div class="dp-corps">
<p>Le Premier Essai s'achève sur la ruine de la synthèse totale. Son chapitre LIII demande s'il peut exister une conscience du monde entier, et le nie, car la conscience est la synthèse du soi et du non-soi ; celle qui envelopperait tout n'aurait pas de non-soi et cesserait d'être une conscience. Reste un résidu déterminant :</p>
<div class="dp-cite">
<p>[…] l'hypothèse d'une pluralité primitive de consciences distinctes, dans le monde, semble donc la seule rationnelle […].</p>
<span class="dp-source">Premier Essai, t. III, Formulaire du Traité de logique générale, p. 289 (résumé du ch. LIII)</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que cette conclusion interdit</span>
<p>La conscience du tout est exclue par logique, non par athéisme, et nul sommet n'embrasse le monde. À l'origine, il <em>semble</em> donc y avoir plusieurs consciences, indépendantes ; la question d'un Dieu unique reste ouverte, et le résumé de 1875 tient encore pour « possibles, légitimes » les deux directions, unité ou pluralité. En 1886, Renouvier tranchera pour l'unité de la conscience première, à partir des mêmes prémisses et sans revenir sur l'exclusion de la conscience du tout.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="1886">
<summary class="dp-titre"><span class="dp-rang">l'argument</span><span class="dp-texte">elle produit Dieu</span></summary>
<div class="dp-corps">
<p>Ce passage de 1886 se borne à appliquer au monde entier l'une des prémisses de la doctrine de 1854 :</p>
<div class="dp-cite">
<p>Le monde, envisagé sous toutes les catégories, implique donc une communauté de lois. Mais dire communauté, c'est dire unité, autant que la communauté s'étend, et l'unité de loi est elle-même une loi. […] Mais, pour la méthode qui n'admet ni loi sans phénomènes, ni phénomènes sans conscience […], une loi une et universelle […] ne peut exister qu'à la condition d'une conscience une et universelle donnée à cet objet.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le retournement du phénoménisme</span>
<p>La prémisse est celle de 1854, <em>pas de loi sans phénomène, pas de phénomène sans conscience.</em> Arme contre la métaphysique, elle servait à abolir la substance et la chose en soi. Appliquée au monde entier, elle produit l'inverse. Si l'espace, le temps et la causalité sont partout les mêmes pour toutes les consciences, cette communauté est une loi ; or une loi doit être représentée dans une conscience ; il existe donc une conscience une et universelle.</p>
<p>Renouvier ne s'est pas converti, mais il a déplié une conséquence qui lui avait échappé et que sa prémisse contenait depuis trente ans.</p>
</div>
<p>Deux garde-fous, deux thèses constantes de son œuvre, tiennent dans l'opération. Le premier préserve le pivot, puisque cette conscience est une et universelle <strong>« à la réserve expresse de l'infinité, qui doit toujours être exclue »</strong> ; le second exige qu'elle soit libre, sans quoi elle aurait des antécédents, « ce qui est contraire à notre thèse du <em>pur commencement</em> ».</p>
<p>Le renversement est complet. En 1854, la pluralité était première. Le texte de 1886 porte :</p>
<div class="dp-cite">
<p>Il faut avoir admis d'abord l'unité et universalité de conscience pour l'explication de cet ordre. Cela fait, un passage de l'unité à la pluralité des consciences est à chercher […] ; il ne nous reste donc plus que l'idée rigoureuse de la création […].</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<p>L'unité est devenue l'origine, la pluralité le dérivé, et le mot de création est lâché.</p>
</div>
</details>

<details class="dp-pli" data-rang="1886">
<summary class="dp-titre"><span class="dp-rang">l'aveu</span><span class="dp-texte">le mobile</span></summary>
<div class="dp-corps">
<p>On chercherait volontiers une cause, découverte scientifique, lecture, conversion ou maladie. Renouvier a devancé la question et y répond deux fois, en général puis sur lui-même.</p>
<p>En général, au début du chapitre, par une phrase citée plus haut :</p>
<div class="dp-cite">
<p>[…] on trouvera presque toujours que c'est une considération de sentiment, ou d'ordre pratique, au fond, qui a été le mobile.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<p>Sur lui-même, au terme de l'argument :</p>
<div class="dp-cite">
<p>[…] la raison pratique aura de la peine à trouver pour ses postulats d'aussi claires garanties que dans l'hypothèse de l'unité de conscience première.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La réponse</span>
<p>Le mobile n'est ni la science, ni la santé, ni un déménagement, ni une conversion. <strong>Les postulats avaient besoin de garanties.</strong> La liberté, l'immortalité et Dieu, les trois thèses de la troisième partie du Deuxième Essai, ne peuvent reposer sur une poussière de consciences indépendantes. Il leur faut un ordre, et tout ordre requiert une origine.</p>
<p>L'aveu est remarquable non par son contenu, mais parce que son auteur s'y applique le diagnostic qu'il venait de porter sur tous les autres. Il avait écrit que le mobile est « presque toujours » pratique. Le sien l'est.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Une règle de méthode</span>
<p>Aucune conjecture n'a été nécessaire. Tout se trouvait à l'adresse que Renouvier avait laissée en note dans son résumé de 1892, « <em>Esquisse</em>, t. II, pp. 108 sq., 348 sq., 395 jusqu'à la fin », dont le dernier renvoi désigne les pages mêmes qu'on vient de lire. Avant de chercher une cause dans la vie d'un auteur, il faut avoir suivi ses renvois.</p>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">l'adresse</span><span class="dp-texte">Trois renvois qui forment un plan</span></summary>
<div class="dp-corps">
<p>Ils se lisent dans l'ordre de leur citation, celui des pages, et forment trois étages dont chacun accomplit un travail que les deux autres ne peuvent faire. Le dernier, « 395 jusqu'à la fin », correspond à l'argument de l'unité et à l'aveu du mobile, dépliés plus haut. Restent les deux premiers et, hors renvoi, une page de la Conclusion qui fait le même pas par la morale.</p>

<p class="dp-epigraphe">p. 108 — le permis de construire</p>
<p>Renouvier y démonte « un système de philosophie qui établit son fondement dans les sciences ». Spencer transporte aux rapports de la représentation une loi empruntée à l'histoire naturelle, et la nébuleuse primitive du physicien devient chez le métaphysicien ce qu'on eût appelé « l'être universel en puissance ». L'Inconnaissable placé derrière tout cela ne sauve rien :</p>
<div class="dp-cite">
<p>Mais placer un <em>Absolument inconnu</em> en arrière d'un système qu'on dit qui enveloppe tout le connaissable, c'est comme n'y rien mettre.</p>
<span class="dp-source">Esquisse, t. II, p. 107-108</span>
</div>
<p>L'étage conclut que ces systèmes se fondent sur des croyances qui s'ignorent, et non sur l'évidence. <strong>Si même les philosophies qui se disent scientifiques reposent sur des croyances, croire est légitime.</strong> Sans ce préalable, les deux étages suivants seraient irrecevables.</p>

<p class="dp-epigraphe">Hors renvoi, p. 305 — l'argument pratique</p>
<p>Le pari est ici celui de <strong>Locke</strong>, non de Pascal. Renouvier le cite sur deux pages, puis en tire ceci :</p>
<div class="dp-cite">
<p>[…] il s'ensuit que le pari par l'acte et le pari par la croyance sont, dans le fait, inséparables. […] nous voyons aussitôt qu'elle a pour objet l'existence d'une sanction suprême de la morale, ou [en] d'autres termes, un ordre moral du monde, qui, <em>vu son universalité</em>, doit se nommer un ordre divin, et qui assure, suivant la formule de Kant, l'harmonie du bonheur et de la vertu.</p>
<span class="dp-source">Esquisse, t. II, p. 305 — « [en] » : mot absent de la transcription, rétabli</span>
</div>

<div class="dp-note">
<span class="dp-etiquette">Pascal, classé ailleurs depuis longtemps</span>
<p>Une Observation du ch. XII démonte le pari pascalien thèse à thèse. Renouvier expose ainsi la troisième, selon laquelle l'intérêt nous <em>somme</em> de conclure :</p>
<div class="dp-cite">
<p>Notre intérêt est d'affirmer que c'est la croix qui a raison. Ceci se prouve par le <em>calcul des chances</em> […].</p>
<span class="dp-source">Deuxième Essai, ch. XII, Observations et développements, A — Pascal et la théorie du vertige moral. Renouvier exposant la troisième thèse de Pascal.</span>
</div>
<p>Le dossier est rangé sous un titre qui juge, le <em>vertige moral</em>, soit l'intérêt qui fait tourner la tête, non la balance qui pèse. C'est pourquoi le pari revient en 1886 « de Locke », comme croyance déjà engagée dans l'acte et non comme sommation par l'enjeu.</p>
</div>
<p class="dp-epigraphe">p. 348 — l'argument théorique, et la synthèse</p>
<div class="dp-cite">
<p>La plus haute conception à laquelle [nous a] conduit notre méthode, après que nous avons exclu l'absolu […], c'est la conscience première et universelle, auteur du monde, libre créateur[s] d'êtres libres. La preuve de l'unité de cet <em>Être suprême</em>, nous l'avons trouvée […] dans le fait de l'existence de lois générales et harmoniques établissant les rapports uniformes des phénomènes et la communication des consciences. Cette harmonie, en effet, implique l'unité d'une conscience qui la conçoit et la réalise […].</p>
<span class="dp-source">Esquisse, t. II, p. 348-349 — « [nous a] » : passage altéré dans la transcription (« je me suis conduire »), restitué ; « créateur[s] » : la transcription porte « créateurs »</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Une seule inférence, faite deux fois</span>
<p>Abstraction faite de leur matière, les deux arguments ont la même forme. <strong>Ordre moral universel → ordre divin. Lois universelles → conscience une.</strong> Le pas, de l'universalité à l'unité, est franchi une fois par la morale et une fois par la théorie.</p>
<p class="dp-renvoi">Ce joint, de l'unité des lois à la conscience une, est le seul trait ondulé du <a href="/recherche/logique-philosophique/systeme-en-formules/">Système en formules</a>, raccord qui tient tout en travaillant.</p>
<p>Cette manière de démontrer, par deux routes dissemblables menant à un seul point, lui est familière. Son dernier livre repose sur le même dispositif, la logique et la physique y arrivant séparément aux mêmes personnes.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le pivot borne aussitôt la conclusion</span>
<p>À peine Dieu posé comme un, la « condition du nombre » revient l'enfermer. Elle « nous force à penser Dieu comme fini à l'égard de l'ordre quantitatif des phénomènes », et il n'est « infini seulement (<em>c'est-à-dire parfait, comme on ferait mieux de s'exprimer</em>) en justice et sainteté ».</p>
<p>Par cette parenthèse, à soixante et onze ans et en pleine démonstration de l'existence de Dieu, Renouvier se reprend pour ne pas laisser passer le mot <em>infini</em>, même comme façon de parler.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Voltaire au milieu de la démonstration</span>
<p>Le paragraphe précédent, dans la même conclusion métaphysique, porte : « Le mot si profond d'un philosophe, cette recette unique contre les poisons de la vie et contre les théories pessimistes : <em>Il faut cultiver notre jardin</em>, n'est pas moins vrai des spéculations les plus élevées que de la philosophie pratique. » Puis : « Nous n'abordons aucune réalité, ni Dieu, ni le monde, ni les hommes, sans la porter vers nous. »</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="1892">
<summary class="dp-titre"><span class="dp-rang">la collation</span><span class="dp-texte">réédite son propre résumé</span></summary>
<div class="dp-corps">
<p>La pièce déterminante est de sa main.</p>
<p>Le <em>Formulaire du Traité de Psychologie rationnelle</em> clôt le Deuxième Essai en 1875. En 1892, Renouvier le remet en tête du Troisième Essai, sous le titre <em>Introduction — Résumé des principes de la psychologie rationnelle</em>. <strong>Le même texte à dix-sept ans d'écart</strong> garde ses quatre sections, sa première phrase et ses seize mille mots, et l'auteur prévient en note :</p>
<div class="dp-cite">
<p>En corrigeant cette troisième édition du résumé de mes <em>Essais</em>, j'ai tenu à conserver fidèlement la trace de la marche de mes idées. Dans cette intention, je me suis contenté de mettre sous une forme dubitative la conclusion qui, dans les deux premières éditions, se présentait seule et sans réserve ; et j'ai ajouté à celle-ci une conclusion définitive plus avancée dans le sens des postulats.</p>
<span class="dp-source">Troisième Essai, Introduction, note</span>
</div>
<p>Alignés mot à mot, les deux derniers états sont <strong>94,3 % identiques</strong>, ce qui rend les divergences lisibles. Les trois principales font ce que dit la note, et un peu plus.</p>

<details class="dp-pli" data-rang="variante 1">
<summary class="dp-titre"><span class="dp-rang">un mot</span><span class="dp-texte">La forme dubitative — « sont » devient « semblent »</span></summary>
<div class="dp-corps">
<p>La phrase, qui porte sur l'unité ou la pluralité de Dieu, est la « conclusion qui se présentait seule et sans réserve ».</p>
<div class="dp-variante">
<div class="dp-var-ligne"><span class="dp-var-an">1875</span><span>Deux directions de l'esprit <span class="dp-avant">sont</span> possibles, légitimes, et ne s'excluent même pas précisément</span></div>
<div class="dp-var-ligne dp-var-ligne--neuf"><span class="dp-var-an">1892</span><span>Deux directions de l'esprit <span class="dp-apres">semblent</span> possibles, légitimes, qui ne s'excluent même pas précisément</span></div>
</div>
<p>Si le verbe n'est pas seul à changer (« et ne s'excluent » devient « qui ne s'excluent », et « œuvres divines », « opérations divines »), c'est lui qui porte le sens. La phrase précédente suit le même chemin. « Mais alors <span class="dp-avant">font défaut</span> les raisons aprioriques » y fait place à « à ce point de vue, <span class="dp-apres">il semble que nous fassent</span> défaut les raisons <em>a priori</em> ».</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le prix d'un « semblent »</span>
<p>En 1875, l'équilibre entre unité et pluralité divines est un résultat. Les deux directions <em>sont</em> également légitimes, et la raison n'a rien à dire de plus. Le texte de 1892 ne le présente plus que sous réserve. Ce changement de verbe fait passer la thèse du rang de conclusion à celui d'hypothèse, et prépare le lecteur au « pas de plus », deux paragraphes plus loin.</p>
<p>Plutôt que de biffer sa conclusion de 1875, Renouvier l'a mise sous forme dubitative, et il l'a dit.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="variante 2">
<summary class="dp-titre"><span class="dp-rang">un accord</span><span class="dp-texte">La Critique change d'objet — « prises » devient « prise »</span></summary>
<div class="dp-corps">
<p>Dans le même tableau, la même case définit ce que la Critique étudie.</p>
<div class="dp-variante">
<div class="dp-var-ligne"><span class="dp-var-an">1875</span><span>A pour objet toutes les relations, <span class="dp-avant">conditions et idées de nécessité, finalité et personnalité</span>, <span class="dp-avant">prises</span> dans le monde et dans l'homme individuel et social.</span></div>
<div class="dp-var-ligne dp-var-ligne--neuf"><span class="dp-var-an">1892</span><span>A pour objet toutes les relations, <span class="dp-apres">représentations et opérations de la personnalité</span>, <span class="dp-apres">prise</span> dans le monde et dans l'homme individuel et social.</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le pluriel qui tombe</span>
<p>En 1875, la Critique porte sur trois choses, dont la personnalité, dernier terme d'une liste. Elle porte en 1892 sur la personnalité, et tout le reste en est une <em>opération</em>. Loin d'être supprimées, la nécessité et la finalité sont absorbées.</p>
<p>La grammaire prouve que le changement est délibéré. « Prises » s'accordait avec trois termes ; « prise » s'accorde avec un seul. <strong>Renouvier a corrigé l'accord derrière lui.</strong> Une coquille ne fait pas cela.</p>
</div>
<p>En 1892, le recentrement sur la personne figure dans une case de tableau, avec un « s » en moins. Le nom viendra onze ans plus tard, en 1903, lorsque la préface du dernier livre déclarera que « le personnalisme est le vrai nom qui convient à la doctrine désignée jusqu'ici sous le titre de néocriticisme ».</p>
</div>
</details>

<details class="dp-pli" data-rang="variante 3">
<summary class="dp-titre"><span class="dp-rang">218 mots</span><span class="dp-texte">La conclusion ajoutée — « On peut faire un pas de plus »</span></summary>
<div class="dp-corps">
<p>Le texte de 1875 s'arrêtait sur <em>Fin du formulaire</em> ; celui de 1892 continue par « la conclusion définitive plus avancée dans le sens des postulats » :</p>
<div class="dp-cite">
<p><span class="dp-ajout">Est-ce donc le dernier mot de la <em>Critique de la connaissance</em> ? On peut faire un pas de plus</span> si l'on réfléchit que l'hypothèse de l'unité de la conscience première et suprême […] permet d'expliquer l'unité des lois que cette conscience a instituées, qui régissent toute représentation, toute conscience imaginable pour nous […]. Au contraire, dans l'hypothèse d'une pluralité de consciences primitives, mutuellement indépendantes, on ne saurait donner la raison de leur similitude de constitution intellectuelle, et de cette communauté des catégories (temps, espace, causalité) […].</p>
<p>Si nous pesons bien cet argument, la philosophie critique, nécessairement bornée par sa thèse du premier commencement, posant la limite extrême de la connaissance, ne s'arrêtera pas avant d'avoir atteint le point le plus élevé de la théorie des postulats de la raison : <span class="dp-ajout">l'unité de la conscience première</span>. Le <em>premier commencement</em> deviendra <span class="dp-ajout">l'acte de la création</span>. L'impénétrable est alors <span class="dp-ajout">Dieu cause de soi</span>, comme quelques théologiens et philosophes l'ont nommé, c'est-à-dire Dieu antérieur à son œuvre et à lui-même.</p>
<span class="dp-source">Troisième Essai, Introduction, dernier paragraphe — absent en 1875</span>
</div>
<p class="dp-chapo">« Faire un pas de plus », « unité de la conscience première », « l'acte de la création » et « cause de soi » sont quatre expressions absentes du résumé de 1875 et toutes présentes dans celui de 1892.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'hypothèse renversée</span>
<p>La troisième phrase énonce que « dans l'hypothèse d'une pluralité de consciences primitives, mutuellement indépendantes, <strong>on ne saurait donner la raison</strong> de leur similitude ». L'hypothèse même que le Formulaire du Premier Essai disait sembler « la seule rationnelle » se voit maintenant refuser toute raison.</p>
<p>L'auteur a alors soixante-dix-sept ans. Loin de retirer l'ancienne page, il la laisse debout, la met sous forme dubitative, ajoute la nouvelle à la suite et signale l'opération en note. C'est ce qu'il appelle conserver « la trace de la marche de mes idées ».</p>
</div>
<details class="dp-pli" data-rang="la série">
<summary class="dp-titre"><span class="dp-rang">trois âges</span><span class="dp-texte">La même phrase en 1864, 1875 et 1892, et un aller-retour</span></summary>
<div class="dp-corps">
<p>Le troisième terme fait voir ce que deux états ne montraient pas. La définition de la neuvième catégorie (la personnalité, dont la fonction est la liberté) se lit ainsi aux trois âges du résumé :</p>
<div class="dp-variante">
<div class="dp-var-ligne"><span class="dp-var-an">1864</span><span>[…] quand la Causalité et la Finalité ayant été bien étudiées <span class="dp-avant">dans leurs rapports entre elles et avec les autres</span>, le Soi et le Non-soi <span class="dp-avant">sont posés</span> avec la plus grande distinction possible dans <span class="dp-avant">la synthèse de</span> la Conscience.</span></div>
<div class="dp-var-ligne"><span class="dp-var-an">1875</span><span>[…] quand la Causalité et la Finalité ayant été bien étudiées dans leurs rapports entre elles et avec les autres, le Soi et le Non-soi sont posés <span class="dp-avant">très-distinctement</span> dans la synthèse de la Conscience.</span></div>
<div class="dp-var-ligne dp-var-ligne--neuf"><span class="dp-var-an">1892</span><span>[…] quand, la Causalité et la Finalité <span class="dp-apres">une fois</span> bien étudiées, le Soi et le Non-Soi <span class="dp-apres">se posent</span> <span class="dp-apres">avec la plus grande distinction possible</span> dans la Conscience.</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Il relisait ses trois éditions</span>
<p>La formule « avec la plus grande distinction possible » est de <strong>1864</strong>. Renouvier l'abrège en 1875 (« très-distinctement »), puis la <strong>rétablit en 1892</strong>. Un homme qui corrige la troisième édition d'un texte en rouvrant la première tient un registre au lieu d'écrire au fil de la plume. « Conserver la trace de la marche de mes idées » était à prendre à la lettre.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Les deux autres retouches de 1892 vont dans le même sens</span>
<p>Le Soi et le Non-Soi <strong>ne sont plus <em>posés</em>, ils <em>se posent</em></strong>. Du passif au pronominal, ils cessent d'être posés dans une synthèse et se posent eux-mêmes dans la conscience. Puis, de « la <em>synthèse de la</em> Conscience » à « la Conscience », l'échafaudage technique tombe et la chose reste.</p>
<p>À soixante-dix-sept ans, en relisant un résumé, l'auteur retire le mot <em>synthèse</em> devant <em>conscience</em>. Onze ans plus tard, il écrira : « Une substance, si nous voulons conserver ce nom, est une conscience. »</p>
</div>
</div>
</details>

<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Une série complète de trois termes</span>
<p>Renouvier parle en 1892 de « cette troisième édition du résumé de mes <em>Essais</em> ». Les voici toutes : <strong>1864</strong>, en tête du Troisième Essai, première édition ; <strong>1875</strong>, rejeté à la fin du Deuxième ; <strong>1892</strong>, remonté en tête du Troisième. Le même texte paraît trois fois en vingt-huit ans, chez un homme qui déplace ses résumés d'un Essai à l'autre et note ce qu'il y a changé.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="1903">
<summary class="dp-titre"><span class="dp-rang">le récit</span><span class="dp-texte">n'y voit plus qu'un complément</span></summary>
<div class="dp-corps">
<p>En sa dernière année, dans la dernière préface de son dernier livre, Renouvier donne enfin son nom à sa doctrine :</p>
<div class="dp-cite">
<p>Le personnalisme est le vrai nom qui convient à la doctrine désignée jusqu'ici sous le titre de néocriticisme.</p>
<span class="dp-source">Le Personnalisme, 1903, préface</span>
</div>
<p>Deux paragraphes plus loin, il date de 1854 le socle de sa doctrine :</p>
<div class="dp-cite">
<p>Le néocriticisme, <em>dès son origine</em> (<em>Essais de critique générale, Premier essai</em>, 1854. — <em>Deuxième essai</em>, 1859) est en opposition décisive avec tous les points caractéristiques de la doctrine kantienne, un relativisme net, qui est en même temps le personnalisme.</p>
<span class="dp-source">Le Personnalisme, 1903, préface</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Il a raison et il a tort, et il faut tenir les deux</span>
<p><strong>Il a raison</strong> sur le socle. Dès le Premier Essai, la neuvième catégorie s'appelle <em>personnalité</em>, et la réfutation des antinomies kantiennes comme le premier commencement y figurent ; la méthode et les catégories se retrouvent telles quelles dans le résumé de 1892. Sur ces points, les textes comparés ici ne montrent aucun déplacement. La comparaison mot à mot porte toutefois sur 1875 et 1892, et ne remonte à 1854 qu'à travers l'avant-propos de 1875, qui déclare inchangées les conclusions de la première édition.</p>
<p><strong>Il a tort</strong>, non dans la lettre, mais dans le récit. La préface ne prétend pas faire remonter à 1854 l'unité de la personne première, puisqu'elle écrit, quatre paragraphes plus loin, que « la doctrine personnaliste a été plus tardive à se compléter par la reconnaissance d'un acte de création comme fait initial, et de l'unité de la personne première et créatrice ». Elle appelle pourtant complément ce qui a été un renversement. Le Formulaire du Premier Essai jugeait que la pluralité des consciences premières « semble […] la seule rationnelle » ; le résumé de 1892 la déclare sans raison. Ce complément portera tout le reste.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Un changement plus étroit qu'il n'y paraît</span>
<p>On croirait que le grand écart porte sur Dieu. Il n'en est rien, car le Dieu <em>fini</em> figure déjà en 1875 : « la personne divine est ainsi soustraite aux attributs infinis […]. Mais la vraie <em>perfection</em> lui reste […] : la perfection de justice et de bonté ». Le pivot l'exigeait depuis 1854, un Dieu infini en acte étant contradictoire. Tout Dieu recevable est donc fini. Ce point n'a pas bougé en cinquante ans.</p>
<p>Ce qui bascule en 1886 tient en une question : <strong>Dieu est-il un ou plusieurs ?</strong> La création, puis l'harmonie préétablie, viendront de la réponse.</p>
</div>
<p>Le mot juste n'est donc ni continuité ni reniement. Renouvier a conservé sa méthode, mais <strong>il a révisé une conclusion</strong>, une seule, par une déduction tirée de sa propre doctrine. Aussi a-t-il pu, de bonne foi, la présenter en 1903 comme un complément plutôt que comme un revirement. Quand une conclusion sort des prémisses de son auteur, elle paraît y avoir toujours été.</p>
</div>
</details>

<details class="dp-pli" data-rang="la balance">
<summary class="dp-titre"><span class="dp-rang">le compte</span><span class="dp-texte">ce qui n'a jamais bougé</span></summary>
<div class="dp-corps">
<p>À cinquante ans de distance, le compte est faisable : ce qui entre, ce qui sort, ce qui tient.</p>
<div class="dp-balance">
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>L'unité de la conscience première</strong> — 1886. À rebours de la pluralité vers laquelle inclinait le Premier Essai.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>L'acte de création</strong> — 1886, consigné en 1892. Le « premier commencement » devient un acte de quelqu'un.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>Dieu dans les lois, non hors d'elles</strong> — 1892. On peut l'envisager « comme le souverain Auteur et siège suprême de ces lois […], mais non comme un être existant en dehors de ces lois ». Les deux formules manquent en 1875.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>La personnalité comme objet unique de la Critique</strong> — 1892, à un « s » près.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>Les monades et l'harmonie préétablie</strong> — les monades dès 1899 (<em>La Nouvelle Monadologie</em>) ; l'harmonie préétablie à la dernière page de 1903.</span></div>
<div class="dp-poste"><span class="dp-signe">−</span><span><strong>La pluralité primitive des consciences</strong> — d'hypothèse qui « semble […] la seule rationnelle » (Formulaire du Premier Essai) à hypothèse dans laquelle « on ne saurait donner la raison » de la similitude des consciences (1892). Non supprimée, mais dérivée de l'unité.</span></div>
<div class="dp-poste"><span class="dp-signe">−</span><span><strong>L'équilibre entre unité et pluralité divines</strong> — 1892, où <em>sont</em> devient <em>semblent</em>.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Un Dieu fini.</strong> Contrairement à ce qu'on attendrait, la phrase « la personne divine est ainsi soustraite aux attributs infinis que la métaphysique appelait des <em>perfections</em>, et qui la détruisaient » figure déjà, mot pour mot, dans le Formulaire de 1875. Le pivot l'imposait dès 1854. Ce qui change en 1892 est que Dieu soit <em>un</em>, non qu'il soit fini.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Le pivot.</strong> Formulaire du Premier Essai (1859, cité dans l'état de 1875) : « l'infini et le nombre sont contradictoires entre eux ». 1903 : « le tout actuel de parties sans fin est un concept contradictoire en soi ». Même argument, même office, quarante-neuf ans.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Le phénoménisme.</strong> Ni loi sans phénomène, ni phénomène sans conscience. Cette prémisse produira Dieu en 1886.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Les neuf catégories</strong>, leur ordre et leurs formes, repris tels quels dans le résumé de 1892.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>La liberté</strong> et le refus des antinomies kantiennes, que la préface de 1903 date à juste titre « dès son origine ».</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce qu'explique la colonne du bas</span>
<p>Ce qui n'a pas bougé forme le socle ; ce qui est entré se compose de conséquences. <strong>Rien, dans les textes examinés ici, ne vient du dehors.</strong> Le seul mobile que Renouvier avoue est un besoin de la raison pratique, lequel appartient au système depuis le Deuxième Essai.</p>
<p>Une pensée qui bouge sans rien recevoir du dehors procède exactement comme un dépliant, où rien n'entre ni ne sort et dont la carte, pourtant, finit ouverte. Renouvier a changé d'avis sans changer de méthode, en dépliant une conséquence qui dormait dans sa prémisse depuis trente ans et contredisait sa conclusion.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="1903">
<summary class="dp-titre"><span class="dp-rang">le prix</span><span class="dp-texte">l'harmonie préétablie</span></summary>
<div class="dp-corps">
<p>Il fallait réviser cette conclusion-là, et non une autre, pour la raison suivante.</p>
<p>Le dernier livre s'achève sur les monades et l'harmonie préétablie. Or celle-ci <strong>exige un coordinateur unique</strong>, puisque, chez Leibniz, Dieu accorde entre elles les séries de toutes les monades sans que rien ne passe de l'une à l'autre. Une pluralité de consciences premières indépendantes ne peut s'accorder. C'est l'argument de 1886, dans la formule de 1892 selon laquelle on ne saurait donner la raison de leur similitude.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le mot, dix-sept ans plus tôt</span>
<p>La relation va plus loin qu'une compatibilité. Lue sans égard à sa date, la phrase de 1886 porte : « Cette <strong>harmonie</strong>, en effet, implique l'unité d'une conscience qui <strong>la conçoit et la réalise</strong> ». Cette conscience, première, unique, libre, finie, conçoit et réalise l'ordre des lois régissant des <em>êtres libres</em>.</p>
<p>Le dispositif y est entier, même si les monades en sont encore absentes et si Leibniz n'est pas nommé dans ce passage. <strong>Il ne manque que l'adjectif.</strong> On le lit en 1903, à la dernière ligne du dernier livre : <em>et c'est l'harmonie préétablie</em>.</p>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La conclusion de 1903, hors de portée avant 1886</span>
<p>Le Renouvier du Premier Essai ne <em>pouvait pas</em> écrire la dernière page du <em>Personnalisme</em>, non faute d'y avoir pensé, mais parce que sa conclusion sur l'origine du monde l'en écartait. Il a fallu que l'unité de la conscience première entre dans le système pour que l'harmonie préétablie devienne une option.</p>
<p>La physique tardive dépend donc d'une thèse posée en 1886 et consignée en 1892, dans un paragraphe ajouté à la fin d'une introduction peu lue. Les systèmes basculent volontiers en de tels endroits.</p>
</div>
<p class="dp-chapo">La page voisine, <a href="../physique-tardive/">La physique du personnalisme</a>, déplie ce dernier livre.</p>
</div>
</details>

</div>
</details>

<p class="dp-epigraphe">— les pièces —</p>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">1854 → 1903</span><span class="dp-texte">La chronologie, et où chaque chose est écrite</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Quelques documents, tous publiés, suffisent ; ils sont ici mis en regard les uns des autres.</p>
<div class="dp-escalier">
<div class="dp-marche"><span class="dp-marche-num">1854</span><span><strong>Premier Essai, ch. LIII.</strong> Une conscience du tout est contradictoire ; le Formulaire de 1875 (t. III, p. 289) en tire que « l'hypothèse d'une pluralité primitive de consciences distinctes, dans le monde, semble donc la seule rationnelle ».</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">1864</span><span>Première édition du résumé du Deuxième Essai, en tête du <em>Troisième</em>. « […] le Soi et le Non-soi <em>sont posés</em> avec la plus grande distinction possible dans <em>la synthèse de</em> la Conscience. » On y lit déjà : « ces fonctions ont des <em>variables indépendantes</em> réelles ».</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">1875</span><span>Deuxième édition du résumé, rejetée à la fin du Deuxième Essai. « Deux directions de l'esprit <em>sont</em> possibles, légitimes. » Le texte s'arrête sur <em>Fin du formulaire</em>.</span></div>
<div class="dp-marche"><span class="dp-marche-num">1885-86</span><span><strong>Esquisse, t. II</strong> — tout y est, aux pages que désigne la note de 1892. <em>p. 108</em> : même les philosophies qui se disent scientifiques reposent sur des croyances ; croire est donc légitime. <em>p. 348</em> : la conscience première, une, libre, finie, « qui conçoit et réalise » l'harmonie des lois. <em>p. 395 jusqu'à la fin</em> : l'argument de l'unité, le mobile avoué, la création, au terme de « Comment je suis arrivé à cette conclusion » (p. 355-405, plus de vingt-cinq mille mots), qui s'ouvre sur la théorie de l'aveu. Hors renvoi, <em>p. 305</em> : le pari de Locke, l'ordre moral universel est un ordre divin.</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">1892</span><span>Troisième édition du résumé, remontée en tête du Troisième Essai. Trois variantes principales : <em>semblent</em>, <em>prise</em> et 218 mots de conclusion nouvelle, plus quelques retouches de détail. Note de l'auteur signalant deux de ces opérations et renvoyant à l'Esquisse.</span></div>
<div class="dp-marche"><span class="dp-marche-num">1899</span><span><em>La Nouvelle Monadologie</em> — le chaînon que la préface de 1903 désigne elle-même : la « théorie cosmogonique et eschatologique du personnalisme », « abordée » dans le Troisième Essai de 1892, y est « exposée » avant d'être « reprise à fond » en 1903.</span></div>
<div class="dp-marche"><span class="dp-marche-num">1903</span><span><strong>Le Personnalisme</strong>, préface : « le vrai nom », « dès son origine », et une doctrine « plus tardive à se compléter » par la création et l'unité de la personne première. <em>Étude sur la perception externe et sur la force</em>, dernier mot : « et c'est l'harmonie préétablie ».</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'apport du troisième terme</span>
<p>Retrouvée en cours de route, la première édition (Paris, Ladrange, 1864) a fait mieux que fermer la démonstration. Elle a montré que Renouvier <strong>relisait ses trois états</strong>, puisqu'en 1892 il <em>revient</em> à une formule de 1864 qu'il avait abrégée en 1875.</p>
<p>Reste que, selon lui, « les deux premières éditions » présentaient la conclusion « seule et sans réserve ». L'assertion est vérifiée pour 1875 ; pour 1864, seule la section A a pu être consultée, et la conclusion sur Dieu est dans la section D. Il manque encore le dernier centimètre.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="méthode">
<summary class="dp-titre"><span class="dp-rang">l'outil</span><span class="dp-texte">Comment la comparaison a été faite, et ce qu'elle ne prouve pas</span></summary>
<div class="dp-corps">
<p>Une page qui confronte un philosophe à ses propres variations doit montrer ses instruments, avec leurs défauts.</p>
<ul class="dp-liste">
<li><strong>Les deux états ont été alignés mot à mot</strong>, après normalisation (pagination, appels de note, italiques, guillemets, césures). On obtient 16 212 mots contre 16 811, et <strong>94,3 % de correspondance</strong>.</li>
<li><strong>Les deux tomes viennent de numérisations différentes</strong>, Gallica pour 1875, Google Books pour 1892. L'océrisation produit donc un bruit réel, qui a fait écarter comme suspectes les divergences d'une ou deux lettres sur un mot.</li>
<li><strong>Un « ajout de 93 mots » a été rejeté</strong>, puisqu'il correspondait au tableau de classification des sciences, transcrit en texte d'un côté et en HTML de l'autre par l'édition numérique. Tout diff mesure aussi les choix de son éditeur moderne.</li>
<li><strong>Seuls les blocs longs et contigus ont été retenus</strong>, car un OCR ne fabrique pas 218 mots de suite, ni ne corrige un accord.</li>
<li><strong>Trois absences apparentes n'étaient que des artefacts de transcription</strong>, ce que doit dire une page qui demande à un philosophe de rendre compte de ses variations. La définition de la substance, qui semblait supprimée en 1875 parce que ma recherche butait sur les astérisques d'italique du fichier, est intacte. En 1892, la formule « variables indépendantes », qui semblait disparue, y figure, mais coupée par une césure de fin de ligne (« des <em>va- riables indépendantes</em> »). Le premier alignement donnait 94,6 %, et les mêmes césures y créaient des divergences fantômes. Une fois les césures recollées et la méthode figée (mots en minuscules, apostrophes comprises ; pagination, appels de note et marques d'italique retirés ; identité mesurée par les plus longs blocs communs, rapportés à la moyenne des deux textes), le chiffre s'établit à 94,3 %. <strong>Sur ces textes, une chaîne cherchée telle quelle ne prouve rien ; il faut normaliser avant de conclure à une absence.</strong></li>
<li><strong>La numérisation de l'<em>Esquisse</em> est fautive par endroits.</strong> Les citations en ont été choisies dans les zones saines ; les trois interventions nécessaires sont entre crochets : « ou [en] d'autres termes » (p. 305 ; la transcription porte « ou d'autres termes »), « à laquelle [nous a] conduit notre méthode » (la transcription porte « à laquelle je me suis conduire notre méthode », leçon cassée ; restitution conjecturale) et « libre créateur[s] d'êtres libres » (la transcription accorde au pluriel un sujet singulier). Aucune n'affecte le sens ; toutes trois sont signalées ici plutôt que corrigées en silence.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que cette page ne dit pas</span>
<p>Elle ne dit pas que Renouvier a menti. Laisser debout son ancienne conclusion, la mettre sous forme dubitative, ajouter la nouvelle à la suite et signaler l'opération en note avec l'adresse des raisons, c'est faire le contraire d'une dissimulation. Le « dès son origine » de 1903 n'efface rien, puisque la même préface reconnaît que la doctrine « a été plus tardive à se compléter ». Il vient d'ailleurs <em>après</em> tout cela, chez un homme de quatre-vingt-huit ans qui regarde cinquante ans de travail et y voit, non sans raison, une seule et même chose.</p>
<p>Elle ne dit pas non plus que la question est close. Reste ouverte une vérification massive, celle de <strong>vingt ans de <em>Critique philosophique</em></strong>. Si le dispositif est monté dès 1886, le tournant lui est antérieur. Il faudrait en chercher dans la revue la date exacte, et peut-être l'occasion.</p>
</div>
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

Cette page suit les règles de ses deux sœurs, [Compliquer les Essais pour les expliquer](essais.md) et [La physique du personnalisme](physique-tardive.md) : le pli conserve tout ; les voies non prises restent visibles ; la profondeur se compte aux filets ; le parcours se souvient ; la typographie dit qui parle, sérif pour Renouvier, linéale pour le commentaire.

Elle y ajoute la sienne. **Ici, le commentaire confronte Renouvier à lui-même**, à ce qu'il a dit de ses variations comme à ce que les textes en montrent. Il ne peut donc rien avancer qui ne soit vérifiable dans les fichiers du site. Chaque variante est donnée dans ses deux états, chaque expression déclarée absente d'un état a été comptée dans les deux, et l'appareil de comparaison est décrit sous le pli « l'outil », avec ce qu'il a dû écarter.

**Sources.** *Essais de critique générale, Premier Essai*, 2ᵉ éd., 1875, t. III (ch. LIII et Formulaire). — *Deuxième Essai*, 2ᵉ éd., 1875, t. III (*Formulaire du Traité de Psychologie rationnelle*, état de 1875). — *Troisième Essai, Les Principes de la nature*, 2ᵉ éd. corrigée et augmentée, 1892, t. I (*Introduction — Résumé des principes de la psychologie rationnelle*, état de 1892, et sa note). — *Esquisse d'une classification systématique des doctrines philosophiques*, t. II, 1886 (« Comment je suis arrivé à cette conclusion »). — *Le Personnalisme, suivi d'une étude sur la perception externe et sur la force*, Félix Alcan, 1903 (préface, et ch. L de l'Étude).
