# Layout Principal de l'Application
**Version** : 1.0
**Statut** : En cours

---
## 1. Contexte
Le layout principal de l'application (`app-layout.html`) est utilisé pour toutes les pages nécessitant un dashboard avec une sidebar, une topbar et un espace de contenu. Ce layout est inspiré de Flowbite pour offrir une expérience utilisateur cohérente et professionnelle. Ce layout est utilisé par le blueprint `app` pour les routes principales de l'application.

## 2. Structure du Layout

### 2.1. Sidebar
- **Description** : La sidebar contient les liens de navigation principaux de l'application.
- **Composants Alpine.js** :
  - `sidebarState` : Gère l'état de la sidebar (ouvert/fermé).
- **Flux de Données** :
  1. L'utilisateur clique sur le bouton de toggle pour ouvrir/fermer la sidebar.
  2. La sidebar se masque sur les écrans mobiles et reste visible sur les écrans larges.
- **Règles Métier** :
  - La sidebar doit être visible par défaut sur les écrans larges (>= 1024px).
  - La sidebar doit être masquée par défaut sur les écrans mobiles (< 1024px).
  - Les liens de navigation doivent être mis à jour en fonction des permissions de l'utilisateur.

### 2.2. Topbar
- **Description** : La topbar contient les informations de l'utilisateur connecté et les notifications.
- **Composants Alpine.js** :
  - `topbarState` : Gère l'état de la topbar et les interactions utilisateur.
- **Flux de Données** :
  1. L'utilisateur clique sur son avatar pour accéder à un menu déroulant.
  2. L'utilisateur peut se déconnecter ou accéder à son profil.
  3. Les notifications sont affichées sous forme de badge.
- **Règles Métier** :
  - La topbar doit être visible en haut de la page à tout moment.
  - Les informations de l'utilisateur doivent être récupérées depuis Flask.
  - Les notifications doivent être mises à jour en temps réel.

### 2.3. Espace de Contenu
- **Description** : L'espace de contenu contient le contenu principal de la page.
- **Composants Alpine.js** :
  - `contentState` : Gère l'état du contenu principal.
- **Flux de Données** :
  1. Le contenu principal est chargé dynamiquement en fonction de la route.
  2. Les composants Alpine.js sont initialisés une fois le contenu chargé.
- **Règles Métier** :
  - L'espace de contenu doit s'adapter à la taille de l'écran.
  - Le contenu doit être chargé de manière asynchrone pour améliorer les performances.

### 2.4. Données du Layout
- **Description** : Les données du layout sont stockées dans la base de données `app.db` (PickleDB).
- **Collections** :
  - `navigation_links` : Stocke les liens de navigation.
  - `users` : Stocke les informations des utilisateurs.
  - `notifications` : Stocke les notifications des utilisateurs.

## 3. Composants Alpine.js

| Composant      | Rôle                                      | Props                     | Communication          |
|----------------|-------------------------------------------|---------------------------|-------------------------|
| sidebarState   | Gère l'état de la sidebar.                | Aucun                     | Appel parent via `$root`|
| topbarState    | Gère l'état de la topbar.                 | user: Object              | Appel parent via `$root`|
| contentState   | Gère l'état du contenu principal.         | Aucun                     | Appel parent via `$root`|

## 4. Flux de Données

### 4.1. Sidebar
1. Utilisateur → Clique sur le bouton de toggle → Sidebar s'ouvre/ferme.

### 4.2. Topbar
1. Utilisateur → Clique sur l'avatar → Menu déroulant s'ouvre.
2. Utilisateur → Clique sur "Déconnexion" → Redirection vers la page de login.

### 4.3. Espace de Contenu
1. Utilisateur → Accède à une route → Contenu principal est chargé.
2. Contenu principal → Initialise les composants Alpine.js.

## 5. Règles Métier

### 5.1. Sidebar
- La sidebar doit être visible par défaut sur les écrans larges.
- La sidebar doit être masquée par défaut sur les écrans mobiles.
- Les liens de navigation doivent être mis à jour en fonction des permissions de l'utilisateur.

### 5.2. Topbar
- La topbar doit être visible en haut de la page à tout moment.
- Les informations de l'utilisateur doivent être récupérées depuis Flask.
- Les notifications doivent être mises à jour en temps réel.

### 5.3. Espace de Contenu
- L'espace de contenu doit s'adapter à la taille de l'écran.
- Le contenu doit être chargé de manière asynchrone pour améliorer les performances.

## 6. Exemple de Données

### 6.1. Utilisateur
```json
{
  "id": 1,
  "username": "admin",
  "isAdmin": true,
  "notifications": [
    {
      "id": 1,
      "message": "Nouvelle notification",
      "read": false
    }
  ]
}
```

### 6.2. Liens de Navigation
```json
{
  "links": [
    {
      "id": 1,
      "label": "Tableau de bord",
      "url": "/dashboard",
      "icon": "home"
    },
    {
      "id": 2,
      "label": "Utilisateurs",
      "url": "/settings/team",
      "icon": "users"
    }
  ]
}
```

## 7. API Backend

### 7.1. Récupération des Informations de l'Utilisateur
- **Endpoint** : `GET /api/user/info`
  - **Réponse** : `{ "status": "success", "user": { "id": number, "username": string, "isAdmin": boolean, "notifications": Array } }`

### 7.2. Récupération des Liens de Navigation
- **Endpoint** : `GET /api/navigation/links`
  - **Réponse** : `{ "status": "success", "links": Array }`

## 8. Liens
- [Styleguide](utils/styleguide.md)
- [Scénarios Gherkin](specs/features/app_layout.feature)
- [Spécifications techniques](specs/_app/app_layout.html.spec)