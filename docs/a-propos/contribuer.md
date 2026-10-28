---
title: "Contribuer"
---

# Contribuer au projet

Les contributions sont les bienvenues. Ce document fixe les conventions qui garantissent des transcriptions cohérentes et exploitables.

## Comment contribuer

1. **Signaler une erreur** : ouvrir une *issue* sur le [dépôt GitHub](https://github.com/renouvier-papers/renouvier-papers.github.io) en indiquant le fichier, le numéro de page `[p. XX]` et la correction proposée.
2. **Corriger une transcription** : soumettre une *pull request* contenant les corrections, en précisant dans le message de commit la page concernée et la nature de la correction.
3. **Transcrire un nouveau texte** : ouvrir d'abord une *issue* annonçant le travail, afin d'éviter les doublons, puis suivre les conventions ci-dessous.

## Conventions de transcription

### Pagination

Les numéros de page s'insèrent dans le texte entre crochets, au début du passage qui ouvre chaque nouvelle page :

```
... fin de la page précédente. [p. 42] Début de la nouvelle page...
```

- Chiffres romains pour les préfaces : `[p. V]`, `[p. XII]`
- Chiffres arabes pour le corps du texte : `[p. 1]`, `[p. 427]`

### Hiérarchie des titres

```markdown
# Titre de partie ou section majeure
## Titre de chapitre
### Titre de sous-section
#### Titre de sous-sous-section
```

La hiérarchie ne dépasse pas quatre niveaux.

### Mise en forme

- **Italiques** : restituer les italiques de l'original avec `*italique*`.
- **Petites capitales** : transcrire en texte courant.
- **Guillemets** : conserver les guillemets français « » de l'original.
- **Tirets** : conserver les tirets longs (—) de l'original.

### Orthographe et ponctuation

- **Conserver l'orthographe d'époque** : « très-grand », « long-temps », etc.
- **Conserver la ponctuation d'origine**.
- **Ne pas moderniser** : la transcription vise la fidélité.

### Notes de bas de page

```markdown
Ce passage est important[^1].

[^1]: Note de Renouvier dans l'original.
```

### Passages incertains

- Mot douteux : `mot[?]`
- Mot illisible : `[illisible]`
- Passage manquant : `[...]`

### Artefacts de numérisation

Supprimer systématiquement la mention « Digitized by Google », les en-têtes et pieds de page répétés ainsi que les numéros de page imprimés.

## Qualité attendue

Avant de soumettre une transcription, vérifier que :

- toutes les pages sont présentes et numérotées ;
- les titres de chapitres sont correctement balisés ;
- les italiques sont restitués ;
- les artefacts de numérisation sont supprimés ;
- une relecture complète a été faite.
