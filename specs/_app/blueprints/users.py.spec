# Blueprint: users.py
**Fichier miroir** : `app/blueprints/users.py`
**Description** : Blueprint pour gérer les utilisateurs, y compris la connexion, la déconnexion, la gestion des sessions, et les opérations CRUD sur les utilisateurs.

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

### `get_users()`
**Description** :
- Récupère la liste des utilisateurs depuis la base de données.
- Utilise PickleDB pour accéder aux informations des utilisateurs.

**Route** :
- **GET /api/users** : Récupère la liste des utilisateurs.

**Retour** :
- Liste des utilisateurs au format JSON.

### `create_user()`
**Description** :
- Crée un nouvel utilisateur dans la base de données.
- Utilise PickleDB pour stocker les informations du nouvel utilisateur.

**Route** :
- **POST /api/users** : Crée un nouvel utilisateur.

**Paramètres** :
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| id        | str    | Identifiant unique de l'utilisateur  | "user1"         |
| password  | str    | Mot de passe de l'utilisateur        | "password123"   |
| isAdmin   | bool   | Rôle de l'utilisateur                | true             |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `activate_user(user_id)`
**Description** :
- Active un utilisateur dans la base de données.
- Utilise PickleDB pour mettre à jour les informations de l'utilisateur.

**Route** :
- **POST /api/users/<user_id>/activate** : Active un utilisateur.

**Paramètres** :
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| user_id   | str    | Identifiant unique de l'utilisateur  | "user1"         |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `modify_user_password(user_id)`
**Description** :
- Modifie le mot de passe d'un utilisateur dans la base de données.
- Utilise PickleDB pour mettre à jour les informations de l'utilisateur.

**Route** :
- **POST /api/users/<user_id>/modify** : Modifie le mot de passe d'un utilisateur.

**Paramètres** :
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| user_id   | str    | Identifiant unique de l'utilisateur  | "user1"         |
| password  | str    | Nouveau mot de passe de l'utilisateur| "newpassword123"|

**Retour** :
- Message de succès ou d'erreur au format JSON.

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
9. Récupérer la liste des utilisateurs via la route `/api/users`.
10. Créer un nouvel utilisateur via la route `/api/users`.
11. Activer un utilisateur via la route `/api/users/<user_id>/activate`.
12. Modifier le mot de passe d'un utilisateur via la route `/api/users/<user_id>/modify`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT USERS         |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - login()                    |  |
|  |  - logout()                   |  |
|  |  - forgot_password()          |  |
|  |  - get_users()                |  |
|  |  - create_user()              |  |
|  |  - activate_user()            |  |
|  |  - modify_user_password()     |  |
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
|  |  9. Récupérer utilisateurs    |  |
|  |  10. Créer utilisateur        |  |
|  |  11. Activer utilisateur      |  |
|  |  12. Modifier mot de passe    |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```