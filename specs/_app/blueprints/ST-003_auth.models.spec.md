# Modèles : Authentification
**Fichier cible** : `app/blueprints/auth/models.py` (backend) et `app/blueprints/auth/static/js/*.js` (frontend)

---

## **Composants Alpine.js**

### `loginFormState()`
Gère le formulaire de connexion.

```javascript
/**
 * Logique du formulaire de connexion.
 * @returns {Object}
 * @property {Object} form - Données du formulaire
 * @property {String} error - Message d'erreur
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} submit - Soumet le formulaire
 */
function loginFormState() {
  return {
    form: {
      username: '',
      password: ''
    },
    error: '',
    isLoading: false,
    
    async submit() {
      this.error = '';
      this.isLoading = true;
      
      try {
        const response = await fetch('/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        });
        
        if (response.ok) {
          window.location.href = '/dashboard';
        } else {
          const data = await response.json();
          this.error = data.message || 'Identifiants invalides';
        }
      } catch (error) {
        this.error = 'Erreur serveur';
      } finally {
        this.isLoading = false;
      }
    }
  };
}
```

---

### `registerFormState()`
Gère le formulaire d'inscription.

```javascript
/**
 * Logique du formulaire d'inscription.
 * @returns {Object}
 * @property {Object} form - Données du formulaire
 * @property {Object} errors - Erreurs par champ
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} validate - Valide le formulaire
 * @property {Function} submit - Soumet le formulaire
 */
function registerFormState() {
  return {
    form: {
      username: '',
      password: '',
      password_confirm: ''
    },
    errors: {},
    isLoading: false,
    
    validate() {
      this.errors = {};
      if (this.form.username.length < 3) {
        this.errors.username = 'Minimum 3 caractères';
      }
      if (this.form.password.length < 8) {
        this.errors.password = 'Minimum 8 caractères';
      }
      if (this.form.password !== this.form.password_confirm) {
        this.errors.password_confirm = 'Mots de passe non identiques';
      }
      return Object.keys(this.errors).length === 0;
    },
    
    async submit() {
      if (!this.validate()) return;
      
      this.isLoading = true;
      try {
        const response = await fetch('/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        });
        
        if (response.ok) {
          window.location.href = '/auth/login?success=true';
        } else {
          const data = await response.json();
          this.errors.general = data.message || 'Erreur d\'inscription';
        }
      } catch (error) {
        this.errors.general = 'Erreur serveur';
      } finally {
        this.isLoading = false;
      }
    }
  };
}
```

---

### `superadminFormState()`
Gère le formulaire de création du premier administrateur.

```javascript
/**
 * Logique du formulaire de création du premier administrateur.
 * @returns {Object}
 * @property {Object} form - Données du formulaire
 * @property {Boolean} isLoading - État de chargement
 * @property {String} error - Message d'erreur
 * @property {String} success - Message de succès
 * @property {Function} passwordStrength - Vérifie la force du mot de passe
 * @property {Function} submitForm - Soumet le formulaire
 */
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

### `teamManagementState(users)`
Gère la liste et les actions sur les utilisateurs (Admin).

```javascript
/**
 * Logique de gestion équipe.
 * @param {Array} users - Liste initiale des utilisateurs
 * @returns {Object}
 * @property {Array} users - Liste des utilisateurs
 * @property {Boolean} showAddModal - Affiche modal ajout
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} loadUsers - Recharge la liste
 * @property {Function} toggleBlock - Bascule blocage utilisateur
 * @property {Function} deleteUser - Supprime utilisateur
 */
function teamManagementState(users = []) {
  return {
    users: users,
    showAddModal: false,
    isLoading: false,
    
    async loadUsers() {
      try {
        const response = await fetch('/api/users');
        const data = await response.json();
        this.users = data.users;
      } catch (error) {
        console.error('Erreur chargement utilisateurs:', error);
      }
    },
    
    async toggleBlock(userId) {
      try {
        const response = await fetch(`/api/users/${userId}/toggle`, {
          method: 'PUT'
        });
        if (response.ok) {
          await this.loadUsers();
        }
      } catch (error) {
        console.error('Erreur blocage utilisateur:', error);
      }
    },
    
    async deleteUser(userId) {
      if (!confirm('Confirmer la suppression ?')) return;
      try {
        const response = await fetch(`/api/users/${userId}`, {
          method: 'DELETE'
        });
        if (response.ok) {
          await this.loadUsers();
        }
      } catch (error) {
        console.error('Erreur suppression:', error);
      }
    },
    
    init() {
      this.loadUsers();
    }
  };
}
```
