# Blueprint: auth/login.py
**Fichier miroir** : `app/blueprints/auth/login.py`
**Description** : Blueprint pour gérer l'authentification des utilisateurs, y compris la connexion, la déconnexion, et la gestion des sessions.

---

## 🔧 Fonctions

### `login()`
**Description** :
- Gère la connexion des utilisateurs via un formulaire de connexion.
- Utilise Flask-Login pour gérer les sessions utilisateur.
- Redirige l'utilisateur vers `/app/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.

**Route** :
- **GET /login** : Affiche le formulaire de connexion.
- **POST /login** : Traite le formulaire de connexion.

**Paramètres** :
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| id        | str    | Identifiant unique de l'utilisateur  | "user1"         |
| password  | str    | Mot de passe de l'utilisateur        | "password123"   |
| redirect  | str    | URL de redirection après connexion   | "/app/dashboard"|

**Retour** :
- En cas de succès, redirige vers la page spécifiée ou `/app/dashboard`.
- En cas d'échec, affiche un message d'erreur.

### `logout()`
**Description** :
- Gère la déconnexion des utilisateurs.
- Utilise Flask-Login pour terminer la session utilisateur.
- Redirige l'utilisateur vers la page de connexion.

**Route** :
- **GET /logout** : Déconnecte l'utilisateur et redirige vers la page de connexion.

**Retour** :
- Redirige vers la page de connexion.

### `forgot_password()`
**Description** :
- Affiche un drawer informatif pour le mot de passe oublié.
- Informe l'utilisateur de contacter l'administrateur principal ou d'envoyer un email à `contact@markidiags.com`.

**Route** :
- **GET /forgot-password** : Affiche le drawer informatif pour le mot de passe oublié.

**Retour** :
- Affiche le drawer informatif pour le mot de passe oublié.

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| db        | PickleDB | Instance de la base de données PickleDB pour stocker les informations des utilisateurs | `pickledb.load('users.db', True)` |

## 📋 Flux Principal
1. Afficher le formulaire de connexion avec les champs pour l'identifiant et le mot de passe.
2. Valider les champs du formulaire.
3. Vérifier les informations de connexion dans la base de données PickleDB.
4. Utiliser Flask-Login pour gérer la session utilisateur.
5. En cas de succès, rediriger l'utilisateur vers `/app/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.
6. En cas d'échec, afficher un message d'erreur.
7. Permettre la déconnexion des utilisateurs via la route `/logout`.
8. Afficher un drawer informatif pour le mot de passe oublié via la route `/forgot-password`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT AUTH/LOGIN    |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - login()                    |  |
|  |  - logout()                   |  |
|  |  - forgot_password()          |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - db (PickleDB)              |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Afficher formulaire       |  |
|  |  2. Valider champs            |  |
|  |  3. Vérifier informations     |  |
|  |  4. Gérer session             |  |
|  |  5. Rediriger utilisateur     |  |
|  |  6. Afficher erreur           |  |
|  |  7. Déconnecter utilisateur   |  |
|  |  8. Afficher drawer mot de    |  |
|  |     passe oublié              |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```