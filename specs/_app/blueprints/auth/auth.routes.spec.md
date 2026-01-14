# Routes : Authentification (ST-003, ST-008)
**Fichier cible** : `app/blueprints/auth/routes.py`

---

## **Endpoints**

| URL | Méthode | Paramètres | Retour | Description |
|-----|---------|-----------|--------|-------------|
| `/auth/login` | GET | - | HTML | Formulaire de connexion |
| `/auth/login` | POST | `username`, `password` | Redirect | Traite la connexion |
| `/auth/register` | GET | - | HTML | Formulaire d'inscription |
| `/auth/register` | POST | `username`, `password`, `password_confirm` | Redirect | Crée un compte |
| `/auth/logout` | POST | - | Redirect | Déconnecte l'utilisateur |
| `/auth/forgot-password` | GET | - | HTML | Formulaire de récupération |
| `/auth/forgot-password` | POST | `username` | Redirect | Génère mot de passe temporaire |
| `/superadmin` | GET | - | HTML | Affiche le formulaire de création du premier administrateur |
| `/superadmin` | POST | `superadmin_password`, `username`, `password`, `confirm_password` | Redirect | Crée le premier administrateur et redirige vers `/auth/login` |
| `/settings/team` | GET | - | HTML | Gestion des utilisateurs (admin) |
| `/api/users` | GET | - | JSON | Liste des utilisateurs |
| `/api/users/add` | POST | `username`, `password`, `email` | JSON | Ajoute collaborateur |
| `/api/users/<id>/password` | PUT | `new_password` | JSON | Change mot de passe |
| `/api/users/<id>/toggle` | PUT | - | JSON | Bascule état bloqué/actif |

---

## **Règles Métier**

### Authentification
- `username` doit être **unique** et alphanumérioque (3-50 caractères)
- `password` doit être **haché** avec bcrypt
- `password` minimum **8 caractères** avec majuscule, minuscule, chiffre
- Les tentatives de connexion échouées sont limitées à 5 avant blocage temporaire

### Inscription
- L'utilisateur doit confirmer le mot de passe
- L'email est optionnel mais unique s'il est fourni
- Après inscription, redirection vers `/auth/login`

### Récupération Mot de Passe
- Générer un mot de passe temporaire aléatoire (12 caractères)
- Afficher le mot de passe à l'écran UNE SEULE FOIS
- Forcer changement au prochain login

### Superadmin
- Accessible uniquement avec le mot de passe `Citron6-Mustang9`
- Vérifie qu'aucun administrateur n'existe déjà avant de créer un nouvel utilisateur
- L'utilisateur créé doit avoir le rôle `admin` et le statut `actif`
- Après création, redirige vers `/auth/login`

### Gestion Équipe (Admin)
- Accessible **uniquement** si `isAdmin = true`
- Administrateur peut : créer utilisateur, changer mot de passe, bloquer/débloquer
- Email du nouvel utilisateur est unique

---

## **Codes d'Erreur**

| Code | Message | Contexte |
|------|---------|----------|
| `400` | Données invalides | Format incorrect ou champs manquants |
| `401` | Identifiants invalides | Username/password incorrect |
| `403` | Accès refusé | Utilisateur bloqué ou non admin |
| `409` | Username/Email existe | Conflit d'unicité |
| `500` | Erreur serveur | Exception non gérée |

---

## **Détails de la Route `/superadmin` (ST-008)**

### **1. Route `/superadmin`**
- **Méthodes** : `GET`, `POST`
- **Description** : Affiche le formulaire de création du premier administrateur et traite la soumission.

#### **GET `/superadmin`**
- **Fonction** : `superadmin()`
- **Retourne** : Template `auth/superadmin.html`.
- **Accès** : Restreint par mot de passe superadmin.

#### **POST `/superadmin`**
- **Fonction** : `create_first_admin()`
- **Paramètres** :
  - `superadmin_password` : Mot de passe superadmin (`Citron6-Mustang9`).
  - `username` : Nom d'utilisateur du premier administrateur.
  - `password` : Mot de passe du premier administrateur.
  - `confirm_password` : Confirmation du mot de passe.
- **Validation** :
  - Vérifie que `superadmin_password` est correct.
  - Vérifie que `username` est unique et non vide.
  - Vérifie que `password` est non vide et correspond à `confirm_password`.
- **Actions** :
  - Crée un nouvel utilisateur avec le rôle `admin` et le statut `actif`.
  - Hache le mot de passe avant de le stocker.
  - Redirige vers `/auth/login` après succès.
- **Erreurs** :
  - `400` : Mot de passe superadmin incorrect ou champs invalides.
  - `403` : Un administrateur existe déjà.

---

## **Exemple de Code pour `/superadmin`**

### **Backend (Flask)**
```python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/superadmin', methods=['GET', 'POST'])
def superadmin():
    if request.method == 'POST':
        # Vérifier le mot de passe superadmin
        if request.form['superadmin_password'] != 'Citron6-Mustang9':
            flash('Mot de passe superadmin incorrect.', 'error')
            return redirect(url_for('auth.superadmin'))

        # Vérifier si un administrateur existe déjà
        if User.query.filter_by(is_admin=True).first():
            flash('Un administrateur existe déjà.', 'error')
            return redirect(url_for('auth.login'))

        # Créer le premier administrateur
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Valider les champs
        if not password:
            flash('Le mot de passe est requis.', 'error')
            return redirect(url_for('auth.superadmin'))
        if password != confirm_password:
            flash('Les mots de passe ne correspondent pas.', 'error')
            return redirect(url_for('auth.superadmin'))

        # Créer l'utilisateur
        new_user = User(
            username=username,
            password_hash=generate_password_hash(password),
            is_admin=True,
            is_active=True
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Administrateur créé avec succès.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/superadmin.html')
```

---

## **Liens**
- [Spécifications fonctionnelles](../../specs/ST-008_superadmin.md)
- [Template Superadmin](../../templates/auth/ST-008_superadmin.html.spec.md)
- [Modèle User](../../bdd/auth/ST-003_users.md)
