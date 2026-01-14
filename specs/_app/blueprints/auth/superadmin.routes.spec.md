# Routes : Superadmin (ST-008)

**Fichier** : `app/blueprints/auth/routes.py`
**Description** : Routes pour la gestion de la page Superadmin.

---

## **Routes**

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

## **Exemple de Code**

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
