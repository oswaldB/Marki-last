# Partial : Auth Layout
**Fichier cible** : `app/templates/auth-layout.html`

---

## **Description**
Layout pour les pages d'authentification (login, register, forgot-password, superadmin). Sans sidebar/topbar.

---

## **Structure HTML**
```html
{% extends "base.html" %}

{% block content %}
<div class="flex h-screen items-center justify-center bg-gradient-to-br from-primary to-primary-dark">
  <div class="w-full max-w-md">
    <!-- Logo -->
    <div class="text-center mb-8">
      <h1 class="text-4xl font-bold text-white mb-2">Marki</h1>
      <p class="text-white text-opacity-80">Gestion des Commissions</p>
    </div>

    <!-- Card -->
    <div class="bg-white rounded-lg shadow-2xl p-8">
      {% block auth_content %}{% endblock %}
    </div>

    <!-- Footer -->
    <div class="text-center mt-8 text-white text-opacity-70 text-sm">
      <p>&copy; 2026 Marki. Tous droits réservés.</p>
    </div>
  </div>
</div>
{% endblock %}
```

---

## **Blocs Hérités**
- `{% block auth_content %}` : Contenu du formulaire d'authentification
