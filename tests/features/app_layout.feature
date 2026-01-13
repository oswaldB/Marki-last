# tests/features/app_layout.feature
# Lien vers la spec : ../../specs/specs/app_layout.md

Fonctionnalité: Layout Principal de l'Application
  En tant que utilisateur
  Je veux un layout cohérent et professionnel
  Afin de naviguer facilement dans l'application

  Contexte:
    Étant donné que je suis connecté en tant qu'utilisateur
    Et que je suis sur la page "/"

  Scénario: Affichage du layout principal (ST-001)
    Étant donné que je charge le layout principal
    Alors je devrais voir la sidebar
    Et je devrais voir la topbar
    Et je devrais voir l'espace de contenu

  Scénario: Responsivité du layout (ST-001)
    Étant donné que je change la taille de l'écran
    Quand je suis sur un écran mobile
    Alors la sidebar devrait être masquée
    Mais la topbar devrait être visible

  Scénario: Mise à jour des informations utilisateur (ST-001)
    Étant donné que mes informations changent
    Quand je recharge la page
    Alors la topbar devrait afficher les nouvelles informations