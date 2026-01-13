# Application Principale
**Version** : 1.0
**Statut** : En cours

---
## 1. Contexte
Le blueprint `app` contient les routes principales de l'application, y compris le tableau de bord et les pages principales. Ce blueprint utilise le layout `app-layout.html` pour offrir une expérience utilisateur cohérente et professionnelle.

## 2. Routes

### 2.1. Tableau de Bord (`/dashboard`)
- **Description** : Page principale de l'application affichant un tableau de bord avec des statistiques et des informations générales.
- **Composants Alpine.js** :
  - `dashboardState` : Gère l'état du tableau de bord.
- **Flux de Données** :
  1. L'utilisateur accède à la page `/dashboard`.
  2. Flask renvoie les données nécessaires pour le tableau de bord.
  3. Les données sont affichées dans le tableau de bord.
- **Règles Métier** :
  - Le tableau de bord doit être accessible à tous les utilisateurs connectés.
  - Les données doivent être mises à jour en temps réel.

### 2.2. Profil de l'Utilisateur (`/profile`)
- **Description** : Page affichant les informations de profil de l'utilisateur connecté.
- **Composants Alpine.js** :
  - `profileState` : Gère l'état de la page de profil.
- **Flux de Données** :
  1. L'utilisateur accède à la page `/profile`.
  2. Flask renvoie les informations de l'utilisateur.
  3. Les informations sont affichées dans la page de profil.
- **Règles Métier** :
  - La page de profil doit être accessible uniquement à l'utilisateur connecté.
  - Les informations doivent être mises à jour en temps réel.

## 3. Composants Alpine.js

| Composant      | Rôle                                      | Props                     | Communication          |
|----------------|-------------------------------------------|---------------------------|-------------------------|
| dashboardState | Gère l'état du tableau de bord.           | Aucun                     | Appel parent via `$root`|
| profileState   | Gère l'état de la page de profil.         | user: Object              | Appel parent via `$root`|

## 4. Flux de Données

### 4.1. Tableau de Bord
1. Utilisateur → Accède à `/dashboard` → Tableau de bord est chargé.
2. Tableau de bord → Récupère les données depuis Flask.
3. Tableau de bord → Affiche les données.

### 4.2. Profil de l'Utilisateur
1. Utilisateur → Accède à `/profile` → Page de profil est chargée.
2. Page de profil → Récupère les informations de l'utilisateur depuis Flask.
3. Page de profil → Affiche les informations.

## 5. Règles Métier

### 5.1. Tableau de Bord
- Le tableau de bord doit être accessible à tous les utilisateurs connectés.
- Les données doivent être mises à jour en temps réel.

### 5.2. Profil de l'Utilisateur
- La page de profil doit être accessible uniquement à l'utilisateur connecté.
- Les informations doivent être mises à jour en temps réel.

## 6. Exemple de Données

### 6.1. Utilisateur
```json
{
  "id": 1,
  "username": "admin",
  "email": "admin@example.com",
  "createdAt": "2023-01-01T00:00:00Z"
}
```

### 6.2. Statistiques du Tableau de Bord
```json
{
  "stats": {
    "totalUsers": 10,
    "activeUsers": 5,
    "totalRevenue": 1000.00
  }
}
```

## 7. API Backend

### 7.1. Récupération des Informations de l'Utilisateur
- **Endpoint** : `GET /api/user/info`
  - **Réponse** : `{ "status": "success", "user": { "id": number, "username": string, "email": string, "createdAt": string } }`

### 7.2. Récupération des Statistiques du Tableau de Bord
- **Endpoint** : `GET /api/dashboard/stats`
  - **Réponse** : `{ "status": "success", "stats": { "totalUsers": number, "activeUsers": number, "totalRevenue": number } }`

## 8. Liens
- [Styleguide](utils/styleguide.md)
- [Scénarios Gherkin](specs/features/app.feature)
- [Spécifications techniques](specs/_app/app.html.spec)