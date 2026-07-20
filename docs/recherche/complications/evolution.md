---
title: "Comment je suis arrivé à cette conclusion"
description: "Ce que Renouvier a changé entre 1854 et 1903, ce qu'il en a dit, et ce que les textes en montrent."
---

# Comment je suis arrivé à cette conclusion

Le titre est de Renouvier. C'est celui du dernier chapitre de son *Esquisse d'une classification systématique des doctrines philosophiques*, tome II, 1886 : vingt-cinq mille mots où il raconte comment il a changé d'avis.

Dix-sept ans plus tard, dans la préface de son dernier livre, il écrit que sa doctrine est la même **« dès son origine »**.

Cette page tient les deux bouts. Elle ne cherche pas à prendre un vieil homme en défaut : elle se sert de ce qu'il a laissé — un aveu daté, un résumé réédité trois fois avec les repentirs signalés, et une préface qui les nie — pour mesurer une chose qu'on ne mesure presque jamais : **de combien une pensée bouge, et par où.**

Fermée, la page tient en quatre mots. Chaque terme s'ouvre sur ce qu'il contient. **Rien ne disparaît quand vous ouvrez.**

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
<p>Le premier mot annonce une question de méthode, et c'est la seule fois que Renouvier la pose sur lui-même. Quelques pages plus haut, il vient d'établir que tout système est une affaire personnelle :</p>
<div class="dp-cite">
<p>[…] chacun d'eux est l'œuvre personnelle, ou du moins l'affirmation personnelle d'un penseur, placé sous l'influence d'un certain tempérament intellectuel et passionnel, d'une certaine éducation, d'un certain milieu […].</p>
<span class="dp-source">Esquisse, t. II, ch. « Comment je suis arrivé à cette conclusion »</span>
</div>
<p>Et il en tire la règle qui commande cette page-ci — c'est lui qui la formule, pas nous :</p>
<div class="dp-cite">
<p>[…] on trouvera presque toujours que c'est une considération de sentiment, ou d'ordre pratique, au fond, qui a été le mobile.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que « comment » exclut</span>
<p>Pas « pourquoi ai-je raison », mais « par quel chemin suis-je venu ». Renouvier réclame pour l'histoire de la philosophie une chose qui n'existe pas : non des <em>confessions</em>, dit-il, mais « des monographies de la marche de la réflexion et de l'enchaînement des idées systématiques ». Elles manquent, et il sait pourquoi :</p>
</div>
<div class="dp-cite">
<p>[…] les philosophes […] veulent autant que possible dérober à autrui leurs variations et leurs erreurs, et se les dissimuler à eux-mêmes. […] On dirait qu'ils se croient immuables, ou qu'ils jugent absurde de le paraître. Et tout naturellement l'infaillibilité accompagne l'immutabilité.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<p>Retenez cette phrase. Elle lui reviendra dessus dix-sept ans plus tard, et c'est lui qui l'aura écrite.</p>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">je</span></summary>
<div class="dp-corps">
<p>Un philosophe qui écrit « je » dans un traité de classification des doctrines commet une inconvenance, et il le sait. C'est précisément ce qu'il reproche aux autres de ne jamais faire :</p>
<div class="dp-cite">
<p>Chaque penseur dogmatique, en vertu d'une fiction dont il est dupe et dont le public a pris l'habitude, […] enseigne et décrète en se targuant de l'autorité d'une raison impersonnelle et d'une expérience commune à tous les hommes.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note">
<span class="dp-etiquette">Pourquoi ce « je » est cohérent</span>
<p>Ce n'est pas une coquetterie d'auteur : c'est une conséquence. Si la vérité est affirmée par une liberté — thèse du Deuxième Essai, « le principe de ces principes est la liberté » —, alors il n'existe pas de raison impersonnelle qui parlerait toute seule. Un philosophe qui écrirait sans « je » mentirait sur sa propre doctrine. Le personnalisme oblige à l'autobiographie.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">suis arrivé</span></summary>
<div class="dp-corps">
<p>Voici le mot qui décide de tout, et il tient en deux syllabes. <strong>Arriver, c'est avoir bougé.</strong></p>
<p>En 1886, le titre d'un chapitre dit : je suis <em>arrivé</em> à cette conclusion — donc je n'y étais pas. En 1903, la préface du dernier livre dit exactement le contraire :</p>
<div class="dp-cite">
<p>Le néocriticisme, <em>dès son origine</em> (<em>Essais de critique générale, Premier essai</em>, 1854. — <em>Deuxième essai</em>, 1859) est en opposition décisive avec tous les points caractéristiques de la doctrine kantienne, un relativisme net, qui est en même temps le personnalisme.</p>
<span class="dp-source">Le Personnalisme, 1903, préface</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Toute la page tient dans cet écart</span>
<p>1886 : <em>je suis arrivé</em>. 1903 : <em>dès son origine</em>. Ce n'est pas une contradiction de détail — c'est la contradiction que Renouvier lui-même avait annoncée, en règle générale, dans le chapitre qui porte le premier de ces deux titres. Il avait écrit que les philosophes se croient immuables. Il a fini par le devenir.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="titre">
<summary class="dp-titre"><span class="dp-rang">le mot</span><span class="dp-texte">à cette conclusion</span></summary>
<div class="dp-corps">
<p>Laquelle ? Le chapitre s'appuie sur celui qui précède : <em>Optimisme et pessimisme. — Le monde moral. — Le fait moral.</em> Mais la conclusion à laquelle il est arrivé, et qu'il n'avait pas au départ, tient en cinq mots :</p>
<p class="dp-epigraphe">l'unité de la conscience première</p>
<p>C'est-à-dire : un Dieu unique, créateur — et fini. En 1854, Renouvier tenait la thèse rigoureusement inverse.</p>
</div>
</details>

<p class="dp-epigraphe">— la page en une phrase —</p>
<p class="dp-these">En 1886, Renouvier écrit que les philosophes dissimulent leurs variations et se croient immuables ; puis il raconte les siennes sur vingt-cinq mille mots. En 1892, il consigne le changement dans un résumé, en signalant ses propres repentirs. En 1903, il écrit qu'il n'a jamais changé.</p>

<details class="dp-pli" data-rang="palier">
<summary class="dp-titre"><span class="dp-rang">↓ déplier</span><span class="dp-texte">La page en un paragraphe</span></summary>
<div class="dp-corps">
<p>En 1854, le Premier Essai conclut qu'une conscience du tout est contradictoire : donc <strong>la pluralité des consciences premières</strong> est « la seule rationnelle ». Trente ans plus tard, Renouvier applique sa propre thèse de jeunesse — pas de loi sans phénomène, pas de phénomène sans conscience — au monde entier, et <strong>elle produit Dieu</strong> : si les lois sont partout les mêmes, il faut bien une conscience une qui les ait posées. Il l'écrit en 1886, dans un chapitre autobiographique, et il avoue <strong>le mobile</strong> : les postulats de la raison pratique ont besoin de garanties que la pluralité ne donne pas. En 1892, il <strong>réédite son propre résumé</strong> et y consigne le changement — trois variantes, mesurables au mot, signalées par lui en note. En 1903, il <strong>nie avoir changé</strong>. Le compte est pourtant faisable : ce qui est entré, ce qui est sorti, et <strong>ce qui n'a jamais bougé</strong>. Il a raison sur presque tout — sauf sur le point précis qui rendra possible, à la dernière page de sa vie, <strong>l'harmonie préétablie</strong>.</p>
<p class="dp-chapo">Chacun des sept termes en gras s'ouvre ci-dessous. Vous pouvez vous arrêter ici : ce paragraphe est vrai. Vous pouvez aussi tirer sur un fil.</p>

<details class="dp-pli" data-rang="1854">
<summary class="dp-titre"><span class="dp-rang">le départ</span><span class="dp-texte">la pluralité des consciences premières</span></summary>
<div class="dp-corps">
<p>Le Premier Essai s'achève sur la ruine de la synthèse totale. Le chapitre LIII demande s'il peut exister une conscience du monde entier, et répond non : la conscience est la synthèse du soi et du non-soi ; une conscience qui envelopperait tout n'aurait pas de non-soi ; elle cesserait d'être une conscience. Puis vient le résidu, et il est décisif :</p>
<div class="dp-cite">
<p>[…] l'hypothèse d'une pluralité primitive de consciences distinctes, dans le monde, semble donc la seule rationnelle […].</p>
<span class="dp-source">Premier Essai, ch. LIII</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Mesurez ce que cela interdit</span>
<p>Pas de Dieu unique — non par athéisme, par logique : une conscience du tout est contradictoire. Le monde n'a pas de sommet. À l'origine, il y a <em>plusieurs</em> consciences, indépendantes. Trente-deux ans plus tard, Renouvier écrira l'exact contraire, et par le même raisonnement, mieux conduit.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="1886">
<summary class="dp-titre"><span class="dp-rang">l'argument</span><span class="dp-texte">elle produit Dieu</span></summary>
<div class="dp-corps">
<p>Voici le passage. Il est de 1886, et il n'ajoute rien à la doctrine de 1854 : il l'applique.</p>
<div class="dp-cite">
<p>Le monde, envisagé sous toutes les catégories, implique donc une communauté de lois. Mais dire communauté, c'est dire unité, autant que la communauté s'étend, et l'unité de loi est elle-même une loi. […] Mais, pour la méthode qui n'admet ni loi sans phénomènes, ni phénomènes sans conscience […], une loi une et universelle […] ne peut exister qu'à la condition d'une conscience une et universelle donnée à cet objet.</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le phénoménisme se retourne</span>
<p>La prémisse est celle de 1854 : <em>pas de loi sans phénomène, pas de phénomène sans conscience.</em> C'était une arme contre la métaphysique — elle servait à abolir la substance et la chose en soi. Appliquée au monde entier, elle produit l'inverse : si l'espace, le temps et la causalité sont partout les mêmes pour toutes les consciences, cette communauté est une loi ; une loi doit être représentée dans une conscience ; donc il y a une conscience une et universelle.</p>
<p>Renouvier ne s'est pas converti. Il a déplié une conséquence qu'il n'avait pas vue, et elle était dans sa prémisse depuis trente ans.</p>
</div>
<p>Deux garde-fous tiennent dans l'opération, et ce sont les deux thèses de sa vie. Le premier : le pivot n'est pas touché — cette conscience est une et universelle, <strong>« à la réserve expresse de l'infinité, qui doit toujours être exclue »</strong>. Le second : elle doit être libre, sans quoi elle aurait des antécédents, « ce qui est contraire à notre thèse du <em>pur commencement</em> ».</p>
<p>Et le renversement est complet. En 1854, la pluralité était première. En 1886 :</p>
<div class="dp-cite">
<p>Il faut avoir admis d'abord l'unité et universalité de conscience pour l'explication de cet ordre. Cela fait, un passage de l'unité à la pluralité des consciences est à chercher […] ; il ne nous reste donc plus que l'idée rigoureuse de la création […].</p>
<span class="dp-source">Esquisse, t. II</span>
</div>
<p>L'unité est devenue l'origine ; la pluralité, le dérivé. Et le mot de création est lâché.</p>
</div>
</details>

<details class="dp-pli" data-rang="1886">
<summary class="dp-titre"><span class="dp-rang">l'aveu</span><span class="dp-texte">le mobile</span></summary>
<div class="dp-corps">
<p>Vous cherchez une cause : une découverte scientifique, une lecture, une conversion, une maladie ? Renouvier vous a devancé, et il répond deux fois — une fois en général, une fois sur lui-même.</p>
<p>En général, quelques pages avant :</p>
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
<span class="dp-etiquette">La réponse, donc</span>
<p>Ni la science, ni la santé, ni un déménagement, ni une conversion. <strong>Les postulats avaient besoin de garanties.</strong> La liberté, l'immortalité, Dieu — les trois thèses de la troisième partie du Deuxième Essai — ne tiennent pas debout sur une poussière de consciences indépendantes. Il leur faut un ordre, et un ordre veut une origine.</p>
<p>Ce qui rend l'aveu remarquable, ce n'est pas son contenu : c'est qu'il applique à lui-même le diagnostic qu'il venait de porter sur tous les autres. Il avait écrit que le mobile est « presque toujours » pratique. Le sien l'est.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Une règle de méthode</span>
<p>Aucune de ces conclusions n'a demandé d'hypothèse. Elles étaient à l'adresse que Renouvier avait laissée en note dans son résumé de 1892 : « <em>Esquisse</em>, t. II, pp. 108 sq., 348 sq., 305 jusqu'à la fin ». Avant de chercher une cause dans la vie d'un auteur, il faut avoir suivi ses renvois.</p>
</div>

<details class="dp-pli" data-rang="détail">
<summary class="dp-titre"><span class="dp-rang">l'adresse</span><span class="dp-texte">Les trois renvois ne sont pas trois références : c'est un plan</span></summary>
<div class="dp-corps">
<p>Il faut les lire dans l'ordre où ils démontrent, et non dans celui où il les cite. Trois étages, et chacun fait un travail que les deux autres ne peuvent pas faire.</p>

<p class="dp-epigraphe">p. 108 — le permis de construire</p>
<p>Renouvier y démonte les philosophies « qui établissent leur fondement dans les sciences ». Spencer transporte aux rapports de la représentation une loi empruntée à l'histoire naturelle ; la nébuleuse primitive du physicien devient, chez le métaphysicien, ce qu'on eût appelé « l'être universel en puissance ». Et l'Inconnaissable placé derrière tout cela ne sauve rien :</p>
<div class="dp-cite">
<p>Mais placer un <em>Absolument inconnu</em> en arrière d'un système qu'on dit qui enveloppe tout le connaissable, c'est comme n'y rien mettre.</p>
<span class="dp-source">Esquisse, t. II, p. 107-108</span>
</div>
<p>Conclusion de l'étage : ces systèmes ne reposent pas sur l'évidence, mais sur des croyances qui s'ignorent. <strong>Si même la science croit, croire est légitime.</strong> Sans ce préalable, les deux étages suivants seraient irrecevables.</p>

<p class="dp-epigraphe">p. 305 — l'argument pratique</p>
<p>Le pari — chez <strong>Locke</strong>, non chez Pascal, et Renouvier le cite sur deux pages. Puis il en tire ceci :</p>
<div class="dp-cite">
<p>[…] il s'ensuit que le pari par l'acte et le pari par la croyance sont, dans le fait, inséparables. […] nous voyons aussitôt qu'elle a pour objet l'existence d'une sanction suprême de la morale, ou [en] d'autres termes, un ordre moral du monde, qui, <em>vu son universalité</em>, doit se nommer un ordre divin, et qui assure, suivant la formule de Kant, l'harmonie du bonheur et de la vertu.</p>
<span class="dp-source">Esquisse, t. II, p. 305</span>
</div>

<div class="dp-note">
<span class="dp-etiquette">Pascal ? Classé ailleurs — et depuis longtemps</span>
<p>Une Observation du ch. XII démonte le pari pascalien thèse à thèse. La troisième — l'intérêt nous <em>somme</em> de conclure — Renouvier l'expose ainsi :</p>
<div class="dp-cite">
<p>Notre intérêt est d'affirmer que c'est la croix qui a raison. Ceci se prouve par le <em>calcul des chances</em> […].</p>
<span class="dp-source">Deuxième Essai, ch. XII, Observations et développements, A — Pascal et la théorie du vertige moral. Renouvier exposant la troisième thèse de Pascal.</span>
</div>
<p>Le dossier est rangé sous un titre qui juge : le <em>vertige moral</em> — l'intérêt qui fait tourner la tête, non la balance qui pèse. Voilà pourquoi, en 1886, le pari revient « de Locke » : non la sommation par l'enjeu, mais la croyance déjà engagée dans l'acte.</p>
</div>
<p class="dp-epigraphe">p. 348 — l'argument théorique, et la synthèse</p>
<div class="dp-cite">
<p>La plus haute conception à laquelle [nous a] conduit notre méthode, après que nous avons exclu l'absolu […], c'est la conscience première et universelle, auteur du monde, libre créateur[s] d'êtres libres. La preuve de l'unité de cet <em>Être suprême</em>, nous l'avons trouvée […] dans le fait de l'existence de lois générales et harmoniques établissant les rapports uniformes des phénomènes et la communication des consciences. Cette harmonie, en effet, implique l'unité d'une conscience qui la conçoit et la réalise […].</p>
<span class="dp-source">Esquisse, t. II, p. 348-349</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Une seule inférence, faite deux fois</span>
<p>Regardez la forme des deux arguments, et non leur matière. <strong>Ordre moral universel → ordre divin. Lois universelles → conscience une.</strong> C'est le même pas, franchi une fois par la morale et une fois par la théorie : de l'universalité à l'unité.</p>
<p class="dp-renvoi">Ce joint — de l'unité des lois à la conscience une — est le seul trait ondulé du <a href="/recherche/logique-philosophique/systeme-en-formules/">Système en formules</a> : un raccord qui tient, en travaillant.</p>
<p>Renouvier ne démontre jamais autrement — c'est déjà le dispositif de son dernier livre, où la logique et la physique arrivent séparément aux mêmes personnes. Deux routes qui ne se ressemblent pas, un seul point.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le pivot borde la conclusion, immédiatement</span>
<p>À peine Dieu posé comme un, la « condition du nombre » revient l'enfermer : elle « nous force à penser Dieu comme fini à l'égard de l'ordre quantitatif des phénomènes », et il n'est « infini seulement (<em>c'est-à-dire parfait, comme on ferait mieux de s'exprimer</em>) en justice et sainteté ».</p>
<p>La parenthèse est le plus beau moment du chapitre. À soixante et onze ans, en pleine démonstration de l'existence de Dieu, Renouvier se reprend en écrivant pour ne pas laisser passer le mot <em>infini</em>, même comme façon de parler.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et Voltaire, au milieu</span>
<p>Deux paragraphes plus haut, dans la même conclusion métaphysique : « Le mot si profond d'un philosophe, cette recette unique contre les poisons de la vie et contre les théories pessimistes : <em>Il faut cultiver notre jardin</em>, n'est pas moins vrai des spéculations les plus élevées que de la philosophie pratique. » Puis : « Nous n'abordons aucune réalité, ni Dieu, ni le monde, ni les hommes, sans la porter vers nous. »</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="1892">
<summary class="dp-titre"><span class="dp-rang">le diff</span><span class="dp-texte">réédite son propre résumé</span></summary>
<div class="dp-corps">
<p>Voici la pièce que personne n'a jamais examinée, et elle est de sa main.</p>
<p>Le <em>Formulaire du Traité de Psychologie rationnelle</em> clôt le Deuxième Essai en 1875. En 1892, Renouvier le remet en tête du Troisième Essai, sous le titre <em>Introduction — Résumé des principes de la psychologie rationnelle</em>. Mêmes quatre sections, même première phrase, seize mille mots de part et d'autre. <strong>Le même texte à dix-sept ans d'écart</strong> — et il prévient en note :</p>
<div class="dp-cite">
<p>En corrigeant cette troisième édition du résumé de mes <em>Essais</em>, j'ai tenu à conserver fidèlement la trace de la marche de mes idées. Dans cette intention, je me suis contenté de mettre sous une forme dubitative la conclusion qui, dans les deux premières éditions, se présentait seule et sans réserve ; et j'ai ajouté à celle-ci une conclusion définitive plus avancée dans le sens des postulats.</p>
<span class="dp-source">Troisième Essai, Introduction, note</span>
</div>
<p>Les deux derniers états ont été alignés mot à mot : <strong>94,3 % identiques</strong>. C'est ce qui rend les divergences lisibles. Elles sont trois, et elles font exactement ce que la note annonce.</p>

<details class="dp-pli" data-rang="variante 1">
<summary class="dp-titre"><span class="dp-rang">un mot</span><span class="dp-texte">La forme dubitative — « sont » devient « semblent »</span></summary>
<div class="dp-corps">
<p>La phrase porte sur l'unité ou la pluralité de Dieu. C'est la « conclusion qui se présentait seule et sans réserve ».</p>
<div class="dp-variante">
<div class="dp-var-ligne"><span class="dp-var-an">1875</span><span>Deux directions de l'esprit <span class="dp-avant">sont</span> possibles, légitimes, et ne s'excluent même pas précisément</span></div>
<div class="dp-var-ligne dp-var-ligne--neuf"><span class="dp-var-an">1892</span><span>Deux directions de l'esprit <span class="dp-apres">semblent</span> possibles, légitimes, qui ne s'excluent même pas précisément</span></div>
</div>
<p>Un verbe. Le reste de la phrase est intact. Et la suivante suit le même chemin : « Mais alors <span class="dp-avant">font défaut</span> les raisons aprioriques » devient « à ce point de vue, <span class="dp-apres">il semble que nous fassent</span> défaut les raisons <em>a priori</em> ».</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que coûte un « semblent »</span>
<p>En 1875, l'équilibre entre unité et pluralité divines est un résultat : les deux directions <em>sont</em> également légitimes, la raison n'a rien à dire de plus. En 1892, elles ne le sont plus qu'en apparence. Le verbe seul déplace la thèse du rang de conclusion à celui d'impression — et prépare le lecteur au « pas de plus » qui vient trois paragraphes après.</p>
<p>Renouvier n'a pas biffé sa thèse de jeunesse. Il l'a mise au conditionnel, et il l'a dit.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="variante 2">
<summary class="dp-titre"><span class="dp-rang">un accord</span><span class="dp-texte">La Critique change d'objet — « prises » devient « prise »</span></summary>
<div class="dp-corps">
<p>Même tableau, même case : la définition de ce que la Critique étudie.</p>
<div class="dp-variante">
<div class="dp-var-ligne"><span class="dp-var-an">1875</span><span>A pour objet toutes les relations, <span class="dp-avant">conditions et idées de nécessité, finalité et personnalité</span>, <span class="dp-avant">prises</span> dans le monde et dans l'homme individuel et social.</span></div>
<div class="dp-var-ligne dp-var-ligne--neuf"><span class="dp-var-an">1892</span><span>A pour objet toutes les relations, <span class="dp-apres">représentations et opérations de la personnalité</span>, <span class="dp-apres">prise</span> dans le monde et dans l'homme individuel et social.</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le pluriel qui tombe</span>
<p>En 1875, la Critique porte sur trois choses, dont la personnalité — dernier terme d'une liste. En 1892, elle porte sur la personnalité, et tout le reste en est une <em>opération</em>. La nécessité et la finalité ne sont pas supprimées : elles sont absorbées.</p>
<p>Et la preuve que c'est délibéré est grammaticale. « Prises » s'accordait avec trois termes ; « prise » s'accorde avec un seul. <strong>Renouvier a corrigé l'accord derrière lui.</strong> Une coquille ne fait pas cela.</p>
</div>
<p>Nous sommes en 1892. Onze ans plus tard, la préface du dernier livre annoncera que « le personnalisme est le vrai nom qui convient à la doctrine désignée jusqu'ici sous le titre de néocriticisme ». Le nom viendra en 1903 ; la chose est ici, dans une case de tableau, avec un « s » en moins.</p>
</div>
</details>

<details class="dp-pli" data-rang="variante 3">
<summary class="dp-titre"><span class="dp-rang">218 mots</span><span class="dp-texte">La conclusion ajoutée — « On peut faire un pas de plus »</span></summary>
<div class="dp-corps">
<p>C'est « la conclusion définitive plus avancée dans le sens des postulats ». Le texte de 1875 s'arrêtait sur <em>Fin du formulaire</em>. Celui de 1892 continue :</p>
<div class="dp-cite">
<p><span class="dp-ajout">Est-ce donc le dernier mot de la <em>Critique de la connaissance</em> ? On peut faire un pas de plus</span> si l'on réfléchit que l'hypothèse de l'unité de la conscience première et suprême […] permet d'expliquer l'unité des lois que cette conscience a instituées, qui régissent toute représentation, toute conscience imaginable pour nous […]. Au contraire, dans l'hypothèse d'une pluralité de consciences primitives, mutuellement indépendantes, on ne saurait donner la raison de leur similitude de constitution intellectuelle, et de cette communauté des catégories (temps, espace, causalité) […].</p>
<p>Si nous pesons bien cet argument, la philosophie critique, nécessairement bornée par sa thèse du premier commencement, posant la limite extrême de la connaissance, ne s'arrêtera pas avant d'avoir atteint le point le plus élevé de la théorie des postulats de la raison : <span class="dp-ajout">l'unité de la conscience première</span>. Le <em>premier commencement</em> deviendra <span class="dp-ajout">l'acte de la création</span>. L'impénétrable est alors <span class="dp-ajout">Dieu cause de soi</span>, comme quelques théologiens et philosophes l'ont nommé, c'est-à-dire Dieu antérieur à son œuvre et à lui-même.</p>
<span class="dp-source">Troisième Essai, Introduction, dernier paragraphe — absent en 1875</span>
</div>
<p class="dp-chapo">« Faire un pas de plus », « unité de la conscience première », « l'acte de la création », « cause de soi » : quatre expressions, zéro occurrence en 1875, toutes présentes en 1892.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce qui vient d'être renversé</span>
<p>Relisez la deuxième phrase : « dans l'hypothèse d'une pluralité de consciences primitives, mutuellement indépendantes, <strong>on ne saurait donner la raison</strong> de leur similitude ». C'est mot pour mot la thèse du chapitre LIII du Premier Essai — « la seule rationnelle » — qui vient d'être déclarée sans raison.</p>
<p>Et l'homme qui écrit cela a soixante-dix-sept ans. Il ne retire pas l'ancienne page : il la laisse debout, met son verbe au conditionnel, ajoute la nouvelle à la suite, et signale l'opération en note. C'est ce qu'il appelle conserver « la trace de la marche de mes idées ».</p>
</div>
<details class="dp-pli" data-rang="la série">
<summary class="dp-titre"><span class="dp-rang">trois âges</span><span class="dp-texte">La même phrase en 1864, 1875 et 1892 — et un aller-retour</span></summary>
<div class="dp-corps">
<p>Voici ce que le troisième terme permet, et que deux états ne montraient pas. La définition de la neuvième catégorie — la personnalité, c'est-à-dire la liberté — aux trois âges du résumé :</p>
<div class="dp-variante">
<div class="dp-var-ligne"><span class="dp-var-an">1864</span><span>[…] quand la Causalité et la Finalité ayant été bien étudiées <span class="dp-avant">dans leurs rapports entre elles et avec les autres</span>, le Soi et le Non-soi <span class="dp-avant">sont posés</span> avec la plus grande distinction possible dans <span class="dp-avant">la synthèse de</span> la Conscience.</span></div>
<div class="dp-var-ligne"><span class="dp-var-an">1875</span><span>[…] quand la Causalité et la Finalité ayant été bien étudiées dans leurs rapports entre elles et avec les autres, le Soi et le Non-soi sont posés <span class="dp-avant">très-distinctement</span> dans la synthèse de la Conscience.</span></div>
<div class="dp-var-ligne dp-var-ligne--neuf"><span class="dp-var-an">1892</span><span>[…] quand, la Causalité et la Finalité <span class="dp-apres">une fois</span> bien étudiées, le Soi et le Non-Soi <span class="dp-apres">se posent</span> <span class="dp-apres">avec la plus grande distinction possible</span> dans la Conscience.</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Il relisait ses trois éditions</span>
<p>Suivez « avec la plus grande distinction possible ». La formule est de <strong>1864</strong>. Renouvier l'abrège en 1875 — « très-distinctement ». Et il la <strong>rétablit en 1892</strong>. Un homme qui corrige la troisième édition d'un texte en rouvrant la première n'écrit pas au fil de la plume : il tient un registre. « Conserver la trace de la marche de mes idées » n'était pas une image.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et les deux autres retouches de 1892 vont où va tout le reste</span>
<p>Le Soi et le Non-Soi <strong>ne sont plus <em>posés</em>, ils <em>se posent</em></strong> : le passif devient pronominal, et la conscience cesse d'être un produit pour devenir un agent. Puis « la <em>synthèse de la</em> Conscience » devient « la Conscience » : l'échafaudage technique tombe, la chose reste.</p>
<p>C'est un homme de soixante-dix-sept ans qui, en relisant un résumé, retire le mot <em>synthèse</em> devant <em>conscience</em>. Onze ans plus tard, il écrira : « Une substance, si nous voulons conserver ce nom, est une conscience. »</p>
</div>
</div>
</details>

<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La série est complète, et elle compte trois termes</span>
<p>Renouvier parle en 1892 de « la troisième édition de ce résumé ». Les voici toutes : <strong>1864</strong>, en tête du Troisième Essai, première édition — <strong>1875</strong>, rejeté à la fin du Deuxième — <strong>1892</strong>, remonté en tête du Troisième. Le même texte, trois fois, sur vingt-huit ans, par un homme qui déplace ses résumés comme on déplace un meuble et qui note ce qu'il y a changé.</p>
</div>
</div>
</details>
</div>
</details>

<details class="dp-pli" data-rang="1903">
<summary class="dp-titre"><span class="dp-rang">le démenti</span><span class="dp-texte">nie avoir changé</span></summary>
<div class="dp-corps">
<p>Dernier livre, dernière préface, dernière année. Renouvier donne enfin son nom à sa doctrine :</p>
<div class="dp-cite">
<p>Le personnalisme est le vrai nom qui convient à la doctrine désignée jusqu'ici sous le titre de néocriticisme.</p>
<span class="dp-source">Le Personnalisme, 1903, préface</span>
</div>
<p>Puis, trois paragraphes plus loin, il ferme la porte :</p>
<div class="dp-cite">
<p>Le néocriticisme, <em>dès son origine</em> (<em>Essais de critique générale, Premier essai</em>, 1854. — <em>Deuxième essai</em>, 1859) est en opposition décisive avec tous les points caractéristiques de la doctrine kantienne, un relativisme net, qui est en même temps le personnalisme.</p>
<span class="dp-source">Le Personnalisme, 1903, préface</span>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Il a raison, et il a tort, et il faut tenir les deux</span>
<p><strong>Il a raison</strong> : le personnalisme est bien là dès 1854. La neuvième catégorie s'appelle <em>personnalité</em>, le refus des antinomies est daté de 1854, le phénoménisme n'a pas bougé d'un mot. Sur la méthode, sur les catégories, sur l'infini, sur la liberté, il n'a rien changé en cinquante ans. Ce n'est pas une reconstruction : c'est vrai, et le diff le prouve autant qu'il prouve le reste.</p>
<p><strong>Il a tort</strong> sur un point, un seul, et c'est celui qui portera tout le reste : en 1854, l'origine du monde est une <em>pluralité</em> de consciences. Cela n'est plus vrai après 1886, et il l'a écrit lui-même, et il a signalé la correction en note. « Dès son origine » est faux à cet endroit précis.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Et le changement est plus étroit qu'il n'y paraît</span>
<p>On croirait que le grand écart porte sur Dieu. Il n'en est rien : le Dieu <em>fini</em> est déjà là en 1875 — « la personne divine est ainsi soustraite aux attributs infinis […]. Mais la vraie <em>perfection</em> lui reste […] : la perfection de justice et de bonté ». Le pivot l'exigeait depuis 1854 : un Dieu infini en acte est contradictoire, donc tout Dieu recevable est fini. Sur ce point, rien n'a bougé en cinquante ans.</p>
<p>Ce qui bascule en 1886, et une seule chose : <strong>Dieu est-il un ou plusieurs ?</strong> Toute la différence entre les deux Renouvier tient dans un article.</p>
</div>
<p>Le mot juste n'est donc ni continuité ni reniement. Renouvier n'a pas changé de doctrine : <strong>il a changé une prémisse</strong>. Une seule. Et il l'a changée par une déduction faite à partir de sa propre doctrine — ce qui explique qu'il ait pu, de bonne foi, ne pas voir qu'il avait bougé. Quand une conclusion sort de vos prémisses, elle a l'air d'y avoir toujours été.</p>
</div>
</details>

<details class="dp-pli" data-rang="la balance">
<summary class="dp-titre"><span class="dp-rang">le compte</span><span class="dp-texte">ce qui n'a jamais bougé</span></summary>
<div class="dp-corps">
<p>Cinquante ans de distance, et le compte est faisable. Ce qui entre, ce qui sort, ce qui tient.</p>
<div class="dp-balance">
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>L'unité de la conscience première</strong> — 1886. La thèse inverse de 1854.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>L'acte de création</strong> — 1886, consigné 1892. Le « premier commencement » devient un acte de quelqu'un.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>Dieu soumis aux lois</strong> — 1892 : on peut l'envisager « comme le souverain Auteur et siège suprême de ces lois […], mais non comme un être existant en dehors de ces lois ». Les deux formules sont absentes de 1875.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>La personnalité comme objet unique de la Critique</strong> — 1892, à un « s » près.</span></div>
<div class="dp-poste dp-poste--plus"><span class="dp-signe">+</span><span><strong>Les monades et l'harmonie préétablie</strong> — 1903, dernière page.</span></div>
<div class="dp-poste"><span class="dp-signe">−</span><span><strong>La pluralité primitive des consciences</strong> — de thèse « la seule rationnelle » (1854) à hypothèse « dont on ne saurait donner la raison » (1892). Non supprimée : dérivée de l'unité.</span></div>
<div class="dp-poste"><span class="dp-signe">−</span><span><strong>L'équilibre entre unité et pluralité divines</strong> — 1892 : <em>sont</em> devient <em>semblent</em>.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Un Dieu fini.</strong> Contrairement à ce qu'on attendrait, ce n'est pas une nouveauté : « la personne divine est ainsi soustraite aux attributs infinis que la métaphysique appelait des <em>perfections</em>, et qui la détruisaient » est déjà dans le Formulaire de 1875, mot pour mot. Le pivot l'imposait dès 1854. Ce qui change en 1892, ce n'est pas que Dieu soit fini — c'est qu'il soit <em>un</em>.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Le pivot.</strong> 1854 : « l'infini et le nombre sont contradictoires entre eux ». 1903 : « le tout actuel de parties sans fin est un concept contradictoire en soi ». Même argument, même office, quarante-neuf ans.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Le phénoménisme.</strong> Ni loi sans phénomène, ni phénomène sans conscience — et c'est cette prémisse qui produira Dieu en 1886.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>Les neuf catégories</strong>, leur ordre, leurs formes. Reprises telles quelles dans le résumé de 1892.</span></div>
<div class="dp-poste dp-poste--socle"><span class="dp-signe">=</span><span><strong>La liberté</strong>, et le refus des antinomies kantiennes — que la préface de 1903 date « dès son origine », à juste titre.</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que la colonne du bas explique</span>
<p>Regardez ce qui n'a pas bougé : c'est le socle. Regardez ce qui est entré : ce sont des conséquences. <strong>Rien n'a été ajouté du dehors.</strong> Aucune lecture, aucune découverte, aucune conversion — le seul apport extérieur au système, dans toute l'affaire, est un besoin de la raison pratique, et Renouvier l'avoue.</p>
<p>Une pensée qui bouge sans rien recevoir du dehors, c'est exactement ce que fait un dépliant : rien n'entre, rien ne sort, et pourtant à la fin la carte est ouverte. Renouvier n'a pas changé d'avis. Il a déplié une conséquence qui dormait dans sa prémisse depuis trente ans — et elle contredisait sa conclusion.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="1903">
<summary class="dp-titre"><span class="dp-rang">le prix</span><span class="dp-texte">l'harmonie préétablie</span></summary>
<div class="dp-corps">
<p>Voici pourquoi cette prémisse-là, et pas une autre, était celle qu'il fallait changer.</p>
<p>Le dernier livre s'achève sur les monades et l'harmonie préétablie. Or l'harmonie préétablie <strong>exige un coordinateur unique</strong> : c'est Dieu qui, chez Leibniz, accorde entre elles les séries de toutes les monades, sans que rien ne passe de l'une à l'autre. Une pluralité de consciences premières indépendantes ne peut pas s'accorder — c'est même exactement l'argument de 1886 : on ne saurait donner la raison de leur similitude.</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le mot est là dix-sept ans avant</span>
<p>Et il y a mieux qu'une compatibilité. Relisez la phrase de 1886, en oubliant sa date : « Cette <strong>harmonie</strong>, en effet, implique l'unité d'une conscience qui <strong>la conçoit et la réalise</strong> » — une conscience première, unique, libre, finie, qui conçoit et réalise l'ordre des lois régissant des <em>êtres libres</em>.</p>
<p>C'est le dispositif entier. Il n'y a pas encore de monades, pas encore le nom de Leibniz. <strong>Il ne manque que l'adjectif.</strong> Il viendra en 1903, à la dernière ligne du dernier livre : <em>et c'est l'harmonie préétablie</em>.</p>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La conclusion de 1903 n'était pas disponible avant 1886</span>
<p>Le Renouvier du Premier Essai ne <em>pouvait pas</em> écrire la dernière page du <em>Personnalisme</em>. Non parce qu'il n'y avait pas pensé : parce que sa thèse sur l'origine du monde l'interdisait. Il a fallu que l'unité de la conscience première entre dans le système pour que l'harmonie préétablie devienne une option.</p>
<p>Autrement dit : la physique tardive tient à un paragraphe ajouté à un résumé, en 1892, en petits caractères, à la fin d'une introduction que personne ne lit. C'est le genre d'endroit où les systèmes basculent.</p>
</div>
<p class="dp-chapo">La page voisine déplie ce dernier livre : <a href="../physique-tardive/">La physique du personnalisme</a>.</p>
</div>
</details>

</div>
</details>

<p class="dp-epigraphe">— les pièces —</p>

<details class="dp-pli" data-rang="essai">
<summary class="dp-titre"><span class="dp-rang">1854 → 1903</span><span class="dp-texte">La chronologie, et où chaque chose est écrite</span></summary>
<div class="dp-corps">
<p class="dp-chapo">Quatre documents suffisent. Aucun n'est inédit ; aucun n'avait été mis en face des autres.</p>
<div class="dp-escalier">
<div class="dp-marche"><span class="dp-marche-num">1854</span><span><strong>Premier Essai, ch. LIII.</strong> Une conscience du tout est contradictoire. Donc « l'hypothèse d'une pluralité primitive de consciences distinctes, dans le monde, semble donc la seule rationnelle ».</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">1864</span><span>Première édition du résumé du Deuxième Essai, en tête du <em>Troisième</em>. « […] le Soi et le Non-soi <em>sont posés</em> avec la plus grande distinction possible dans <em>la synthèse de</em> la Conscience. » Et déjà : « ces fonctions ont des <em>variables indépendantes</em> réelles ».</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">1875</span><span>Deuxième édition du résumé, rejetée à la fin du Deuxième Essai. « Deux directions de l'esprit <em>sont</em> possibles, légitimes. » Le texte s'arrête sur <em>Fin du formulaire</em>.</span></div>
<div class="dp-marche"><span class="dp-marche-num">1885-86</span><span><strong>Esquisse, t. II</strong> — tout y est, en trois étages que la note de 1892 désigne dans le désordre. <em>p. 108</em> : même la science croit, donc croire est légitime. <em>p. 305</em> : le pari de Locke, l'ordre moral universel est un ordre divin. <em>p. 348</em> : la conscience première, une, libre, finie, « qui conçoit et réalise » l'harmonie des lois. <em>p. 355 sq.</em> : « Comment je suis arrivé à cette conclusion », près de 25 000 mots — le mobile avoué, et la théorie de l'aveu.</span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">1892</span><span>Troisième édition du résumé, remontée en tête du Troisième Essai. Trois variantes : <em>semblent</em>, <em>prise</em>, et 218 mots de conclusion nouvelle. Note de l'auteur signalant l'opération et renvoyant à l'Esquisse.</span></div>
<div class="dp-marche"><span class="dp-marche-num">1899</span><span><em>La Nouvelle Monadologie</em> — le chaînon que la préface de 1903 désignera elle-même : la théorie des monades y est « exposée » avant d'y être « reprise à fond ». <a href="/oeuvres/autres/nouvelle-monadologie/">Transcription sur ce site</a>.</span></div>
<div class="dp-marche"><span class="dp-marche-num">1903</span><span><strong>Le Personnalisme</strong>, préface : « le vrai nom », et « dès son origine ». <em>Étude sur la perception externe et sur la force</em>, dernier mot : « et c'est l'harmonie préétablie ».</span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que le troisième terme a montré</span>
<p>La première édition — 1864 — a été retrouvée en cours de route, et elle a fait mieux que fermer la démonstration : elle a montré que Renouvier <strong>relisait ses trois états</strong>. Car en 1892 il <em>revient</em> à une formule de 1864 qu'il avait abrégée en 1875. Un homme qui corrige la troisième édition d'un texte en rouvrant la première n'écrit pas au fil de la plume : il tient un registre.</p>
<p>Reste que « les deux premières éditions » présentaient la conclusion « seule et sans réserve », dit-il. Nous le vérifions pour 1875 ; pour 1864, seule la section A nous est parvenue, et la conclusion sur Dieu est dans la section D. Le dernier centimètre manque encore.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="méthode">
<summary class="dp-titre"><span class="dp-rang">l'outil</span><span class="dp-texte">Comment la comparaison a été faite, et ce qu'elle ne prouve pas</span></summary>
<div class="dp-corps">
<p>Une page qui accuse un philosophe de s'être contredit doit montrer ses instruments. Voici les miens, avec leurs défauts.</p>
<ul class="dp-liste">
<li><strong>Les deux états ont été alignés mot à mot</strong>, après normalisation (pagination, appels de note, italiques, guillemets, césures). Résultat : 16 212 mots contre 16 811, et <strong>94,3 % de correspondance</strong>.</li>
<li><strong>Les deux tomes viennent de numérisations différentes</strong> — Gallica pour 1875, Google Books pour 1892. L'océrisation produit donc un bruit réel : les divergences d'une ou deux lettres sur un mot ont été écartées comme suspectes.</li>
<li><strong>Un « ajout de 93 mots » a été rejeté</strong> : c'était le tableau de classification des sciences, transcrit en texte d'un côté et en HTML de l'autre par l'édition numérique. Un diff mesure aussi les choix de son éditeur moderne.</li>
<li><strong>Seuls les blocs longs et contigus ont été retenus</strong> — un OCR ne fabrique pas 218 mots de suite, ni ne corrige un accord.</li>
<li><strong>Trois absences apparentes n'étaient que des artefacts de transcription</strong>, et il faut le dire puisque cette page reproche à un philosophe d'avoir bougé sans le dire. La définition de la substance semblait supprimée en 1875 : elle est intacte, ma recherche butait sur les astérisques d'italique du fichier. La formule « variables indépendantes » semblait disparue en 1892 : elle y est, mais coupée par une césure de fin de ligne — « des <em>va- riables indépendantes</em> ». Et le premier alignement donnait 94,6 % : les mêmes césures y créaient des divergences fantômes. Une fois les césures recollées et la méthode figée — mots en minuscules, apostrophes comprises ; pagination, appels de note et marques d'italique retirés ; identité mesurée par les plus longs blocs communs, rapportés à la moyenne des deux textes —, le chiffre s'établit à 94,3 %. <strong>Sur ces textes, une chaîne cherchée telle quelle ne prouve rien ; il faut normaliser avant de conclure à une absence.</strong></li>
<li><strong>La numérisation de l'<em>Esquisse</em> est fautive par endroits.</strong> Les citations en ont été choisies dans les zones saines ; les deux restitutions nécessaires sont entre crochets : « à laquelle [nous a] conduit notre méthode » (le fichier porte « à laquelle je me suis conduire notre méthode », leçon cassée ; restitution conjecturale) et « libre créateur[s] d'êtres libres » (le fichier accorde au pluriel un sujet singulier). Aucune n'affecte le sens ; toutes deux sont signalées ici plutôt que corrigées en silence.</li>
</ul>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Ce que cette page ne dit pas</span>
<p>Elle ne dit pas que Renouvier a menti. Un homme qui laisse debout son ancienne conclusion, met son verbe au conditionnel, ajoute la nouvelle à la suite et signale l'opération en note avec l'adresse des raisons — cet homme fait le contraire d'une dissimulation. Le « dès son origine » de 1903 n'efface rien : il vient <em>après</em> tout cela, chez un homme de quatre-vingt-huit ans qui regarde cinquante ans de travail et y voit, non sans raison, une seule et même chose.</p>
<p>Elle ne dit pas non plus que la question est close. Une vérification reste ouverte, et elle est massive : <strong>vingt ans de <em>Critique philosophique</em></strong>. Si le dispositif est monté dès 1886, le tournant lui est antérieur, et c'est dans la revue qu'il faudrait chercher la date exacte — peut-être l'occasion.</p>
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

Cette page suit les règles de ses deux sœurs — [Compliquer les Essais pour les expliquer](essais.md) et [La physique du personnalisme](physique-tardive.md) : le pli conserve tout ; les voies non prises restent visibles ; la profondeur se compte aux filets ; le parcours se souvient ; la typographie dit qui parle, sérif pour Renouvier, linéale pour le commentaire.

Elle en ajoute une, qui lui est propre. **Ici, le commentaire porte une accusation** — celle d'avoir bougé sans le dire. Il ne peut donc rien avancer qui ne soit vérifiable dans les fichiers du site : chaque variante est donnée dans ses deux états, chaque expression déclarée absente d'un état a été comptée dans les deux, et l'appareil de comparaison est décrit sous le pli « l'outil », avec ce qu'il a dû écarter.

**Sources.** *Essais de critique générale, Premier Essai*, 2ᵉ éd., 1875, t. III (ch. LIII et Formulaire). — *Deuxième Essai*, 2ᵉ éd., 1875, t. III (*Formulaire du Traité de Psychologie rationnelle*, état de 1875). — *Troisième Essai, Les Principes de la nature*, 2ᵉ éd. corrigée et augmentée, 1892, t. I (*Introduction — Résumé des principes de la psychologie rationnelle*, état de 1892, et sa note). — *Esquisse d'une classification systématique des doctrines philosophiques*, t. II, 1886 (« Comment je suis arrivé à cette conclusion »). — *Le Personnalisme, suivi d'une étude sur la perception externe et sur la force*, Félix Alcan, 1903 (préface, et ch. L de l'Étude).
