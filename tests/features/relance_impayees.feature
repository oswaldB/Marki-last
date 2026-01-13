# tests/features/relance_impayees.feature
# Lien vers la spec : ../../specs/specs/relance_impayees.md

Fonctionnalité: Relance des Factures Impayées
  En tant que utilisateur
  Je veux gérer les relances des factures impayées
  Afin de récupérer les paiements en retard

  Contexte:
    Étant donné que je suis connecté en tant qu'utilisateur
    Et que je suis sur la page "/relances/dashboard"

  Scénario: Création d'une campagne de relance (ST-005)
    Étant donné que je crée une campagne de relance
    Quand je définis les critères de sélection
    Et que je définis la séquence d'emails
    Alors la campagne devrait être créée avec succès

  Scénario: Envoi des relances (ST-005)
    Étant donné que j'ai une campagne active
    Quand le délai de relance est atteint
    Alors les emails de relance devraient être envoyés
    Et les statuts des factures devraient être mis à jour

  Scénario: Gestion des erreurs d'envoi (ST-005)
    Étant donné que j'ai une campagne active
    Quand un email ne peut pas être envoyé
    Alors je devrais recevoir une notification d'erreur