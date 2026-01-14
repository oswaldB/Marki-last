# language: fr
@st-008
Fonctionnalité: ST-008 - Création du Premier Administrateur
  Contexte:
    Étant donné un utilisateur qui accède à la page superadmin (ST-008)
    Et la base de données est vide (ST-008)

  Scénario: Accès à la page superadmin avec le bon mot de passe
    Quand je saisis le mot de passe superadmin "Citron6-Mustang9" (ST-008)
    Et je clique sur le bouton "Créer le Premier Administrateur" (ST-008)
    Alors je devrais voir le formulaire de création (ST-008)

  Scénario: Création réussie du premier administrateur
    Étant donné que je suis sur la page superadmin (ST-008)
    Quand je saisis le nom d'utilisateur "admin" (ST-008)
    Et je saisis le mot de passe "MonMotDePasse123!" (ST-008)
    Et je confirme le mot de passe "MonMotDePasse123!" (ST-008)
    Et je clique sur le bouton "Créer le Premier Administrateur" (ST-008)
    Alors un nouvel utilisateur devrait être créé avec le rôle "admin" (ST-008)
    Et je devrais être redirigé vers la page de login (ST-008)

  Scénario: Échec de création avec mot de passe superadmin incorrect
    Quand je saisis le mot de passe superadmin "MauvaisMotDePasse" (ST-008)
    Et je clique sur le bouton "Créer le Premier Administrateur" (ST-008)
    Alors je devrais voir un message d'erreur "Mot de passe superadmin incorrect." (ST-008)

  Scénario: Échec de création avec mots de passe non correspondants
    Étant donné que je suis sur la page superadmin (ST-008)
    Quand je saisis le nom d'utilisateur "admin" (ST-008)
    Et je saisis le mot de passe "MotDePasse1" (ST-008)
    Et je confirme le mot de passe "MotDePasse2" (ST-008)
    Et je clique sur le bouton "Créer le Premier Administrateur" (ST-008)
    Alors je devrais voir un message d'erreur "Les mots de passe ne correspondent pas." (ST-008)