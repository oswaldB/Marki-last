# **Spécifications Techniques – Authentification Marki**
**Version 1.0** | **Blueprint dédié** | **Flask + SQLite3**

---

## **1. Contexte**
Ce document décrit l’implémentation d’un système d’authentification pour **Marki**, basé sur :
- **Flask** (backend) + **Jinja2** (templates) + **Tailwind CSS** (styling).
- **SQLite3** pour la persistance des utilisateurs.
- **Flask-Login** pour la gestion des sessions.
- **Procédure de réinitialisation de mot de passe** (avec tokens sécurisés).

**Objectif** : Permettre aux utilisateurs de se connecter, se déconnecter, et réinitialiser leur mot de passe via une interface full-page avec le logo Marki.

---

## **2. Structure de la Base de Données SQLite3**

### **2.1. Table `users`**
```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,    -- Identifiant unique
    email TEXT UNIQUE NOT NULL,       -- Email pour la réinitialisation
    password TEXT NOT NULL,           -- Mot de passe haché (bcrypt)
    reset_token TEXT,                 -- Token pour la réinitialisation
    reset_token_expiration TIMESTAMP  -- Date d'expiration du token
);
```

### **2.2. Exemple de données initiales**
```python
# Utilisateur admin par défaut (optionnel)
default_password = generate_password_hash("admin123")
INSERT OR IGNORE INTO users (username, email, password)
VALUES ("admin", "admin@marki.com", ?);
```

---

## **3. Fonctionnalités Clés**

### **3.1. Pages et Routes**
| Route                     | Méthode | Description                                  | Template associé          |
|---------------------------|---------|----------------------------------------------|---------------------------|
| `/auth/login`             | GET/POST | Page de login full-page avec logo Marki.     | `login.html`              |
| `/auth/logout`            | GET     | Déconnexion de l’utilisateur.                | Redirection               |
| `/auth/reset_password`    | GET/POST | Demande de réinitialisation (formulaire email). | `reset_password.html`     |
| `/auth/reset_password/<token>` | GET/POST | Réinitialisation du mot de passe (lien sécurisé). | `set_new_password.html` |

### **3.2. Middleware de Protection**
- **`@login_required`** (Flask-Login) :
  - Appliqué à toutes les routes des autres blueprints (ex: `/dashboard`).
  - Redirige vers `/auth/login` si non authentifié.

---

## **4. Implémentation Technique**

### **4.1. Fichiers et Dossiers**
```
mon_projet/
├── app.py                  # Point d'entrée Flask
├── auth.py                 # Blueprint d'authentification
├── database.py             # Gestion de la base SQLite3
├── static/
│   └── logo-marki.png      # Logo pour la page de login
└── templates/
    ├── login.html          # Page de login
    ├── reset_password.html # Formulaire de demande de réinitialisation
    └── set_new_password.html # Formulaire de nouveau mot de passe
```

### **4.2. Code Clé**

#### **a. Initialisation de la base (`database.py`)**
```python
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (...)''')
    # Ajout d'un utilisateur admin (optionnel)
    conn.commit()
    conn.close()

def get_user_by_username(username):
    # Requête pour récupérer un utilisateur par username
    pass

def update_password(email, new_password):
    # Met à jour le mot de passe après réinitialisation
    pass
```

#### **b. Blueprint Auth (`auth.py`)**
```python
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer

auth_bp = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_data = get_user_by_username(username)
        if user_data and check_password_hash(user_data[3], password):
            login_user(User(*user_data))
            return redirect(url_for('main.index'))
        flash('Identifiant ou mot de passe incorrect.')
    return render_template('login.html')

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form.get('email')
        # Générer un token et envoyer un email
        flash('Lien de réinitialisation envoyé.')
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html')
```

#### **c. Intégration Flask-Login (`app.py`)**
```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    # Charge l'utilisateur depuis la base
    pass
```

---

## **5. Sécurité**
- **Hachage des mots de passe** : Utilisation de `werkzeug.security.generate_password_hash`.
- **Tokens de réinitialisation** :
  - Générés avec `itsdangerous.URLSafeTimedSerializer`.
  - Expiration : 1 heure.
- **Protection CSRF** : À activer via `flask_wtf.csrf` (recommandé).

---

## **6. Templates (Exemples)**

#### **a. `login.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Connexion - Marki</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 h-screen flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-md w-96">
        <img src="{{ url_for('static', filename='logo-marki.png') }}" alt="Marki" class="mx-auto mb-6 w-32">
        <form method="POST">
            <input type="text" name="username" placeholder="Identifiant" class="w-full p-2 mb-4 border rounded">
            <input type="password" name="password" placeholder="Mot de passe" class="w-full p-2 mb-4 border rounded">
            <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Se connecter</button>
        </form>
        <p class="mt-4 text-center">
            <a href="{{ url_for('auth.reset_password') }}" class="text-blue-500">Mot de passe oublié ?</a>
        </p>
    </div>
</body>
</html>
```

#### **b. `reset_password.html`**
```html
<form method="POST" class="max-w-md mx-auto mt-8">
    <input type="email" name="email" placeholder="Votre email" class="w-full p-2 mb-4 border rounded">
    <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded">Envoyer le lien</button>
</form>
```

---

## **7. Procédure de Réinitialisation**
1. L’utilisateur saisit son email sur `/auth/reset_password`.
2. Un **token sécurisé** est généré et stocké en base avec une date d’expiration.
3. Un email est envoyé avec un lien vers `/auth/reset_password/<token>`.
4. L’utilisateur définit un nouveau mot de passe (validé côté serveur).

---

## **8. Tests Recommandés**
- **Tests unitaires** (avec `pytest`) :
  - Vérifier la création/utilisateur.
  - Tester la validation des tokens.
- **Tests d’intégration** (avec Cypress) :
  - Parcours complet : login → réinitialisation → nouveau login.

---

## **9. Dépendances**
```bash
pip install flask flask-login itsdangerous werkzeug
```

---

## **10. Notes Supplémentaires**
- **Compatibilité** : Ce système est conçu pour fonctionner avec le **middleware de blueprints** existant chez Steroids Studio.
- **Extensibilité** :
  - Ajout d’une confirmation par email (via `flask_mail`).
  - Intégration avec un système de rôles (ex: `admin`, `user`).

---
