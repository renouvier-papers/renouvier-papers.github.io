"""Renouvier Papers : crochets de construction du site (MkDocs, clé « hooks » de mkdocs.yml).

Ce fichier fait quatre choses, toutes au moment où le site est construit. Aucun fichier de
docs/ n'est modifié.

1. SOMMAIRES. Une page dont l'en-tête YAML contient « sommaire: rubrique » reçoit la liste
   hiérarchisée de tout ce que la navigation de mkdocs.yml range dans sa rubrique ; avec
   « sommaire: portail », elle reçoit une carte par grande rubrique du site. La liste se place
   à l'endroit du commentaire <!-- sommaire --> (à défaut, à la fin de la page). Elle se met à
   jour toute seule quand la navigation change. Clés facultatives de l'en-tête :
     notices:   (rubrique) intitulé d'un groupe -> phrase affichée sous son titre ; l'ordre des
                notices fixe l'ordre des groupes, les groupes sans notice suivent dans l'ordre du menu
     cartes:    (portail) intitulé d'une rubrique -> « texte », « unite » (« volume, volumes ») et
                « groupes » (« auteur, auteurs ») de sa carte
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

En cas d'imprévu, chaque fonction laisse la page telle quelle et écrit un avertissement dans
le journal de construction : le site est construit quand même.
"""
import html
import logging
import re
import unicodedata
from collections import Counter

from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page
from mkdocs.utils import get_relative_url
from mkdocs.utils import meta as mk_meta

log = logging.getLogger('mkdocs.hooks.renouvier')

# Mots dont la forme est imposée dans les titres passés en minuscules (clé en minuscules).
EXCEPTIONS = {
    'mm': 'MM',
}

MARQUEUR = '<!-- sommaire -->'
_NAV = {'nav': None}
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


# =====================================================================================
#  1. Sommaires
# =====================================================================================
def on_nav(nav, config, files):
    """Garde la navigation sous la main et donne une adresse aux rubriques sans page propre."""
    _NAV['nav'] = nav
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
    return nav


def _ancrer(groupe, index, vues):
    for item in groupe.children:
        if isinstance(item, Section):
            item.rp_ancre = _unique(groupe.rp_ancre + '--' + ancre(_titre_et_date(item.title)[0]), vues)
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


def _ligne(item, page):
    """Une ligne du sommaire : un texte d'un seul tenant."""
    titre, date = _titre_et_date(item.title)
    e = etat(item)
    desc = ''
    if isinstance(item, Page):
        d = entete(item).get('description')
        if d:
            desc = f'<span class="rp-cat__desc">{html.escape(str(d))}</span>'
    corps = (f'<span class="rp-cat__corps"><span class="rp-cat__titre">{html.escape(titre)}</span>{desc}</span>'
             f'{_marque(e)}'
             + (f'<span class="rp-cat__date">{html.escape(date)}</span>' if date else ''))
    if e in ('vide', 'absent'):
        return f'<li class="rp-cat__item is-avenir"><span class="rp-cat__ligne">{corps}</span></li>'
    return f'<li class="rp-cat__item"><a class="rp-cat__ligne" href="{_lien(item, page)}">{corps}</a></li>'


def _ligne_multiple(section, page):
    """Une ligne du sommaire : un ouvrage en plusieurs tomes ou éditions."""
    titre, date = _titre_et_date(section.title)
    puces = []
    etats = [etat(p) for p in section.children]
    tous_bruts = bool(etats) and all(e == 'brut' for e in etats)
    for enfant, e in zip(section.children, etats):
        nom = html.escape(enfant.title or '')
        if e in ('vide', 'absent'):
            puces.append(f'<span class="rp-puce is-avenir" title="Texte à venir">{nom}</span>')
        else:
            brut = '' if tous_bruts or e != 'brut' else ' is-brut'
            bulle = ' title="Texte brut : pas encore relu"' if brut else ''
            puces.append(f'<a class="rp-puce{brut}" href="{_lien(enfant, page)}"{bulle}>{nom}</a>')
    ident = f' id="{section.rp_ancre}"' if getattr(section, 'rp_ancre', None) else ''
    return (f'<li class="rp-cat__item rp-cat__item--multiple"{ident}><div class="rp-cat__ligne">'
            f'<span class="rp-cat__corps"><span class="rp-cat__titre">{html.escape(titre)}</span>'
            f'<span class="rp-cat__tomes">{"".join(puces)}</span></span>'
            f'{_marque("brut") if tous_bruts else ""}'
            + (f'<span class="rp-cat__date">{html.escape(date)}</span>' if date else '')
            + '</div></li>')


def _liste(items, page, niveau):
    """Lignes d'un groupe ; un sous-groupe qui contient lui-même des groupes devient un intertitre."""
    sortie, lignes = [], []

    def vider():
        if lignes:
            sortie.append('<ul class="rp-cat" data-search-exclude>\n' + '\n'.join(lignes) + '\n</ul>')
            lignes.clear()

    for item in items:
        if isinstance(item, Section):
            if all(not isinstance(e, Section) for e in item.children):
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


LEGENDE = ('La mention « brut » signale un texte issu de la reconnaissance optique de caractères, '
           'qui n\'a pas encore été relu.')


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
        blocs.append(f'## {e.title} {{ #{ident} }}')
        notice = notices.get(e.title)
        if notice:
            blocs.append(f'{str(notice).strip()}\n{{ .rp-notice }}')
        blocs.append(_liste(e.children, page, 2))
    vider()
    groupes = [e for e in enfants if isinstance(e, Section)]
    if len(groupes) >= 8:
        # accès direct aux groupes, pour les écrans qui n'affichent pas la table des matières
        liens = ''.join(f'<a class="rp-puce" href="#{getattr(g, "rp_ancre", None) or ancre(g.title)}">'
                        f'{html.escape(g.title)}</a>' for g in groupes)
        blocs.insert(0, f'<nav class="rp-index" aria-label="Accès direct" data-search-exclude>{liens}</nav>')
    if any(etat(p) == 'brut' for p in _pages(rubrique)):
        blocs.insert(0, f'{LEGENDE}\n{{ .rp-legende }}')
    return '\n\n'.join(b for b in blocs if b)


def sommaire_portail(page):
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
        pages = [p for p in _pages(rubrique) if p is not index]
        n = sum(1 for p in pages if etat(p) in ('ok', 'brut'))
        if n:
            compte = _nombre(n, _paire(r.get('unite'), ('texte', 'textes')))
            groupes = _paire(r.get('groupes'), None)
            if groupes:
                g = sum(1 for e in rubrique.children if isinstance(e, Section))
                compte += ', ' + _nombre(g, groupes)
        else:
            compte = 'À venir'
        cartes.append(
            f'<a class="rp-carte" href="{_lien(index, page)}">'
            f'<span class="rp-carte__titre">{html.escape(rubrique.title)}</span>'
            f'<span class="rp-carte__texte">{html.escape(str(r.get("texte") or ""))}</span>'
            f'<span class="rp-carte__compte">{html.escape(compte)}</span>'
            '</a>')
    return '<div class="rp-portail" data-search-exclude>\n' + '\n'.join(cartes) + '\n</div>'


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
