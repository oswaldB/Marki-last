# ST-008 : Template - Superadmin

**Fichier** : `app/templates/auth/superadmin.html`
**Description** : Template pour la page de création du premier administrateur.

---

## **Structure du Template**

### **1. Étendue**
- **Layout** : Étend `app-layout.html`.
- **Bloc** : `page_content`.

### **2. Composant Alpine.js**
- **Fonction** : `superadminFormState()`
- **État** :
  - `form` : Objet contenant les champs du formulaire (`superadminPassword`, `username`, `password`, `confirmPassword`).
  - `isLoading` : Booléen pour gérer l'état de chargement.
  - `error` : Message d'erreur.
  - `success` : Message de succès.

### **3. Méthodes**
- **`passwordStrength()`** : Vérifie la force du mot de passe.
- **`submitForm()`** : Soumet le formulaire et gère les réponses.

### **4. Structure HTML**

#### **Formulaire**
- **Champs** :
  - `superadmin_password` : Champ de texte pour le mot de passe superadmin.
  - `username` : Champ de texte pour le nom d'utilisateur.
  - `password` : Champ de texte pour le mot de passe.
  - `confirm_password` : Champ de texte pour la confirmation du mot de passe.
- **Bouton** : Bouton de soumission avec gestion de l'état de chargement.

#### **Messages**
- **Erreur** : Affiche les messages d'erreur.
- **Succès** : Affiche les messages de succès.

---

## **Exemple de Code**

### **HTML**
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

---

## **Alpine.js**

### **Fonction `superadminFormState()`**
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

## **Liens**
- [Spécifications fonctionnelles](../../../specs/ST-008_superadmin.md)
- [Routes Superadmin](../../blueprints/ST-008_auth.routes.spec.md)
- [Modèle User](../../../bdd/auth/ST-003_users.md)
