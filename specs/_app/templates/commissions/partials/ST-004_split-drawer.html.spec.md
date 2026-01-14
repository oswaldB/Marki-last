# Partial : Split Drawer
**Fichier cible** : `app/templates/commissions/partials/split-drawer.html`

---

## **Description**
Drawer pour subdiviser une ligne de commission.

---

## **Structure HTML**
```html
<div x-show="showSplitDrawer" class="fixed inset-0 z-50">
  <!-- Backdrop -->
  <div class="absolute inset-0 bg-black bg-opacity-50" @click="showSplitDrawer = false"></div>

  <!-- Drawer -->
  <div class="absolute right-0 top-0 h-full w-96 bg-white shadow-2xl flex flex-col">
    <!-- Header -->
    <div class="flex items-center justify-between p-6 border-b border-border">
      <h2 class="text-xl font-bold text-text">Découper la Commission</h2>
      <button @click="showSplitDrawer = false" class="text-text-light hover:text-text">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Content -->
    <div class="flex-1 overflow-y-auto p-6 space-y-4">
      <!-- Commission Info -->
      <div class="p-4 bg-bg-light rounded-lg">
        <p class="text-sm text-text-light mb-1">Facture:</p>
        <p class="font-semibold text-text" x-text="selectedCommission?.nfacture"></p>
        <p class="text-sm text-text-light mt-3 mb-1">Montant TTC:</p>
        <p class="font-semibold text-text" x-text="'€' + selectedCommission?.montant_ttc.toLocaleString('fr-FR')"></p>
      </div>

      <!-- Subdivisions Form -->
      <div class="space-y-3">
        <label class="block text-sm font-medium text-text">Subdivisions:</label>
        <template x-for="(sub, index) in subdivisions" :key="index">
          <div class="space-y-2 p-3 bg-bg-light rounded-lg">
            <input type="text"
                   x-model="sub.intervenant"
                   placeholder="Intervenant"
                   class="w-full px-3 py-2 border border-border rounded text-sm">
            <input type="number"
                   x-model="sub.montant"
                   placeholder="Montant TTC"
                   step="0.01"
                   class="w-full px-3 py-2 border border-border rounded text-sm">
          </div>
        </template>
      </div>

      <!-- Add Subdivision Button -->
      <button @click="subdivisions.push({intervenant: '', montant: 0})"
              class="w-full px-3 py-2 border border-dashed border-primary text-primary text-sm font-medium rounded hover:bg-primary hover:bg-opacity-5 transition-colors">
        + Ajouter une ligne
      </button>
    </div>

    <!-- Footer -->
    <div class="p-6 border-t border-border flex gap-3">
      <button @click="showSplitDrawer = false" 
              class="flex-1 px-4 py-2 border border-border text-text rounded-lg hover:bg-bg-light transition-colors">
        Annuler
      </button>
      <button @click="split({subdivisions: subdivisions})" 
              :disabled="isLoading"
              class="flex-1 px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors disabled:opacity-50">
        Valider
      </button>
    </div>
  </div>
</div>
```
