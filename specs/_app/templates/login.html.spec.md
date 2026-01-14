# Template : Login (ST-003)
**Fichier cible** : `app/templates/auth/login.html`

---

## **Description**
Page de connexion pour l'authentification.

---

## **Structure HTML**
```html
{% extends "auth-layout.html" %}

{% block auth_content %}
<div x-data="loginFormState()">
  <!-- Title -->
  <h2 class="text-2xl font-bold text-text mb-6">Connexion</h2>

  <!-- Error Message -->
  <div x-show="error" class="mb-4 p-4 bg-error bg-opacity-10 border border-error rounded-lg">
    <p class="text-error text-sm" x-text="error"></p>
  </div>

  <!-- Form -->
  <form @submit.prevent="submit" class="space-y-4">
    <!-- Username -->
    <div>
      <label class="block text-sm font-medium text-text mb-2">Identifiant</label>
      <input type="text"
             x-model="form.username"
             required
             class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
             placeholder="Votre identifiant">
    </div>

    <!-- Password -->
    <div>
      <label class="block text-sm font-medium text-text mb-2">Mot de passe</label>
      <input type="password"
             x-model="form.password"
             required
             class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
             placeholder="Votre mot de passe">
    </div>

    <!-- Submit Button -->
    <button type="submit"
            :disabled="isLoading"
            class="w-full py-2 px-4 bg-primary text-white font-medium rounded-lg hover:bg-primary-dark transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
      <span x-show="!isLoading">Se connecter</span>
      <span x-show="isLoading">Connexion en cours...</span>
    </button>
  </form>

  <!-- Links -->
  <div class="mt-6 space-y-2 text-center text-sm">
    <p>
      <a href="/auth/forgot-password" class="text-primary hover:text-primary-dark transition-colors">Mot de passe oublié ?</a>
    </p>
  </div>
</div>
{% endblock %}
```

---

## **Composant Alpine.js**
Voir [auth.models.spec.md](../blueprints/auth.models.spec.md#loginformstate)
