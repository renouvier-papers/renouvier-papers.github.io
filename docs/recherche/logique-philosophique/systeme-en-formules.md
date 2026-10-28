---
title: "Le système en formules"
description: "La charpente logique du néocriticisme, terme à terme et joint à joint, comme instrument de vérification plutôt que comme résumé."
---

# Le système en formules

Au seuil du Deuxième Essai, Renouvier a lui-même fixé le cahier des charges de cette page :

> **« J'arrive aux catégories empiriquement ; je les fixe par hypothèse, et je les propose pour être vérifiées. »**
> 
> Charles Renouvier, *Essais de critique générale. Deuxième Essai. Traité de psychologie rationnelle d'après les principes du criticisme*, 2e éd. revue et considérablement augmentée, Paris, Au Bureau de la *Critique philosophique*, 1875, t. I, p. 2.

Cette page prend l'offre au mot. Au lieu de raconter le système, elle le démonte avec un outil que Renouvier pratiquait lui-même, la logique formelle, objet de plusieurs chapitres du Premier Essai. Le système entier tient d'abord en **une formule** ; chaque terme s'ouvre ensuite sur sa dérivation, jusqu'aux définitions.

L'essentiel est pourtant ailleurs. Tous les « donc » ne se valent pas, et l'exercice vise à distinguer ceux qui **déduisent**, ceux qui **définissent**, celui qui **suppose** sans le dire, ceux qui **choisissent** et celui qui **raccorde** sous tension deux époques du système. Le style du trait qui souligne chaque connecteur indique la nature du joint.

**Mode d'emploi.** Touchez un <strong>terme</strong> pour afficher sa définition, dans les mots de Renouvier quand ils existent ; un <strong>connecteur</strong>, pour connaître l'opération logique qu'il exécute et le statut de *ce pas-ci*. Les chevrons descendent d'un étage, comme ailleurs sur le site.

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
/* ═══ La couche logique (lg-) ═══
   Une formule est une rangée de jetons : termes (lg-t) et connecteurs (lg-c).
   Chaque jeton est un bouton ; le clic remplit la console du bloc.
   Le STATUT d'un connecteur est porté par le style de son soulignement :
   plein = déduction · pointillé = définition · tirets = prémisse à découvert
   · double = choix · ondulé = raccord sous tension. */
#dp .lg-bloc { margin: 1.1rem 0 1.4rem; }
#dp .lg-formule {
  display: flex; flex-wrap: wrap; align-items: baseline; gap: .05rem .34rem;
  padding: .85rem 1rem; border: 1px solid var(--dp-rule); border-radius: 2px;
  font-family: var(--dp-sans); font-size: .98rem; line-height: 2;
}
#dp .lg-formule--maitre { border-color: var(--dp-accent); font-size: 1.05rem; padding: 1rem 1.1rem; }
#dp .lg-t, #dp .lg-c {
  font: inherit; background: none; border: 0; margin: 0; padding: .02rem .16rem;
  color: inherit; cursor: pointer; border-radius: 2px;
  text-decoration-line: underline; text-underline-offset: .34em; text-decoration-thickness: 1px;
}
#dp .lg-t { font-weight: 640; text-decoration-style: dotted; text-decoration-color: color-mix(in srgb, var(--dp-muted) 60%, transparent); }
#dp .lg-c { color: var(--dp-accent); font-weight: 520; text-decoration-thickness: 1.7px; text-decoration-color: var(--dp-accent); }
#dp .lg-c--val    { text-decoration-style: solid; }
#dp .lg-c--def    { text-decoration-style: dotted; }
#dp .lg-c--cache  { text-decoration-style: dashed; }
#dp .lg-c--choix  { text-decoration-style: double; }
#dp .lg-c--raccord{ text-decoration-style: wavy; }
#dp .lg-c--op     { text-decoration-line: none; }
#dp .lg-t:hover, #dp .lg-c:hover { background: var(--dp-faint); }
#dp .lg-t:focus-visible, #dp .lg-c:focus-visible { outline: 2px solid var(--dp-accent); outline-offset: 2px; }
#dp .lg-actif { background: var(--dp-faint); }
#dp .lg-x { color: var(--dp-muted); }               /* parenthèses et ponctuation */
#dp .lg-console {
  display: none; margin-top: .55rem; padding: .8rem .95rem;
  border-left: 2px solid var(--dp-accent); background: var(--dp-faint);
  font-size: .875rem; line-height: 1.62;
}
#dp .lg-console.lg-ouverte { display: block; }
#dp .lg-console .dp-cite { margin: .6rem 0; background: transparent; }
#dp .lg-etat {
  margin: .55rem 0 0; font-size: .72rem; letter-spacing: .07em; text-transform: uppercase;
  color: var(--dp-accent);
}
#dp .lg-lib { display: none; }
#dp .lg-legende {
  display: flex; flex-wrap: wrap; gap: .4rem 1.1rem; margin: .8rem 0 1.2rem;
  font-size: .78rem; color: var(--dp-muted);
}
#dp .lg-legende .lg-c { pointer-events: none; font-size: .9rem; }
#dp .lg-invite { margin: .3rem 0 0; font-size: .78rem; color: var(--dp-muted); font-style: italic; }
@media (max-width: 44rem) {
  #dp .lg-formule { font-size: .92rem; padding: .7rem .75rem; }
  #dp .lg-formule--maitre { font-size: .96rem; }
}
</style>
<div class="dp-outils">
<button class="dp-bouton" type="button" data-dp="tout">Tout déplier</button>
<button class="dp-bouton" type="button" data-dp="rien">Tout replier</button>
<button class="dp-bouton" type="button" data-dp="neufs">Aller au premier pli non ouvert</button>
<span class="dp-compteur" id="dp-compteur" aria-live="polite"></span>
</div>

<div class="lg-legende" aria-label="Légende des joints">
<span><span class="lg-c lg-c--val">⊢</span> déduction</span>
<span><span class="lg-c lg-c--def">⊢</span> définition</span>
<span><span class="lg-c lg-c--cache">⊢</span> prémisse à découvert</span>
<span><span class="lg-c lg-c--choix">⊢</span> choix</span>
<span><span class="lg-c lg-c--raccord">⊢</span> raccord sous tension</span>
</div>

<p class="dp-chapo">Le système, de 1854 à 1903, tient en une ligne ; sur sept « donc », un seul est souligné double.</p>

<div class="lg-bloc">
<p class="lg-formule lg-formule--maitre" role="group" aria-label="La charpente en une formule">
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="infini">Infini</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="nombre">Nombre</button>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-t" type="button" data-lg="absurde">⊥</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--cache" type="button" data-lg="d1">⊢₁</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="ensoi">ChoseEnSoi</button>
<button class="lg-c lg-c--def" type="button" data-lg="d2">⊢₂</button>
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="connaitre">Connaître := Relier</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--val" type="button" data-lg="d3">⊢₃</button>
<span class="lg-x">(</span>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="omega">Savoir(Ω)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="commencement">Commencement</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--val" type="button" data-lg="d4">⊢₄</button>
<button class="lg-c lg-c--op" type="button" data-lg="poss">◇</button><button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--val" type="button" data-lg="d5">⊢₅</button>
<button class="lg-t" type="button" data-lg="croyable">Croyable(Liberté)</button>
<button class="lg-c lg-c--choix" type="button" data-lg="d6">⊢₆</button>
<button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--def" type="button" data-lg="d7">⊢₇</button>
<button class="lg-t" type="button" data-lg="personne">Personne</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez un terme ou un connecteur —</p>
</div>

<div class="lg-lib" hidden>

<div id="lg-infini">
<span class="dp-etiquette">terme — Infini</span>
<p><strong>Infini</strong> := ce qui ne s'achève pas. Toute la doctrine repose sur la distinction de deux énoncés que le langage confond, <em>aller</em> à l'infini (pour tout n, un n+1 est possible) et <em>être</em> en nombre infini (un tout achevé de parties sans fin). Le premier est permis ; le second est ⊥.</p>
<div class="dp-cite"><p>[…] l'infini et le nombre sont contradictoires entre eux […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
<p class="lg-etat">rôle : définition porteuse — voir le pli « le pivot »</p>
</div>

<div id="lg-nombre">
<span class="dp-etiquette">terme — Nombre</span>
<p><strong>Nombre</strong> := un tout, la synthèse de l'un et du multiple, σ(Un, Multiple). Dire « il y en a sept », c'est avoir <em>fini</em> de compter. Le nombre est un achèvement.</p>
<div class="dp-cite"><p>[…] le <em>nombre</em>, c'est-à-dire […] le <em>tout</em>, qui est la synthèse de l'un et du multiple […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
<p class="lg-etat">rôle : le « := » sur lequel Cantor divergera — voir « le pivot »</p>
</div>

<div id="lg-et">
<span class="dp-etiquette">connecteur — ∧ (« et »)</span>
<p>La conjonction « A ∧ B » n'est vraie que si A et B le sont ensemble. Le pivot porte pourtant sur cette opération, la plus innocente de la logique, puisque la question est de savoir si l'on peut poser <em>ensemble</em> Infini et Nombre.</p>
</div>

<div id="lg-implique">
<span class="dp-etiquette">connecteur — → (« si… alors »)</span>
<p>L'implication « A → B » n'est fausse que si A est vrai et B faux. Ici, si une chose était à la fois nombre et infini, contradiction s'ensuivrait. Tout le travail du système revient à la contraposée, qui rend l'antécédent inacceptable puisque ⊥ l'est.</p>
</div>

<div id="lg-absurde">
<span class="dp-etiquette">terme — ⊥ (la contradiction)</span>
<p>Le faux absolu, qui consiste à tenir ensemble une proposition et sa négation, est <strong>l'unique arme du système</strong>. Renouvier n'interdit que le contradictoire, jamais l'inconnu, l'invérifiable ou l'étrange. Tout ce qui n'implique pas ⊥ reste ouvert, et la croyance (⊢₅) vivra de cette ouverture.</p>
</div>

<div id="lg-non">
<span class="dp-etiquette">connecteur — ¬ (« non »)</span>
<p>La négation renverse la valeur de ce qui la suit. Elle frappe ici deux fois, la chose en soi et le savoir du Tout, deux renoncements dont le système fait ses deux ressources.</p>
</div>

<div id="lg-d1">
<span class="dp-etiquette">⊢₁ — de « pas d'infini actuel » à « pas de chose en soi »</span>
<p>Ce pas repose sur une prémisse que la déduction tait, selon laquelle <strong>dans l'en soi, tout est actuel</strong>, le « possible » n'existant que pour un esprit. Alors seulement « divisible sans fin » devient, en soi, « divisé en une infinité », et le pivot s'applique.</p>
<p class="lg-etat">statut : prémisse à découvert — voir « la serrure de l'en-soi »</p>
</div>

<div id="lg-ensoi">
<span class="dp-etiquette">terme — ChoseEnSoi</span>
<p>Ce qui existerait hors de toute représentation, tel quel, sans témoin. Le kantisme la garde, inconnaissable ; Renouvier la déclare contradictoire, à commencer par l'espace, le temps, la matière et le mouvement, qu'on prétendrait exister en soi :</p>
<div class="dp-cite"><p>L'espace, le temps, la matière, le mouvement, s'ils étaient en soi, impliqueraient le continu en soi, et par suite un nombre infini de parties en soi de ce continu, ce qui est absurde […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d2">
<span class="dp-etiquette">⊢₂ — de « pas d'en soi » à « connaître, c'est relier »</span>
<p>Si rien n'est donné en soi, tout est donné <em>en rapport</em>, et connaître ne peut plus consister à atteindre une chose, mais seulement à déterminer des relations. Ce pas redéfinit sans démontrer. Il constitue le geste fondateur et s'assume comme tel.</p>
<p class="lg-etat">statut : définition</p>
</div>

<div id="lg-connaitre">
<span class="dp-etiquette">terme — Connaître := Relier</span>
<p>C'est la thèse des thèses, qui réduit les neuf catégories à la table des manières de relier (voir le pli « σ — la seule opération du système »).</p>
<div class="dp-cite"><p>Ainsi, Tout phénomène est donné par rapport à d'autres phénomènes.</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d3">
<span class="dp-etiquette">⊢₃ — la limite, déduite</span>
<p>Si connaître := relier, connaître exige un vis-à-vis ; or le Tout, par définition, n'en a pas. La conclusion s'ensuit d'elle-même, par la plus nette des déductions du système.</p>
<p class="lg-etat">statut : déduction — voir « Ω — un seul lemme, deux théorèmes positifs »</p>
</div>

<div id="lg-omega">
<span class="dp-etiquette">terme — Savoir(Ω)</span>
<p><strong>Ω</strong> := le tout des phénomènes. Par définition, rien n'est hors de lui. Aucun rapport ne le détermine donc, et ce qui ne peut être déterminé par aucun rapport ne peut être su.</p>
<div class="dp-cite"><p>[…] la relation composant la synthèse totale, ou le tout du monde, existe toute entre ses propres éléments, cela par définition ; le monde n'est donc pas l'un des termes d'un rapport […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-commencement">
<span class="dp-etiquette">terme — Commencement</span>
<p>Le passé est une série <em>effective</em>, non une possibilité. Une série effective est achevée de fait ; achevée, elle est nombrée ; nombrée, elle est finie (pivot). Elle a donc un premier terme.</p>
<div class="dp-cite"><p>Nous devons poser en fait le premier commencement, parce qu'une suite indéfinie et effective de phénomènes antérieurs est contradictoire ; mais il ne nous est pas possible d'embrasser et d'expliquer cette limite.</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d4">
<span class="dp-etiquette">⊢₄ — du commencement au possible de la liberté</span>
<p>Un commencement appelle des causes premières ; une cause première n'est pas causée ; « commencer sans être déterminé » est donc <em>instancié</em> dans le monde. Dès lors, la liberté, ce même pouvoir logé dans une conscience, n'implique aucune contradiction (◇Liberté).</p>
<p class="lg-etat">statut : déduction — voir « la liberté »</p>
</div>

<div id="lg-poss">
<span class="dp-etiquette">connecteur — ◇ (« possible »)</span>
<p>Le ◇ retenu ici est le possible logique, défini comme ce dont la position n'implique pas ⊥. Renouvier connaît aussi des possibles réels, mais ils restent étrangers à ce pas. ◇Liberté dit donc seulement que la liberté a le droit d'être, non qu'elle <em>est</em>. Toute la différence entre ⊢₄ et ⊢₆ tient dans ce losange.</p>
</div>

<div id="lg-liberte">
<span class="dp-etiquette">terme — Liberté</span>
<p>Le pouvoir de commencer une série, que le langage de 1864, inchangé en trois éditions, formule ainsi :</p>
<div class="dp-cite"><p>[…] ces fonctions ont des <em>variables indépendantes</em> réelles, et elles-mêmes ne <em>sont</em> pas simplement, mais <em>se font</em>.</p><span class="dp-source">Formulaire du Traité de Psychologie rationnelle, 1864 ; même texte en 1875 (Deuxième Essai, t. III, p. 292) et en 1892 (Troisième Essai, t. I, p. XXVI)</span></div>
</div>

<div id="lg-d5">
<span class="dp-etiquette">⊢₅ — l'application de la règle de croyance</span>
<p>La règle s'écrit Croyable(p) := ¬Dém(p → ⊥). Puisque ◇Liberté, la liberté est croyable. Ce pas est une déduction irréprochable ; mais, ¬Liberté n'étant pas davantage démontrée contradictoire, <strong>la règle arme les deux camps</strong>. Le pas suivant ne pourra donc être une déduction.</p>
<p class="lg-etat">statut : déduction</p>
</div>

<div id="lg-croyable">
<span class="dp-etiquette">terme — Croyable(Liberté)</span>
<p>La croyance est libre partout où la raison n'a pas prononcé ⊥, et là seulement.</p>
<div class="dp-cite"><p>[…] les croyances, qui, sans prétendre dépasser ces bornes en s'obstinant dans l'affirmation d'objets que la raison a déclarés contradictoires, demeurent libres de s'étendre au delà […]</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
</div>

<div id="lg-d6">
<span class="dp-etiquette">⊢₆ — le pari</span>
<p>Ce joint est le seul de la ligne-système à être souligné double ; l'étage tardif en ajoutera un second, en 1903. Le dilemme du chapitre XIII ayant établi qu'aucune preuve n'existe, d'aucun côté, ce pas est non une déduction mais un <strong>acte</strong>. Si la liberté est réelle, cet acte est lui-même ce qu'il affirme.</p>
<div class="dp-cite"><p>Alors c'est à la liberté qu'il appartient de déclarer si la liberté est ou non.</p><span class="dp-source">Deuxième Essai, ch. XIII</span></div>
<p class="lg-etat">statut : choix signalé par l'auteur — voir « la liberté »</p>
</div>

<div id="lg-d7">
<span class="dp-etiquette">⊢₇ — de la liberté à la personne</span>
<p>La Personne := la conscience, σ(Soi, Non-Soi), en tant que ses actes ont des variables indépendantes. Cette neuvième catégorie devient le nom du système entier ; l'étage tardif l'étendra vers le haut (conscience première, 1886) et vers le bas (monades, 1899-1903).</p>
<p class="lg-etat">statut : définition — voir « l'étage tardif »</p>
</div>

<div id="lg-personne">
<span class="dp-etiquette">terme — Personne</span>
<div class="dp-cite"><p>9. Personnalité : <em>Liberté</em>. — La <em>Personnalité</em> réunit toutes les catégories, du point de vue de l'homme […]</p><span class="dp-source">Formulaire du Traité de Psychologie rationnelle</span></div>
<p>Le mot viendra en 1903 (« le personnalisme est le vrai nom »), mais sa place, la dernière case du tableau, était réservée dès 1854.</p>
</div>

</div>

<details class="dp-pli" data-rang="rouage 1">
<summary class="dp-titre"><span class="dp-rang">le point de départ</span><span class="dp-texte">Le pivot — ( Infini ∧ Nombre → ⊥ )</span></summary>
<div class="dp-corps">
<p>Tout le système procède de deux définitions et d'un choc, ici mis à plat :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="nombre">Nombre(x)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<button class="lg-t" type="button" data-lg="acheve">Achevé(x)</button>
<span class="lg-x">&nbsp;&nbsp;·&nbsp;&nbsp;</span>
<button class="lg-t" type="button" data-lg="infini">Infini(x)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="acheve">Achevable(x)</button>
<span class="lg-x">&nbsp;&nbsp;·&nbsp;&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="pv1">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-c lg-c--op" type="button" data-lg="poss">◇</button><span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="nombre">Nombre(x)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="infini">Infini(x)</button>
<span class="lg-x">)</span>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez les deux := puis le ⊢ —</p>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le lieu réel de la querelle</span>
<p>La déduction est inattaquable, puisque <em>achevé et inachevable</em>, ensemble, donnent ⊥. Toute la charge repose donc sur les deux <strong>:=</strong>, et c'est là que Cantor frappera. Selon son critère, deux ensembles ont même nombre (même puissance) s'ils sont en bijection, d'où, chez Frege puis Russell, la définition du nombre comme classe d'équivalence. <em>Achevé</em> n'y figure plus ; un ensemble est donné par sa condition d'appartenance, non par un comptage qui finit. Les deux camps sont logiquement irréprochables ; <strong>ils s'affrontent sur un :=, non sur un théorème</strong>. La forme ne peut que rendre ce déplacement visible, ce qui n'est pas rien.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="rouage 2">
<summary class="dp-titre"><span class="dp-rang">⊢₁</span><span class="dp-texte">La serrure de l'en-soi — et sa prémisse à découvert</span></summary>
<div class="dp-corps">
<p>Le Formulaire écrit ce pas en ces termes : « L'espace, le temps, la matière, le mouvement, s'ils étaient en soi, impliqueraient le continu en soi, et par suite un nombre infini de parties en soi de ce continu, ce qui est absurde ». Sa mise en forme fait apparaître un maillon manquant :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="ensoi">EnSoi(X)</button>
<button class="lg-c lg-c--cache" type="button" data-lg="e1">→</button>
<button class="lg-t" type="button" data-lg="actuel">ToutActuel(X)</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<span class="lg-x">(</span><button class="lg-t" type="button" data-lg="continu">Continu(X)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="actuel">ToutActuel(X)</button><span class="lg-x">)</span>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-t" type="button" data-lg="infparties">∞Parties(X)</button>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-t" type="button" data-lg="absurde">⊥</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-t" type="button" data-lg="continu">Continu(X)</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="e2">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="ensoi">EnSoi(X)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez le → en tirets —</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Une prémisse écrite hors de la déduction</span>
<p>Si « divisible sans fin » (permis) devient, en soi, « divisé en une infinité » (⊥), c'est que le possible relève de la représentation et que, hors de tout esprit, rien n'est « en puissance », tout étant ce qu'il est. Renouvier énonce ce principe en toutes lettres, par sa face inverse :</p>
<div class="dp-cite">
<p>[…] on ne réfléchit pas que l'indéfinité de la représentation possible, ou universelle, ne saurait conférer l'existence à d'autres rapports particuliers que ceux qui sont effectivement compris dans les phénomènes donnés […]</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Le possible ne confère pas l'existence ; l'existence en soi ne garde donc aucun possible. Cohérente avec le système et défendable, la prémisse porte pourtant tout le pas et mérite d'être vue. Elle correspond au seul → en tirets de la page.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-defsym">
<span class="dp-etiquette">connecteur — := (« est défini comme »)</span>
<p>Indémontrable, le := <strong>pose</strong>. On le conteste sans le réfuter, en proposant un autre := et en comparant ce que chacun permet de faire. C'est le connecteur le plus puissant et le plus vulnérable de la page, puisque trois des grandes querelles du système (Cantor, la force, la substance) sont des querelles de :=.</p>
</div>
<div id="lg-acheve">
<span class="dp-etiquette">terme — Achevé</span>
<p>Ce dont la synthèse est faite (un tout posé, un comptage fini). L'<em>achevable</em>, ce qui pourrait l'être, en est l'ombre modale. Le pivot joue ces deux mots l'un contre l'autre.</p>
</div>
<div id="lg-pv1">
<span class="dp-etiquette">⊢ — la déduction du pivot</span>
<p>Des deux définitions, la conclusion suit en deux lignes. Si Nombre(x), alors Achevé(x) ; si Infini(x), alors jamais achevable, donc non achevé. Les deux ensemble donnent ⊥, par une déduction valide sans reste.</p>
<p class="lg-etat">statut : déduction — la charge est sur les deux :=</p>
</div>
<div id="lg-e1">
<span class="dp-etiquette">→ en tirets — la prémisse à découvert</span>
<p><strong>EnSoi ⇒ ToutActuel</strong> signifie que, hors de tout esprit, rien n'est « en puissance ». La déduction du Formulaire saute ce maillon. Celui-ci est défendable, et défendu ailleurs (voir l'encart), mais il n'est pas <em>dans</em> le pas. Un réaliste qui prête au continu en soi des parties seulement « potentielles », à la manière d'Aristote, refuse ce point même ; un kantien n'en a pas besoin, puisque pour Kant l'espace et le temps ne sont pas des choses en soi.</p>
<p class="lg-etat">statut : prémisse à découvert</p>
</div>
<div id="lg-actuel">
<span class="dp-etiquette">terme — ToutActuel</span>
<p>État d'une chose dont rien n'est « en réserve », toutes ses déterminations étant posées. Il s'oppose au potentiel, qui, chez Renouvier, n'existe que relativement à une représentation.</p>
</div>
<div id="lg-continu">
<span class="dp-etiquette">terme — Continu</span>
<p>Ce qui n'a pas de dernières parties (entre deux points, toujours un troisième). Représenté, le continu, règle de division toujours ouverte, est inoffensif. En soi, il devrait être <em>fait</em> de ses parties, et elles seraient sans nombre.</p>
</div>
<div id="lg-infparties">
<span class="dp-etiquette">terme — ∞Parties</span>
<p>Une infinité <em>actuelle</em> de parties est un nombre infini, cela même que le pivot vient d'interdire.</p>
</div>
<div id="lg-e2">
<span class="dp-etiquette">⊢ — le rejet de l'antécédent</span>
<p>La conséquence étant ⊥, l'antécédent tombe, et ni l'espace, ni le temps, ni la matière, ni le mouvement n'existent en soi. Le réalisme qui les tenait pour des choses perd son objet par l'arithmétique.</p>
<p class="lg-etat">statut : déduction (une fois accordées la prémisse à découvert et la continuité de X)</p>
</div>
</div>

<details class="dp-pli" data-rang="rouage 3">
<summary class="dp-titre"><span class="dp-rang">⊢₂</span><span class="dp-texte">σ — la seule opération du système</span></summary>
<div class="dp-corps">
<p>Une seule machine engendre les neuf catégories. Chacune est la synthèse de deux contraires corrélatifs, opération que nous noterons <strong>σ</strong> (le symbole est de nous ; l'opération est de lui, à chaque ligne du Formulaire) :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="sigma">σ(a, b)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<span class="lg-x">la synthèse qui pose ensemble deux contraires corrélatifs</span>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>La page des <a href="/recherche/complications/essais/">Essais</a> déplie une à une les neuf instances :</p>
<p class="lg-formule" aria-label="Les neuf instances de sigma">
<span>Déterminé := σ(Distinct, Identique)</span><span class="lg-x">·</span>
<span>Tout := σ(Un, Multiple)</span><span class="lg-x">·</span>
<span>Étendue := σ(Point, Espace)</span><span class="lg-x">·</span>
<span>Durée := σ(Instant, Temps)</span><span class="lg-x">·</span>
<span>Espèce := σ(Différence, Genre)</span><span class="lg-x">·</span>
<span>Changement := σ(Rapport, Non-rapport)</span><span class="lg-x">·</span>
<span>Force := σ(Acte, Puissance)</span><span class="lg-x">·</span>
<span>Passion := σ(État, Tendance)</span><span class="lg-x">·</span>
<span><strong>Conscience := σ(Soi, Non-Soi)</strong></span>
</p>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La loi des corrélats et le théorème d'innocuité</span>
<p>La règle de σ veut que ni a ni b ne soit représentable seul. Renouvier la formule et en tire d'un coup deux résultats :</p>
<div class="dp-cite">
<p>[…] ces termes contraires sont abstraits et corrélatifs, et ne s'appliquent séparément, dans la rigueur de leur signification pure, à aucune autre représentation que celle d'eux-mêmes. Par exemple, aucune chose n'est <em>une</em>, abstraction faite de toute multiplicité ; aucune n'est <em>multiple</em>, abstraction faite de toute unité ; mais toute chose est représentée comme un <em>tout</em>.</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Selon le premier, les prétendus absolus (l'Un seul, le Simple seul, l'Infini seul) sont des <strong>a sans b</strong>, qui ne dénotent rien. Le second, dirigé contre Kant, établit que les catégories, bien employées, <strong>ne produisent aucune antinomie</strong>, les antinomies naissant toutes de l'usage d'un terme arraché à son corrélat. La machine est sûre ; seul son emploi hors règle échoue.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Les forces, au passage</span>
<p>La loi des corrélats désamorce d'avance la physique des causes-choses : « Il n'existe donc pas de <em>causes substantielles</em>, et les <em>forces</em> sont des rapports <em>sui generis</em> donnés entre des phénomènes. » Cette ligne est celle que 1903 rouvrira, par l'autre bout, dans <a href="/recherche/complications/physique-tardive/">La physique du personnalisme</a>.</p>
</div>
</div>
</details>

<details class="dp-pli" data-rang="rouage 4">
<summary class="dp-titre"><span class="dp-rang">⊢₃</span><span class="dp-texte">Ω — un seul lemme, deux théorèmes positifs</span></summary>
<div class="dp-corps">
<p>La quatrième partie du Premier Essai éprouve les catégories une à une sur le monde, et le Formulaire en résume les échecs en huit articles, l'étendue et la durée allant ensemble. Mis en forme, ces échecs se ramènent à <strong>un seul lemme</strong> :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="omegadef">Ω</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<span class="lg-x">le tout des phénomènes</span>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-t" type="button" data-lg="correlat">σ exige deux places</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="o1">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="omega">Savoir(Ω)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Deux catégories, pourtant, <em>produisent</em> en échouant. Appliqués à Ω, le devenir et la causalité rendent, outre l'ignorance, deux théorèmes :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="passe">PasséEffectif(Ω)</button>
<button class="lg-c lg-c--val" type="button" data-lg="o2">⊢</button>
<button class="lg-t" type="button" data-lg="commencement">Commencement</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-t" type="button" data-lg="commencement">Commencement</button>
<button class="lg-c lg-c--val" type="button" data-lg="o3">⊢</button>
<button class="lg-t" type="button" data-lg="premieres">CausesPremières</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">La neuvième instance et son ombre portée</span>
<p>Le lemme s'applique enfin à la dernière catégorie. Conscience := σ(Soi, Non-Soi) ; si Soi := Ω, alors Non-Soi := rien, et σ n'a plus sa seconde place :</p>
<div class="dp-cite">
<p>[…] une conscience enveloppant la totalité des phénomènes cesse de répondre à la notion de conscience […]</p>
<span class="dp-source">Formulaire du Traité de logique générale</span>
</div>
<p>Le Formulaire en tire que la pluralité des consciences premières « semble » la seule hypothèse rationnelle. En outre, le théorème des causes premières contient la question qui occupera la vie de son auteur, « une <strong>ou plusieurs</strong> causes premières », dont le Formulaire laisse l'article indécis. La page <a href="/recherche/complications/evolution/">Comment je suis arrivé à cette conclusion</a> retrace l'histoire de cette indécision.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-sigma">
<span class="dp-etiquette">terme — σ (la synthèse)</span>
<p>L'opération native du système consiste à prendre deux contraires qui ne valent rien l'un sans l'autre et à poser leur tenue ensemble. Neuf instances la déclinent, du Déterminé à la Conscience. Le symbole σ est notre notation ; chaque formule de cette page est un commentaire, contestable comme tel.</p>
</div>
<div id="lg-omegadef">
<span class="dp-etiquette">terme — Ω</span>
<p>Le tout des phénomènes. Sa définition contient sa perte, car « rien hors de lui » signifie « aucun vis-à-vis », donc aucune place dans une relation et, par suite, aucune prise pour σ.</p>
</div>
<div id="lg-correlat">
<span class="dp-etiquette">lemme — σ exige deux places</span>
<p>Toute détermination est une synthèse ; toute synthèse a deux termes ; déterminer x, c'est lui donner un vis-à-vis. Le lemme vaut d'un coup pour les neuf catégories, ce qui explique que la quatrième partie du Premier Essai, si longue en chapitres, soit si courte en logique.</p>
</div>
<div id="lg-o1">
<span class="dp-etiquette">⊢ — la limite</span>
<p>Ω étant sans vis-à-vis, σ reste sans seconde place, d'où ¬Savoir(Ω). La science est bornée par la grammaire de la relation, non par faiblesse.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-passe">
<span class="dp-etiquette">terme — PasséEffectif</span>
<p>Le passé, ayant eu lieu, n'est pas un « possible ». Série effective, il est achevé de fait, donc nombré, et le pivot le déclare fini.</p>
</div>
<div id="lg-o2">
<span class="dp-etiquette">⊢ — le théorème du commencement</span>
<p>Série effective ⊢ finie ⊢ premier terme. Prenant Kant exactement à rebours, Renouvier tranche par l'arithmétique du pivot là où la première antinomie laissait thèse et antithèse dos à dos.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-o3">
<span class="dp-etiquette">⊢ — le théorème des causes premières</span>
<div class="dp-cite"><p>[…] le principe de contradiction oblige à admettre une ou plusieurs causes premières qui terminent la suite ascendante des événements.</p><span class="dp-source">Formulaire du Traité de logique générale</span></div>
<p class="lg-etat">statut : déduction — l'article (« une ou plusieurs ») reste ouvert</p>
</div>
<div id="lg-premieres">
<span class="dp-etiquette">terme — CausesPremières</span>
<p>Des termes qui commencent des séries sans être eux-mêmes des conséquents. Leur existence est déduite ; leur <em>nombre</em> ne l'est pas, et cette case vide est celle où 1886 viendra écrire « une ».</p>
</div>
</div>

<details class="dp-pli" data-rang="rouages 5-6-7">
<summary class="dp-titre"><span class="dp-rang">⊢₄ ⊢₅ ⊢₆</span><span class="dp-texte">La liberté — le possible, le dilemme, la règle, le pari</span></summary>
<div class="dp-corps">
<p>Quatre pièces s'emboîtent ici, dont une seule n'est pas une déduction. Vient d'abord le possible, hérité du théorème des causes premières :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="premieres">CausePremière(c)</button>
<button class="lg-c lg-c--op" type="button" data-lg="implique">→</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="cause">Causé(c)</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="l1">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="poss">◇</button><button class="lg-t" type="button" data-lg="liberte">Liberté</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Suit le dilemme du chapitre XIII, le plus beau morceau de logique du corpus, parce qu'il se retourne sur lui-même :</p>
<div class="lg-bloc">
<p class="lg-formule">
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--op" type="button" data-lg="l2a">→</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<span class="lg-x">(</span>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<button class="lg-c lg-c--op" type="button" data-lg="l2b">→</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--val" type="button" data-lg="l3">⊢</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve(Liberté)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="preuve">Preuve(¬Liberté)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— touchez les deux → : ils n'échouent pas pour la même raison —</p>
</div>
<p>Viennent ensuite la règle de croyance et son application, irréprochable et à double tranchant :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="croyable">Croyable(p)</button>
<button class="lg-c lg-c--def" type="button" data-lg="defsym">:=</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="dem">Dém( p → ⊥ )</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<button class="lg-c lg-c--val" type="button" data-lg="l4">⊢</button>
<button class="lg-t" type="button" data-lg="croyable">Croyable(Liberté)</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="croyable">Croyable(¬Liberté)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<p>Reste enfin le pari, le joint double :</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="croyable">Croyable(Liberté)</button>
<button class="lg-c lg-c--choix" type="button" data-lg="d6">⊢₆</button>
<button class="lg-t" type="button" data-lg="liberte">Liberté</button>
<span class="lg-x">&nbsp;—&nbsp;par l'acte&nbsp;</span>
<button class="lg-t" type="button" data-lg="aff">Affirmer(Liberté)</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">L'honnêteté du système tient à la symétrie</span>
<p>La formule montre, là où les résumés le cachent, que la règle rend croyables <strong>les deux</strong> thèses. À ce point précis du raisonnement, un déterministe est aussi en règle que Renouvier. C'est pourquoi ⊢₆ ne peut être une déduction, et pourquoi Renouvier l'a écrit lui-même au lieu de le déguiser, ce qui fait sa grandeur. Le système contient l'aveu de son propre point de bascule.</p>
</div>
<div class="dp-note">
<span class="dp-etiquette">Les probabilités, insuffisantes de l'aveu même de l'auteur</span>
<p>Le chapitre XIII recourt au calcul des probabilités (la loi des grands nombres vérifiée par l'expérience est compatible avec des possibles réellement égaux). Dès 1864, le Formulaire juge que ce calcul « fournit ainsi, selon sa nature, une sorte de probabilité, plutôt qu'une démonstration de la liberté comme réelle ». Une <em>probabilité de la liberté</em> n'étant pas une preuve, le pari reste entier.</p>
<p class="lg-invite">source : Formulaire du Traité de Psychologie rationnelle — 1864 (Troisième Essai, 1re éd.), p. XXXVII ; 1875 (Deuxième Essai, 2e éd., t. III), p. 307 ; 1892 (Troisième Essai, 2e éd., t. I), p. XLII.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-cause">
<span class="dp-etiquette">terme — Causé</span>
<p>Déterminé par des antécédents selon une loi. Une cause première ne l'est pas, par définition, puisque la dire causée reviendrait à la poser « avant elle-même ».</p>
</div>
<div id="lg-l1">
<span class="dp-etiquette">⊢ — du théorème au possible</span>
<p>Le monde contient déjà des commencements non déterminés (les causes premières). Une conscience qui commencerait ses séries (la liberté) n'ajoute donc aucune contradiction à l'inventaire. ◇Liberté exprime le droit d'exister, non encore l'existence.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-l2a">
<span class="dp-etiquette">→ — la première branche du dilemme</span>
<p>Si je suis libre, c'est <em>librement</em> que je juge la question. Acte et non constat, mon jugement ne prouve rien. La liberté, vraie, détruit la preuve de la liberté.</p>
</div>
<div id="lg-l2b">
<span class="dp-etiquette">→ — la seconde branche</span>
<p>Si je suis déterminé, mon jugement (quel qu'il soit, vrai ou faux) était inévitable et ne prouve rien non plus. « C'est une manière d'être dans le <em>vrai</em>, que de suivre une loi nécessaire en affirmant le <em>faux</em> des autres hommes » (Formulaire, 1875, t. III, p. 302). La nécessité, vraie, avale ainsi toute preuve, y compris la sienne.</p>
</div>
<div id="lg-l3">
<span class="dp-etiquette">⊢ — l'impasse démontrée</span>
<p>Les deux branches réunies rendent toute preuve impossible, d'un côté comme de l'autre. Théorème d'impossibilité, et non constat d'ignorance provisoire, ce résultat déblaie le terrain pour un acte.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-preuve">
<span class="dp-etiquette">terme — Preuve</span>
<p>Une démonstration contraignante, valable pour tout esprit, indépendante de celui qui la donne. Le dilemme la rend ici impossible, car toute « preuve » de la liberté passe par un jugement dont le statut est la question même.</p>
</div>
<div id="lg-dem">
<span class="dp-etiquette">terme — Dém( p → ⊥ )</span>
<p>« Il est démontré que p implique contradiction. » La croyance n'est bornée que par cela, le seul ⊥ établi, et non par l'invraisemblable ou l'inouï.</p>
</div>
<div id="lg-l4">
<span class="dp-etiquette">⊢ — l'application, à double tranchant</span>
<p>◇Liberté donne Croyable(Liberté). Or rien n'a démontré ¬Liberté contradictoire, d'où aussi Croyable(¬Liberté). La déduction, parfaite, laisse ouvertes les deux portes, et à dessein.</p>
<p class="lg-etat">statut : déduction</p>
</div>
<div id="lg-aff">
<span class="dp-etiquette">terme — Affirmer(Liberté)</span>
<p>Affirmer la liberté est un acte, non une proposition, et, si la liberté est réelle, <em>l'affirmer librement est un cas de ce qu'on affirme</em>, propriété qu'aucune proposition ne possède. L'affirmation exerce la liberté sans la prouver. En revanche, si la nécessité est vraie, l'affirmer n'est qu'un événement de plus.</p>
<div class="dp-cite"><p>Le principe de ces principes est la liberté.</p><span class="dp-source">Deuxième Essai — le second ordre de la certitude</span></div>
<p class="lg-etat">conséquence : chaque ⊢ de cette page, une fois <em>affirmé</em>, repose sur ⊢₆</p>
</div>
</div>

<details class="dp-pli" data-rang="rouages 8-9">
<summary class="dp-titre"><span class="dp-rang">⊢₇ et après</span><span class="dp-texte">L'étage tardif — le raccord de 1886, le choix de 1903</span></summary>
<div class="dp-corps">
<p>Deux arguments s'ajoutent à la charpente après 1885 et introduisent les deux derniers joints, l'ondulé et le second double.</p>

<p class="dp-epigraphe">1886 — l'argument de l'unité</p>
<div class="lg-bloc">
<p class="lg-formule">
<span class="lg-x">(</span>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="loisansphi">Loi sans Phénomène</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="phisansc">Phénomène sans Conscience</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="communaute">Communauté(Lois)</button>
<button class="lg-c lg-c--raccord" type="button" data-lg="t1">⊢</button>
<button class="lg-t" type="button" data-lg="c0">ConsciencePremière</button>
</p>
<div class="lg-console" aria-live="polite"></div>
<p class="lg-invite">— le seul ⊢ ondulé du corpus : touchez-le —</p>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Les deux forces qui tirent sur le joint ondulé</span>
<p><strong>Ce qui pousse</strong>, c'est le phénoménisme de 1854 lui-même. Une loi n'existe que représentée ; les lois sont les mêmes pour toutes les consciences ; une loi une exige « une conscience une et universelle donnée à cet objet ». Sans apport étranger, la prémisse de jeunesse produit Dieu d'elle-même.</p>
<p><strong>Ce qui tire en face</strong>, c'est le chapitre LIII, resté debout. Une conscience du Tout est ⊥, faute de non-soi. Le raccord de Renouvier passe au plus juste. C₀ n'enveloppe pas Ω ; son non-soi consiste en ses créatures libres ; on peut, dit le résumé de 1892, l'envisager « comme le souverain Auteur et siège suprême de ces lois […], mais non comme un être existant en dehors de ces lois » ; elle est finie, et le pivot y veille. <strong>Reste l'objection qu'un kantien ferait</strong>, selon laquelle la communauté des catégories pourrait être un fait sans auteur. Renouvier répond par sa définition (une loi non représentée n'existe pas), ce qui reconduit le débat à un :=. Le joint tient, mais il travaille. L'histoire de sa pose figure sur la page <a href="/recherche/complications/evolution/">Comment je suis arrivé à cette conclusion</a>.</p>
</div>

<p class="dp-epigraphe">1903 — le choix sur la force</p>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="source">Source(idée de Force) = Volonté</button>
<span class="lg-x">&nbsp;·&nbsp;</span>
<span class="lg-x">(</span>
<button class="lg-t" type="button" data-lg="nominale">Force := ValeurNominale</button>
<button class="lg-c lg-c--op" type="button" data-lg="ou">∨</button>
<button class="lg-t" type="button" data-lg="forcevol">Force := Volonté</button>
<span class="lg-x">)</span>
<button class="lg-c lg-c--choix" type="button" data-lg="t2">⊢</button>
<button class="lg-t" type="button" data-lg="forcevol">Force := Volonté</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="lg-bloc">
<p class="lg-formule">
<button class="lg-t" type="button" data-lg="forcevol">Force := Volonté</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-t" type="button" data-lg="rienpasse">RienNePasse</button>
<button class="lg-c lg-c--val" type="button" data-lg="t3">⊢</button>
<button class="lg-t" type="button" data-lg="monades">Monades</button>
<button class="lg-c lg-c--val" type="button" data-lg="t4">⊢</button>
<button class="lg-t" type="button" data-lg="harmonie">Harmonie</button>
<span class="lg-x">&nbsp;—&nbsp;avec&nbsp;</span>
<button class="lg-t" type="button" data-lg="liberte">variables indépendantes</button>
<button class="lg-c lg-c--op" type="button" data-lg="et">∧</button>
<button class="lg-c lg-c--op" type="button" data-lg="non">¬</button><button class="lg-t" type="button" data-lg="infini">Infini</button>
</p>
<div class="lg-console" aria-live="polite"></div>
</div>
<div class="dp-note">
<span class="dp-etiquette">Le second choix, argumenté mais choix</span>
<p>La disjonction est réelle, et la première branche respectable, celle des mathématiciens et des physiciens qui ont « dû l'abandonner, ou du moins la réduire à sa valeur nominale ». Renouvier prend l'autre pour une raison qu'il donne, la branche nominale renonçant à comprendre quand la sienne comprend, au prix de peupler la matière de volontés. Formellement, ce pas n'est ni une ∨-élimination (raisonnement par cas) ni un syllogisme disjonctif (lequel exigerait de réfuter l'autre branche), mais le choix motivé d'une branche, non un théorème. Le détail figure dans <a href="/recherche/complications/physique-tardive/">La physique du personnalisme</a>.</p>
</div>
</div>
</details>

<div class="lg-lib" hidden>
<div id="lg-loisansphi">
<span class="dp-etiquette">terme — Loi sans Phénomène</span>
<p>Une loi qui régnerait sur rien est exclue, puisqu'une loi est un « phénomène complexe constamment impliqué dans d'autres phénomènes » et n'a d'autre lieu que ce qu'elle règle.</p>
</div>
<div id="lg-phisansc">
<span class="dp-etiquette">terme — Phénomène sans Conscience</span>
<p>Un donné sans témoin est exclu par la définition initiale, selon laquelle les choses sont données « en qualité de représentations ». Cette moitié, la plus dure du phénoménisme, portera tout le poids de 1886.</p>
</div>
<div id="lg-communaute">
<span class="dp-etiquette">terme — Communauté(Lois)</span>
<p>Le fait est qu'espace, temps et causalité sont les mêmes pour toutes les consciences, et que nous sommes « membres du même monde intelligible ». La pluralité de 1854 laissait ce fait sans raison.</p>
</div>
<div id="lg-t1">
<span class="dp-etiquette">⊢ ondulé — le raccord de 1886</span>
<p>« Cette harmonie, en effet, implique l'unité d'une conscience qui la conçoit et la réalise. » Le pas est le sien, mot pour mot, et il doit passer entre deux murs qu'il a lui-même bâtis, le ch. LIII (pas de conscience du Tout) et le pivot (pas d'infini). C₀ en résulte, une, libre, <em>finie</em>, avec un dehors. Le raccord passe, en travaillant.</p>
<p class="lg-etat">statut : raccord sous tension — Esquisse, t. II, 1886</p>
</div>
<div id="lg-c0">
<span class="dp-etiquette">terme — ConsciencePremière</span>
<div class="dp-cite"><p>[…] la conscience première et universelle, auteur du monde, libre créateur d'êtres libres.</p><span class="dp-source">Esquisse, t. II, p. 348 — la transcription porte « créateurs », coquille corrigée ici</span></div>
<p>Son unité fournit l'article que la case « une ou plusieurs » attendait depuis 1854 ; le pivot la veut finie, le pur commencement, libre.</p>
</div>
<div id="lg-ou">
<span class="dp-etiquette">connecteur — ∨ (« ou »)</span>
<p>La disjonction est vraie dès que l'une au moins des deux branches l'est. En choisir une quand aucun théorème ne ferme l'autre relève d'une décision, non d'une règle logique ; tel est le geste exact de 1903 sur la force.</p>
</div>
<div id="lg-source">
<span class="dp-etiquette">terme — Source(idée de Force)</span>
<div class="dp-cite"><p>L'expérience nous fait connaître les modifications mutuelles des mouvements des corps en leurs rencontres ; mais c'est par une illusion mentale seulement, que nous appliquons à leurs rapports […] les idées de force, impulsive ou résistante, avec une signification secrètement empruntée aux cas où les agents seraient supposés volontaires.</p><span class="dp-source">Étude sur la perception externe et sur la force, ch. XX, p. 352</span></div>
<p>Le sens de l'idée de force vient du vouloir, constat génétique dont il ne suit pas encore que la force <em>soit</em> volonté ; d'où la disjonction, et le choix.</p>
</div>
<div id="lg-nominale">
<span class="dp-etiquette">terme — Force := ValeurNominale</span>
<div class="dp-cite"><p>[…] les mathématiciens et les physiciens ont dû l'abandonner, ou du moins la réduire à sa valeur nominale, exprimant un rapport défini d'antécédent à conséquent […]</p><span class="dp-source">Le Personnalisme, préface</span></div>
<p>La branche positiviste remplace la force par des fonctions. Renouvier la juge tenable, mais vide.</p>
</div>
<div id="lg-forcevol">
<span class="dp-etiquette">terme — Force := Volonté</span>
<p>La branche retenue garde au mot son seul contenu connu. Il s'ensuit immédiatement que les porteurs de force sont des vouloirs, donc des consciences. La physique change d'habitants.</p>
</div>
<div id="lg-t2">
<span class="dp-etiquette">⊢ double — le choix de 1903</span>
<p>Aucun théorème ne ferme la branche nominale. Renouvier élit l'autre pour un motif (comprendre plutôt que renoncer), mais un motif n'est pas une démonstration. Second joint double du corpus, ce pas est argumenté et non signé, ce qui le distingue de ⊢₆.</p>
<p class="lg-etat">statut : choix motivé</p>
</div>
<div id="lg-rienpasse">
<span class="dp-etiquette">terme — RienNePasse</span>
<div class="dp-cite"><p>[…] aucun intermédiaire n'est perçu, aucune hypothèse rationnelle ne s'offre, au delà du fait lui-même, et de notre idée de cause, et d'une liaison vérifiée, qui puisse nous faire comprendre cette liaison elle-même […]</p><span class="dp-source">Étude sur la perception externe et sur la force, ch. L, p. 531</span></div>
</div>
<div id="lg-monades">
<span class="dp-etiquette">terme — Monades</span>
<div class="dp-cite"><p>[…] on peut les appeler des monades […]</p><span class="dp-source">Étude, ch. L, p. 533-534</span></div>
<p>Agents mentaux sans fenêtres, elles corrigent deux fois Leibniz, avec des variables indépendantes en plus (la liberté) et l'infini en moins. L'« automate incorporel » cesse d'être automate.</p>
</div>
<div id="lg-harmonie">
<span class="dp-etiquette">terme — Harmonie</span>
<p>Des séries qui s'accordent sans que rien ne passe requièrent un accordeur, C₀, posée en 1886, dix-sept ans avant que le dernier mot du dernier livre ne soit écrit : « et c'est l'harmonie préétablie ».</p>
</div>
<div id="lg-t3">
<span class="dp-etiquette">⊢ — des vouloirs sans fenêtres aux monades</span>
<p>Si les éléments sont des vouloirs et que rien ne transite entre eux, chacun se développe du dedans, et la définition de la monade est atteinte par déduction, une fois le choix ⊢ fait en amont.</p>
<p class="lg-etat">statut : déduction (conditionnelle au choix)</p>
</div>
<div id="lg-t4">
<span class="dp-etiquette">⊢ — des monades à l'harmonie</span>
<p>Entre des séries closes qui pourtant se répondent, l'accord ne peut être que préréglé. La conclusion suit ; encore exigeait-elle C₀, puisque sans le raccord de 1886 ce ⊢ serait insolvable.</p>
<p class="lg-etat">statut : déduction (conditionnelle au raccord)</p>
</div>
</div>

<details class="dp-pli" data-rang="l'audit">
<summary class="dp-titre"><span class="dp-rang">bilan</span><span class="dp-texte">Le tableau de contrôle — chaque joint, son statut, sa source</span></summary>
<div class="dp-corps">
<p>Le tableau suivant dresse l'audit complet des articulations maîtresses. Les statuts sont nos jugements, donc des commentaires, contestables comme tels ; les sources sont les siennes.</p>
<div class="dp-escalier">
<div class="dp-marche"><span class="dp-marche-num">⊢₁</span><span><strong>prémisse à découvert</strong> — du pivot à ¬ChoseEnSoi ; le maillon tu, « en soi ⇒ tout actuel ». <em>Formulaire ; l'appui est p. 282 du même texte.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₂</span><span><strong>définition</strong> — Connaître := Relier ; le geste fondateur, assumé. <em>Formulaire.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₃</span><span><strong>déduction</strong> — le lemme d'Ω (pas de vis-à-vis, pas de savoir). <em>Premier Essai, quatrième partie.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₄</span><span><strong>déduction</strong> — commencement, causes premières, donc ◇Liberté. <em>Formulaire.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₅</span><span><strong>déduction</strong> — la règle de croyance, appliquée ; elle arme les deux camps. <em>Formulaire.</em></span></div>
<div class="dp-marche dp-marche--pli"><span class="dp-marche-num">⊢₆</span><span><strong>choix — signé</strong> — « C'est à la liberté qu'il appartient de déclarer si la liberté est ou non. » <em>Deuxième Essai, ch. XIII.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢₇</span><span><strong>définition</strong> — Personne := la conscience à variables indépendantes. <em>Formulaire de 1864, inchangé.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢ 1886</span><span><strong>raccord sous tension</strong> — de l'unité des lois à la conscience première, entre les deux murs de 1854. <em>Esquisse, t. II.</em></span></div>
<div class="dp-marche"><span class="dp-marche-num">⊢ 1903</span><span><strong>choix — motivé</strong> — Force := Volonté, contre la branche nominale laissée ouverte. <em>Le Personnalisme.</em></span></div>
</div>
<div class="dp-note dp-note--cle">
<span class="dp-etiquette">Le bilan en une phrase</span>
<p>Cinquante ans de système tiennent en neuf articulations maîtresses, soit <strong>trois déductions, deux définitions, une prémisse à découvert, un raccord, deux choix</strong>, dont l'un est signé par l'auteur et l'autre argumenté par lui. Un philosophe qu'on vérifie n'en est pas diminué. Celui-ci a construit de telle sorte qu'on <em>puisse</em> le vérifier, et a lui-même souligné le joint principal, ce qui est rare.</p>
</div>
</div>
</details>

<div class="dp-legende">
<p><strong>Comment lire cette page.</strong> Le <span style="font-family: var(--dp-serif); font-style: italic;">sérif</span> cite Renouvier mot pour mot ; la linéale — y compris chaque formule — est notre commentaire. Le trait sous un joint dit sa nature : plein, déduit ; pointillé, défini ; tirets, supposé ; double, choisi ; ondulé, raccordé sous tension.</p>
<p><strong>Ce que la forme peut, et ce qu'elle ne peut pas.</strong> Une formalisation teste la <em>validité</em> : si les prémisses, alors la conclusion. Elle ne teste ni la vérité des prémisses, ni la justesse des définitions — elle les met à nu, c'est tout son office, et c'est déjà beaucoup : trois des grandes querelles autour de ce système (Cantor, la force, la substance) se révèlent être des querelles de :=, pas de théorèmes.</p>
<p><strong>Le vertige, pour finir.</strong> Dans ce système, la certitude est une clef de voûte, pas une première pierre — « le principe de ces principes est la liberté ». Chaque ⊢ de cette page, du moment qu'on l'<em>affirme</em>, repose donc sur ⊢₆. L'audit lui-même est un acte. Renouvier n'aurait pas voulu qu'il en fût autrement.</p>
<p><strong>Sources.</strong> Œuvres de Charles Renouvier, disponibles sur ce site. Les symboles (σ, Ω, ⊢ et le reste) sont de nous.</p>
<p><strong>Ce qui manque encore — et c'est une invitation.</strong> Descendre d'un étage : formaliser chaque catégorie avec ses Observations, mettre en forme le calcul des probabilités du chapitre XIII, et donner sa page à la contestation — chaque statut de l'audit est discutable, et la page est construite pour qu'on puisse la prendre en défaut. « Je les propose pour être vérifiées » : nous aussi.</p>
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

(function () {
  var racine = document.getElementById('dp');
  if (!racine) return;
  racine.addEventListener('click', function (e) {
    var jeton = e.target.closest('[data-lg]');
    if (!jeton || !racine.contains(jeton)) return;
    var source = document.getElementById('lg-' + jeton.getAttribute('data-lg'));
    var bloc = jeton.closest('.lg-bloc');
    var sortie = bloc ? bloc.querySelector('.lg-console') : null;
    if (!source || !sortie) return;
    sortie.innerHTML = source.innerHTML;
    sortie.classList.add('lg-ouverte');
    var actifs = bloc.querySelectorAll('.lg-actif');
    for (var i = 0; i < actifs.length; i++) actifs[i].classList.remove('lg-actif');
    jeton.classList.add('lg-actif');
  });
})();
</script>
</div>
