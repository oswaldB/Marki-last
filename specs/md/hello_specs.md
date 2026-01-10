# Page de Salutation Personnalisée
**Version** : 1.1
**Statut** : Validé

---
## 1. Contexte
Permettre aux utilisateurs de recevoir une salutation personnalisée en fonction de leur prénom et de changer leur prénom si nécessaire.

## 2. Fonctionnalités
- Afficher un message de salutation générique si aucun prénom n'est fourni.
- Afficher un message de salutation personnalisé si un prénom est fourni.
- Permettre à l'utilisateur de changer son prénom via un lien "Pas le bon prénom ?".

## 3. Flux de Données
1. Utilisateur visite `/hello` ou `/hello/<prénom>`.
2. La page Flask récupère le prénom depuis l'URL.
3. La page affiche le message de salutation approprié.
4. Si l'utilisateur clique sur "Pas le bon prénom ?", un formulaire s'affiche pour changer le prénom.
5. L'utilisateur soumet le nouveau prénom et la page affiche la nouvelle salutation.

## 4. Règles Métier
- Si aucun prénom n'est fourni, afficher "Bonjour !".
- Si un prénom est fourni, afficher "Bonjour <prénom> !".
- Si l'utilisateur clique sur "Pas le bon prénom ?", afficher un formulaire pour changer le prénom.
- Si l'utilisateur soumet un nouveau prénom, afficher "Bonjour <nouveau prénom> !".

## 5. Exemples de Données
- URL : `/hello` → Message : "Bonjour !"
- URL : `/hello/toto` → Message : "Bonjour toto !"
- URL : `/hello/toto` → Clique sur "Pas le bon prénom ?" → Saisit "titi" → Message : "Bonjour titi !"

## 6. Liens
- [Scénarios Gherkin](specs/features/hello.feature)
