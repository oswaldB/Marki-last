# Blueprint: dashboard/dashboard.py
**Fichier miroir** : `app/blueprints/dashboard/dashboard.py`
**Description** : Blueprint pour gérer le tableau de bord de l'application Marki.

---

## 🔧 Fonctions

### `dashboard()`
**Description** :
- Affiche le tableau de bord de l'application Marki.
- Vérifie que l'utilisateur est authentifié avant d'afficher la page.
- Utilise Flask-Login pour gérer l'authentification.
- Redirige l'utilisateur vers `/login` s'il n'est pas authentifié.

**Route** :
- **GET /dashboard** : Affiche le tableau de bord.

**Retour** :
- Affiche le template `dashboard.html` si l'utilisateur est authentifié.
- Redirige vers `/login` si l'utilisateur n'est pas authentifié.

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| db        | SQLite | Instance de la base de données SQLite pour accéder aux informations des utilisateurs | `sqlite3.connect('marki.db')` |

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

## 📋 Flux Principal
1. Vérifier l'état de connexion de l'utilisateur avec Flask-Login.
2. Si l'utilisateur n'est pas authentifié, rediriger vers `/login`.
3. Afficher le template `dashboard.html` avec les informations de l'utilisateur.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT DASHBOARD     |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - dashboard()                |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - db (SQLite)              |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Vérifier authentification |  |
|  |  2. Rediriger si non auth.    |  |
|  |  3. Afficher dashboard        |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```