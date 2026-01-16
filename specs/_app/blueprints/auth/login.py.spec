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
import datetime

# Initialisation
db = sqlite3.connect('marki.db')
cursor = db.cursor()

# Récupération d'un utilisateur
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
user_data = cursor.fetchone()

# Vérification des informations de connexion et de l'état actif
if user_data and user_data[2] == hashed_password and user_data[4]:
    # Connexion réussie
    
    # Création d'une session
    expires_at = datetime.datetime.now() + datetime.timedelta(days=1)
    cursor.execute("INSERT INTO sessions (user_id, token, expires_at) VALUES (?, ?, ?)", 
                   (user_data[0], 'unique_token', expires_at))
    db.commit()
    
    # Ajout d'un log
    cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)", 
                   (user_data[0], 'login', 'User logged in successfully'))
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
8. En cas de succès, rediriger l'utilisateur vers `/app/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.
9. En cas d'échec, afficher un message d'erreur.
10. Permettre la déconnexion des utilisateurs via la route `/logout`.
11. Supprimer la session de la table `sessions` lors de la déconnexion.
12. Ajouter un log dans la table `logs` pour l'action de déconnexion.
13. Afficher un drawer informatif pour le mot de passe oublié via la route `/forgot-password`.

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
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```