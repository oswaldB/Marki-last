# API: Superadmin RESTful API
**Fichier** : app/blueprints/auth/routes.py
**Type** : API REST pour la gestion des admins

---
## Description
L'API Superadmin fournit des endpoints RESTful pour gérer les administrateurs via des requêtes HTTP. Conçue pour être utilisée avec Alpine.js et fetch().

## Endpoints API

### 1. GET /api/admins
**Récupérer la liste des admins**

**Réponse réussie (200 OK)**
```json
{
  "success": true,
  "admins": [
    {
      "id": 1,
      "username": "admin1",
      "name": "Administrateur 1",
      "isAdmin": true
    }
  ]
}
```

**Exemple d'utilisation avec fetch**
```javascript
fetch('/api/admins')
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      console.log('Admins:', data.admins);
    }
  });
```

### 2. POST /api/admins
**Créer un nouvel admin**

**Requête**
```json
{
  "username": "nouveau_admin",
  "password": "motdepasse_secure",
  "name": "Nouvel Administrateur"
}
```

**Réponse réussie (201 Created)**
```json
{
  "success": true,
  "admin": {
    "id": 2,
    "username": "nouveau_admin",
    "name": "Nouvel Administrateur",
    "isAdmin": true
  },
  "message": "Admin créé avec succès"
}
```

**Exemple avec fetch**
```javascript
fetch('/api/admins', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    username: 'nouveau_admin',
    password: 'motdepasse_secure',
    name: 'Nouvel Administrateur'
  })
})
.then(response => response.json())
.then(data => {
  if (data.success) {
    console.log('Admin créé:', data.admin);
  }
});
```

### 3. GET /api/admins/<id>
**Récupérer un admin spécifique**

**Réponse réussie (200 OK)**
```json
{
  "success": true,
  "admin": {
    "id": 1,
    "username": "admin1",
    "name": "Administrateur 1",
    "isAdmin": true
  }
}
```

### 4. PUT /api/admins/<id>
**Mettre à jour un admin**

**Requête**
```json
{
  "username": "admin_mis_a_jour",
  "password": "nouveau_motdepasse",
  "name": "Administrateur Mis à Jour"
}
```

**Réponse réussie (200 OK)**
```json
{
  "success": true,
  "admin": {
    "id": 1,
    "username": "admin_mis_a_jour",
    "name": "Administrateur Mis à Jour",
    "isAdmin": true
  },
  "message": "Admin mis à jour avec succès"
}
```

### 5. DELETE /api/admins/<id>
**Supprimer un admin**

**Réponse réussie (200 OK)**
```json
{
  "success": true,
  "message": "Admin supprimé avec succès"
}
```

## Gestion des Erreurs

### Erreurs communes

**401 Unauthorized**
```json
{
  "success": false,
  "error": "Non autorisé",
  "message": "Veuillez vous authentifier"
}
```

**404 Not Found**
```json
{
  "success": false,
  "error": "Non trouvé",
  "message": "Admin non trouvé"
}
```

**400 Bad Request**
```json
{
  "success": false,
  "error": "Requête invalide",
  "message": "Le champ username est requis"
}
```

**500 Internal Server Error**
```json
{
  "success": false,
  "error": "Erreur serveur",
  "message": "Une erreur est survenue"
}
```

## Authentification

### Middleware d'authentification
Toutes les requêtes API doivent inclure un en-tête d'authentification ou utiliser la session.

**Exemple avec session**
```javascript
// Vérifier l'authentification avant d'appeler l'API
if (!window.isAuthenticated) {
  window.location.href = '/superadmin/entrance';
  return;
}
```

## Intégration avec Alpine.js

### Exemple de composant Alpine.js
```html
<div x-data="adminsManager()" x-init="loadAdmins()">
  <template x-for="admin in admins" :key="admin.id">
    <div>
      <span x-text="admin.username"></span>
      <button @click="deleteAdmin(admin.id)">Supprimer</button>
    </div>
  </template>
</div>

<script>
function adminsManager() {
  return {
    admins: [],
    
    loadAdmins() {
      fetch('/api/admins')
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            this.admins = data.admins;
          }
        });
    },
    
    deleteAdmin(id) {
      if (confirm('Voulez-vous vraiment supprimer cet admin ?')) {
        fetch(`/api/admins/${id}`, { method: 'DELETE' })
          .then(response => response.json())
          .then(data => {
            if (data.success) {
              this.loadAdmins();
            }
          });
      }
    }
  };
}
</script>
```

## Bonnes Pratiques

### Côté Client
- Toujours gérer les erreurs des requêtes fetch
- Afficher des messages utilisateur clairs
- Utiliser des loaders pendant les requêtes
- Valider les données avant envoi

### Côté Serveur
- Valider toutes les entrées
- Utiliser des transactions pour les opérations critiques
- Journaliser les actions importantes
- Limiter le taux de requêtes

## Tests Requis

### Tests API
- Vérification de l'authentification
- Test de tous les endpoints CRUD
- Validation des réponses JSON
- Test des erreurs et codes HTTP

### Tests Frontend
- Test de l'affichage de la liste
- Test de la création d'admin
- Test de la mise à jour
- Test de la suppression
- Test des messages d'erreur

## Évolutions Futures
- Ajout de la pagination
- Recherche et filtrage
- Export des données
- Audit des actions
- Webhooks pour les événements