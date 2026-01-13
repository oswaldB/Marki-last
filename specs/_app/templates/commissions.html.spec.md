# Template : Commissions
**Fichier cible** : `app/templates/commissions/index.html`

---

## **Description**
Page de gestion des commissions avec filtres et actions.

---

## **Structure HTML**
```html
{% extends "app-layout.html" %}

{% block page_content %}
<div x-data="commissionsListState()" class="space-y-6">
  <!-- Page Header -->
  <div>
    <h1 class="text-3xl font-bold text-text">Commissions</h1>
    <p class="text-text-light mt-2">Gestion et suivi des commissions</p>
  </div>

  <!-- Status Tabs -->
  <div class="flex gap-4 border-b border-border">
    <button @click="setStatus('conflit')" 
            :class="status === 'conflit' ? 'border-b-2 border-error text-error' : 'text-text-light'"
            class="pb-4 font-medium transition-colors">
      En Conflit <span class="text-sm" x-show="conflictCount > 0" x-text="`(${conflictCount})`"></span>
    </button>
    <button @click="setStatus('valide')" 
            :class="status === 'valide' ? 'border-b-2 border-primary text-primary' : 'text-text-light'"
            class="pb-4 font-medium transition-colors">
      Valides
    </button>
    <button @click="setStatus('archive')" 
            :class="status === 'archive' ? 'border-b-2 border-secondary text-secondary' : 'text-text-light'"
            class="pb-4 font-medium transition-colors">
      Archivées
    </button>
  </div>

  <!-- Search Bar -->
  <div>
    <input type="text"
           x-model="filters.search"
           @input="loadCommissions()"
           placeholder="Rechercher par numéro de facture..."
           class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
  </div>

  <!-- Table -->
  <div class="bg-white rounded-lg shadow overflow-hidden" x-show="!isLoading">
    <table class="w-full">
      <thead class="bg-bg-light border-b border-border">
        <tr>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Facture</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Intervenant</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Montant TTC</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Statut</th>
          <th class="px-6 py-3 text-right text-sm font-semibold text-text">Actions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-border">
        <template x-for="commission in commissions" :key="commission.nfacture">
          <tr class="hover:bg-bg-light transition-colors">
            <td class="px-6 py-4 text-sm text-text" x-text="commission.nfacture"></td>
            <td class="px-6 py-4 text-sm text-text" x-text="commission.intervenant"></td>
            <td class="px-6 py-4 text-sm font-medium text-text" x-text="'€' + commission.montant_ttc.toLocaleString('fr-FR')"></td>
            <td class="px-6 py-4 text-sm">
              <span class="px-3 py-1 rounded-full text-xs font-medium"
                    :class="{
                      'bg-error bg-opacity-20 text-error': commission.statut === 'conflit',
                      'bg-success bg-opacity-20 text-success': commission.statut === 'valide',
                      'bg-secondary bg-opacity-20 text-secondary': commission.statut === 'archive'
                    }"
                    x-text="commission.statut"></span>
            </td>
            <td class="px-6 py-4 text-right space-x-2">
              <button x-show="commission.statut === 'conflit'"
                      @click="showRepairModal(commission)"
                      class="text-primary hover:text-primary-dark text-sm font-medium">
                Réparer
              </button>
              <button x-show="commission.statut === 'valide'"
                      @click="showSplitDrawer(commission)"
                      class="text-secondary hover:text-secondary text-sm font-medium">
                Découper
              </button>
              <button @click="settleCommission(commission.nfacture, new Date().toISOString().split('T')[0])"
                      class="text-success hover:text-success text-sm font-medium">
                Régler
              </button>
              <button @click="archiveCommission(commission.nfacture)"
                      class="text-text-light hover:text-text text-sm font-medium">
                Archiver
              </button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
    
    <!-- Empty State -->
    <div x-show="commissions.length === 0" class="text-center py-12">
      <p class="text-text-light">Aucune commission</p>
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

  <!-- Modals & Drawers -->
  {% include "commissions/partials/repair-modal.html" %}
  {% include "commissions/partials/split-drawer.html" %}
</div>
{% endblock %}
```

---

## **Composant Alpine.js**
Voir [commissions.models.spec.md](../blueprints/commissions.models.spec.md#commissionsliststate)
