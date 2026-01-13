# tests/features/topbar.feature
# Lien vers la spec : ../../specs/specs/topbar.md

Fonctionnalité: Topbar
  En tant que utilisateur
  Je veux une topbar cohérente et professionnelle
  Afin d'afficher mes informations et mes notifications

  Contexte:
    Étant donné que je suis connecté en tant qu'utilisateur
    Et que je suis sur la page "/"

  Scénario: Affichage de la topbar (ST-007)
    Étant donné que je charge le layout principal
    Alors je devrais voir la topbar
    Et je devrais voir mes informations de l'utilisateur

  Scénario: Menu déroulant (ST-007)
    Étant donné que je suis sur la topbar
    Quand je clique sur mon avatar
    Alors le menu déroulant devrait s'ouvrir
    Et je devrais voir les actions disponibles

  Scénario: Notifications (ST-007)
    Étant donné que je reçois une nouvelle notification
    Quand je clique sur le badge de notification
    Alors la liste des notifications devrait s'afficher