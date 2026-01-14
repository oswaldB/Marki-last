# Template : Relance - Campagnes
**Fichier cible** : `app/templates/relances/campaigns.html`

---

## **Description**
Gestion des campagnes de relance avec création, édition et suppression.

---

## **Structure HTML**
```html
{% extends "app-layout.html" %}

{% block page_content %}
<div x-data="relanceCampaignsState()" class="space-y-6">
  <!-- Page Header -->
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-text">Campagnes de Relance</h1>
      <p class="text-text-light mt-2">Créer et gérer les campagnes de relance</p>
    </div>
    <button @click="showCreateModal = true"
            class="px-6 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors">
      + Nouvelle Campagne
    </button>
  </div>

  <!-- Campaigns Table -->
  <div class="bg-white rounded-lg shadow overflow-hidden" x-show="!isLoading">
    <table class="w-full">
      <thead class="bg-bg-light border-b border-border">
        <tr>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Nom</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Description</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Statut</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Relances</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Créée le</th>
          <th class="px-6 py-3 text-right text-sm font-semibold text-text">Actions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-border">
        <template x-for="campaign in campaigns" :key="campaign.id">
          <tr class="hover:bg-bg-light transition-colors">
            <td class="px-6 py-4 text-sm font-medium text-text" x-text="campaign.nom"></td>
            <td class="px-6 py-4 text-sm text-text-light" x-text="campaign.description || '-'"></td>
            <td class="px-6 py-4 text-sm">
              <span class="px-3 py-1 rounded-full text-xs font-medium"
                    :class="{
                      'bg-success bg-opacity-20 text-success': campaign.statut === 'active',
                      'bg-secondary bg-opacity-20 text-secondary': campaign.statut === 'completed',
                      'bg-border bg-opacity-20 text-text-light': campaign.statut === 'paused'
                    }"
                    x-text="campaign.statut"></span>
            </td>
            <td class="px-6 py-4 text-sm text-text" x-text="campaign.nombre_relances"></td>
            <td class="px-6 py-4 text-sm text-text-light" x-text="new Date(campaign.date_creation).toLocaleDateString('fr-FR')"></td>
            <td class="px-6 py-4 text-right space-x-2">
              <button @click="showEditModal(campaign)" class="text-primary hover:text-primary-dark text-sm">Éditer</button>
              <button @click="toggleCampaignStatus(campaign)" class="text-secondary hover:text-secondary text-sm" 
                      x-text="campaign.statut === 'active' ? 'Pause' : 'Reprendre'"></button>
              <button @click="deleteCampaign(campaign.id)" class="text-error hover:text-error text-sm">Supprimer</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <!-- Empty State -->
    <div x-show="campaigns.length === 0" class="text-center py-12">
      <p class="text-text-light">Aucune campagne</p>
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

  <!-- Modals -->
  {% include "relances/partials/campaign-modal.html" %}
</div>
{% endblock %}
```

---

## **Composant Alpine.js**

```javascript
function relanceCampaignsState() {
  return {
    campaigns: [],
    isLoading: true,
    showCreateModal: false,
    showEditModal: false,
    selectedCampaign: null,

    async loadCampaigns() {
      this.isLoading = true;
      try {
        const response = await fetch('/api/relances/campaigns');
        const data = await response.json();
        this.campaigns = data.campaigns;
      } catch (error) {
        console.error('Erreur chargement:', error);
      } finally {
        this.isLoading = false;
      }
    },

    showEditModal(campaign) {
      this.selectedCampaign = campaign;
      this.showEditModal = true;
    },

    async toggleCampaignStatus(campaign) {
      const newStatus = campaign.statut === 'active' ? 'paused' : 'active';
      try {
        await fetch(`/api/relances/campaigns/${campaign.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ statut: newStatus })
        });
        await this.loadCampaigns();
      } catch (error) {
        console.error('Erreur:', error);
      }
    },

    async deleteCampaign(id) {
      if (!confirm('Confirmer la suppression ?')) return;
      try {
        await fetch(`/api/relances/campaigns/${id}`, { method: 'DELETE' });
        await this.loadCampaigns();
      } catch (error) {
        console.error('Erreur suppression:', error);
      }
    },

    init() {
      this.loadCampaigns();
    }
  };
}
```
