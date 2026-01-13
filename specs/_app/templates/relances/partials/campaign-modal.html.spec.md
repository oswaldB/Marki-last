# Partial : Relance - Campaign Modal
**Fichier cible** : `app/templates/relances/partials/campaign-modal.html`

---

## **Description**
Modal pour créer ou éditer une campagne de relance avec critères et séquences.

---

## **Structure HTML**
```html
<div x-show="showCreateModal || showEditModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center overflow-y-auto" @click.away="showCreateModal = false; showEditModal = false;">
  <div class="bg-white rounded-lg shadow-2xl max-w-4xl w-full mx-4 my-8" @click.stop x-data="relanceCampaignFormState(selectedCampaign)">
    <!-- Header -->
    <div class="flex items-center justify-between p-6 border-b border-border">
      <h2 class="text-xl font-bold text-text" x-text="selectedCampaign ? 'Éditer la Campagne' : 'Nouvelle Campagne'"></h2>
      <button @click="showCreateModal = false; showEditModal = false;" class="text-text-light hover:text-text">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Content -->
    <div class="p-6 space-y-6">
      <!-- Basic Info -->
      <div class="space-y-4">
        <h3 class="text-lg font-semibold text-text">Informations Générales</h3>
        
        <div>
          <label class="block text-sm font-medium text-text mb-2">Nom de la campagne:</label>
          <input type="text"
                 x-model="form.nom"
                 placeholder="ex: Relance 30 jours"
                 class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
        </div>

        <div>
          <label class="block text-sm font-medium text-text mb-2">Description:</label>
          <textarea x-model="form.description"
                    rows="2"
                    placeholder="Description optionnelle..."
                    class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"></textarea>
        </div>
      </div>

      <!-- Criteria -->
      <div class="border-t border-border pt-6 space-y-4">
        <h3 class="text-lg font-semibold text-text">Critères de Sélection</h3>
        
        <div class="space-y-3">
          <label class="flex items-center">
            <input type="radio" x-model="form.selection_type" value="automatic" class="mr-2">
            <span class="text-sm text-text">Sélection Automatique</span>
          </label>
          
          <template x-if="form.selection_type === 'automatic'">
            <div class="ml-6 space-y-3 p-4 bg-bg-light rounded-lg">
              <div>
                <label class="block text-sm font-medium text-text mb-2">Montant minimum:</label>
                <input type="number" x-model="form.min_amount" step="0.01" class="w-full px-4 py-2 border border-border rounded-lg text-sm">
              </div>
              <div>
                <label class="block text-sm font-medium text-text mb-2">Jours après échéance:</label>
                <input type="number" x-model="form.days_overdue" class="w-full px-4 py-2 border border-border rounded-lg text-sm">
              </div>
            </div>
          </template>

          <label class="flex items-center">
            <input type="radio" x-model="form.selection_type" value="manual" class="mr-2">
            <span class="text-sm text-text">Sélection Manuelle</span>
          </label>
        </div>
      </div>

      <!-- Sequence -->
      <div class="border-t border-border pt-6 space-y-4">
        <h3 class="text-lg font-semibold text-text">Séquence d'Emails</h3>
        
        <div class="space-y-3">
          <template x-for="(step, index) in form.sequence" :key="index">
            <div class="p-4 bg-bg-light rounded-lg space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="font-medium text-text">Étape <span x-text="index + 1"></span></h4>
                <button @click="form.sequence.splice(index, 1)" type="button" class="text-error hover:text-error text-sm">
                  Supprimer
                </button>
              </div>

              <div>
                <label class="block text-sm font-medium text-text mb-2">Délai (en jours):</label>
                <input type="number" x-model="step.delay" class="w-full px-3 py-2 border border-border rounded text-sm">
              </div>

              <div>
                <label class="block text-sm font-medium text-text mb-2">Objet de l'email:</label>
                <input type="text" x-model="step.subject" placeholder="ex: Rappel facture {{numero_facture}}" class="w-full px-3 py-2 border border-border rounded text-sm">
              </div>

              <div>
                <label class="block text-sm font-medium text-text mb-2">Contenu:</label>
                <textarea x-model="step.content" rows="4" class="w-full px-3 py-2 border border-border rounded text-sm font-mono"></textarea>
              </div>
            </div>
          </template>

          <button @click="form.sequence.push({delay: 0, subject: '', content: ''})" type="button" class="w-full px-3 py-2 border border-dashed border-primary text-primary rounded text-sm hover:bg-primary hover:bg-opacity-5 transition-colors">
            + Ajouter une étape
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="p-6 border-t border-border flex justify-end gap-3">
      <button @click="showCreateModal = false; showEditModal = false;" class="px-4 py-2 border border-border text-text rounded-lg hover:bg-bg-light transition-colors">
        Annuler
      </button>
      <button @click="saveCampaign()" 
              :disabled="isSaving"
              class="px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors disabled:opacity-50">
        <span x-show="!isSaving">Enregistrer</span>
        <span x-show="isSaving">Sauvegarde...</span>
      </button>
    </div>
  </div>
</div>

<script>
  function relanceCampaignFormState(existingCampaign) {
    return {
      form: existingCampaign ? { ...existingCampaign } : {
        nom: '',
        description: '',
        selection_type: 'automatic',
        min_amount: 0,
        days_overdue: 30,
        sequence: [{ delay: 0, subject: '', content: '' }]
      },
      isSaving: false,

      async saveCampaign() {
        this.isSaving = true;
        try {
          const url = existingCampaign ? `/api/relances/campaigns/${existingCampaign.id}` : '/api/relances/campaigns';
          const method = existingCampaign ? 'PUT' : 'POST';
          
          await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.form)
          });
          
          window.location.reload();
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
