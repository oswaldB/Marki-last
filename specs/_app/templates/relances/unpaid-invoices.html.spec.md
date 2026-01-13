# Template : Relance - Factures Impayées
**Fichier cible** : `app/templates/relances/unpaid-invoices.html`

---

## **Description**
Gestion des factures impayées avec tableau des factures sans email et gestion manuelle.

---

## **Structure HTML**
```html
{% extends "app-layout.html" %}

{% block page_content %}
<div x-data="relanceUnpaidInvoicesState()" class="space-y-6">
  <!-- Page Header -->
  <div class="flex items-center justify-between">
    <div>
      <h1 class="text-3xl font-bold text-text">Factures Impayées</h1>
      <p class="text-text-light mt-2">Gestion des factures à relancer</p>
    </div>
    <button @click="refreshInvoices()" class="px-6 py-2 bg-secondary text-white rounded-lg hover:bg-opacity-90 transition-colors">
      ↻ Rafraîchir
    </button>
  </div>

  <!-- Tabs -->
  <div class="flex gap-4 border-b border-border">
    <button @click="activeTab = 'all'" 
            :class="activeTab === 'all' ? 'border-b-2 border-primary text-primary' : 'text-text-light'"
            class="pb-4 font-medium transition-colors">
      Toutes <span class="text-sm" x-text="`(${allInvoices.length})`"></span>
    </button>
    <button @click="activeTab = 'no-email'" 
            :class="activeTab === 'no-email' ? 'border-b-2 border-error text-error' : 'text-text-light'"
            class="pb-4 font-medium transition-colors">
      Sans Email <span class="text-sm" x-text="`(${noEmailInvoices.length})`"></span>
    </button>
  </div>

  <!-- Filters -->
  <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
    <input type="text"
           x-model="filters.search"
           @input="loadInvoices()"
           placeholder="Numéro facture, client..."
           class="px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
    
    <input type="number"
           x-model="filters.minAmount"
           @input="loadInvoices()"
           placeholder="Montant min"
           step="0.01"
           class="px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">

    <input type="date"
           x-model="filters.dateFrom"
           @change="loadInvoices()"
           class="px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">

    <select x-model="filters.payee" @change="loadInvoices()" class="px-4 py-2 border border-border rounded-lg">
      <option value="">Tous les payeurs</option>
      <option value="proprietaire">Propriétaire</option>
      <option value="notaire">Notaire</option>
      <option value="apporteur_affaire">Apporteur d'affaires</option>
    </select>
  </div>

  <!-- All Invoices Table -->
  <div x-show="activeTab === 'all'" class="bg-white rounded-lg shadow overflow-hidden">
    <table class="w-full">
      <thead class="bg-bg-light border-b border-border">
        <tr>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Facture</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Client</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Montant TTC</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Reste à Payer</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Échéance</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Payeur</th>
          <th class="px-6 py-3 text-right text-sm font-semibold text-text">Actions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-border">
        <template x-for="invoice in allInvoices" :key="invoice.id">
          <tr class="hover:bg-bg-light transition-colors">
            <td class="px-6 py-4 text-sm font-medium text-text" x-text="invoice.numero_facture"></td>
            <td class="px-6 py-4 text-sm text-text" x-text="invoice.proprietaire_prenom + ' ' + invoice.proprietaire_nom"></td>
            <td class="px-6 py-4 text-sm text-text" x-text="'€' + invoice.montant.toLocaleString('fr-FR')"></td>
            <td class="px-6 py-4 text-sm font-medium text-error" x-text="'€' + invoice.reste_a_payer.toLocaleString('fr-FR')"></td>
            <td class="px-6 py-4 text-sm text-text" x-text="new Date(invoice.date_echeance).toLocaleDateString('fr-FR')"></td>
            <td class="px-6 py-4 text-sm text-text-light" x-text="invoice.payeur"></td>
            <td class="px-6 py-4 text-right">
              <button @click="addToReminder(invoice)" class="text-primary hover:text-primary-dark text-sm">Relancer</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <div x-show="allInvoices.length === 0" class="text-center py-12">
      <p class="text-text-light">Aucune facture</p>
    </div>
  </div>

  <!-- No Email Table -->
  <div x-show="activeTab === 'no-email'" class="bg-white rounded-lg shadow overflow-hidden">
    <div class="p-4 bg-error bg-opacity-10 border-b border-error text-error text-sm">
      ⚠️ Ces factures ne peuvent pas être relancées par email - action manuelle requise
    </div>
    
    <table class="w-full">
      <thead class="bg-bg-light border-b border-border">
        <tr>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Facture</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Client</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Montant</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Payeur</th>
          <th class="px-6 py-3 text-left text-sm font-semibold text-text">Email Manquant</th>
          <th class="px-6 py-3 text-right text-sm font-semibold text-text">Actions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-border">
        <template x-for="invoice in noEmailInvoices" :key="invoice.id">
          <tr class="hover:bg-bg-light transition-colors">
            <td class="px-6 py-4 text-sm font-medium text-text" x-text="invoice.numero_facture"></td>
            <td class="px-6 py-4 text-sm text-text" x-text="invoice.proprietaire_prenom + ' ' + invoice.proprietaire_nom"></td>
            <td class="px-6 py-4 text-sm text-text" x-text="'€' + invoice.montant.toLocaleString('fr-FR')"></td>
            <td class="px-6 py-4 text-sm text-text-light" x-text="invoice.payeur"></td>
            <td class="px-6 py-4 text-sm">
              <span class="px-2 py-1 bg-error bg-opacity-10 text-error text-xs rounded" 
                    x-text="invoice.payeur === 'proprietaire' ? 'Propriétaire' : invoice.payeur === 'notaire' ? 'Notaire' : 'Apporteur'"></span>
            </td>
            <td class="px-6 py-4 text-right">
              <button @click="editInvoiceEmail(invoice)" class="text-secondary hover:text-secondary text-sm">Ajouter Email</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <div x-show="noEmailInvoices.length === 0" class="text-center py-12">
      <p class="text-text-light">Aucune facture sans email</p>
    </div>
  </div>

  <!-- Drawers -->
  {% include "relances/partials/add-email-drawer.html" %}
</div>
{% endblock %}
```

---

## **Composant Alpine.js**

```javascript
function relanceUnpaidInvoicesState() {
  return {
    activeTab: 'all',
    allInvoices: [],
    noEmailInvoices: [],
    filters: {
      search: '',
      minAmount: '',
      dateFrom: '',
      payee: ''
    },
    isLoading: true,
    showEmailDrawer: false,
    selectedInvoice: null,

    async loadInvoices() {
      this.isLoading = true;
      try {
        const params = new URLSearchParams(this.filters);
        const response = await fetch(`/api/relances/unpaid-invoices?${params}`);
        const data = await response.json();
        this.allInvoices = data.invoices;
        this.noEmailInvoices = data.invoices.filter(i => !i[i.payeur + '_email']);
      } catch (error) {
        console.error('Erreur chargement:', error);
      } finally {
        this.isLoading = false;
      }
    },

    async refreshInvoices() {
      try {
        await fetch('/api/relances/unpaid-invoices/refresh', { method: 'POST' });
        await this.loadInvoices();
      } catch (error) {
        console.error('Erreur rafraîchissement:', error);
      }
    },

    async addToReminder(invoice) {
      try {
        await fetch('/api/relances/add-invoice', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ invoice_id: invoice.id })
        });
        alert('Facture ajoutée à une relance');
      } catch (error) {
        console.error('Erreur ajout:', error);
      }
    },

    editInvoiceEmail(invoice) {
      this.selectedInvoice = invoice;
      this.showEmailDrawer = true;
    },

    init() {
      this.loadInvoices();
    }
  };
}
```
