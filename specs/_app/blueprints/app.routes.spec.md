# Routes : Application Principale
**Fichier cible** : `app/blueprints/app/routes.py`

---

## **Endpoints**

| URL | Méthode | Paramètres | Retour | Description |
|-----|---------|-----------|--------|-------------|
| `/dashboard` | GET | - | HTML | Page principale du tableau de bord |
| `/profile` | GET | - | HTML | Profil de l'utilisateur connecté |
| `/api/user/info` | GET | - | JSON | Informations de l'utilisateur |
| `/api/dashboard/stats` | GET | - | JSON | Statistiques du tableau de bord |

---

## **Description des Routes**

### `/dashboard` (GET)
Affiche la page principale avec un tableau de bord.

**Template** : `app/dashboard.html`
**Données requises** :
- Statistiques (utilisateurs, revenus, etc.)
- Informations de session

**Réponse** : HTML du tableau de bord

---

### `/profile` (GET)
Affiche le profil de l'utilisateur connecté.

**Template** : `app/profile.html`
**Données requises** :
- Informations utilisateur (id, username, email, createdAt)

**Réponse** : HTML du profil

---

### `/api/user/info` (GET)
API pour récupérer les informations de l'utilisateur.

**Réponse** :
```json
{
  "status": "success",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "createdAt": "2023-01-01T00:00:00Z"
  }
}
```

**Codes d'erreur** :
- `401` : Utilisateur non authentifié
- `500` : Erreur serveur

---

### `/api/dashboard/stats` (GET)
API pour récupérer les statistiques du tableau de bord.

**Réponse** :
```json
{
  "status": "success",
  "stats": {
    "totalUsers": 10,
    "activeUsers": 5,
    "totalRevenue": 1000.00
  }
}
```

**Codes d'erreur** :
- `401` : Utilisateur non authentifié
- `500` : Erreur serveur
