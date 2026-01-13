# Modèles : Gestion des Commissions
**Fichier cible** : `app/blueprints/commissions/models.py` (backend) et `app/blueprints/commissions/static/js/*.js` (frontend)

---

## **Composants Alpine.js**

### `commissionsListState(initialStatus='valide')`
Gère la liste des commissions avec filtres.

```javascript
/**
 * Logique de la liste des commissions.
 * @param {String} initialStatus - Statut initial ('valide', 'conflit', 'archive')
 * @returns {Object}
 * @property {Array} commissions - Liste affichée
 * @property {String} status - Filtre actif
 * @property {Object} filters - Filtres additionnels
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} loadCommissions - Recharge la liste
 * @property {Function} setStatus - Change le filtre statut
 * @property {Function} archiveCommission - Archive une commission
 * @property {Function} settleCommission - Règle une commission
 */
function commissionsListState(initialStatus = 'valide') {
  return {
    commissions: [],
    status: initialStatus,
    filters: {
      search: '',
      dateFrom: '',
      dateTo: ''
    },
    isLoading: false,
    
    async loadCommissions() {
      this.isLoading = true;
      try {
        const params = new URLSearchParams({
          status: this.status,
          search: this.filters.search
        });
        const response = await fetch(`/api/commissions?${params}`);
        const data = await response.json();
        this.commissions = data.commissions;
      } catch (error) {
        console.error('Erreur chargement:', error);
      } finally {
        this.isLoading = false;
      }
    },
    
    setStatus(status) {
      this.status = status;
      this.loadCommissions();
    },
    
    async archiveCommission(nfacture) {
      try {
        const response = await fetch(`/api/commissions/${nfacture}/archive`, {
          method: 'POST'
        });
        if (response.ok) {
          await this.loadCommissions();
        }
      } catch (error) {
        console.error('Erreur archivage:', error);
      }
    },
    
    async settleCommission(nfacture, dateReglement) {
      try {
        const response = await fetch(`/api/commissions/${nfacture}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ 
            date_reglement: dateReglement,
            statut: 'reglees'
          })
        });
        if (response.ok) {
          await this.loadCommissions();
        }
      } catch (error) {
        console.error('Erreur règlement:', error);
      }
    },
    
    init() {
      this.loadCommissions();
    }
  };
}
```

---

### `commissionDetailState(nfacture)`
Gère les détails et édition d'une commission.

```javascript
/**
 * Logique détail d'une commission.
 * @param {String} nfacture - Numéro de facture
 * @returns {Object}
 * @property {Object} commission - Données de la commission
 * @property {Boolean} isLoading - État de chargement
 * @property {Boolean} isEditing - Mode édition
 * @property {Function} loadCommission - Charge les détails
 * @property {Function} update - Met à jour la commission
 */
function commissionDetailState(nfacture) {
  return {
    commission: {},
    isLoading: true,
    isEditing: false,
    
    async loadCommission() {
      try {
        const response = await fetch(`/api/commissions/${nfacture}`);
        const data = await response.json();
        this.commission = data.commission;
      } catch (error) {
        console.error('Erreur chargement:', error);
      } finally {
        this.isLoading = false;
      }
    },
    
    async update(updates) {
      try {
        const response = await fetch(`/api/commissions/${nfacture}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(updates)
        });
        if (response.ok) {
          await this.loadCommission();
          this.isEditing = false;
        }
      } catch (error) {
        console.error('Erreur mise à jour:', error);
      }
    },
    
    init() {
      this.loadCommission();
    }
  };
}
```

---

### `commissionSplitState(nfacture)`
Gère la subdivision d'une commission.

```javascript
/**
 * Logique subdivision d'une commission.
 * @param {String} nfacture - Numéro de facture
 * @returns {Object}
 * @property {Array} subdivisions - Lignes subdivisées
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} split - Subdivise la commission
 */
function commissionSplitState(nfacture) {
  return {
    subdivisions: [],
    isLoading: false,
    
    async split(subdivisionData) {
      this.isLoading = true;
      try {
        const response = await fetch(`/api/commissions/${nfacture}/split`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(subdivisionData)
        });
        if (response.ok) {
          const data = await response.json();
          this.subdivisions = data.subdivisions;
        }
      } catch (error) {
        console.error('Erreur subdivision:', error);
      } finally {
        this.isLoading = false;
      }
    }
  };
}
```
