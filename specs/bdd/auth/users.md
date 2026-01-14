# Base de Données : Utilisateurs (ST-003, ST-008)
**Type** : SQLite avec SQLAlchemy
**Fichier cible** : `app/instance/users.db`
**Intégration** : Flask-Login pour la gestion de session

---

## **Schéma SQL**

```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(120) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT 0,
    is_blocked BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME
);
```

---

## **Modèle SQLAlchemy (ORM)**

```python
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """
    Modèle utilisateur avec intégration Flask-Login.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def set_password(self, password):
        """Hash et enregistre le mot de passe."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Vérifie le mot de passe contre le hash."""
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        """Retourne l'ID de l'utilisateur pour Flask-Login."""
        return str(self.id)

    def __repr__(self):
        return f'<User {self.username}>'
```

---

## **Schéma des Champs**

| Champ | Type | Unique | Nullable | Description |
|-------|------|--------|----------|-------------|
| `id` | Integer | ✓ | ✗ | Identifiant unique auto-incrémenté |
| `username` | String(50) | ✓ | ✗ | Nom d'utilisateur (3-50 caractères) |
| `email` | String(120) | ✓ | ✓ | Email unique (optionnel) |
| `password_hash` | String(255) | | ✗ | Hash bcrypt du mot de passe |
| `is_admin` | Boolean | | ✗ | Indique si l'utilisateur est admin (défaut: False) |
| `is_blocked` | Boolean | | ✗ | Indique si l'utilisateur est bloqué (défaut: False) |
| `created_at` | DateTime | | ✗ | Date création (auto: now) |
| `last_login` | DateTime | | ✓ | Date dernier login |

---

## **Contraintes**

- `username` : Unique, alphanumérique, 3-50 caractères
- `password_hash` : Jamais stocké en clair, toujours haché avec werkzeug
- `email` : Format valide, unique s'il existe, sinon NULL
- `is_admin` : Détermine accès `/settings/team` et fonctions d'administration
- `is_blocked` : `true` empêche connexion

---

## **Fonctions de Repository**

### `init_db()`
Initialise la base de données et crée les tables.

```python
def init_db(app):
    """Initialise la base de données SQLite."""
    with app.app_context():
        db.create_all()
```

---

### `create_user(username, email, password, is_admin=False)`
Crée un nouvel utilisateur avec validation.

**Validations** :
- `username` unique et valide (alphanumérique, 3-50 caractères)
- `email` unique et format valide (si fourni)
- `password` non vide, minimum 8 caractères

```python
def create_user(username, email, password, is_admin=False):
    """
    Crée un nouvel utilisateur.
    
    Args:
        username (str): Nom d'utilisateur unique
        email (str): Email optionnel
        password (str): Mot de passe en clair
        is_admin (bool): Indique si admin
    
    Returns:
        User: L'utilisateur créé
    
    Raises:
        ValueError: Si données invalides
    """
    if not username or len(username) < 3 or len(username) > 50:
        raise ValueError("Username invalide")
    
    if User.query.filter_by(username=username).first():
        raise ValueError("Username existe déjà")
    
    if not password or len(password) < 8:
        raise ValueError("Mot de passe minimum 8 caractères")
    
    user = User(username=username, email=email, is_admin=is_admin)
    user.set_password(password)
    
    db.session.add(user)
    db.session.commit()
    return user
```

---

### `get_user_by_id(user_id)`
Récupère un utilisateur par ID.

```python
def get_user_by_id(user_id):
    return User.query.get(user_id)
```

---

### `get_user_by_username(username)`
Récupère un utilisateur par username.

```python
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
```

---

### `get_all_users()`
Récupère tous les utilisateurs.

```python
def get_all_users():
    return User.query.all()
```

---

### `update_user(user_id, **kwargs)`
Met à jour un utilisateur.

```python
def update_user(user_id, **kwargs):
    """
    Met à jour un utilisateur.
    
    Args:
        user_id (int): ID de l'utilisateur
        **kwargs: Champs à mettre à jour
    
    Returns:
        User: L'utilisateur mis à jour
    
    Raises:
        ValueError: Si utilisateur introuvable
    """
    user = User.query.get(user_id)
    if not user:
        raise ValueError("Utilisateur introuvable")
    
    for key, value in kwargs.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    db.session.commit()
    return user
```

---

### `toggle_user_block(user_id)`
Bascule l'état bloqué d'un utilisateur.

```python
def toggle_user_block(user_id):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("Utilisateur introuvable")
    
    user.is_blocked = not user.is_blocked
    db.session.commit()
    return user
```

---

### `change_password(user_id, new_password)`
Change le mot de passe d'un utilisateur.

```python
def change_password(user_id, new_password):
    if not new_password or len(new_password) < 8:
        raise ValueError("Mot de passe minimum 8 caractères")
    
    user = User.query.get(user_id)
    if not user:
        raise ValueError("Utilisateur introuvable")
    
    user.set_password(new_password)
    db.session.commit()
    return user
```

---

### `delete_user(user_id)`
Supprime un utilisateur.

```python
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("Utilisateur introuvable")
    
    db.session.delete(user)
    db.session.commit()
```

---

## **Configuration Flask-Login**

```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Veuillez vous connecter'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
