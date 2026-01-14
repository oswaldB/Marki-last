# ST-008 : Page Superadmin - Création du Premier Administrateur

**Date** : 2026-01-14
**Auteur** : Mistral Vibe
**Statut** : En cours

---

## **1. Contexte et Objectifs**

La page Superadmin est une page sécurisée qui permet de créer le premier utilisateur administrateur de l'application. Cette page est accessible uniquement avec un mot de passe spécifique et est conçue pour être utilisée une seule fois lors de la première installation de l'application.

---

## **2. Spécifications Fonctionnelles**

### **2.1. Accès à la Page**
- **URL** : `/superadmin`
- **Méthode** : `GET`
- **Accès** : Restreint par mot de passe.
- **Mot de Passe** : `Citron6-Mustang9`

### **2.2. Formulaire de Création**
- **Champs** :
  - **Mot de Passe** : Champ de texte pour saisir le mot de passe.
  - **Nom d'Utilisateur** : Champ de texte pour le nom du premier administrateur.
  - **Mot de Passe Utilisateur** : Champ de texte pour le mot de passe du premier administrateur.
  - **Confirmation du Mot de Passe** : Champ de texte pour confirmer le mot de passe.
- **Bouton** : "Créer le Premier Administrateur"

### **2.3. Validation**
- **Mot de Passe Superadmin** : Doit être `Citron6-Mustang9`.
- **Nom d'Utilisateur** : Doit être unique et non vide.
- **Mot de Passe Utilisateur** : Doit être non vide.
- **Confirmation du Mot de Passe** : Doit correspondre au mot de passe utilisateur.

### **2.4. Création de l'Administrateur**
- **Rôle** : L'utilisateur créé doit avoir le rôle `admin`.
- **Statut** : L'utilisateur doit être actif.
- **Redirection** : Après création, rediriger vers la page de login.

### **2.5. Sécurité**
- **Session** : La session doit être sécurisée.
- **CSRF** : Protection contre les attaques CSRF.
- **Rate Limiting** : Limiter le nombre de tentatives de connexion.

---

## **3. Spécifications Techniques**

### **3.1. Backend**
- **Fichier** : `app/blueprints/auth/routes.py`
- **Route** : `/superadmin`
- **Méthodes** : `GET`, `POST`
- **Fonctions** :
  - `superadmin()` : Affiche le formulaire de création.
  - `create_first_admin()` : Crée le premier administrateur.

### **3.2. Frontend**
- **Fichier** : `app/templates/auth/superadmin.html`
- **Template** : Utilise `base.html` comme layout de base (sans `app-layout.html`).
- **Composants Alpine.js** :
  - `superadminFormState()` : Gère l'état du formulaire.
  - `passwordStrength()` : Vérifie la force du mot de passe.

### **3.3. Base de Données**
- **Table** : `users`
- **Champs** :
  - `id` : Clé primaire.
  - `username` : Nom d'utilisateur unique.
  - `password_hash` : Hash du mot de passe.
  - `is_admin` : Booléen, vrai pour les administrateurs.
  - `is_active` : Booléen, vrai pour les utilisateurs actifs.
  - `created_at` : Date de création.

---

## **4. Règles Métier**

### **4.1. Accès**
- La page `/superadmin` doit être accessible uniquement avec le mot de passe `Citron6-Mustang9`.
- Après la création du premier administrateur, la page doit être désactivée.

### **4.2. Validation**
- Le mot de passe superadmin doit être vérifié avant l'affichage du formulaire.
- Le nom d'utilisateur doit être unique.
- Le mot de passe doit être fort et confirmé.

### **4.3. Création**
- L'utilisateur créé doit avoir le rôle `admin`.
- L'utilisateur doit être marqué comme actif.
- Après création, l'utilisateur doit être redirigé vers la page de login.

### **4.4. Sécurité**
- Le mot de passe doit être haché avant d'être stocké dans la base de données.
- La session doit être sécurisée avec un token CSRF.
- Le nombre de tentatives de connexion doit être limité.

---

## **5. Exemple de Code**

### **5.1. Backend (Flask)**
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

### **5.2. Frontend (HTML)**
```html
{% extends "app-layout.html" %}

{% block page_content %}
<div x-data="superadminFormState()" class="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-md">
  <h1 class="text-2xl font-bold text-text mb-6">Créer le Premier Administrateur</h1>

  <form @submit.prevent="submitForm" class="space-y-4">
    <!-- Mot de Passe Superadmin -->
    <div>
      <label for="superadmin_password" class="block text-sm font-medium text-text-light">Mot de Passe Superadmin</label>
      <input type="password" id="superadmin_password" x-model="form.superadminPassword" required
             class="mt-1 block w-full px-3 py-2 border border-border rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary">
    </div>

    <!-- Nom d'Utilisateur -->
    <div>
      <label for="username" class="block text-sm font-medium text-text-light">Nom d'Utilisateur</label>
      <input type="text" id="username" x-model="form.username" required
             class="mt-1 block w-full px-3 py-2 border border-border rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary">
    </div>



    <!-- Mot de Passe -->
    <div>
      <label for="password" class="block text-sm font-medium text-text-light">Mot de Passe</label>
      <input type="password" id="password" x-model="form.password" required
             class="mt-1 block w-full px-3 py-2 border border-border rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary">
      <p class="mt-2 text-sm text-text-light" x-text="passwordStrength()"></p>
    </div>

    <!-- Confirmation du Mot de Passe -->
    <div>
      <label for="confirm_password" class="block text-sm font-medium text-text-light">Confirmation du Mot de Passe</label>
      <input type="password" id="confirm_password" x-model="form.confirmPassword" required
             class="mt-1 block w-full px-3 py-2 border border-border rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary">
    </div>

    <!-- Bouton de Soumission -->
    <div>
      <button type="submit" :disabled="isLoading"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary">
        <span x-show="!isLoading">Créer le Premier Administrateur</span>
        <span x-show="isLoading" class="flex items-center">
          <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Création en cours...
        </span>
      </button>
    </div>

    <!-- Message d'Erreur -->
    <div x-show="error" class="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
      <p x-text="error"></p>
    </div>

    <!-- Message de Succès -->
    <div x-show="success" class="mt-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded">
      <p x-text="success"></p>
    </div>
  </form>
</div>

<script>
function superadminFormState() {
  return {
    form: {
      superadminPassword: '',
      username: '',

      password: '',
      confirmPassword: ''
    },
    isLoading: false,
    error: '',
    success: '',

    passwordStrength() {
      if (this.form.password.length === 0) return '';
      return 'Mot de passe valide.';
    },

    async submitForm() {
      this.isLoading = true;
      this.error = '';
      this.success = '';

      try {
        const response = await fetch('/superadmin', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token() }}'
          },
          body: JSON.stringify(this.form)
        });

        const data = await response.json();

        if (response.ok) {
          this.success = data.message;
          window.location.href = '/auth/login';
        } else {
          this.error = data.error || 'Une erreur est survenue.';
        }
      } catch (error) {
        this.error = 'Une erreur est survenue. Veuillez réessayer.';
      } finally {
        this.isLoading = false;
      }
    }
  };
}
</script>

{% endblock %}
```

### **5.3. Alpine.js**
```javascript
function superadminFormState() {
  return {
    form: {
      superadminPassword: '',
      username: '',
  
      password: '',
      confirmPassword: ''
    },
    isLoading: false,
    error: '',
    success: '',

    passwordStrength() {
      if (this.form.password.length === 0) return '';
      return 'Mot de passe valide.';
    },

    async submitForm() {
      this.isLoading = true;
      this.error = '';
      this.success = '';

      try {
        const response = await fetch('/superadmin', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token() }}'
          },
          body: JSON.stringify(this.form)
        });

        const data = await response.json();

        if (response.ok) {
          this.success = data.message;
          window.location.href = '/auth/login';
        } else {
          this.error = data.error || 'Une erreur est survenue.';
        }
      } catch (error) {
        this.error = 'Une erreur est survenue. Veuillez réessayer.';
      } finally {
        this.isLoading = false;
      }
    }
  };
}
```

---

## **6. Tests**

### **6.1. Tests Unitaires**
- **Fichier** : `tests/unit/auth/test_superadmin.py`
- **Couverture** :
  - Test de la route `/superadmin`.
  - Test de la création du premier administrateur.
  - Test de la validation du mot de passe superadmin.
  - Test de la validation des champs du formulaire (username, password, confirm_password).

### **6.2. Tests Behave**
- **Fichier** : `tests/features/superadmin.feature`
- **Couverture** :
  - Accès à la page superadmin.
  - Création du premier administrateur.
  - Redirection après création.

### **6.3. Tests Cypress**
- **Fichier** : `tests/cypress/e2e/auth/superadmin.cy.js`
- **Couverture** :
  - Affichage du formulaire (username, password, confirm_password).
  - Validation des champs.
  - Soumission du formulaire.
  - Redirection après création.

---

## **7. Sécurité**

### **7.1. Protection CSRF**
- Utiliser `{{ csrf_token() }}` dans le formulaire.
- Vérifier le token CSRF dans le backend.

### **7.2. Rate Limiting**
- Limiter le nombre de tentatives de connexion.
- Bloquer l'IP après plusieurs tentatives infructueuses.

### **7.3. Hachage du Mot de Passe**
- Utiliser `werkzeug.security.generate_password_hash` pour hacher le mot de passe.
- Ne jamais stocker le mot de passe en clair.

---

## **8. Liens**

- [Spécifications techniques des routes](../../_app/blueprints/auth/auth.routes.spec.md)
- [Spécifications techniques du template](../../_app/templates/auth/superadmin.html.spec.md)
- [Modèle User](../../bdd/auth/ST-003_users.md)

## **9. Conclusion**

La page Superadmin est conçue pour être utilisée une seule fois lors de la première installation de l'application. Elle permet de créer le premier utilisateur administrateur de manière sécurisée et contrôlée.

---

**Generated by Mistral Vibe.**
**Co-Authored-By: Mistral Vibe <vibe@mistral.ai>**