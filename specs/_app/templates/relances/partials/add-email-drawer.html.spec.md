# Partial : Relance - Add Email Drawer
**Fichier cible** : `app/templates/relances/partials/add-email-drawer.html`

---

## **Description**
Drawer pour ajouter/modifier l'email d'une facture impayée.

---

## **Structure HTML**
```html
<div x-show="showEmailDrawer" class="fixed inset-0 z-50">
  <!-- Backdrop -->
  <div class="absolute inset-0 bg-black bg-opacity-50" @click="showEmailDrawer = false"></div>

  <!-- Drawer -->
  <div class="absolute right-0 top-0 h-full w-96 bg-white shadow-2xl flex flex-col">
    <!-- Header -->
    <div class="flex items-center justify-between p-6 border-b border-border">
      <h2 class="text-xl font-bold text-text">Ajouter Email</h2>
      <button @click="showEmailDrawer = false" class="text-text-light hover:text-text">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Content -->
    <div class="flex-1 overflow-y-auto p-6 space-y-4">
      <!-- Invoice Info -->
      <div class="p-4 bg-bg-light rounded-lg space-y-2">
        <p class="text-sm text-text-light">Facture:</p>
        <p class="font-semibold text-text" x-text="selectedInvoice?.numero_facture"></p>
        <p class="text-sm text-text-light mt-3">Client:</p>
        <p class="font-semibold text-text" x-text="selectedInvoice?.proprietaire_prenom + ' ' + selectedInvoice?.proprietaire_nom"></p>
        <p class="text-sm text-text-light mt-3">Payeur responsable:</p>
        <p class="font-semibold text-text" x-text="selectedInvoice?.payeur"></p>
      </div>

      <!-- Email Inputs -->
      <div class="space-y-4">
        <div x-show="selectedInvoice?.payeur === 'proprietaire' || !selectedInvoice?.proprietaire_email">
          <label class="block text-sm font-medium text-text mb-2">Email Propriétaire:</label>
          <input type="email" 
                 x-model="proprietaire_email"
                 placeholder="email@example.com"
                 class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
        </div>

        <div x-show="selectedInvoice?.payeur === 'notaire' || !selectedInvoice?.notaire_email">
          <label class="block text-sm font-medium text-text mb-2">Email Notaire:</label>
          <input type="email" 
                 x-model="notaire_email"
                 placeholder="email@example.com"
                 class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
        </div>

        <div x-show="selectedInvoice?.payeur === 'apporteur_affaire' || !selectedInvoice?.apporteur_affaire_email">
          <label class="block text-sm font-medium text-text mb-2">Email Apporteur d'affaires:</label>
          <input type="email" 
                 x-model="apporteur_affaire_email"
                 placeholder="email@example.com"
                 class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="p-6 border-t border-border flex gap-3">
      <button @click="showEmailDrawer = false" 
              class="flex-1 px-4 py-2 border border-border text-text rounded-lg hover:bg-bg-light transition-colors">
        Annuler
      </button>
      <button @click="saveEmail()" 
              :disabled="isSaving"
              class="flex-1 px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors disabled:opacity-50">
        <span x-show="!isSaving">Enregistrer</span>
        <span x-show="isSaving">Sauvegarde...</span>
      </button>
    </div>
  </div>
</div>

<script>
  function relanceEmailDrawerState() {
    return {
      proprietaire_email: '',
      notaire_email: '',
      apporteur_affaire_email: '',
      isSaving: false,

      async saveEmail() {
        this.isSaving = true;
        try {
          const updates = {};
          if (this.proprietaire_email) updates.proprietaire_email = this.proprietaire_email;
          if (this.notaire_email) updates.notaire_email = this.notaire_email;
          if (this.apporteur_affaire_email) updates.apporteur_affaire_email = this.apporteur_affaire_email;

          await fetch(`/api/relances/invoices/${this.selectedInvoice.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updates)
          });
          
          this.showEmailDrawer = false;
          location.reload();
        } catch (error) {
          console.error('Erreur sauvegarde:', error);
        } finally {
          this.isSaving = false;
        }
      }
    };
  }
</script>
```
