# Base de Données: marki.db
**Fichier miroir** : `app/bdd/marki.db`
**Description** : Base de données SQLite unique pour le projet Marki, stockant les informations des utilisateurs, les sessions, les logs, les impayés, les listes, les séquences, et autres données nécessaires. Cette base de données est unique pour tout le projet et contient plusieurs tables.

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

### Table: impayes

```sql
CREATE TABLE impayes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference TEXT UNIQUE NOT NULL,
    montant REAL NOT NULL,
    date_echeance TEXT NOT NULL,
    statut TEXT NOT NULL,
    email_particulier TEXT,
    email_apporteur TEXT,
    jours_retard INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Explications
- **id** : Identifiant unique de l'impayé, auto-incrémenté.
- **reference** : Référence unique de l'impayé.
- **montant** : Montant de l'impayé.
- **date_echeance** : Date d'échéance de l'impayé.
- **statut** : Statut de l'impayé (par exemple, "impayé", "partiellement payé", "payé").
- **email_particulier** : Email du particulier (peut être NULL).
- **email_apporteur** : Email de l'apporteur (peut être NULL).
- **jours_retard** : Nombre de jours de retard.
- **created_at** : Date et heure de création de l'entrée.

### Table: listes_manuelles

```sql
CREATE TABLE listes_manuelles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Explications
- **id** : Identifiant unique de la liste manuelle, auto-incrémenté.
- **nom** : Nom de la liste manuelle.
- **created_at** : Date et heure de création de la liste.

### Table: liste_manuelle_impayes

```sql
CREATE TABLE liste_manuelle_impayes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liste_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    FOREIGN KEY (liste_id) REFERENCES listes_manuelles(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications
- **id** : Identifiant unique de l'association, auto-incrémenté.
- **liste_id** : ID de la liste manuelle.
- **impaye_id** : ID de l'impayé associé.

### Table: listes_automatiques

```sql
CREATE TABLE listes_automatiques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    criteres TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Explications
- **id** : Identifiant unique de la liste automatique, auto-incrémenté.
- **nom** : Nom de la liste automatique.
- **criteres** : Critères de filtrage pour la liste (stockés sous forme de JSON).
- **created_at** : Date et heure de création de la liste.

### Table: liste_automatique_impayes

```sql
CREATE TABLE liste_automatique_impayes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liste_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    FOREIGN KEY (liste_id) REFERENCES listes_automatiques(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications
- **id** : Identifiant unique de l'association, auto-incrémenté.
- **liste_id** : ID de la liste automatique.
- **impaye_id** : ID de l'impayé associé.

### Table: sequences

```sql
CREATE TABLE sequences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    templates TEXT NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Explications
- **id** : Identifiant unique de la séquence, auto-incrémenté.
- **nom** : Nom de la séquence.
- **templates** : Templates dynamiques de la séquence (stockés sous forme de JSON).
- **is_active** : Indique si la séquence est active.
- **created_at** : Date et heure de création de la séquence.

### Table: sequence_listes

```sql
CREATE TABLE sequence_listes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER NOT NULL,
    liste_id INTEGER NOT NULL,
    type_liste TEXT NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequences(id)
);
```

### Explications
- **id** : Identifiant unique de l'association, auto-incrémenté.
- **sequence_id** : ID de la séquence.
- **liste_id** : ID de la liste associée.
- **type_liste** : Type de liste (manuelle ou automatique).

### Table: relances_actions

```sql
CREATE TABLE relances_actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    template TEXT NOT NULL,
    date_envoi TEXT NOT NULL,
    statut TEXT NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequences(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications
- **id** : Identifiant unique de l'action, auto-incrémenté.
- **sequence_id** : ID de la séquence.
- **impaye_id** : ID de l'impayé.
- **template** : Template de l'email.
- **date_envoi** : Date d'envoi de l'email.
- **statut** : Statut de l'action (par exemple, "à envoyer", "envoyé", "erreur").

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
11. Insérer un impayé avec `INSERT INTO impayes (reference, montant, date_echeance, statut, email_particulier, email_apporteur, jours_retard) VALUES (?, ?, ?, ?, ?, ?, ?)`.
12. Récupérer les informations d'un impayé avec `SELECT * FROM impayes WHERE reference = ?`.
13. Mettre à jour les informations d'un impayé avec `UPDATE impayes SET statut = ?, email_particulier = ?, email_apporteur = ?, jours_retard = ? WHERE id = ?`.
14. Supprimer un impayé avec `DELETE FROM impayes WHERE id = ?`.
15. Créer une liste manuelle avec `INSERT INTO listes_manuelles (nom) VALUES (?)`.
16. Associer un impayé à une liste manuelle avec `INSERT INTO liste_manuelle_impayes (liste_id, impaye_id) VALUES (?, ?)`.
17. Créer une liste automatique avec `INSERT INTO listes_automatiques (nom, criteres) VALUES (?, ?)`.
18. Associer un impayé à une liste automatique avec `INSERT INTO liste_automatique_impayes (liste_id, impaye_id) VALUES (?, ?)`.
19. Créer une séquence avec `INSERT INTO sequences (nom, templates, is_active) VALUES (?, ?, ?)`.
20. Associer une liste à une séquence avec `INSERT INTO sequence_listes (sequence_id, liste_id, type_liste) VALUES (?, ?, ?)`.
21. Créer une action de relance avec `INSERT INTO relances_actions (sequence_id, impaye_id, template, date_envoi, statut) VALUES (?, ?, ?, ?, ?)`.

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

cursor.execute('''
    CREATE TABLE IF NOT EXISTS impayes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference TEXT UNIQUE NOT NULL,
        montant REAL NOT NULL,
        date_echeance TEXT NOT NULL,
        statut TEXT NOT NULL,
        email_particulier TEXT,
        email_apporteur TEXT,
        jours_retard INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS listes_manuelles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS liste_manuelle_impayes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        liste_id INTEGER NOT NULL,
        impaye_id INTEGER NOT NULL,
        FOREIGN KEY (liste_id) REFERENCES listes_manuelles(id),
        FOREIGN KEY (impaye_id) REFERENCES impayes(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS listes_automatiques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        criteres TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS liste_automatique_impayes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        liste_id INTEGER NOT NULL,
        impaye_id INTEGER NOT NULL,
        FOREIGN KEY (liste_id) REFERENCES listes_automatiques(id),
        FOREIGN KEY (impaye_id) REFERENCES impayes(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sequences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        templates TEXT NOT NULL,
        is_active BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sequence_listes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sequence_id INTEGER NOT NULL,
        liste_id INTEGER NOT NULL,
        type_liste TEXT NOT NULL,
        FOREIGN KEY (sequence_id) REFERENCES sequences(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS relances_actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sequence_id INTEGER NOT NULL,
        impaye_id INTEGER NOT NULL,
        template TEXT NOT NULL,
        date_envoi TEXT NOT NULL,
        statut TEXT NOT NULL,
        FOREIGN KEY (sequence_id) REFERENCES sequences(id),
        FOREIGN KEY (impaye_id) REFERENCES impayes(id)
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

# Insertion d'un impayé
cursor.execute("INSERT INTO impayes (reference, montant, date_echeance, statut, email_particulier, email_apporteur, jours_retard) VALUES (?, ?, ?, ?, ?, ?, ?)", 
               ('IMP001', 100.0, '2026-01-31', 'impayé', 'email1@example.com', 'email2@example.com', 10))
db.commit()
impaye_id = cursor.lastrowid

# Récupération d'un impayé
cursor.execute("SELECT * FROM impayes WHERE reference = ?", ('IMP001',))
impaye_data = cursor.fetchone()

# Mise à jour d'un impayé
cursor.execute("UPDATE impayes SET statut = ?, email_particulier = ?, email_apporteur = ?, jours_retard = ? WHERE id = ?", 
               ('payé', 'new_email1@example.com', 'new_email2@example.com', 5, impaye_id))
db.commit()

# Création d'une liste manuelle
cursor.execute("INSERT INTO listes_manuelles (nom) VALUES (?)", 
               ('Liste 1',))
db.commit()
liste_manuelle_id = cursor.lastrowid

# Association d'un impayé à une liste manuelle
cursor.execute("INSERT INTO liste_manuelle_impayes (liste_id, impaye_id) VALUES (?, ?)", 
               (liste_manuelle_id, impaye_id))
db.commit()

# Création d'une liste automatique
cursor.execute("INSERT INTO listes_automatiques (nom, criteres) VALUES (?, ?)", 
               ('Liste Auto 1', '{"statut": "impayé", "jours_retard": "> 30"}'))
db.commit()
liste_automatique_id = cursor.lastrowid

# Association d'un impayé à une liste automatique
cursor.execute("INSERT INTO liste_automatique_impayes (liste_id, impaye_id) VALUES (?, ?)", 
               (liste_automatique_id, impaye_id))
db.commit()

# Création d'une séquence
cursor.execute("INSERT INTO sequences (nom, templates, is_active) VALUES (?, ?, ?)", 
               ('Séquence 1', '[{"contenu": "Bonjour {{nom}}", "delai": 1}]', False))
db.commit()
sequence_id = cursor.lastrowid

# Association d'une liste à une séquence
cursor.execute("INSERT INTO sequence_listes (sequence_id, liste_id, type_liste) VALUES (?, ?, ?)", 
               (sequence_id, liste_manuelle_id, 'manuelle'))
db.commit()

# Création d'une action de relance
cursor.execute("INSERT INTO relances_actions (sequence_id, impaye_id, template, date_envoi, statut) VALUES (?, ?, ?, ?, ?)", 
               (sequence_id, impaye_id, 'Bonjour {{nom}}', '2026-01-18', 'à envoyer'))
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
|  |  - Table: impayes             |  |
|  |    - id                       |  |
|  |    - reference                |  |
|  |    - montant                  |  |
|  |    - date_echeance            |  |
|  |    - statut                   |  |
|  |    - email_particulier        |  |
|  |    - email_apporteur          |  |
|  |    - jours_retard             |  |
|  |    - created_at               |  |
|  |  - Table: listes_manuelles   |  |
|  |    - id                       |  |
|  |    - nom                      |  |
|  |    - created_at               |  |
|  |  - Table: liste_manuelle_impayes |
|  |    - id                       |  |
|  |    - liste_id                 |  |
|  |    - impaye_id                |  |
|  |  - Table: listes_automatiques |  |
|  |    - id                       |  |
|  |    - nom                      |  |
|  |    - criteres                 |  |
|  |    - created_at               |  |
|  |  - Table: liste_automatique_impayes |
|  |    - id                       |  |
|  |    - liste_id                 |  |
|  |    - impaye_id                |  |
|  |  - Table: sequences           |  |
|  |    - id                       |  |
|  |    - nom                      |  |
|  |    - templates                |  |
|  |    - is_active                |  |
|  |    - created_at               |  |
|  |  - Table: sequence_listes     |  |
|  |    - id                       |  |
|  |    - sequence_id              |  |
|  |    - liste_id                 |  |
|  |    - type_liste               |  |
|  |  - Table: relances_actions    |  |
|  |    - id                       |  |
|  |    - sequence_id              |  |
|  |    - impaye_id                |  |
|  |    - template                 |  |
|  |    - date_envoi               |  |
|  |    - statut                   |  |
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
|  |  11. Insérer impayé           |  |
|  |  12. Récupérer impayé         |  |
|  |  13. Mettre à jour impayé     |  |
|  |  14. Supprimer impayé         |  |
|  |  15. Créer liste manuelle    |  |
|  |  16. Associer impayé          |  |
|  |  17. Créer liste automatique  |  |
|  |  18. Associer impayé          |  |
|  |  19. Créer séquence           |  |
|  |  20. Associer liste           |  |
|  |  21. Créer action de relance  |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```