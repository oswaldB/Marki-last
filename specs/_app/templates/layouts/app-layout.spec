# Layout: App Layout
**Fichier** : app/templates/app-layout.html
**Type** : Layout principal avec navigation (nécessite authentification)

---
## Description
L'App Layout est le layout principal pour les pages authentifiées. Il inclut une sidebar et une topbar pour la navigation, et est conçu pour les pages principales de l'application.

## Structure
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

## Composants Inclus
1. **Sidebar** : Navigation principale (partials/sidebar.html)
2. **Topbar** : Informations utilisateur et actions rapides (partials/topbar.html)

## Cas d'Utilisation
- Tableau de bord principal
- Pages de gestion (utilisateurs, paramètres)
- Pages métiers principales
- Toutes les pages nécessitant une navigation complète

## Comportement
- Layout flexbox pour une disposition responsive
- Sidebar fixe à gauche (largeur: 16rem/256px)
- Topbar fixe en haut
- Contenu principal scrollable
- Padding par défaut de 1.5rem (24px) autour du contenu

## Exemple d'Implémentation
```html
{% extends "app-layout.html" %}

{% block page_content %}
  <div class="container mx-auto">
    <h1 class="text-3xl font-bold mb-6">Tableau de bord</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
      <!-- Widgets -->
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-xl font-semibold mb-2">Statistiques</h2>
        <p class="text-3xl font-bold">1,234</p>
      </div>
    </div>
    
    <div class="bg-white rounded-lg shadow p-6">
      <h2 class="text-xl font-semibold mb-4">Activité récente</h2>
      <!-- Contenu -->
    </div>
  </div>
{% endblock %}
```

## Dépendances
- Tailwind CSS (via base.html)
- Alpine.js (via base.html)
- partials/sidebar.html
- partials/topbar.html

## Middleware Requis
- Authentification obligatoire
- Vérification des permissions utilisateur
- Gestion de session active

## Tests Requis
- Vérification de la présence de la sidebar et topbar
- Test de responsive (sidebar masquée sur mobile)
- Validation des liens de navigation
- Test d'accessibilité (navigation clavier)
- Performance de chargement (< 800ms avec cache)

## Notes Techniques
- La sidebar et la topbar peuvent être personnalisées en écrasant les blocs correspondants
- Le bloc `page_content` est réservé au contenu spécifique de la page
- Utiliser les classes Tailwind pour les ajustements de style