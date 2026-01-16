# Base de Données: marki.db
**Fichier miroir** : `app/bdd/marki.db`
**Description** : Base de données SQLite unique pour le projet Marki, stockant les informations des utilisateurs, les sessions, les logs, et autres données nécessaires. Cette base de données est unique pour tout le projet et contient plusieurs tables.

---

## 🔧 Structure de la Base de Données

### Table: users

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    isAdmin BOOLEAN DEFAULT FALSE,
    isActive BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Explications
- **id** : Identifiant unique de l'utilisateur, auto-incrémenté.
- **username** : Nom d'utilisateur unique, utilisé pour la connexion.
- **password** : Mot de passe haché de l'utilisateur.
- **isAdmin** : Booléen indiquant si l'utilisateur est un administrateur.
- **isActive** : Booléen indiquant si l'utilisateur est actif.
- **created_at** : Date et heure de création de l'utilisateur.

### Table: sessions

```sql
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    token TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Explications
- **id** : Identifiant unique de la session, auto-incrémenté.
- **user_id** : Identifiant de l'utilisateur associé à la session.
- **token** : Jeton de session unique.
- **created_at** : Date et heure de création de la session.
- **expires_at** : Date et heure d'expiration de la session.

### Table: logs

```sql
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT NOT NULL,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Explications
- **id** : Identifiant unique du log, auto-incrémenté.
- **user_id** : Identifiant de l'utilisateur associé au log (peut être NULL pour les actions système).
- **action** : Action effectuée (par exemple, "login", "logout", "create_user", etc.).
- **details** : Détails supplémentaires sur l'action.
- **created_at** : Date et heure de création du log.

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| db        | SQLite | Instance de la base de données SQLite pour stocker les informations du projet | `sqlite3.connect('marki.db')` |

## 📋 Flux Principal
1. Initialiser la base de données SQLite avec `sqlite3.connect('marki.db')`.
2. Créer les tables si elles n'existent pas.
3. Insérer un nouvel utilisateur avec `INSERT INTO users (username, password, isAdmin, isActive) VALUES (?, ?, ?, ?)`.
4. Récupérer les informations d'un utilisateur avec `SELECT * FROM users WHERE username = ?`.
5. Mettre à jour les informations d'un utilisateur avec `UPDATE users SET password = ?, isAdmin = ?, isActive = ? WHERE id = ?`.
6. Supprimer un utilisateur avec `DELETE FROM users WHERE id = ?`.
7. Créer une session avec `INSERT INTO sessions (user_id, token, expires_at) VALUES (?, ?, ?)`.
8. Récupérer une session avec `SELECT * FROM sessions WHERE token = ?`.
9. Supprimer une session avec `DELETE FROM sessions WHERE token = ?`.
10. Ajouter un log avec `INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)`.

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

# Fermeture de la connexion
db.close()
```

## 🎨 Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] BDD MARKI.DB             |
|                                     |
|  +-------------------------------+  |
|  |  📊 Structure                  |  |
|  |  - Table: users               |  |
|  |    - id                       |  |
|  |    - username                 |  |
|  |    - password                 |  |
|  |    - isAdmin                  |  |
|  |    - isActive                 |  |
|  |    - created_at               |  |
|  |  - Table: sessions            |  |
|  |    - id                       |  |
|  |    - user_id                  |  |
|  |    - token                    |  |
|  |    - created_at               |  |
|  |    - expires_at               |  |
|  |  - Table: logs                |  |
|  |    - id                       |  |
|  |    - user_id                  |  |
|  |    - action                   |  |
|  |    - details                  |  |
|  |    - created_at               |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Initialiser BDD           |  |
|  |  2. Créer tables              |  |
|  |  3. Insérer utilisateur       |  |
|  |  4. Récupérer utilisateur     |  |
|  |  5. Mettre à jour utilisateur |  |
|  |  6. Supprimer utilisateur     |  |
|  |  7. Créer session             |  |
|  |  8. Récupérer session         |  |
|  |  9. Supprimer session         |  |
|  |  10. Ajouter log              |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```