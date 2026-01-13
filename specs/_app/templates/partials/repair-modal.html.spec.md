# Partial : Repair Modal
**Fichier cible** : `app/templates/commissions/partials/repair-modal.html`

---

## **Description**
Modal pour afficher la facture PDF en cas de conflit.

---

## **Structure HTML**
```html
<div x-show="showRepairModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center" @click.away="showRepairModal = false">
  <div class="bg-white rounded-lg shadow-2xl max-w-4xl w-full mx-4" @click.stop>
    <!-- Header -->
    <div class="flex items-center justify-between p-6 border-b border-border">
      <h2 class="text-xl font-bold text-text">Réparation - <span x-text="selectedCommission?.nfacture"></span></h2>
      <button @click="showRepairModal = false" class="text-text-light hover:text-text">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Content -->
    <div class="p-6">
      <!-- Conflict Details -->
      <div class="mb-6 p-4 bg-error bg-opacity-10 border border-error rounded-lg">
        <p class="text-error text-sm font-medium mb-2">Détails du conflit:</p>
        <p class="text-text" x-text="selectedCommission?.conflit_detail"></p>
      </div>

      <!-- PDF Viewer -->
      <div class="bg-bg-light rounded-lg h-96 flex items-center justify-center">
        <iframe :src="'/api/get-file?url=' + encodeURIComponent(selectedCommission?.lien_facture || '')"
                class="w-full h-full rounded-lg"
                title="Facture PDF"></iframe>
      </div>
    </div>

    <!-- Footer -->
    <div class="p-6 border-t border-border flex justify-end gap-3">
      <button @click="showRepairModal = false" 
              class="px-4 py-2 border border-border text-text rounded-lg hover:bg-bg-light transition-colors">
        Fermer
      </button>
    </div>
  </div>
</div>
```
