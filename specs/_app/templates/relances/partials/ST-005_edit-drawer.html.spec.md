# Partial : Relance - Edit Drawer
**Fichier cible** : `app/templates/relances/partials/edit-drawer.html`

---

## **Description**
Drawer pour modifier le contenu d'une relance (message, etc.).

---

## **Structure HTML**
```html
<div x-show="showEditDrawer" class="fixed inset-0 z-50">
  <!-- Backdrop -->
  <div class="absolute inset-0 bg-black bg-opacity-50" @click="showEditDrawer = false"></div>

  <!-- Drawer -->
  <div class="absolute right-0 top-0 h-full w-2/3 bg-white shadow-2xl flex flex-col overflow-y-auto">
    <!-- Header -->
    <div class="flex items-center justify-between p-6 border-b border-border sticky top-0 bg-white">
      <h2 class="text-xl font-bold text-text">Modifier le Message</h2>
      <button @click="showEditDrawer = false" class="text-text-light hover:text-text">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Content -->
    <div class="flex-1 p-6 space-y-6">
      <!-- Info -->
      <div class="p-4 bg-bg-light rounded-lg">
        <p class="text-sm text-text-light mb-2">Facture:</p>
        <p class="font-semibold text-text" x-text="selectedReminder?.facture_numero"></p>
        <p class="text-sm text-text-light mt-3 mb-2">Destinataire:</p>
        <p class="font-semibold text-text" x-text="selectedReminder?.recipient"></p>
      </div>

      <!-- Message Editor -->
      <div>
        <label class="block text-sm font-medium text-text mb-3">Contenu du message:</label>
        <textarea x-model="editContent"
                  rows="12"
                  class="w-full px-4 py-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent font-mono text-sm"
                  placeholder="Entrez le contenu du message..."></textarea>
        <p class="text-xs text-text-light mt-2">
          Variables disponibles: <code>{{nom}}</code>, <code>{{montant}}</code>, <code>{{date_echeance}}</code>
        </p>
      </div>

      <!-- AI Generation -->
      <div class="border-t border-border pt-6">
        <h3 class="text-sm font-semibold text-text mb-4">Générer avec ChatGPT</h3>
        <div class="space-y-3">
          <textarea x-model="aiPrompt"
                    rows="4"
                    placeholder="Décrivez le style du message à générer..."
                    class="w-full px-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent text-sm"></textarea>
          <button @click="generateWithAI()"
                  :disabled="isGenerating"
                  class="w-full px-4 py-2 bg-secondary text-white rounded-lg hover:bg-opacity-90 transition-colors disabled:opacity-50 text-sm">
            <span x-show="!isGenerating">Générer un message</span>
            <span x-show="isGenerating">Génération en cours...</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="p-6 border-t border-border flex gap-3 sticky bottom-0 bg-white">
      <button @click="showEditDrawer = false" 
              class="flex-1 px-4 py-2 border border-border text-text rounded-lg hover:bg-bg-light transition-colors">
        Annuler
      </button>
      <button @click="saveMessage()" 
              :disabled="isSaving"
              class="flex-1 px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors disabled:opacity-50">
        <span x-show="!isSaving">Enregistrer</span>
        <span x-show="isSaving">Sauvegarde...</span>
      </button>
    </div>
  </div>
</div>

<script>
  function relanceEditDrawerState() {
    return {
      editContent: '',
      aiPrompt: '',
      isGenerating: false,
      isSaving: false,

      async generateWithAI() {
        this.isGenerating = true;
        try {
          const response = await fetch('/api/relances/generate-ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              prompt: this.aiPrompt,
              variables: ['nom', 'montant', 'date_echeance']
            })
          });
          const data = await response.json();
          this.editContent = data.message;
        } catch (error) {
          console.error('Erreur génération:', error);
        } finally {
          this.isGenerating = false;
        }
      },

      async saveMessage() {
        this.isSaving = true;
        try {
          await fetch(`/api/relances/${this.selectedReminder.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content: this.editContent })
          });
          this.showEditDrawer = false;
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
