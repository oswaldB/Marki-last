# Partial : Relance - Detail Modal
**Fichier cible** : `app/templates/relances/partials/detail-modal.html`

---

## **Description**
Modal pour visualiser les détails d'une relance (contenu, destinataire, statut).

---

## **Structure HTML**
```html
<div x-show="showDetailModal" class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center" @click.away="showDetailModal = false">
  <div class="bg-white rounded-lg shadow-2xl max-w-2xl w-full mx-4" @click.stop>
    <!-- Header -->
    <div class="flex items-center justify-between p-6 border-b border-border">
      <h2 class="text-xl font-bold text-text">Détails de la Relance</h2>
      <button @click="showDetailModal = false" class="text-text-light hover:text-text">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    <!-- Content -->
    <div class="p-6 space-y-6">
      <!-- Status Badge -->
      <div class="flex items-center gap-3">
        <p class="text-sm font-medium text-text-light">Statut:</p>
        <span class="px-3 py-1 rounded-full text-xs font-medium"
              :class="{
                'bg-secondary bg-opacity-20 text-secondary': selectedReminder?.statut === 'pending',
                'bg-success bg-opacity-20 text-success': selectedReminder?.statut === 'sent',
                'bg-error bg-opacity-20 text-error': selectedReminder?.statut === 'failed'
              }"
              x-text="selectedReminder?.statut"></span>
      </div>

      <!-- Recipient Info -->
      <div class="grid grid-cols-2 gap-4 pb-4 border-b border-border">
        <div>
          <p class="text-sm text-text-light mb-1">Destinataire:</p>
          <p class="font-medium text-text" x-text="selectedReminder?.recipient"></p>
        </div>
        <div>
          <p class="text-sm text-text-light mb-1">Email:</p>
          <p class="font-medium text-text" x-text="selectedReminder?.email"></p>
        </div>
      </div>

      <!-- Invoice Info -->
      <div class="grid grid-cols-2 gap-4 pb-4 border-b border-border">
        <div>
          <p class="text-sm text-text-light mb-1">Facture:</p>
          <p class="font-medium text-text" x-text="selectedReminder?.facture_numero"></p>
        </div>
        <div>
          <p class="text-sm text-text-light mb-1">Montant:</p>
          <p class="font-medium text-text" x-text="'€' + selectedReminder?.montant.toLocaleString('fr-FR')"></p>
        </div>
      </div>

      <!-- Message Content -->
      <div>
        <p class="text-sm text-text-light mb-3 font-medium">Contenu du message:</p>
        <div class="bg-bg-light rounded-lg p-4 text-text whitespace-pre-wrap" x-text="selectedReminder?.content"></div>
      </div>

      <!-- Dates -->
      <div class="grid grid-cols-2 gap-4">
        <div>
          <p class="text-sm text-text-light mb-1">Date d'envoi:</p>
          <p class="font-medium text-text" x-text="new Date(selectedReminder?.date).toLocaleString('fr-FR')"></p>
        </div>
        <div>
          <p class="text-sm text-text-light mb-1">Date d'ouverture:</p>
          <p class="font-medium text-text" x-text="selectedReminder?.open_date ? new Date(selectedReminder.open_date).toLocaleString('fr-FR') : '-'"></p>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="p-6 border-t border-border flex justify-end">
      <button @click="showDetailModal = false" 
              class="px-4 py-2 border border-border text-text rounded-lg hover:bg-bg-light transition-colors">
        Fermer
      </button>
    </div>
  </div>
</div>
```
