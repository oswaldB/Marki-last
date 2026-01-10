# tests/features/auth/reset_password.feature
Feature: Réinitialisation du mot de passe
  Scenario: Demande de réinitialisation du mot de passe
    Given Je suis sur la page "/auth/reset_password"
    When Je saisis l'email "admin@marki.com"
    And Je clique sur le bouton "Envoyer le lien"
    Then Je vois le message "Lien de réinitialisation envoyé"
    And Je suis redirigé vers la page de connexion