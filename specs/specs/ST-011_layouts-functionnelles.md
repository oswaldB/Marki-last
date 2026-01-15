# ST-011 : Système de Layouts pour Marki
**Date** : 2026-01-16
**Auteur** : Product Manager

---
## Contexte
Le système de layouts de Marki permet une gestion flexible et modulaire des interfaces utilisateur. Il repose sur une architecture hiérarchique avec un template de base (`base.html`) qui peut être étendu par différents layouts spécifiques selon les besoins des pages.

## Objectifs
- Centraliser les dépendances communes (Tailwind CSS, Alpine.js)
- Fournir des structures de page réutilisables
- Gérer l'authentification de manière déclarative
- Optimiser le chargement des ressources

## Architecture des Layouts

### 1. Base Template (`base.html`)
**Fichier** : `app/templates/base.html`

Le template de base contient :
- La structure HTML5 de base
- Les métadonnées communes
- Les inclusions des dépendances CSS/JS
- Les blocs Jinja2 pour l'extension

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Marki</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Alpine.js -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
  <!-- Blocs optionnels -->
  {% block sidebar %}{% include "partials/sidebar.html" %}{% endblock %}
  {% block topbar %}{% include "partials/topbar.html" %}{% endblock %}
  
  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

### 2. Simple Layout
**Fichier** : `app/templates/simple-layout.html`

Layout minimal sans éléments de navigation, idéal pour :
- Pages publiques (landing, login, register)
- Pages statiques
- Pages d'erreur

```html
{% extends "base.html" %}

{% block sidebar %}{% endblock %}  <!-- Désactive la sidebar -->
{% block topbar %}{% endblock %}   <!-- Désactive la topbar -->

{% block content %}
  <!-- Contenu spécifique à la page -->
{% endblock %}
```

### 3. App Layout
**Fichier** : `app/templates/app-layout.html`

Layout complet avec navigation, réservé aux pages authentifiées :
- Tableau de bord
- Paramètres utilisateur
- Pages métiers

```html
{% extends "base.html" %}

{% block content %}
  <div class="flex h-screen">
    <!-- Sidebar -->
    <aside class="w-64 bg-bg-light border-r border-border">
      {% block sidebar %}{% include "partials/sidebar.html" %}{% endblock %}
    </aside>
    
    <!-- Contenu principal -->
    <div class="flex-1 flex flex-col">
      <!-- Topbar -->
      <header class="bg-white border-b border-border">
        {% block topbar %}{% include "partials/topbar.html" %}{% endblock %}
      </header>
      
      <!-- Contenu de la page -->
      <main class="flex-1 overflow-auto p-6">
        {% block page_content %}{% endblock %}
      </main>
    </div>
  </div>
{% endblock %}
```

### 4. Simple Private Layout
**Fichier** : `app/templates/simple-private-layout.html`

Layout minimal pour les pages authentifiées sans navigation :
- Pages de configuration simple
- Modales ou overlays
- Pages de confirmation

```html
{% extends "base.html" %}

{% block sidebar %}{% endblock %}  <!-- Désactive la sidebar -->
{% block topbar %}{% endblock %}   <!-- Désactive la topbar -->

{% block content %}
  <div class="min-h-screen bg-bg-light p-6">
    <!-- Contenu privé sans navigation -->
    {% block page_content %}{% endblock %}
  </div>
{% endblock %}
```

## Règles d'Utilisation

### Choix du Layout
1. **Pages publiques** : Utiliser `simple-layout.html`
2. **Pages principales authentifiées** : Utiliser `app-layout.html`
3. **Pages secondaires authentifiées** : Utiliser `simple-private-layout.html`

### Bonnes Pratiques
- Toujours étendre un layout, jamais `base.html` directement
- Utiliser les blocs nommés pour le contenu spécifique
- Éviter de dupliquer du code entre les layouts
- Documenter les dépendances spécifiques dans les layouts

## Exemples d'Implémentation

### Page de Login (Simple Layout)
```html
{% extends "simple-layout.html" %}

{% block content %}
  <div class="flex items-center justify-center min-h-screen">
    <form class="p-8 bg-white rounded shadow">
      <!-- Formulaire de login -->
    </form>
  </div>
{% endblock %}
```

### Page de Dashboard (App Layout)
```html
{% extends "app-layout.html" %}

{% block page_content %}
  <h1 class="text-2xl font-bold mb-6">Tableau de bord</h1>
  <div class="grid grid-cols-3 gap-6">
    <!-- Widgets -->
  </div>
{% endblock %}
```

### Page de Confirmation (Simple Private Layout)
```html
{% extends "simple-private-layout.html" %}

{% block page_content %}
  <div class="max-w-md mx-auto bg-white p-6 rounded shadow">
    <h2 class="text-xl mb-4">Confirmation requise</h2>
    <p>Êtes-vous sûr de vouloir effectuer cette action ?</p>
  </div>
{% endblock %}
```

## Gestion des Dépendances

### Tailwind CSS
- Chargé via CDN dans `base.html`
- Configuration par défaut
- Classes utilitaires disponibles globalement

### Alpine.js
- Chargé via CDN dans `base.html`
- Disponible pour tous les layouts
- Utilisé pour les composants interactifs

## Évolutions Futures
- Ajout d'un système de thèmes
- Intégration de composants partagés
- Optimisation du chargement des ressources
- Support des layouts responsives avancés

## Validation
- Tous les layouts doivent être testés avec Cypress
- Vérification de l'accessibilité (a11y)
- Tests de performance de chargement