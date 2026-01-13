# Template : Relance - Dashboard
**Fichier cible** : `app/templates/relances/index.html`

---

## **Description**
Dashboard principal avec résumé des campagnes et calendrier des envois.

---

## **Structure HTML**
```html
{% extends "app-layout.html" %}

{% block page_content %}
<div x-data="relanceDashboardState()" class="space-y-8">
  <!-- Page Header -->
  <div>
    <h1 class="text-3xl font-bold text-text">Relances des Factures Impayées</h1>
    <p class="text-text-light mt-2">Gestion des campagnes et suivi des envois</p>
  </div>

  <!-- Stats Cards -->
  <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
    <!-- Active Campaigns -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-primary">
      <p class="text-text-light text-sm font-medium">Campagnes Actives</p>
      <p class="text-3xl font-bold text-text mt-2" x-text="stats.activeCampaigns"></p>
    </div>

    <!-- Total Reminders Sent -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-success">
      <p class="text-text-light text-sm font-medium">Relances Envoyées</p>
      <p class="text-3xl font-bold text-text mt-2" x-text="stats.remindersSent"></p>
    </div>

    <!-- Failed Reminders -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-error">
      <p class="text-text-light text-sm font-medium">Relances Échouées</p>
      <p class="text-3xl font-bold text-text mt-2" x-text="stats.remindersFailed"></p>
    </div>

    <!-- Open Rate -->
    <div class="bg-white rounded-lg shadow p-6 border-l-4 border-secondary">
      <p class="text-text-light text-sm font-medium">Taux d'Ouverture</p>
      <p class="text-3xl font-bold text-text mt-2" x-text="stats.openRate + '%'"></p>
    </div>
  </div>

  <!-- Calendar Section -->
  <div class="bg-white rounded-lg shadow p-6">
    <h2 class="text-2xl font-bold text-text mb-6">Calendrier des Envois</h2>
    
    <!-- Filters -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      <input type="text"
             x-model="filters.search"
             @input="loadCalendar()"
             placeholder="Rechercher..."
             class="px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
      
      <select x-model="filters.campaign" @change="loadCalendar()" class="px-4 py-2 border border-border rounded-lg">
        <option value="">Toutes les campagnes</option>
        <template x-for="campaign in campaigns" :key="campaign.id">
          <option :value="campaign.id" x-text="campaign.nom"></option>
        </template>
      </select>

      <select x-model="filters.status" @change="loadCalendar()" class="px-4 py-2 border border-border rounded-lg">
        <option value="">Tous les statuts</option>
        <option value="pending">En attente</option>
        <option value="sent">Envoyée</option>
        <option value="failed">Échouée</option>
      </select>

      <input type="date" x-model="filters.date" @change="loadCalendar()" class="px-4 py-2 border border-border rounded-lg">
    </div>

    <!-- Calendar Table -->
    <div class="overflow-x-auto" x-show="!isLoading">
      <table class="w-full">
        <thead class="bg-bg-light border-b border-border">
          <tr>
            <th class="px-6 py-3 text-left text-sm font-semibold text-text">Date</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-text">Campagne</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-text">Destinataire</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-text">Facture</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-text">Statut</th>
            <th class="px-6 py-3 text-right text-sm font-semibold text-text">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-border">
          <template x-for="reminder in calendarReminders" :key="reminder.id">
            <tr class="hover:bg-bg-light transition-colors">
              <td class="px-6 py-4 text-sm text-text" x-text="new Date(reminder.date).toLocaleDateString('fr-FR')"></td>
              <td class="px-6 py-4 text-sm text-text" x-text="reminder.campaign_name"></td>
              <td class="px-6 py-4 text-sm text-text" x-text="reminder.recipient"></td>
              <td class="px-6 py-4 text-sm text-text" x-text="reminder.facture_numero"></td>
              <td class="px-6 py-4 text-sm">
                <span class="px-3 py-1 rounded-full text-xs font-medium"
                      :class="{
                        'bg-secondary bg-opacity-20 text-secondary': reminder.statut === 'pending',
                        'bg-success bg-opacity-20 text-success': reminder.statut === 'sent',
                        'bg-error bg-opacity-20 text-error': reminder.statut === 'failed'
                      }"
                      x-text="reminder.statut"></span>
              </td>
              <td class="px-6 py-4 text-right space-x-2">
                <button @click="showDetailModal(reminder)" class="text-primary hover:text-primary-dark text-sm">Voir</button>
                <button @click="toggleStatus(reminder)" class="text-secondary hover:text-secondary text-sm">Marquer</button>
                <button @click="showEditDrawer(reminder)" class="text-text-light hover:text-text text-sm">Modifier</button>
              </td>
            </tr>
          </template>
        </tbody>
      </table>
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

  <!-- Modals & Drawers -->
  {% include "relances/partials/detail-modal.html" %}
  {% include "relances/partials/edit-drawer.html" %}
</div>
{% endblock %}
```

---

## **Composant Alpine.js**

```javascript
function relanceDashboardState() {
  return {
    stats: {
      activeCampaigns: 0,
      remindersSent: 0,
      remindersFailed: 0,
      openRate: 0
    },
    campaigns: [],
    calendarReminders: [],
    filters: {
      search: '',
      campaign: '',
      status: '',
      date: ''
    },
    isLoading: true,
    showDetailModal: false,
    showEditDrawer: false,
    selectedReminder: null,

    async loadStats() {
      try {
        const response = await fetch('/api/relances/stats');
        const data = await response.json();
        this.stats = data.stats;
      } catch (error) {
        console.error('Erreur chargement stats:', error);
      }
    },

    async loadCampaigns() {
      try {
        const response = await fetch('/api/relances/campaigns');
        const data = await response.json();
        this.campaigns = data.campaigns;
      } catch (error) {
        console.error('Erreur chargement campagnes:', error);
      }
    },

    async loadCalendar() {
      this.isLoading = true;
      try {
        const params = new URLSearchParams(this.filters);
        const response = await fetch(`/api/relances/calendar?${params}`);
        const data = await response.json();
        this.calendarReminders = data.reminders;
      } catch (error) {
        console.error('Erreur chargement calendrier:', error);
      } finally {
        this.isLoading = false;
      }
    },

    async toggleStatus(reminder) {
      const newStatus = reminder.statut === 'pending' ? 'sent' : 'failed';
      try {
        await fetch(`/api/relances/${reminder.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ statut: newStatus })
        });
        await this.loadCalendar();
      } catch (error) {
        console.error('Erreur mise à jour:', error);
      }
    },

    showDetailModal(reminder) {
      this.selectedReminder = reminder;
      this.showDetailModal = true;
    },

    showEditDrawer(reminder) {
      this.selectedReminder = reminder;
      this.showEditDrawer = true;
    },

    init() {
      this.loadStats();
      this.loadCampaigns();
      this.loadCalendar();
    }
  };
}
```
