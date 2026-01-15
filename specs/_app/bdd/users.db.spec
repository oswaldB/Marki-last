# Base de Données: users.db
**Fichier miroir** : `app/bdd/users.db`
**Description** : Base de données PickleDB pour stocker les informations des utilisateurs, y compris les identifiants, les mots de passe hachés, et les rôles.

---

## 🔧 Structure de la Base de Données

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

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| user_counter | int | Compteur auto-incrémenté pour générer des identifiants uniques | 1 |

## 📋 Flux Principal
1. Initialiser la base de données PickleDB avec `pickledb.load('users.db', True)`.
2. Utiliser `db.incr('user_counter')` pour générer un nouvel identifiant unique.
3. Stocker les informations de l'utilisateur avec `db.set(f'user:{user_id}', user_data)`.
4. Récupérer les informations de l'utilisateur avec `db.get(f'user:{user_id}')`.
5. Mettre à jour les informations de l'utilisateur avec `db.set(f'user:{user_id}', updated_user_data)`.
6. Supprimer un utilisateur avec `db.rem(f'user:{user_id}')`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BDD USERS.DB            |
|                                     |
|  +-------------------------------+  |
|  |  📊 Structure                  |  |
|  |  - user_counter               |  |
|  |  - user:<id>                  |  |
|  |    - id                       |  |
|  |    - password                 |  |
|  |    - isAdmin                  |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Initialiser BDD           |  |
|  |  2. Générer identifiant       |  |
|  |  3. Stocker utilisateur       |  |
|  |  4. Récupérer utilisateur     |  |
|  |  5. Mettre à jour utilisateur |  |
|  |  6. Supprimer utilisateur     |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```