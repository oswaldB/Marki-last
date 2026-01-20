# Blueprint: auth/routes.py
**Fichier miroir** : `app/blueprints/auth/routes.py`
**Base de données** : SQLite (`marki.db`)

---

## 🔧 Fonctions

### `get_db()`
**Description** :
- Initialise et retourne une connexion à la base de données SQLite.
- Configure `row_factory` pour retourner les résultats sous forme de dictionnaires.

**Retour** :
- `db` : Objet de connexion à la base de données SQLite.

---

### `login()`
**Description** :
- Gère la connexion des utilisateurs via un formulaire de connexion.
- Valide les champs `id` et `password`.
- Vérifie les informations de connexion dans la base de données.
- Utilise Flask-Login pour gérer la session utilisateur.
- Redirige l'utilisateur vers `/app/dashboard` ou vers une URL spécifiée via le paramètre `redirect`.

**Paramètres** :
- `id` (str) : Identifiant unique de l'utilisateur.
- `password` (str) : Mot de passe de l'utilisateur.
- `redirect_url` (str, optionnel) : URL de redirection après connexion réussie. Par défaut : `/app/dashboard`.

**Logique** :
1. Valider que `id` et `password` ne sont pas vides.
2. Récupérer les informations de l'utilisateur depuis la base de données.
3. Vérifier que l'utilisateur est actif (`isActive = True`).
4. Hacher le mot de passe et comparer avec le mot de passe stocké.
5. Créer une session utilisateur avec Flask-Login.
6. Ajouter un log de connexion dans la base de données.
7. Rediriger l'utilisateur vers `redirect_url`.

**Retour** :
- Redirection vers `redirect_url` en cas de succès.
- Message d'erreur en cas d'échec.

---

### `logout()`
**Description** :
- Gère la déconnexion des utilisateurs.
- Supprime la session utilisateur.
- Ajoute un log de déconnexion dans la base de données.

**Logique** :
1. Supprimer la session utilisateur avec `session.pop('user_id', None)`.
2. Ajouter un log de déconnexion dans la base de données.
3. Rediriger l'utilisateur vers la page de connexion.

**Retour** :
- Redirection vers la page de connexion (`/login`).

---

### `forgot_password()`
**Description** :
- Affiche un drawer informatif pour le mot de passe oublié.
- Le drawer contient des instructions pour contacter l'administrateur.

**Paramètres** :
- Aucun.

**Retour** :
- Rend le template `login.html` avec le paramètre `forgot_password=True`.

---

## 📋 Variables Globales

| Nom               | Type   | Description                          | Exemple          |
|-------------------|--------|--------------------------------------|------------------|
| `current_user`    | objet  | Utilisateur actuel (Flask-Login)     | `User(id=1)`     |

---

## 📝 Flux Principal

### Connexion
1. L'utilisateur accède à la page `/login`.
2. Le formulaire de connexion est affiché.
3. L'utilisateur saisit son `id` et son `password`.
4. Le formulaire est soumis à la route `/login`.
5. La fonction `login()` valide les champs.
6. Si les champs sont valides, la fonction vérifie les informations de connexion dans la base de données.
7. Si les informations sont correctes, l'utilisateur est connecté et redirigé vers `redirect_url`.
8. Si les informations sont incorrectes, un message d'erreur est affiché.

### Déconnexion
1. L'utilisateur clique sur le lien de déconnexion.
2. La fonction `logout()` est appelée.
3. La session utilisateur est supprimée.
4. Un log de déconnexion est ajouté dans la base de données.
5. L'utilisateur est redirigé vers la page de connexion.

### Mot de Passe Oublié
1. L'utilisateur clique sur le lien "Mot de passe oublié ?".
2. La fonction `forgot_password()` est appelée.
3. Le template `login.html` est rendu avec le paramètre `forgot_password=True`.
4. Un drawer informatif est affiché avec des instructions pour contacter l'administrateur.

---

## 📊 Structure de la Base de Données

### Utilisateurs
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

### Sessions
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

### Logs (PickleDB)
Les logs des utilisateurs seront stockés dans une base de données PickleDB séparée.
- **Fichier** : `logs.db`
- **Structure** :
  ```python
  {
      "user_<user_id>": [
          {
              "action": str,
              "details": str,
              "created_at": str
          }
      ]
  }
  ```

---

## 🔧 API de Connexion

### Route
- **POST /login** : Route pour gérer la connexion des utilisateurs.

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

---

## 📌 Gestion des Sessions

### Flask-Login
- **login_user** : Fonction pour connecter un utilisateur.
- **logout_user** : Fonction pour déconnecter un utilisateur.
- **current_user** : Objet pour accéder à l'utilisateur actuel.

### Exemple d'Utilisation
```python
from flask_login import login_user, logout_user, current_user

# Connexion d'un utilisateur
login_user(user)

# Déconnexion d'un utilisateur
logout_user()

# Accès à l'utilisateur actuel
if current_user.is_authenticated:
    print(f"Utilisateur connecté : {current_user.id}")
```

---

## 📄 Drawer d'Inscription

### Description
- Affiche un drawer informatif pour l'inscription.
- Contient des instructions pour contacter l'administrateur.

### Contenu
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

---

## 📄 Drawer Mot de Passe Oublié

### Description
- Affiche un drawer informatif pour le mot de passe oublié.
- Contient des instructions pour contacter l'administrateur.

### Contenu
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

---

## 📝 Notes Supplémentaires

### Validation des Champs
- Les champs `id` et `password` doivent être validés avant l'envoi du formulaire.
- Utilisation de Alpine.js pour la validation côté client.

### Hachage du Mot de Passe
- Le mot de passe doit être haché avant d'être stocké dans la base de données.
- Utilisation de `hashlib.sha256` pour le hachage.

### Redirection
- La redirection après connexion doit être configurable via le paramètre `redirect`.
- Par défaut, la redirection se fait vers `/app/dashboard`.

### Messages d'Erreur
- Les messages d'erreur doivent être affichés en cas d'échec de la connexion.
- Utilisation de `flash` pour afficher les messages d'erreur.

### Logs
- Les logs de connexion et de déconnexion doivent être ajoutés dans la base de données.
- Utilisation de la table `logs` pour stocker les logs.

---

## 📋 Exemple de Code

### Connexion
```python
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        redirect_url = request.args.get('redirect', '/app/dashboard')
        
        # Validation des champs
        if not id or not password:
            flash('Identifiant et mot de passe sont requis.', 'error')
            return redirect(url_for('auth.login'))
        
        # Vérification des informations de connexion
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (id,))
        user_data = cursor.fetchone()
        
        if user_data and user_data['isActive']:
            # Vérification du mot de passe
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user_data['password'] == hashed_password:
                # Création d'une session
                session['user_id'] = user_data['id']
                
                # Ajout d'un log
                cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)",
                               (user_data['id'], 'login', 'User logged in successfully'))
                db.commit()
                
                db.close()
                return redirect(redirect_url)
            else:
                flash('Identifiant ou mot de passe incorrect.', 'error')
        else:
            flash('Identifiant ou mot de passe incorrect.', 'error')
        
        db.close()
    
    return render_template('login.html')
```

### Déconnexion
```python
@bp.route('/logout')
def logout():
    # Suppression de la session
    session.pop('user_id', None)
    
    # Ajout d'un log
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)",
                   (current_user.id, 'logout', 'User logged out successfully'))
    db.commit()
    db.close()
    
    return redirect(url_for('auth.login'))
```

### Mot de Passe Oublié
```python
@bp.route('/forgot-password')
def forgot_password():
    return render_template('login.html', forgot_password=True)
```
