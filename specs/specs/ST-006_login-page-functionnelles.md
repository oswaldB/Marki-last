# ST-006 : Page de Connexion
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer une page de connexion pour permettre aux utilisateurs de s'authentifier et d'accéder aux parties protégées de l'application. La connexion se fait via un identifiant unique et non une adresse email. Utilisation de Flask-Login pour gérer les sessions et l'authentification.

## 📜 Règles Métier
- **Accessibilité** : Cette page doit être accessible sans authentification.
- **Formulaire de Connexion** : Doit inclure des champs pour l'identifiant et le mot de passe.
- **Validation** : Les champs doivent être validés avant l'envoi du formulaire.
- **Authentification** : Utilisation de Flask-Login pour gérer l'authentification et les sessions.
- **Redirection** : Après une connexion réussie, l'utilisateur doit être redirigé vers `/app/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.
- **Messages d'Erreur** : Afficher des messages d'erreur en cas d'échec de la connexion.
- **Mot de Passe Oublié** : Doit inclure un lien vers un drawer informatif pour le mot de passe oublié.
- **Inscription** : Doit inclure un lien vers un drawer informatif pour l'inscription.
- **Identifiant Unique** : La connexion se fait via un identifiant unique et non une adresse email.
- **Rôle Utilisateur** : Les utilisateurs peuvent avoir un rôle `isAdmin` qui détermine leurs permissions.

## 📝 Exigences Techniques
- **Formulaire** : Utilisation de formulaires HTML pour la saisie des informations de connexion.
- **Validation** : Utilisation de JavaScript (Alpine.js) pour la validation côté client.
- **Authentification** : Utilisation de Flask-Login pour l'authentification côté serveur et la gestion des sessions.
- **Redirection** : Utilisation de Flask pour rediriger l'utilisateur après une connexion réussie.
- **Messages d'Erreur** : Affichage des messages d'erreur en cas d'échec de la connexion.
- **Drawer d'Inscription** : Utilisation de Alpine.js pour afficher un drawer informatif pour l'inscription.
- **Lien Mot de Passe Oublié** : Lien vers une page de récupération de mot de passe.
- **API de Connexion** : Utilisation d'une route `/api/login` pour gérer la connexion via une requête POST.
- **Base de Données** : Utilisation de PickleDB pour stocker les informations des utilisateurs.
- **Structure des Utilisateurs** : Chaque utilisateur doit avoir un identifiant unique, un mot de passe haché, et un champ `isAdmin` pour déterminer les permissions.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] LOGIN PAGE              |
|                                     |
|  +-------------------------------+  |
|  |  🎨 Logo Marki                 |  |
|  +-------------------------------+  |
|  |  📧 Identifiant                |  |
|  |  ________________________     |  |
|  |  🔒 Mot de passe              |  |
|  |  ________________________     |  |
|  |  [🖱 Bouton] SE CONNECTER      |  |
|  |  [🔗 Lien] Mot de passe oublié |  |
|  |  [🔗 Lien] S'inscrire         |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

## 📋 Flux Principal
1. Afficher le formulaire de connexion avec les champs pour l'identifiant et le mot de passe.
2. Valider les champs du formulaire avec Alpine.js.
3. Soumettre le formulaire à l'API `/api/login` pour l'authentification.
4. Utiliser Flask-Login pour gérer la session utilisateur.
5. En cas de succès, rediriger l'utilisateur vers `/app/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.
6. En cas d'échec, afficher un message d'erreur.
7. Afficher un drawer informatif pour l'inscription lorsque l'utilisateur clique sur le lien "S'inscrire".
8. Afficher un drawer informatif pour le mot de passe oublié lorsque l'utilisateur clique sur le lien "Mot de passe oublié ?".

## 📊 Structure de la Base de Données PickleDB

### Utilisateurs
```json
{
  "user_counter": 1,
  "user:1": {
    "id": "user1",
    "password": "hashed_password",
    "isAdmin": false
  },
  "user:2": {
    "id": "admin1",
    "password": "hashed_password",
    "isAdmin": true
  }
}
```

### Explications
- **user_counter** : Compteur auto-incrémenté pour générer des identifiants uniques.
- **user:<id>** : Chaque utilisateur est stocké avec un identifiant unique.
- **id** : Identifiant unique de l'utilisateur.
- **password** : Mot de passe haché de l'utilisateur.
- **isAdmin** : Booléen indiquant si l'utilisateur est un administrateur.

## 🔧 API de Connexion

### Route
- **POST /api/login** : Route pour gérer la connexion des utilisateurs.

### Paramètres
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| id        | str    | Identifiant unique de l'utilisateur  | "user1"         |
| password  | str    | Mot de passe de l'utilisateur        | "password123"   |

### Réponse
- **Succès** :
  ```json
  {
    "status": "success",
    "message": "Connexion réussie",
    "redirect": "/app/dashboard"
  }
  ```
- **Échec** :
  ```json
  {
    "status": "error",
    "message": "Identifiant ou mot de passe incorrect"
  }
  ```

### Redirection
- **Par Défaut** : `/app/dashboard`
- **Paramètre `redirect`** : Si un paramètre `?redirect=/path` est présent dans l'URL, rediriger vers `/path` après une connexion réussie.

## 📌 Gestion des Sessions
- **Flask-Login** : Utilisé pour gérer les sessions utilisateur.
- **login_user** : Fonction pour connecter un utilisateur.
- **logout_user** : Fonction pour déconnecter un utilisateur.
- **current_user** : Objet pour accéder à l'utilisateur actuel.

## 📄 Drawer d'Inscription
```
+-------------------------------------+
|  🏗 [MARKI] DRAWER INSCRIPTION      |
|                                     |
|  +-------------------------------+  |
|  |  📄 Informations               |  |
|  |  Merci de contacter votre     |  |
|  |  administrateur principal.    |  |
|  |  Si vous êtes l'administrateur|  |
|  |  principal, veuillez envoyer  |  |
|  |  un email à :                |  |
|  |  contact@markidiags.com       |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

## 📄 Drawer Mot de Passe Oublié
```
+-------------------------------------+
|  🏗 [MARKI] DRAWER MOT DE PASSE     |
|  OUBLIÉ                            |
|                                     |
|  +-------------------------------+  |
|  |  📄 Informations               |  |
|  |  Merci de contacter votre     |  |
|  |  administrateur principal.    |  |
|  |  Si vous êtes l'administrateur|  |
|  |  principal, veuillez envoyer  |  |
|  |  un email à :                |  |
|  |  contact@markidiags.com       |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```