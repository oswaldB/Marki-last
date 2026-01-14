# Template : Dashboard
**Fichier cible** : `app/templates/dashboard.html`

---

## **Description**
Page principale du tableau de bord avec statistiques.

---

## **Structure HTML**
```html
{% extends "app-layout.html" %}

{% block page_content %}
<div x-data="dashboardState()" class="space-y-8">
  <!-- Page Header -->
  <div>
    <h1 class="text-3xl font-bold text-text">Tableau de Bord</h1>
    <p class="text-text-light mt-2">Bienvenue sur votre espace de gestion</p>
  </div>

  <!-- Stats Cards -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6" x-show="!isLoading">
    <!-- Total Users Card -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-primary">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-text-light text-sm font-medium">Utilisateurs Actifs</p>
          <p class="text-3xl font-bold text-text mt-2" x-text="stats.activeUsers"></p>
        </div>
        <svg class="w-12 h-12 text-primary opacity-20" fill="currentColor" viewBox="0 0 20 20">
          <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v-1h8v1zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"></path>
        </svg>
      </div>
    </div>

    <!-- Total Revenue Card -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-success">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-text-light text-sm font-medium">Revenu Total</p>
          <p class="text-3xl font-bold text-text mt-2" x-text="'€' + stats.totalRevenue.toLocaleString('fr-FR')"></p>
        </div>
        <svg class="w-12 h-12 text-success opacity-20" fill="currentColor" viewBox="0 0 20 20">
          <path d="M8.16 5.314l4.897-1.596A1 1 0 0115 4.366V12a6 6 0 11-12 0c0-2.748 1.122-5.233 2.936-7.022A9.996 9.996 0 0115 1c5.523 0 10 4.477 10 10s-4.477 10-10 10S0 16.523 0 11s4.477-10 10-10h.5"></path>
        </svg>
      </div>
    </div>

    <!-- Commissions Card -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-secondary">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-text-light text-sm font-medium">Commissions Valides</p>
          <p class="text-3xl font-bold text-text mt-2" x-text="stats.validCommissions || 0"></p>
        </div>
        <svg class="w-12 h-12 text-secondary opacity-20" fill="currentColor" viewBox="0 0 20 20">
          <path d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2H4a1 1 0 110-2V4z"></path>
        </svg>
      </div>
    </div>
  </div>

  <!-- Loading State -->
  <div x-show="isLoading" class="text-center py-12">
    <div class="inline-block animate-spin">
      <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
      </svg>
    </div>
  </div>
</div>
{% endblock %}
```

---

## **Composant Alpine.js**
Voir [app.models.spec.md](../blueprints/app.models.spec.md#dashboardstate)
