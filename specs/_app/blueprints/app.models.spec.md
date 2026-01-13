# Modèles : Application Principale
**Fichier cible** : `app/blueprints/app/models.py`

---

## **Composants Alpine.js**

### `dashboardState()`
Gère l'état du tableau de bord.

```javascript
/**
 * Logique du tableau de bord.
 * @returns {Object}
 * @property {Object} stats - Statistiques affichées
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} loadStats - Charge les statistiques
 */
function dashboardState() {
  return {
    stats: {
      totalUsers: 0,
      activeUsers: 0,
      totalRevenue: 0.00
    },
    isLoading: true,
    
    async loadStats() {
      try {
        const response = await fetch('/api/dashboard/stats');
        const data = await response.json();
        this.stats = data.stats;
      } catch (error) {
        console.error('Erreur chargement stats:', error);
      } finally {
        this.isLoading = false;
      }
    },
    
    init() {
      this.loadStats();
    }
  };
}
```

---

### `profileState()`
Gère l'état du profil utilisateur.

```javascript
/**
 * Logique du profil utilisateur.
 * @returns {Object}
 * @property {Object} user - Données utilisateur
 * @property {Boolean} isLoading - État de chargement
 * @property {Function} loadUser - Charge les infos utilisateur
 */
function profileState() {
  return {
    user: {
      id: null,
      username: '',
      email: '',
      createdAt: ''
    },
    isLoading: true,
    
    async loadUser() {
      try {
        const response = await fetch('/api/user/info');
        const data = await response.json();
        this.user = data.user;
      } catch (error) {
        console.error('Erreur chargement profil:', error);
      } finally {
        this.isLoading = false;
      }
    },
    
    init() {
      this.loadUser();
    }
  };
}
```
