"""Renouvier Papers : crochets de construction du site (MkDocs, clé « hooks » de mkdocs.yml).

Ce fichier fait six choses, toutes au moment où le site est construit. Aucun fichier de
docs/ n'est modifié.

1. SOMMAIRES. Une page dont l'en-tête YAML contient « sommaire: rubrique » reçoit la liste
   hiérarchisée de tout ce que la navigation de mkdocs.yml range dans sa rubrique ; avec
   « sommaire: portail » (l'accueil), elle reçoit une ligne par grande rubrique du site : son nom
   et une phrase qui dit ce qu'on y trouve. La liste se place à l'endroit du commentaire
   <!-- sommaire --> (à défaut, à la fin de la page). Elle se met à jour toute seule quand la
   navigation change. Sur l'accueil, ce qui suit le commentaire (mode d'emploi, présentation du
   projet) est composé sur les deux mêmes colonnes que les rubriques : titre à gauche, texte à droite.
   Le sommaire d'une rubrique est une carte : chaque groupe (une catégorie d'ouvrages, une revue,
   un auteur) y tient en quelques lignes, son titre, ce qu'il contient, son nombre de volumes et
   leurs carrés ; un clic sur le groupe déplie la liste de ses textes. Quand la rubrique est
   longue, les groupes sont repliés à l'arrivée : on voit d'abord l'ensemble, le détail ensuite.
   Clés facultatives de l'en-tête :
     notices:   (rubrique) intitulé d'un groupe -> phrase affichée sous son titre ; l'ordre des
                notices fixe l'ordre des groupes, les groupes sans notice suivent dans l'ordre du menu.
                Sans notice, le groupe annonce de lui-même les titres qu'il contient
     repli:     (rubrique) « oui » : groupes repliés à l'arrivée ; « non » : groupes dépliés ; sans
                cette clé, ils sont repliés dès que la rubrique compte plus de REPLI_AUTO lignes
     cartes:    (portail) intitulé d'une rubrique -> « texte » (la phrase affichée sur l'accueil ;
                un titre d'ouvrage s'y écrit entre astérisques, *Uchronie*, pour être en italique)
                et « unite » (« volume, volumes » : ce que comptent les groupes de sa carte)
   Chaque ligne indique l'état du texte, lu dans le fichier : « brut » si la page porte le
   bandeau « texte brut non corrigé », « à venir » (sans lien) si la page est vide ou absente.

2. TITRES EN CAPITALES. Un titre écrit tout en capitales (« ## BORNES DE LA CONNAISSANCE. »)
   est affiché en minuscules avec sa majuscule initiale (« Bornes de la connaissance. »). Les
   noms propres retrouvent leur capitale d'après l'usage du texte lui-même (un mot qui s'écrit
   presque toujours avec une capitale au milieu des phrases en garde une), les chiffres romains
   restent en capitales, et un accent absent des capitales est rétabli quand le mot n'existe
   qu'accentué. Quand seule l'étiquette qui ouvre le titre est en capitales (« CHAPITRE XIII.
   Problèmes ajournés. »), elle seule est convertie (« Chapitre XIII. Problèmes ajournés. »).
   Pour qu'une page garde ses capitales : « capitales: conserver » dans son en-tête.
   Pour corriger un mot précis : le dictionnaire EXCEPTIONS ci-dessous.

3. FIL D'ARIANE. Les rubriques qui n'ont pas de page à elles (« Autres ouvrages », un auteur,
   un ouvrage en plusieurs tomes) renvoient à leur entrée dans le sommaire de la rubrique.

4. RECHERCHE. L'index de recherche de Material embarque le texte intégral de chaque page : avec
   toutes les transcriptions, il dépassait 200 Mo et le navigateur n'arrivait jamais au bout de
   son chargement. Pour les transcriptions (dossiers de TRANSCRIPTIONS ci-dessous), l'index ne
   garde donc que les titres (ouvrages, chapitres, paragraphes) et les premières lignes de chaque
   section ; les autres pages restent indexées en entier.

5. MENU LATÉRAL. Les intitulés longs du menu sont hiérarchisés : l'auteur d'un article passe en
   surtitre au-dessus du titre (« F. Pillon — L'évolution historique de l'atomisme »), une série
   (« — 1re série ») ou une précision finale entre parenthèses (« (1876) ») passent au second
   plan, un titre très long est limité à trois lignes. Une entrée dont le fichier n'existe pas
   encore porte la mention « à venir » (et rp.js lui retire son lien, qui ne mènerait nulle part).
   Les intitulés de mkdocs.yml ne sont pas modifiés : seul leur affichage dans le menu l'est.

6. GRAND TITRE ET ESPACES INSÉCABLES. Un titre de page long est composé dans un corps plus petit
   et sa précision finale entre parenthèses passe au second plan. Dans les transcriptions, une
   espace insécable est posée devant ; : ! ? » et après « là où il n'y en avait pas, pour qu'aucune
   ligne ne commence par un signe de ponctuation. Rien n'est modifié dans les fichiers.

En cas d'imprévu, chaque fonction laisse la page telle quelle et écrit un avertissement dans
le journal de construction : le site est construit quand même.
"""
import html
import logging
import re
import unicodedata
from collections import Counter

from markupsafe import Markup

from mkdocs.structure.nav import Link, Section
from mkdocs.structure.pages import Page
from mkdocs.utils import get_relative_url
from mkdocs.utils import meta as mk_meta

log = logging.getLogger('mkdocs.hooks.renouvier')

# Mots dont la forme est imposée dans les titres passés en minuscules (clé en minuscules).
EXCEPTIONS = {
    'mm': 'MM',
}

MARQUEUR = '<!-- sommaire -->'
REPLI_AUTO = 15        # au-delà de ce nombre de lignes, les groupes d'une rubrique sont repliés à l'arrivée
_NAV = {'nav': None, 'imbrication': True, 'unites': None}
_ETATS = {}
_ENTETES = {}


# =====================================================================================
#  Outils
# =====================================================================================
def ancre(texte):
    """Identifiant d'ancre : minuscules sans accents, mots séparés par des traits d'union."""
    texte = texte.replace('œ', 'oe').replace('Œ', 'oe').replace('æ', 'ae').replace('Æ', 'ae')
    texte = unicodedata.normalize('NFKD', texte)
    texte = ''.join(c for c in texte if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z0-9]+', '-', texte).strip('-') or 'section'


def _lire_debut(chemin, taille=16000):
    try:
        with open(chemin, encoding='utf-8-sig', errors='replace') as f:
            return f.read(taille)
    except OSError:
        return ''


def entete(page):
    """En-tête YAML d'une page, lu dans le fichier (la page n'est pas forcément déjà chargée)."""
    chemin = page.file.abs_src_path
    if chemin not in _ENTETES:
        try:
            _ENTETES[chemin] = mk_meta.get_data(_lire_debut(chemin))[1] or {}
        except Exception:  # en-tête illisible : on fait sans
            _ENTETES[chemin] = {}
    return _ENTETES[chemin]


def etat(item):
    """'ok', 'brut' (bandeau « texte brut non corrigé »), 'vide' (page sans texte) ou 'absent'."""
    if not isinstance(item, Page):
        return 'absent'
    chemin = item.file.abs_src_path
    if chemin not in _ETATS:
        debut = _lire_debut(chemin)
        if not debut:
            _ETATS[chemin] = 'absent'
        else:
            corps = re.sub(r'(?s)\A---\n.*?\n---\n', '', debut)
            if re.search(r'(?mi)^!!!\s+\w+\s+"[^"\n]*(texte brut|non corrig)', corps):
                _ETATS[chemin] = 'brut'
            else:
                texte = re.sub(r'(?m)^(#|>|!!!|---|\s{4}).*$', '', corps)
                _ETATS[chemin] = 'ok' if len(texte.strip()) >= 300 else 'vide'
    return _ETATS[chemin]


def _page_index(section):
    if section.children and isinstance(section.children[0], Page) and section.children[0].is_index:
        return section.children[0]
    return None


def _titre_et_date(titre):
    """« Uchronie (1876) » -> (« Uchronie », « 1876 »). Sans millésime final, la date est vide."""
    m = re.match(r'^(.*\S)\s*\(([^()]*\b1[5-9]\d\d\b[^()]*)\)\s*$', titre or '')
    if m and len(m.group(2)) <= 28:
        return m.group(1), m.group(2)
    return titre or '', ''


def _pages(item):
    if isinstance(item, Section):
        for enfant in item.children:
            yield from _pages(enfant)
    else:
        yield item


def _volumes(rubrique):
    """Les pages d'une rubrique, à ceci près qu'un groupe qui a sa propre page d'accueil (une année de revue
    découpée en livraisons) compte pour une seule unité, représentée par cette page."""
    for enfant in rubrique.children:
        if isinstance(enfant, Section):
            index = _page_index(enfant)
            if index is not None:
                yield index
            else:
                yield from _volumes(enfant)
        else:
            yield enfant


# =====================================================================================
#  Intitulés du menu latéral
# =====================================================================================
# Le menu latéral est étroit, les intitulés des revues sont longs. Un article (« F. Pillon —
# L'évolution historique de l'atomisme ») y est rendu sur deux registres : l'auteur en surtitre,
# le titre dessous. Une série (« — 1re série ») ou une précision finale entre parenthèses
# (« (1876) ») passent au second plan. L'intitulé lui-même n'est pas modifié : seul son balisage
# dans le menu l'est, par l'attribut « typeset » que lit le gabarit du menu de Material. Onglets,
# fil d'Ariane, titres de page et recherche gardent l'intitulé tel quel.
_SERIE = re.compile(r'^(?:\d+(?:re|er|e)|première|deuxième|seconde|nouvelle) série$', re.I)
_ORDINAL = re.compile(r'^\d+(?:re|er|e)\b')
_PRECISION = re.compile(r'^(.*\S)\s*(\([^()]{2,60}\))$')
_LONG = 64       # au-delà, un titre est limité à trois lignes dans le menu (sauf page courante)


def decouper_intitule(intitule):
    """Renvoie (surtitre, titre, série, précision) ; chaîne vide pour une partie absente.

    « F. Pillon — La critique de l'infini »   -> ('F. Pillon', "La critique de l'infini", '', '')
    « La Critique philosophique — 1re série » -> ('', 'La Critique philosophique', '1re série', '')
    « Uchronie (1876) »                       -> ('', 'Uchronie', '', '(1876)')
    « 1re année (1872) »                      -> ('', '1re année (1872)', '', '') : rien à hiérarchiser
    """
    surtitre = serie = precision = ''
    titre = (intitule or '').strip()
    avant, tiret, apres = titre.partition(' — ')
    if tiret:
        avant, apres = avant.strip(), apres.strip()
        if _SERIE.match(apres):
            titre, serie = avant, apres
        elif avant and apres and len(avant) <= 30 and len(avant.split()) <= 3:
            surtitre, titre = avant, apres
    m = _PRECISION.match(titre)
    if m and not _ORDINAL.match(titre):
        titre, precision = m.group(1), m.group(2)
    return surtitre, titre, serie, precision


def _balises_intitule(intitule, a_venir=False):
    """Le balisage de l'intitulé pour le menu, ou None quand le texte nu suffit."""
    surtitre, titre, serie, precision = decouper_intitule(intitule)
    if not (surtitre or serie or precision or a_venir) and len(titre) < _LONG:
        return None
    e = html.escape
    bulle = f' title="{e(intitule, quote=True)}"' if len(titre) >= _LONG else ''
    sortie = ''
    if surtitre:
        sortie += f'<span class="rp-nav__sur">{e(surtitre)}</span><span class="rp-nav__sep"> — </span>'
    sortie += f'<span class="rp-nav__titre"{bulle}>{e(titre)}'
    if precision:
        insecable = ' rp-nav__insecable' if len(precision) <= 14 else ''
        sortie += f' <span class="rp-nav__precision{insecable}">{e(precision)}</span>'
    sortie += '</span>'
    if serie:
        sortie += f'<span class="rp-nav__sep"> — </span><span class="rp-nav__serie">{e(serie)}</span>'
    if a_venir:
        sortie += '<span class="rp-nav__avenir">à venir</span>'
    return Markup(sortie)


def _page_manquante(item):
    """Une entrée de mkdocs.yml dont le fichier n'existe pas encore : MkDocs en fait un lien brut vers « x.md »."""
    url = getattr(item, 'url', '') or ''
    return isinstance(item, Link) and url.endswith('.md') and not re.match(r'^(?:[a-z][a-z0-9+.-]*:|//)', url, re.I)


def _intitules(items):
    for item in items:
        balises = _balises_intitule(getattr(item, 'title', None), _page_manquante(item))
        if balises is not None:
            item.typeset = {'title': balises}
        if isinstance(item, Section):
            _intitules(item.children)


# =====================================================================================
#  1. Sommaires
# =====================================================================================
def on_nav(nav, config, files):
    """Garde la navigation sous la main et donne une adresse aux rubriques sans page propre."""
    _NAV['nav'] = nav
    _NAV['unites'] = None
    # la carte d'une rubrique emboîte du Markdown dans des blocs HTML : il y faut l'extension md_in_html
    _NAV['imbrication'] = any(str(x) == 'md_in_html' for x in (config.get('markdown_extensions') or []))
    try:
        for rubrique in nav.items:
            if not isinstance(rubrique, Section):
                continue
            index = _page_index(rubrique)
            if index is None or str(entete(index).get('sommaire', '')).lower() not in ('rubrique', 'true'):
                continue
            vues = set()
            for groupe in rubrique.children:
                if not isinstance(groupe, Section):
                    continue
                groupe.rp_ancre = _unique(ancre(groupe.title), vues)
                groupe.rp_url = index.url + '#' + groupe.rp_ancre
                _ancrer(groupe, index, vues)
    except Exception as e:  # ne jamais empêcher la construction
        log.warning('Renouvier Papers : ancres du fil d\'Ariane non posées (%s)', e)
    try:
        _intitules(nav.items)
    except Exception as e:
        log.warning('Renouvier Papers : intitulés du menu non balisés (%s)', e)
    return nav


def _ancrer(groupe, index, vues):
    for item in groupe.children:
        if isinstance(item, Section):
            item.rp_ancre = _unique(groupe.rp_ancre + '--' + ancre(_titre_et_date(item.title)[0]), vues)
            if _page_index(item) is None:      # une année de revue qui a sa page garde son adresse
                item.rp_url = index.url + '#' + item.rp_ancre
            _ancrer(item, index, vues)


def _unique(identifiant, vues):
    base, n = identifiant, 2
    while identifiant in vues:
        identifiant = f'{base}-{n}'
        n += 1
    vues.add(identifiant)
    return identifiant


def _lien(item, page):
    return html.escape(get_relative_url(item.url, page.url), quote=True)


ETIQUETTES = {
    'brut': ('brut', 'Texte brut : issu de la reconnaissance optique, pas encore relu'),
    'vide': ('à venir', 'Texte à venir'),
    'absent': ('à venir', 'Texte à venir'),
}


def _marque(e):
    if e not in ETIQUETTES:
        return ''
    mot, bulle = ETIQUETTES[e]
    return f'<span class="rp-etat rp-etat--{"brut" if e == "brut" else "avenir"}" title="{bulle}">{mot}</span>'


def _carre(item, e):
    """Le carré d'état d'un volume transcrit : plein, la relecture est faite ; vide, le texte est encore
    brut. Rien pour les pages qui ne sont pas des transcriptions."""
    if e not in ('ok', 'brut') or not isinstance(item, Page) or not item.file.src_uri.startswith(TRANSCRIPTIONS):
        return ''
    return '<i class="rp-carre%s" aria-hidden="true"></i>' % (' rp-carre--vide' if e == 'brut' else '')


RIEN = '<i class="rp-carre rp-carre--rien" aria-hidden="true"></i>'


def _carre_ou_place(item, e):
    """Le carré d'état, ou sa place laissée vide : les titres d'une liste commencent tous au même endroit."""
    return _carre(item, e) or RIEN


def _ligne(item, page):
    """Une ligne du sommaire : un texte d'un seul tenant."""
    titre, date = _titre_et_date(item.title)
    e = etat(item)
    desc = ''
    if isinstance(item, Page):
        d = entete(item).get('description')
        if d:
            desc = f'<span class="rp-cat__desc">{html.escape(str(d))}</span>'
    corps = (f'<span class="rp-cat__corps"><span class="rp-cat__titre">{_carre_ou_place(item, e)}{html.escape(titre)}</span>{desc}</span>'
             f'{_marque(e)}'
             + (f'<span class="rp-cat__date">{html.escape(date)}</span>' if date else ''))
    if e in ('vide', 'absent'):
        return f'<li class="rp-cat__item is-avenir"><span class="rp-cat__ligne">{corps}</span></li>'
    return f'<li class="rp-cat__item"><a class="rp-cat__ligne" href="{_lien(item, page)}">{corps}</a></li>'


def _nom_de_puce(titre):
    """« 2e livraison (juillet 1878) » -> « Juillet 1878 » ; les autres titres sont gardés."""
    m = re.match(r'^\d+(?:re|e) livraison \((.+)\)$', titre or '')
    if m:
        return m.group(1)[:1].upper() + m.group(1)[1:]
    return _titre_et_date(titre)[0] or titre or ''


def _ligne_multiple(section, page):
    """Une ligne du sommaire : un ouvrage en plusieurs tomes ou éditions, une année de revue (avec sa page
    d'accueil, à laquelle renvoie le titre, et ses livraisons ou rubriques en puces)."""
    titre, date = _titre_et_date(section.title)
    index = _page_index(section)
    enfants = [e for e in section.children if e is not index]
    puces = []
    etats = [etat(p) for p in enfants]
    tous_bruts = bool(etats) and all(e == 'brut' for e in etats)
    for enfant, e in zip(enfants, etats):
        nom = html.escape(_nom_de_puce(enfant.title) if index is not None else (enfant.title or ''))
        if e in ('vide', 'absent'):
            puces.append(f'<span class="rp-puce is-avenir" title="Texte à venir">{nom}</span>')
        else:
            brut = '' if tous_bruts or e != 'brut' else ' is-brut'
            bulle = ' title="Texte brut : pas encore relu"' if brut else ''
            puces.append(f'<a class="rp-puce{brut}" href="{_lien(enfant, page)}"{bulle}>{_carre(enfant, e)}{nom}</a>')
    ident = f' id="{section.rp_ancre}"' if getattr(section, 'rp_ancre', None) else ''
    nom_titre = html.escape(titre)
    if index is not None and etat(index) not in ('vide', 'absent'):
        nom_titre = f'<a class="rp-cat__lien" href="{_lien(index, page)}">{nom_titre}</a>'
    # les carrés sont dans les puces : la place d'un carré garde le titre aligné sur ceux des autres lignes
    nom_titre = RIEN + nom_titre
    return (f'<li class="rp-cat__item rp-cat__item--multiple"{ident}><div class="rp-cat__ligne">'
            f'<span class="rp-cat__corps"><span class="rp-cat__titre">{nom_titre}</span>'
            f'<span class="rp-cat__tomes">{"".join(puces)}</span></span>'
            f'{_marque("brut") if tous_bruts else ""}'
            + (f'<span class="rp-cat__date">{html.escape(date)}</span>' if date else '')
            + '</div></li>')


def _en_articles(pages):
    """Les pages d'une année de revue sont-elles des articles (un auteur, un titre souvent long) ? Des
    tomes, des livraisons ou des rubriques tiennent en puces ; des articles, non."""
    if not pages:
        return False
    signes = sum(1 for p in pages if decouper_intitule(getattr(p, 'title', ''))[0])
    return signes * 2 >= len(pages) or max(len(getattr(p, 'title', '') or '') for p in pages) > 60


def _ligne_annee(section, page):
    """Une ligne du sommaire : une année de revue qui a sa page d'accueil et dont les textes sont des
    articles. La ligne mène à cette page (source, plan et tables du volume, chaque article relié) ; elle
    annonce le contenu de l'année, auteur puis titre. Les articles eux-mêmes ne sont pas donnés en puces :
    leurs titres sont trop longs pour y tenir."""
    titre, date = _titre_et_date(section.title)
    index = _page_index(section)
    e = etat(index)
    annonce = []
    for enfant in section.children:
        if enfant is index:
            continue
        auteur, nom, serie, precision = decouper_intitule(enfant.title)
        nom = ' '.join(x for x in (nom, precision) if x) + (f' — {serie}' if serie else '')
        nom = html.escape(nom.rstrip('.'))
        annonce.append(f'<span class="rp-cat__auteur">{html.escape(auteur)}</span>, {nom}' if auteur else nom)
    desc = '<span class="rp-cat__desc rp-cat__desc--annonce">' + '\u00a0; '.join(annonce) + '</span>' if annonce else ''
    ident = f' id="{section.rp_ancre}"' if getattr(section, 'rp_ancre', None) else ''
    corps = (f'<span class="rp-cat__corps"><span class="rp-cat__titre">{_carre_ou_place(index, e)}{html.escape(titre)}</span>{desc}</span>'
             f'{_marque(e)}'
             + (f'<span class="rp-cat__date">{html.escape(date)}</span>' if date else ''))
    return f'<li class="rp-cat__item rp-cat__item--annee"{ident}><a class="rp-cat__ligne" href="{_lien(index, page)}">{corps}</a></li>'


def _sous_groupes(items):
    """Vrai quand l'un des éléments est lui-même un groupe de groupes (une édition qui réunit plusieurs
    ouvrages en plusieurs tomes) : ses voisins de même rang sont alors, comme lui, donnés sous un intertitre."""
    return any(isinstance(i, Section) and any(isinstance(e, Section) for e in i.children) for i in items)


def _liste(items, page, niveau):
    """Lignes d'un groupe. Un ouvrage en plusieurs tomes ou éditions tient sur une ligne ; un sous-groupe
    qui contient lui-même des groupes devient un intertitre, et ses voisins de même rang avec lui (les deux
    éditions des Essais : la première réunit quatre volumes, la seconde trois ouvrages en plusieurs tomes)."""
    sortie, lignes = [], []
    intertitres = _sous_groupes(items)

    def vider():
        if lignes:
            sortie.append('<ul class="rp-cat" data-search-exclude>\n' + '\n'.join(lignes) + '\n</ul>')
            lignes.clear()

    for item in items:
        if isinstance(item, Section):
            index = _page_index(item)
            if index is not None and all(not isinstance(e, Section) for e in item.children):
                # une année de revue qui a sa page d'accueil
                autres = [e for e in item.children if e is not index]
                if _en_articles(autres) and etat(index) not in ('vide', 'absent'):
                    lignes.append(_ligne_annee(item, page))
                else:
                    lignes.append(_ligne_multiple(item, page))
            elif not intertitres and all(not isinstance(e, Section) for e in item.children):
                lignes.append(_ligne_multiple(item, page))
            else:
                vider()
                ident = f' {{ #{item.rp_ancre} }}' if getattr(item, 'rp_ancre', None) else ''
                sortie.append('#' * min(niveau + 1, 4) + f' {item.title}{ident}')
                sortie.append(_liste(item.children, page, niveau + 1))
        else:
            lignes.append(_ligne(item, page))
    vider()
    return '\n\n'.join(sortie)


def _paire(valeur, defaut):
    if isinstance(valeur, str) and ',' in valeur:
        a, b = [x.strip() for x in valeur.split(',', 1)]
        return a, b
    if isinstance(valeur, (list, tuple)) and len(valeur) == 2:
        return str(valeur[0]), str(valeur[1])
    return defaut


def _nombre(n, paire):
    return f'{n}\u00a0{paire[0] if n == 1 else paire[1]}'


LEGENDE = ('<i class="rp-carre" aria-hidden="true"></i>Carré plein : la relecture est faite. '
           '<i class="rp-carre rp-carre--vide" aria-hidden="true"></i>Carré vide, mention « brut » : texte issu '
           'de la reconnaissance optique de caractères, qui n\'a pas encore été relu.')
LEGENDE_FAITE = '<i class="rp-carre" aria-hidden="true"></i>Carré plein : la relecture du texte est faite.'


def _unite(rubrique):
    """Le nom de ce que compte une rubrique (« volume, volumes »), tel que le fixe la page d'accueil
    (clé « cartes » de son en-tête, où sont réglées les rubriques)."""
    if _NAV['unites'] is None:
        _NAV['unites'] = {}
        nav = _NAV['nav']
        for p in (nav.pages if nav is not None else []):
            meta = entete(p)
            if str(meta.get('sommaire', '')).lower() == 'portail':
                for titre, r in (meta.get('cartes') or {}).items():
                    if isinstance(r, dict) and r.get('unite'):
                        _NAV['unites'][titre] = _paire(r.get('unite'), None)
                break
    return _NAV['unites'].get(rubrique.title) or ('texte', 'textes')


_TOME = re.compile(r'^Tome ([IVXLC]+)$')


def _apercu(groupe):
    """Ce qu'un groupe contient, dit en une phrase par ses titres : « Science de la morale, Uchronie, … ».
    Sert quand la page de la rubrique ne lui donne pas de notice. Les titres d'ouvrages sont en italique ;
    les divisions (une édition, une introduction, des tomes) en romain, et une suite de tomes est résumée."""
    index = _page_index(groupe)
    enfants = [e for e in groupe.children if e is not index]
    divisions = _sous_groupes(enfants)
    noms, tomes = [], []

    def vider_tomes():
        if len(tomes) >= 3:
            noms.append(f'tomes {tomes[0]} à {tomes[-1]}')
        elif tomes:
            noms.append(('tome ' if len(tomes) == 1 else 'tomes ') + ' et '.join(tomes))
        tomes.clear()

    for e in enfants:
        titre, date = _titre_et_date(e.title)
        m = _TOME.match(titre)
        if m:
            tomes.append(m.group(1))
            continue
        vider_tomes()
        if divisions and isinstance(e, Section):
            noms.append(html.escape(e.title or ''))                 # une édition, avec ses dates
        elif date or isinstance(e, Section):
            noms.append(f'<em>{html.escape(titre)}</em>')           # un ouvrage
        else:
            noms.append(html.escape(titre))
    vider_tomes()
    if noms and not noms[0].startswith('<em>'):
        noms[0] = noms[0][:1].upper() + noms[0][1:]
    # « Victor Hugo, le poète » : dès qu'un titre contient une virgule, le point-virgule sépare les titres
    return ('\u00a0; ' if any(',' in n for n in noms) else ', ').join(noms)


def _mesure(groupe, page, unite):
    """Le décompte d'un groupe et ses carrés (un par volume)."""
    etats = [e for e in (etat(p) for p in _volumes(groupe)) if e in ('ok', 'brut')]
    n = len(etats)
    if not n:
        return '<span class="rp-groupe__compte">à venir</span>'
    sortie = f'<span class="rp-groupe__compte">{html.escape(_nombre(n, unite))}</span>'
    if page.file.src_uri.startswith(TRANSCRIPTIONS):
        b = etats.count('brut')
        # les carrés ne sont pas lus par les lecteurs d'écran : le relevé les dit en mots (il n'est pas affiché)
        releve = 'relecture faite' if not b else f'relecture : {n - b} sur {n}'
        sortie += ('<span class="rp-carte__pixels" aria-hidden="true">'
                   + ''.join('<i class="b"></i>' if e == 'brut' else '<i></i>' for e in etats) + '</span>'
                   + f'<span class="rp-groupe__releve"> ({releve})</span>')
    return sortie


def _titre_de_groupe(intitule):
    """Le titre d'un groupe tel qu'il s'écrit sur la carte : sa série (« — 1re série ») ou sa précision
    finale (« (supplément, 1878-1885) ») passent au second plan, comme dans le menu et les grands titres."""
    surtitre, titre, serie, precision = decouper_intitule(intitule)
    if surtitre or not (serie or precision):
        return intitule or ''
    if precision:
        titre += f' <span class="rp-titre__precision">{html.escape(precision)}</span>'
    if serie:
        titre += f' <span class="rp-titre__precision">— {html.escape(serie)}</span>'
    return titre


def _nombre_de_lignes(items, groupes=False):
    """Nombre de lignes qu'affiche une liste : un ouvrage en plusieurs tomes compte pour une, comme une
    année de revue. Au premier rang (« groupes »), chaque section est un groupe dont on compte les lignes."""
    n, intertitres = 0, _sous_groupes(items)
    for item in items:
        if isinstance(item, Section) and _page_index(item) is None and (
                groupes or intertitres or any(isinstance(e, Section) for e in item.children)):
            n += _nombre_de_lignes(item.children)
        else:
            n += 1
    return n


def sommaire_rubrique(page):
    rubrique = page.parent
    if not isinstance(rubrique, Section):
        return ''
    notices = page.meta.get('notices') or {}
    enfants = [e for e in rubrique.children if e is not page]
    if notices:
        # l'ordre des notices fixe celui des groupes ; les autres suivent dans l'ordre du menu
        rang = {titre: i for i, titre in enumerate(notices)}
        libres = [e for e in enfants if not isinstance(e, Section)]
        groupes = sorted((e for e in enfants if isinstance(e, Section)),
                         key=lambda g: rang.get(g.title, len(rang)))
        enfants = libres + groupes
    groupes = [e for e in enfants if isinstance(e, Section)]
    emboite = bool(_NAV['imbrication'])
    # Groupes repliés à l'arrivée ? Oui dès que la liste est longue (on voit d'abord l'ensemble), sauf
    # avis contraire de la page (clé « repli » de son en-tête).
    voeu = str(page.meta.get('repli', '')).strip().lower()
    if voeu in ('oui', 'yes', 'true', '1'):
        replie = True
    elif voeu in ('non', 'no', 'false', '0'):
        replie = False
    else:
        replie = len(groupes) >= 2 and _nombre_de_lignes(enfants, groupes=True) > REPLI_AUTO
    replie = replie and emboite
    unite = _unite(rubrique)
    blocs, libres = [], []

    def vider():
        if libres:
            blocs.append(_liste(libres, page, 1))
            libres.clear()

    for e in enfants:
        if not isinstance(e, Section):
            libres.append(e)
            continue
        vider()
        ident = getattr(e, 'rp_ancre', None) or ancre(e.title)
        notice = notices.get(e.title)
        if not emboite:
            # sans l'extension md_in_html : la liste à plat, comme avant
            blocs.append(f'## {e.title} {{ #{ident} }}')
            if notice:
                blocs.append(f'{str(notice).strip()}\n{{ .rp-notice }}')
            blocs.append(_liste(e.children, page, 2))
            continue
        tete = [f'## {_titre_de_groupe(e.title)} {{ #{ident} .rp-groupe__titre }}']
        if notice:
            tete.append(f'{str(notice).strip()}\n{{ .rp-groupe__apercu .rp-notice }}')
        else:
            apercu = _apercu(e)
            if apercu:
                tete.append(f'<p class="rp-groupe__apercu rp-groupe__apercu--auto" data-search-exclude>{apercu}</p>')
        tete.append(f'<p class="rp-groupe__mesure" data-search-exclude>{_mesure(e, page, unite)}</p>')
        blocs.append('\n\n'.join([
            f'<div class="rp-groupe{"" if replie else " is-ouvert"}" markdown="1">',
            '<div class="rp-groupe__tete" markdown="1">', *tete, '</div>',
            '<div class="rp-groupe__corps" markdown="1">', _liste(e.children, page, 2), '</div>',
            '</div>']))
    vider()
    if len(groupes) >= 8 and not replie:
        # accès direct aux groupes, pour les écrans qui n'affichent pas la table des matières
        liens = ''.join(f'<a class="rp-puce" href="#{getattr(g, "rp_ancre", None) or ancre(g.title)}">'
                        f'{html.escape(g.title)}</a>' for g in groupes)
        blocs.insert(0, f'<nav class="rp-index" aria-label="Accès direct" data-search-exclude>{liens}</nav>')
    etats = {etat(p) for p in _pages(rubrique)}
    legende = ''
    if 'brut' in etats:
        legende = f'{LEGENDE}\n{{ .rp-legende }}'
    elif 'ok' in etats and page.file.src_uri.startswith(TRANSCRIPTIONS):
        legende = f'{LEGENDE_FAITE}\n{{ .rp-legende }}'
    if not emboite:
        return '\n\n'.join(b for b in [legende] + blocs if b)
    if legende:
        blocs.insert(0, '<div class="rp-sommaire__entete" markdown="1">\n\n' + legende + '\n\n</div>')
    return '\n\n'.join(
        [f'<div class="rp-sommaire{" rp-sommaire--replie" if replie else ""}" markdown="1">']
        + [b for b in blocs if b] + ['</div>'])


def _phrase(texte):
    """La phrase d'une rubrique sur l'accueil : texte simple, où un titre entre astérisques est en italique."""
    return re.sub(r'\*([^*\n]+)\*', r'<em>\1</em>', html.escape(str(texte or '').strip()))


def sommaire_portail(page):
    """L'accueil : une ligne par rubrique, son nom et ce qu'on y trouve. Ni décompte ni état des textes
    (ils sont sur la carte de chaque rubrique) ; une rubrique qui n'a encore aucun texte est dite « à venir »."""
    nav = _NAV['nav']
    if nav is None:
        return ''
    reglages = page.meta.get('cartes') or {}
    cartes = []
    for rubrique in nav.items:
        if not isinstance(rubrique, Section):
            continue
        index = _page_index(rubrique)
        if index is None or index is page:
            continue
        r = reglages.get(rubrique.title) or {}
        if isinstance(r, str):
            r = {'texte': r}
        texte = _phrase(r.get('texte'))
        if not any(etat(p) in ('ok', 'brut') for p in _volumes(rubrique) if p is not index):
            if texte and texte[-1] not in '.!?…':
                texte += '.'
            texte += (' ' if texte else '') + 'À venir.'
        cartes.append(
            f'<a class="rp-carte" href="{_lien(index, page)}">'
            f'<span class="rp-carte__titre">{html.escape(rubrique.title)}</span>'
            f'<span class="rp-carte__texte">{texte}</span>'
            '</a>')
    if not cartes:
        return ''
    return ('<nav class="rp-portail" aria-label="Rubriques du site" data-search-exclude>\n'
            + '\n'.join(cartes) + '\n</nav>')


def inserer_sommaire(markdown, page):
    genre = str(page.meta.get('sommaire', '')).lower()
    if genre == 'portail':
        bloc = sommaire_portail(page)
    elif genre in ('rubrique', 'true'):
        bloc = sommaire_rubrique(page)
    else:
        return markdown
    if not bloc:
        return markdown
    if MARQUEUR in markdown:
        if genre == 'portail' and _NAV['imbrication']:
            # Ce qui suit les rubriques (mode d'emploi, présentation du projet) est enveloppé : la feuille
            # de style le compose sur les deux colonnes des rubriques, titre à gauche, texte à droite.
            avant, suite = markdown.split(MARQUEUR, 1)
            if suite.strip():
                return (avant + bloc + '\n\n<div class="rp-suite" markdown="1">\n\n'
                        + suite.strip('\n') + '\n\n</div>\n')
        return markdown.replace(MARQUEUR, bloc, 1)
    return markdown.rstrip() + '\n\n' + bloc + '\n'


# =====================================================================================
#  2. Titres en capitales
# =====================================================================================
_LETTRES_MIN = 'a-zàâäáãåæçéèêëíìîïñóòôöõœúùûüýÿ'
_LETTRES_MAJ = 'A-ZÀÂÄÁÃÅÆÇÉÈÊËÍÌÎÏÑÓÒÔÖÕŒÚÙÛÜÝŸ'
_MOT = re.compile(rf'[{_LETTRES_MAJ}{_LETTRES_MIN}]+')
_MOT_MIN = re.compile(rf'(?<![{_LETTRES_MAJ}{_LETTRES_MIN}])[{_LETTRES_MIN}]+(?![{_LETTRES_MAJ}{_LETTRES_MIN}])')
# mot à capitale initiale au milieu d'une phrase : précédé d'une minuscule, d'une virgule ou d'un
# point-virgule (avec, éventuellement, une élision : « de l'Église », « qu'Aristote »)
_MOT_CAP = re.compile(
    rf"(?<=[{_LETTRES_MIN},;] )(?:(?:[dlnscjmt]|qu|jusqu|lorsqu|puisqu)[’'])?([{_LETTRES_MAJ}][{_LETTRES_MIN}]+)")
_TITRE = re.compile(r'^(#{1,6})([ \t]+)(.*?)([ \t]*)$')
_PROTEGE = re.compile(
    r'\[p\.\s[^\]]*\]'            # marqueurs de page
    r'|\[\^[^\]]*\]'              # appels de note
    r'|\\\(.*?\\\)'               # formules
    r'|<[^>]+>'                   # balises
    r'|\{[:#.][^}]*\}\s*$'        # attributs en fin de titre
    r'|`[^`]*`'                   # code
    r'|\]\([^)]*\)'               # cible d'un lien
)
_ROMAIN = re.compile(r'^(?=[IVXLC])(C{0,2})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
_SUJETS = {'y', 'il', 'elle', 'on', 'qui', 'ne', 'en'}
_DETERMINANTS = {'les', 'des', 'aux', 'le', 'la', 'du', 'un', 'une', 'ces', 'nos', 'chez'}
_STATS = {'pret': False, 'maj': Counter(), 'min': Counter(), 'variantes': {}, 'fichiers': {}}


def _sans_accents(mot):
    return ''.join(c for c in unicodedata.normalize('NFD', mot) if not unicodedata.combining(c))


_ROMAIN_LARGE = re.compile(r'^[IVX]{2,}$')
_ROMAIN_ORDINAL = re.compile(r'^[IVXLC]+(er|re|e|me|ème|d|de|nd|nde)$')
# « CHAPITRE II DE L'ÊTRE » : le numéro du chapitre et son titre se suivent sans ponctuation
_ORD = r'(?:PREMIER|PREMI[ÈE]RE|SECONDE?|DERNI[ÈE]RE?|UNIQUE|[A-ZÉÈ-]+I[ÈE]ME)'
_NOM_DIV = r'(?:CHAPITRE|LIVRE|PARTIE|SECTION|LE[ÇC]ON|TITRE|ARTICLE|NOTE|APPENDICE|[ÉE]TUDE|TOME)'
_NUMERO = re.compile(
    rf'^\W*(?:{_NOM_DIV}\s+(?:[IVXLC]+|\d+|{_ORD})|{_ORD}\s+{_NOM_DIV})\s+(?=[«"“]?[^\W\d_])')


def _est_romain(mot):
    return bool(_ROMAIN.match(mot) or _ROMAIN_LARGE.match(mot))


def _lettres_hors_protection(texte):
    return _PROTEGE.sub(' ', texte)


def en_capitales(texte):
    """Vrai si le titre est écrit en capitales (au moins un vrai mot, 80 % de capitales)."""
    mots = [m for m in _MOT.findall(_lettres_hors_protection(texte)) if not _est_romain(m)]
    lettres = ''.join(m for m in mots if len(m) >= 2)
    if len(lettres) < 4:
        return False
    maj = sum(1 for c in lettres if c.isupper())
    return maj / len(lettres) >= 0.8


_CAPS = rf"(?:[{_LETTRES_MAJ}][’'])?[{_LETTRES_MAJ}]{{2,}}(?:[-’'][{_LETTRES_MAJ}]+)*"
_ETIQUETTE = re.compile(rf"^[^\w<\[{{`\\]*{_CAPS}(?:[\s.,:—–-]+(?:{_CAPS}|\d+)(?![{_LETTRES_MIN}]))*")
_DIVISIONS = re.compile(
    r'^(CHAPITRE|LIVRE|PARTIE|SECTION|SECT|LE[ÇC]ON|TITRE|ARTICLE|NOTES?|APPENDICE|[ÉE]TUDE|TOME|CAPUT|'
    r'INTRODUCTION|PR[ÉE]FACE|CONCLUSION|AVERTISSEMENT|AVANT-PROPOS|POSTFACE|SUPPL[ÉE]MENT|R[ÉE]SUM[ÉE]|'
    r'PREMIER|PREMI[ÈE]RE|SECONDE?|DERNI[ÈE]RE?|[A-ZÉÈ]+I[ÈE]ME)$')


def etiquette_capitales(texte):
    """Longueur de l'étiquette en capitales qui ouvre un titre (« CHAPITRE XIII. » …), ou 0."""
    m = _ETIQUETTE.match(texte)
    if not m:
        return 0
    suite = texte[m.end():]
    if not re.search(rf'[{_LETTRES_MIN}]', _lettres_hors_protection(suite)):
        return 0
    mots = [x for x in _MOT.findall(m.group()) if len(x) >= 2 and not _est_romain(x)]
    if not mots:
        return 0
    if _DIVISIONS.match(mots[0]) or (len(mots) >= 2 and sum(len(x) for x in mots) >= 8):
        return m.end()
    # un seul mot en capitales suivi d'un tiret (« CORRESPONDANCE — À M. J. Milsand », titres des revues)
    if len(mots) == 1 and len(mots[0]) >= 4 and re.match(r'\s*[—–]\s', suite):
        return m.end()
    return 0


_BLOC_BRUT = re.compile(r'<(pre|code|style|script|textarea|svg|math)\b', re.I)


def _titres_capitales(markdown):
    """Lignes de titre en capitales d'un fichier, hors blocs de code, de style et de script."""
    trouves, cloture = [], None
    for i, ligne in enumerate(markdown.split('\n')):
        nue = ligne.strip()
        if cloture:
            if (cloture in ('```', '~~~') and nue.startswith(cloture)) or (
                    cloture.startswith('</') and cloture in nue.lower()):
                cloture = None
            continue
        if nue.startswith(('```', '~~~')):
            cloture = nue[:3]
            continue
        m_bloc = _BLOC_BRUT.search(nue)
        if m_bloc:
            fin = f'</{m_bloc.group(1).lower()}>'
            if fin not in nue.lower()[m_bloc.end():]:
                cloture = fin
            continue
        m = _TITRE.match(ligne)
        if not m:
            continue
        if en_capitales(m.group(3)):
            trouves.append((i, m, None))
        else:
            fin = etiquette_capitales(m.group(3))
            if fin:
                trouves.append((i, m, fin))
    return trouves


def _compter(texte):
    """Usage d'un texte : formes en minuscules, et formes à capitale au milieu des phrases."""
    minuscules = Counter(_MOT_MIN.findall(texte))
    majuscules = Counter(m.lower() for m in _MOT_CAP.findall(texte))
    return majuscules, minuscules


def _preparer_stats(files):
    """Un seul passage sur les textes qui ont des titres en capitales."""
    if _STATS['pret']:
        return
    _STATS['pret'] = True
    for f in files.documentation_pages():
        try:
            with open(f.abs_src_path, encoding='utf-8-sig', errors='replace') as fh:
                texte = fh.read()
        except OSError:
            continue
        titres = _titres_capitales(texte)
        if not titres:
            continue
        maj, mini = _compter(texte)
        _STATS['maj'].update(maj)
        _STATS['min'].update(mini)
        besoin = set()
        for _, m, fin in titres:
            for mot in _MOT.findall(_lettres_hors_protection(m.group(3)[:fin])):
                besoin.add(mot.lower())
        _STATS['fichiers'][f.abs_src_path] = {
            mot: (maj.get(mot, 0), mini.get(mot, 0)) for mot in besoin}
    # formes accentuées rangées par squelette sans accents (« deuxieme » -> « deuxième ») ;
    # on garde les deux plus fréquentes pour écarter les cas ambigus (« eleve » : élève ou élevé ?)
    variantes = {}
    for forme, n in _STATS['min'].items():
        nu = _sans_accents(forme)
        if nu != forme and n >= 3:
            variantes.setdefault(nu, []).append((n, forme))
    _STATS['variantes'] = {nu: sorted(v, reverse=True)[:2] for nu, v in variantes.items()}


def _nom_propre(mot, locales, apres_determinant):
    """Le mot (en minuscules) prend-il une capitale ? D'abord l'usage du texte, puis celui du corpus."""
    c, l = locales.get(mot, (0, 0))
    if c + l < 5:
        c, l = c + _STATS['maj'].get(mot, 0), l + _STATS['min'].get(mot, 0)
    if c < 2:
        return False
    if c >= 3 * max(l, 1) or (l == 0 and c >= 2):
        return True
    # usage partagé (« les Grecs » / « les philosophes grecs ») : capitale après un déterminant
    return apres_determinant and c >= l


def _accentuer(mot):
    """Rétablit l'accent absent d'une capitale quand le mot ne s'écrit, dans le corpus, qu'accentué."""
    formes = _STATS['variantes'].get(mot)
    if not formes or _sans_accents(mot) != mot:
        return mot
    n, forme = formes[0]
    if len(formes) > 1 and formes[1][0] * 10 >= n * 3:
        return mot                      # deux formes accentuées se disputent le mot : on ne tranche pas
    if _STATS['min'].get(mot, 0) * 8 <= n:
        return forme
    return mot


def convertir_titre(texte, locales, entier=True):
    """« DEUXIÈME PARTIE. REVUE DES PHÉNOMÈNES. » -> « Deuxième partie. Revue des phénomènes. »
    entier : tout le titre est en capitales (et non la seule étiquette qui l'ouvre)."""
    morceaux, pos = [], 0
    for m in _PROTEGE.finditer(texte):
        if m.start() > pos:
            morceaux.append((texte[pos:m.start()], False))
        morceaux.append((m.group(), True))
        pos = m.end()
    if pos < len(texte):
        morceaux.append((texte[pos:], False))

    sortie = []
    debut = True              # le prochain mot ouvre le titre ou une phrase
    precedent = ''            # mot précédent, en minuscules
    numero = _NUMERO.match(texte) if entier else None
    reprise = numero.end() if numero else -1     # où commence le titre après « Chapitre II »
    base = 0
    for segment, protege in morceaux:
        if protege:
            sortie.append(segment)
            base += len(segment)
            continue
        i = 0
        for m in _MOT.finditer(segment):
            entre = segment[i:m.start()]
            sortie.append(entre)
            if re.search(r'[.!?…][»"”)\]]?\s+[«"“(]?$|\s[—–]\s+$', entre):
                debut = True
            if reprise >= 0 and reprise <= base + m.start() <= reprise + 1:
                debut = True
            mot = m.group()
            suite = segment[m.end():m.end() + 2]
            bas = mot.lower()
            elision = suite[:1] in ('’', "'")
            colle_trait = entre.endswith('-') or suite[:1] == '-'
            if bas in EXCEPTIONS:
                neuf = EXCEPTIONS[bas]
            elif _ROMAIN_ORDINAL.match(mot):
                neuf = mot                  # « Ier », « IIe », « XIXe »
            elif len(mot) == 1 and mot.islower() and not debut:
                neuf = mot
            elif len(mot) == 1:
                if elision:
                    neuf = mot.upper() if debut else bas
                elif bas == 'y' and not debut:
                    neuf = 'y'
                elif bas in ('a', 'à') and not debut and (
                        precedent in _SUJETS or entre.endswith(('’', "'"))):
                    neuf = 'a'              # « il y a », « ce qu'il a »
                elif bas in ('a', 'à') and not debut and suite[:1] == ' ' and suite[1:2].isalpha():
                    neuf = 'à'              # « INTRODUCTION A LA PHILOSOPHIE »
                else:
                    neuf = mot.upper()      # lettre d'énumération, initiale, symbole
            elif _est_romain(mot.upper()) and not elision and not colle_trait and mot.upper() == mot:
                neuf = mot                  # chiffre romain
            else:
                bas = _accentuer(bas)
                apres_det = precedent in _DETERMINANTS or entre.endswith(('’', "'"))
                abrege = len(bas) <= 3 and suite[:1] == '.' and _suivi_nom_propre(segment, m.end(), locales)
                if debut or abrege or _nom_propre(bas, locales, apres_det):
                    neuf = bas[0].upper() + bas[1:]
                else:
                    neuf = bas
            sortie.append(neuf)
            precedent = bas
            debut = False
            i = m.end()
        sortie.append(segment[i:])
        base += len(segment)
    return ''.join(sortie)


def _suivi_nom_propre(segment, fin, locales):
    """« CH. RENOUVIER » : une abréviation suivie d'un nom propre garde sa capitale."""
    m = re.match(r'\.\s+([' + _LETTRES_MAJ + _LETTRES_MIN + r']+)', segment[fin:])
    if not m:
        return False
    suivant = m.group(1).lower()
    return len(suivant) >= 3 and _nom_propre(suivant, locales, False)


def titres_en_minuscules(markdown, page, files):
    if str(page.meta.get('capitales', '')).lower().startswith('conserv'):
        return markdown
    titres = _titres_capitales(markdown)
    if not titres:
        return markdown
    _preparer_stats(files)
    locales = _STATS['fichiers'].get(page.file.abs_src_path, {})
    lignes = markdown.split('\n')
    for i, m, fin in titres:
        texte = m.group(3)
        if fin is None:
            neuf = convertir_titre(texte, locales)
        else:
            neuf = convertir_titre(texte[:fin], locales, entier=False) + texte[fin:]
        lignes[i] = m.group(1) + m.group(2) + neuf + m.group(4)
    return '\n'.join(lignes)


# =====================================================================================
#  4. Index de recherche
# =====================================================================================
TRANSCRIPTIONS = ('oeuvres/', 'revues/', 'autres-auteurs/', 'archives/')
EXTRAIT = 220          # caractères gardés au début de chaque section d'une transcription
_INDEX = {'n': 0}


def _extrait(texte):
    brut = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', texte)).strip()
    if len(brut) > EXTRAIT:
        brut = re.sub(r'&\w*$', '', brut[:EXTRAIT].rsplit(' ', 1)[0]).rstrip(' ,;:') + '…'
    return f'<p>{brut}</p>' if brut else ''


def on_page_context(context, page, config, nav):
    """Après le passage du greffon de recherche sur la page : n'en garder que l'essentiel."""
    try:
        greffon = config.plugins.get('material/search')
        entrees = getattr(getattr(greffon, 'search_index', None), 'entries', None)
        if entrees is None:
            return context
        chemin = page.file.src_uri
        if chemin.startswith(TRANSCRIPTIONS) and not page.is_index:
            for e in entrees[_INDEX['n']:]:
                texte = e.get('text') or ''
                if len(texte) > EXTRAIT:
                    e['text'] = _extrait(texte)
        _INDEX['n'] = len(entrees)
    except Exception as e:
        log.warning('Renouvier Papers : index de recherche non allégé pour %s (%s)', page.file.src_path, e)
    return context


# =====================================================================================
#  6. Dernières retouches de la page : grand titre, espaces insécables
# =====================================================================================
# Ces deux retouches portent sur la page telle qu'elle est affichée ; les fichiers ne changent pas.
#
# a) Le grand titre. Un titre long (un article de revue, avec son sous-titre et son auteur) est
#    composé dans un corps plus petit, et sa précision finale entre parenthèses, « (Renouvier) »,
#    « (1864) », passe au second plan, comme dans le menu.
_H1 = re.compile(r'<h1\b([^>]*)>(.*?)</h1>', re.S)
_PRECISION_H1 = re.compile(r'^(.*\S)\s*(\([^()<>]{2,60}\))\s*$', re.S)
TITRE_MOYEN, TITRE_LONG = 60, 110      # au-delà de ces longueurs, le corps du titre diminue


def grand_titre(contenu):
    m = _H1.search(contenu)
    if not m:
        return contenu
    attributs, corps = m.group(1), m.group(2)
    texte = html.unescape(re.sub(r'<[^>]+>', '', corps)).strip()
    classe = 'rp-titre--long' if len(texte) > TITRE_LONG else 'rp-titre--moyen' if len(texte) > TITRE_MOYEN else ''
    precision = _PRECISION_H1.match(corps)
    if precision and _ORDINAL.match(texte):
        precision = None                              # « 1re année (1872) » : rien à hiérarchiser
    if not classe and not precision:
        return contenu
    if precision:
        corps = f'{precision.group(1)} <span class="rp-titre__precision">{precision.group(2)}</span>'
    if classe:
        if 'class="' in attributs:
            attributs = attributs.replace('class="', f'class="{classe} ', 1)
        else:
            attributs += f' class="{classe}"'
    return f'{contenu[:m.start()]}<h1{attributs}>{corps}</h1>{contenu[m.end():]}'


# b) Les espaces insécables. Les textes relus portent une espace insécable devant ; : ! ? » et
#    après « ; les autres (textes bruts, transcriptions plus anciennes) n'ont qu'une espace
#    ordinaire, si bien qu'une ligne peut commencer par un point-virgule ou finir sur un guillemet
#    ouvrant. On applique à toutes les transcriptions la convention des textes relus, ainsi qu'à
#    l'accueil et aux pages « À propos ». Les balises, le code et les formules ne sont jamais touchés.
INSECABLES = TRANSCRIPTIONS + ('index.md', 'a-propos/')      # là où la convention s'applique (pas la rubrique Recherche)
_INSECABLE = re.compile(
    r'<(pre|code|script|style|textarea|svg|math)\b[^>]*>.*?</\1\s*>'      # blocs laissés tels quels
    r'|<(span|div) class="arithmatex">.*?</\2>'                           # formules
    r'|<[^>]*>'                                                           # balises
    r'|(?<=\S) (?=[;:!?»])'                                               # espace devant ; : ! ? »
    r'|(?<=«) (?=\S)',                                                    # espace après «
    re.S)


def espaces_insecables(contenu):
    return _INSECABLE.sub(lambda m: ' ' if m.group(0) == ' ' else m.group(0), contenu)


def on_page_content(contenu, page, config, files):
    try:
        contenu = grand_titre(contenu)
    except Exception as e:
        log.warning('Renouvier Papers : grand titre laissé tel quel dans %s (%s)', page.file.src_path, e)
    try:
        if page.file.src_uri.startswith(INSECABLES):
            contenu = espaces_insecables(contenu)
    except Exception as e:
        log.warning('Renouvier Papers : espaces insécables non posées dans %s (%s)', page.file.src_path, e)
    return contenu


def on_pre_build(config):
    _INDEX['n'] = 0
    _STATS.update({'pret': False, 'maj': Counter(), 'min': Counter(), 'variantes': {}, 'fichiers': {}})
    _ETATS.clear()
    _ENTETES.clear()


# =====================================================================================
#  Branchement
# =====================================================================================
def on_page_markdown(markdown, page, config, files):
    try:
        if page.meta.get('sommaire'):
            markdown = inserer_sommaire(markdown, page)
    except Exception as e:
        log.warning('Renouvier Papers : sommaire non produit pour %s (%s)', page.file.src_path, e)
    try:
        markdown = titres_en_minuscules(markdown, page, files)
    except Exception as e:
        log.warning('Renouvier Papers : titres laissés en capitales dans %s (%s)', page.file.src_path, e)
    return markdown
