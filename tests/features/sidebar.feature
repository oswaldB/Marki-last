# tests/features/sidebar.feature
# Lien vers la spec : ../../specs/specs/sidebar.md

Fonctionnalité: Sidebar
  En tant que utilisateur
  Je veux une sidebar cohérente et professionnelle
  Afin de naviguer facilement dans l'application

  Contexte:
    Étant donné que je suis connecté en tant qu'utilisateur
    Et que je suis sur la page "/"

  Scénario: Affichage de la sidebar (ST-006)
    Étant donné que je charge le layout principal
    Alors je devrais voir la sidebar
    Et je devrais voir les liens de navigation

  Scénario: Toggle de la sidebar (ST-006)
    Étant donné que je suis sur un écran mobile
    Quand je clique sur le bouton de toggle
    Alors la sidebar devrait s'ouvrir ou se fermer

  Scénario: Mise à jour des liens de navigation (ST-006)
    Étant donné que mes permissions changent
    Quand je recharge la page
    Alors les liens de navigation devraient être mis à jour