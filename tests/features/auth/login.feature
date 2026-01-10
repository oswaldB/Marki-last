# tests/features/auth/login.feature
Feature: Authentification des utilisateurs
  Scenario: Connexion avec des identifiants valides
    Given Je suis sur la page "/auth/login"
    When Je saisis l'identifiant "admin"
    And Je saisis le mot de passe "admin123"
    And Je clique sur le bouton "Se connecter"
    Then Je vois le message "Utilisateur connecté avec succès"
    And Je suis redirigé vers la page d'accueil