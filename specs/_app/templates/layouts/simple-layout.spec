# Layout: Simple Layout
**Fichier** : app/templates/simple-layout.html
**Type** : Layout public sans navigation

---
## Description
Le Simple Layout fournit une structure minimale pour les pages publiques qui ne nécessitent pas de navigation (sidebar ou topbar). Il est conçu pour être léger et rapide à charger.

## Structure
```html
{% extends "base.html" %}

{% block sidebar %}{% endblock %}  <!-- Désactive la sidebar -->
{% block topbar %}{% endblock %}   <!-- Désactive la topbar -->

{% block content %}
  <!-- Contenu spécifique à la page -->
{% endblock %}
```

## Cas d'Utilisation
- Pages de login/registration
- Pages statiques (CGU, FAQ)
- Pages d'erreur (404, 500)
- Landing pages

## Comportement
- Héritage complet de `base.html`
- Suppression des éléments de navigation
- Contenu centré par défaut
- Compatible avec tous les composants Alpine.js

## Exemple d'Implémentation
```html
{% extends "simple-layout.html" %}

{% block content %}
  <div class="flex items-center justify-center min-h-screen bg-gray-50">
    <div class="w-full max-w-md p-8 space-y-8 bg-white rounded-lg shadow">
      <h1 class="text-2xl font-bold text-center">Bienvenue sur Marki</h1>
      <form method="POST" action="/login">
        <!-- Formulaire de connexion -->
      </form>
    </div>
  </div>
{% endblock %}
```

## Dépendances
- Tailwind CSS (via base.html)
- Alpine.js (via base.html)
- Aucun composant spécifique requis

## Tests Requis
- Vérification de l'absence de sidebar/topbar
- Test de responsive design
- Validation de l'accessibilité (contrastes, labels)
- Performance de chargement (< 500ms)