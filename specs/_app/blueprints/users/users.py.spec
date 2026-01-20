# Blueprint: users.py
**Fichier miroir** : `app/blueprints/users.py`
**Description** : Blueprint pour gérer les utilisateurs, y compris la connexion, la déconnexion, la gestion des sessions, et les opérations CRUD sur les utilisateurs.

---

## 🔧 Fonctions

### `login()`
**Description** :
- Gère la connexion des utilisateurs via un formulaire de connexion.
- Utilise Flask-Login pour gérer les sessions utilisateur.
- Redirige l'utilisateur vers `/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.

**Route** :
- **GET /login** : Affiche le formulaire de connexion.
- **POST /login** : Traite le formulaire de connexion.

**Paramètres** :
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| id        | str    | Identifiant unique de l'utilisateur  | "user1"         |
| password  | str    | Mot de passe de l'utilisateur        | "password123"   |
| redirect  | str    | URL de redirection après connexion   | "/dashboard"|

**Retour** :
- En cas de succès, redirige vers la page spécifiée ou `/dashboard`.
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
- Utilise SQLite pour accéder aux informations des utilisateurs.

**Route** :
- **GET /api/users** : Récupère la liste des utilisateurs.

**Retour** :
- Liste des utilisateurs au format JSON.

### `create_user()`
**Description** :
- Crée un nouvel utilisateur dans la base de données.
- Utilise SQLite pour stocker les informations du nouvel utilisateur.

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
- Utilise SQLite pour mettre à jour les informations de l'utilisateur.

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
- Utilise SQLite pour mettre à jour les informations de l'utilisateur.

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
| db        | SQLite | Instance de la base de données SQLite pour stocker les informations des utilisateurs | `sqlite3.connect('marki.db')` |

## 📝 Spécifications SQLite

### Initialisation
- **Fonction** : `sqlite3.connect('marki.db')`
- **Description** : Initialise une connexion à la base de données SQLite.
- **Paramètres** :
  - `path` : Chemin vers le fichier de la base de données.
- **Retour** : Une instance de la base de données SQLite.

### Opérations de Base
- **`cursor.execute(sql)`** : Exécute une requête SQL.
- **`cursor.fetchone()`** : Récupère une seule ligne de résultat.
- **`cursor.fetchall()`** : Récupère toutes les lignes de résultat.
- **`db.commit()`** : Valide les changements dans la base de données.

### Exemple d'Utilisation
```python
import sqlite3

# Initialisation
db = sqlite3.connect('marki.db')
cursor = db.cursor()

# Création des tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        isAdmin BOOLEAN DEFAULT FALSE,
        isActive BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT NOT NULL,
        details TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

db.commit()

# Insertion d'un utilisateur
cursor.execute("INSERT INTO users (username, password, isAdmin, isActive) VALUES (?, ?, ?, ?)", 
               ('user1', 'hashed_password', False, True))
db.commit()
user_id = cursor.lastrowid

# Récupération d'un utilisateur
cursor.execute("SELECT * FROM users WHERE username = ?", ('user1',))
user_data = cursor.fetchone()

# Mise à jour d'un utilisateur
cursor.execute("UPDATE users SET password = ?, isAdmin = ?, isActive = ? WHERE id = ?", 
               ('new_hashed_password', True, True, user_id))
db.commit()

# Création d'une session
import datetime
expires_at = datetime.datetime.now() + datetime.timedelta(days=1)
cursor.execute("INSERT INTO sessions (user_id, token, expires_at) VALUES (?, ?, ?)", 
               (user_id, 'unique_token', expires_at))
db.commit()

# Récupération d'une session
cursor.execute("SELECT * FROM sessions WHERE token = ?", ('unique_token',))
session_data = cursor.fetchone()

# Ajout d'un log
cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)", 
               (user_id, 'login', 'User logged in successfully'))
db.commit()

# Suppression d'un utilisateur
cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
db.commit()

# Fermeture de la connexion
db.close()
```

## 📋 Flux Principal
1. Afficher le formulaire de connexion avec les champs pour l'identifiant et le mot de passe.
2. Valider les champs du formulaire.
3. Vérifier les informations de connexion dans la base de données SQLite (table `users`).
4. Vérifier que l'utilisateur est actif (`isActive = TRUE`).
5. Créer une session dans la table `sessions` avec un jeton unique.
6. Ajouter un log dans la table `logs` pour l'action de connexion.
7. Utiliser Flask-Login pour gérer la session utilisateur.
8. En cas de succès, rediriger l'utilisateur vers `/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.
9. En cas d'échec, afficher un message d'erreur.
10. Permettre la déconnexion des utilisateurs via la route `/logout`.
11. Supprimer la session de la table `sessions` lors de la déconnexion.
12. Ajouter un log dans la table `logs` pour l'action de déconnexion.
13. Afficher un drawer informatif pour le mot de passe oublié via la route `/forgot-password`.
14. Récupérer la liste des utilisateurs via la route `/api/users`.
15. Créer un nouvel utilisateur via la route `/api/users`.
16. Activer un utilisateur via la route `/api/users/<user_id>/activate`.
17. Modifier le mot de passe d'un utilisateur via la route `/api/users/<user_id>/modify`.

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
|  |  - db (SQLite)              |  |
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