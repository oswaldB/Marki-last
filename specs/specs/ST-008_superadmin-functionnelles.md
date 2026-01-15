# ST-008 : Superadmin
**Date** : 2026-01-16
**Auteur** : Product Manager

---
## Contexte
Créer une page /superadmin qui permet de gérer les admins de l'application. Les admins sont des utilisateurs avec le champ `isAdmin` à `true`.

## Acteurs
- Superadmin
- Système

## Flux Principal
1. Le superadmin accède à la page /superadmin/entrance.
2. Le système demande un mot de passe.
3. Le superadmin entre le mot de passe `Citron6-Mustang9`.
4. Le système vérifie le mot de passe et redirige vers /superadmin.
5. Le superadmin peut créer, modifier et supprimer des admins.

## Règles Métier
- Le mot de passe pour accéder à la page /superadmin/entrance est `Citron6-Mustang9`.
- Seuls les utilisateurs avec `isAdmin` à `true` peuvent être considérés comme des admins.
- Les admins peuvent effectuer des actions spécifiques dans l'application.
- Les utilisateurs doivent se connecter avec un identifiant unique et non un email.
- Les pages superadmin utilisent le layout simple public (sans sidebar ni topbar).

## Interface Utilisateur
- Page /superadmin/entrance : Formulaire de connexion avec champ mot de passe (utilise simple-layout)
- Page /superadmin : Tableau des admins avec bouton de création (utilise simple-layout)
- Formulaire de création/modification d'admin avec champs : identifiant, mot de passe, nom

## Scénarios Gherkin
```gherkin
Feature: Superadmin
  Scenario: Accès à la page /superadmin
    Given Je suis sur la page /superadmin/entrance
    When Je saisis le mot de passe "Citron6-Mustang9"
    And Je clique sur "Valider"
    Then Je suis redirigé vers /superadmin
    And Je vois la liste des admins

  Scenario: Création d'un admin
    Given Je suis sur la page /superadmin
    When Je saisis les informations d'un nouvel admin avec un identifiant unique
    And Je clique sur "Créer"
    Then Le nouvel admin est ajouté à la liste
    And Je vois un message de confirmation

  Scenario: Modification d'un admin
    Given Je suis sur la page /superadmin
    When Je sélectionne un admin
    And Je modifie ses informations
    And Je clique sur "Modifier"
    Then Les informations de l'admin sont mises à jour
    And Je vois un message de confirmation

  Scenario: Suppression d'un admin
    Given Je suis sur la page /superadmin
    When Je sélectionne un admin
    And Je clique sur "Supprimer"
    Then L'admin est supprimé de la liste
    And Je vois un message de confirmation
```