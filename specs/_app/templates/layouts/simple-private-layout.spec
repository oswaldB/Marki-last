# Layout: Simple Private Layout
**Fichier** : app/templates/simple-private-layout.html
**Type** : Layout authentifié sans navigation

---
## Description
Le Simple Private Layout est conçu pour les pages authentifiées qui ne nécessitent pas de navigation complexe. Il offre une structure minimaliste tout en garantissant que l'utilisateur est authentifié.

## Structure
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

## Cas d'Utilisation
- Pages de configuration simple
- Modales ou overlays nécessitant authentification
- Pages de confirmation d'actions
- Pages de résultats (après soumission de formulaire)
- Pages d'impression

## Comportement
- Héritage de `base.html` avec suppression des éléments de navigation
- Fond léger par défaut (bg-bg-light)
- Padding de 1.5rem (24px) autour du contenu
- Hauteur minimale de 100vh
- Contenu centré par défaut

## Exemple d'Implémentation
```html
{% extends "simple-private-layout.html" %}

{% block page_content %}
  <div class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow">
    <div class="flex justify-between items-start mb-6">
      <div>
        <h1 class="text-2xl font-bold">Confirmation de suppression</h1>
        <p class="text-text-light mt-1">Cette action est irréversible.</p>
      </div>
    </div>
    
    <div class="bg-bg-light rounded-lg p-6 mb-6">
      <h2 class="text-lg font-semibold mb-2">Élément à supprimer :</h2>
      <p class="text-text">Document #12345 - Rapport annuel 2023</p>
    </div>
    
    <div class="flex justify-end space-x-4">
      <a href="/dashboard" class="px-4 py-2 bg-gray-200 rounded-md hover:bg-gray-300">Annuler</a>
      <form method="POST" action="/delete/12345">
        <button type="submit" class="px-4 py-2 bg-error text-white rounded-md hover:bg-error-dark">
          Supprimer définitivement
        </button>
      </form>
    </div>
  </div>
{% endblock %}
```

## Dépendances
- Tailwind CSS (via base.html)
- Alpine.js (via base.html)
- Middleware d'authentification

## Middleware Requis
- Authentification obligatoire
- Vérification de session valide
- Gestion des permissions si nécessaire

## Avantages
- Chargement plus rapide que l'App Layout (pas de sidebar/topbar)
- Expérience utilisateur focalisée sur l'action en cours
- Réduction de la complexité visuelle
- Facile à personnaliser pour des besoins spécifiques

## Tests Requis
- Vérification de l'authentification (redirection si non connecté)
- Test de responsive design
- Validation de l'accessibilité (contrastes, focus)
- Performance de chargement (< 600ms)
- Test des actions critiques (formulaires, boutons)

## Bonnes Pratiques
- Utiliser pour les pages nécessitant une action unique
- Limiter le contenu à l'essentiel
- Fournir des chemins de retour clairs
- Documenter les actions irréversibles
- Utiliser des couleurs contrastées pour les actions critiques