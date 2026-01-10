# Page de Salutation Personnalisée
**Version** : 1.0
**Statut** : Validé

---
## 1. Contexte
Permettre aux utilisateurs de recevoir une salutation personnalisée en fonction de leur prénom.

## 2. Fonctionnalités
- Afficher un message de salutation générique si aucun prénom n'est fourni.
- Afficher un message de salutation personnalisé si un prénom est fourni.

## 3. Flux de Données
1. Utilisateur visite `/hello` ou `/hello/<prénom>`.
2. La page Flask récupère le prénom depuis l'URL.
3. La page affiche le message de salutation approprié.

## 4. Règles Métier
- Si aucun prénom n'est fourni, afficher "Bonjour !".
- Si un prénom est fourni, afficher "Bonjour <prénom> !".

## 5. Exemples de Données
- URL : `/hello` → Message : "Bonjour !"
- URL : `/hello/toto` → Message : "Bonjour toto !"

## 6. Liens
- [Scénarios Gherkin](specs/features/hello.feature)
