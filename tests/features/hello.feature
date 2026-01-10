@st-002
Feature: Page Hello World
  Scenario: Affichage de la page Hello World
    Given Je suis sur la page hello "/hello"
    Then Je vois le titre "Hello World"
    And Je vois le sous-titre "Bienvenue sur Marki"
    And Je vois le texte "Ceci est une page de démonstration"
    And Je vois un bouton "Retour à l'accueil"