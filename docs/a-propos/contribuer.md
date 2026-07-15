---
title: Contribuer
nav_order: 9
---

# Contribuer au projet

Merci de votre intérêt. Ce document décrit les conventions à suivre pour produire des transcriptions cohérentes et utilisables.

## Comment contribuer

1. **Signaler une erreur** : ouvrez une *issue* sur le [dépôt GitHub](https://github.com/renouvier-papers/renouvier-papers.github.io) en indiquant le fichier, le numéro de page `[p. XX]` et la correction proposée.
2. **Corriger une transcription** : soumettez une *pull request* avec vos corrections. Indiquez dans le message de commit la page et la nature de la correction.
3. **Transcrire un nouveau texte** : ouvrez d'abord une *issue* pour signaler que vous commencez le travail, afin d'éviter les doublons. Suivez les conventions ci-dessous.

## Conventions de transcription

### Pagination

Les numéros de pages sont insérés dans le texte entre crochets, au début du passage correspondant à la nouvelle page :

```
... fin de la page précédente. [p. 42] Début de la nouvelle page...
```

- Pages en chiffres romains pour les préfaces : `[p. V]`, `[p. XII]`
- Pages en chiffres arabes pour le corps du texte : `[p. 1]`, `[p. 427]`

### Hiérarchie des titres

```markdown
# Titre de partie ou section majeure
## Titre de chapitre
### Titre de sous-section
#### Titre de sous-sous-section
```

On n'utilise pas plus de quatre niveaux.

### Mise en forme

- **Italiques** : restituer les italiques de l'original avec `*italique*`.
- **Petites capitales** : transcrire en texte normal.
- **Guillemets** : conserver les guillemets français « » de l'original.
- **Tirets** : conserver les tirets longs (—) de l'original.

### Orthographe et ponctuation

- **Conserver l'orthographe d'époque** : « très-grand », « long-temps », etc.
- **Conserver la ponctuation d'origine**.
- **Ne pas moderniser** : le but est une transcription fidèle.

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

Supprimer systématiquement « Digitized by Google », les en-têtes et pieds de page répétés, les numéros de pages imprimés.

## Qualité attendue

Avant de soumettre une transcription, assurez-vous que :

- Toutes les pages sont présentes et numérotées
- Les titres de chapitres sont correctement balisés
- Les italiques sont restitués
- Les artefacts de numérisation sont supprimés
- Une relecture complète a été faite
