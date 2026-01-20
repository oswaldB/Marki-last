# Format des Fichiers de Blueprint

Ce document définit le format et les conventions pour les fichiers de spécifications des blueprints dans le dossier `specs/_app/blueprints/` du projet Marki.

---

## 📂 Structure des Dossiers

Les fichiers de spécifications des blueprints doivent être organisés selon la structure suivante :

```bash
specs/
└── _app/
    └── blueprints/
        ├── <nom_du_blueprint>/
        │   ├── <nom_du_blueprint>.spec  # Spécifications techniques du blueprint
        │   └── ...
        └── README.md                  # Description générale des blueprints
```

**Exemple** :
- Spécifications d'un blueprint : `specs/_app/blueprints/auth/auth.spec`

---

## 📄 Format du Fichier

### Nom du Fichier

Les fichiers de spécifications des blueprints doivent être nommés selon le format suivant :
- `<nom_du_blueprint>.spec`

**Exemple** :
- `auth.spec`

### Contenu du Fichier

Chaque fichier de spécifications d'un blueprint doit contenir les sections suivantes :

#### 1. **En-tête**
```markdown
# Blueprint: <Nom du Blueprint>
**Fichier miroir** : `app/blueprints/<nom_du_blueprint>/routes.py`
**Description** : <Description courte du blueprint.>
**Date de création** : <YYYY-MM-DD>
**Auteur** : <Nom de l'auteur>
```

**Exemple** :
```markdown
# Blueprint: Auth
**Fichier miroir** : `app/blueprints/auth/routes.py`
**Description** : Gestion de l'authentification des utilisateurs.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard
```

#### 2. **Routes**
Cette section doit lister les routes du blueprint.

```markdown
## 📍 Routes

| Route               | Méthode | Description                          | Fonction associée       |
|---------------------|---------|--------------------------------------|------------------------|
| `/login`            | POST    | Connexion de l'utilisateur           | `login_user`           |
| `/register`         | POST    | Inscription de l'utilisateur         | `register_user`        |
| `/logout`           | GET     | Déconnexion de l'utilisateur         | `logout_user`          |
```

**Exemple** :
```markdown
## 📍 Routes

| Route               | Méthode | Description                          | Fonction associée       |
|---------------------|---------|--------------------------------------|------------------------|
| `/login`            | POST    | Connexion de l'utilisateur           | `login_user`           |
| `/register`         | POST    | Inscription de l'utilisateur         | `register_user`        |
| `/logout`           | GET     | Déconnexion de l'utilisateur         | `logout_user`          |
```

#### 3. **Fonctions**
Cette section doit décrire les fonctions du blueprint.

```markdown
## 🔧 Fonctions

### `<Nom de la Fonction>`
**Description** :
<Description de la fonction.>

**Route** : `<Route associée>`

**Méthode** : `<Méthode HTTP>`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| <param1>  | <type> | <validation>                   | <exemple>        |
| <param2>  | <type> | <validation>                   | <exemple>        |

**Retour** :
<Description du retour.>

**Exemple** :
```json
{ "status": "success|error", "message": str }
```

**Code** :
```python
@bp.route('<Route>', methods=['<Méthode>'])
def <nom_de_la_fonction>():
    # Logique de la fonction
    pass
```
```

**Exemple** :
```markdown
## 🔧 Fonctions

### `login_user`
**Description** :
Authentifie un utilisateur et retourne un token.

**Route** : `/login`

**Méthode** : `POST`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Format valide et existe en BDD | test@example.com |
| password  | str    | Correspond au hash en BDD      | Secure123        |

**Retour** :
```json
{ "status": "success|error", "token": str, "message": str }
```

**Code** :
```python
@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    # Logique d'authentification
    pass
```

### `register_user`
**Description** :
Enregistre un nouvel utilisateur.

**Route** : `/register`

**Méthode** : `POST`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Format valide et unique        | test@example.com |
| password  | str    | 8+ caractères (1 maj, 1 chiffre)| Secure123        |
| name      | str    | 2+ caractères, lettres uniquement| Test User        |

**Retour** :
```json
{ "status": "success|error", "user_id": int, "message": str }
```

**Code** :
```python
@bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    # Logique d'inscription
    pass
```
```

#### 4. **Variables Globales**
Cette section doit lister les variables globales utilisées dans le blueprint.

```markdown
## 📝 Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| <variable1>       | <type> | <description>                        | <exemple>|
| <variable2>       | <type> | <description>                        | <exemple>|
```

**Exemple** :
```markdown
## 📝 Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| `user_counter`    | int    | Compteur auto-incrémenté (SQLite)    | 1       |
| `MIN_PASSWORD_LEN`| int    | Longueur minimale du mot de passe    | 8       |
```

#### 5. **Flux Principal**
Cette section doit décrire le flux principal du blueprint.

```markdown
## 📋 Flux Principal

1. <Étape 1>
2. <Étape 2>
3. <Étape 3>
```

**Exemple** :
```markdown
## 📋 Flux Principal

1. L'utilisateur soumet le formulaire de connexion.
2. Le serveur valide les informations d'identification.
3. Si valide, un token est généré et retourné.
4. Si invalide, une erreur est retournée.
```

---

## 📝 Bonnes Pratiques

1. **Clarté** : Utilisez des descriptions claires et concises.
2. **Consistance** : Maintenez une consistance dans les formats et les conventions.
3. **Exemples** : Fournissez des exemples pour illustrer les spécifications.
4. **Mises à Jour** : Documentez toute mise à jour ou modification.
5. **Validation** : Assurez-vous que les spécifications sont validées par l'équipe avant d'être fusionnées.

---

## 📌 Exemple Complet

### Fichier : `specs/_app/blueprints/auth/auth.spec`
```markdown
# Blueprint: Auth
**Fichier miroir** : `app/blueprints/auth/routes.py`
**Description** : Gestion de l'authentification des utilisateurs.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard

---

## 📍 Routes

| Route               | Méthode | Description                          | Fonction associée       |
|---------------------|---------|--------------------------------------|------------------------|
| `/login`            | POST    | Connexion de l'utilisateur           | `login_user`           |
| `/register`         | POST    | Inscription de l'utilisateur         | `register_user`        |
| `/logout`           | GET     | Déconnexion de l'utilisateur         | `logout_user`          |

---

## 🔧 Fonctions

### `login_user`
**Description** :
Authentifie un utilisateur et retourne un token.

**Route** : `/login`

**Méthode** : `POST`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Format valide et existe en BDD | test@example.com |
| password  | str    | Correspond au hash en BDD      | Secure123        |

**Retour** :
```json
{ "status": "success|error", "token": str, "message": str }
```

**Code** :
```python
@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    # Logique d'authentification
    pass
```

### `register_user`
**Description** :
Enregistre un nouvel utilisateur.

**Route** : `/register`

**Méthode** : `POST`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Format valide et unique        | test@example.com |
| password  | str    | 8+ caractères (1 maj, 1 chiffre)| Secure123        |
| name      | str    | 2+ caractères, lettres uniquement| Test User        |

**Retour** :
```json
{ "status": "success|error", "user_id": int, "message": str }
```

**Code** :
```python
@bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    # Logique d'inscription
    pass
```

---

## 📝 Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| `user_counter`    | int    | Compteur auto-incrémenté (SQLite)    | 1       |
| `MIN_PASSWORD_LEN`| int    | Longueur minimale du mot de passe    | 8       |

---

## 📋 Flux Principal

1. L'utilisateur soumet le formulaire de connexion.
2. Le serveur valide les informations d'identification.
3. Si valide, un token est généré et retourné.
4. Si invalide, une erreur est retournée.
```

---

## 📌 Notes Supplémentaires

- Les spécifications techniques doivent être synchronisées avec les fichiers de spécifications dans `specs/specs/`.
- Toute modification doit être validée par l'équipe avant d'être fusionnée.
