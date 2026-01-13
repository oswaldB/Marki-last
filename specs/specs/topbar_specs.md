# Topbar
**Version** : 1.0
**Statut** : En cours

---
## 1. Contexte
La topbar est un composant principal du layout `app-layout.html`. Elle contient les informations de l'utilisateur connecté et les notifications. La topbar est inspirée de Flowbite pour offrir une expérience utilisateur cohérente et professionnelle.

## 2. Structure de la Topbar

### 2.1. Informations de l'Utilisateur
- **Description** : Section affichant les informations de l'utilisateur connecté.
- **Composants Alpine.js** :
  - `userInfoState` : Gère l'état des informations de l'utilisateur.
- **Flux de Données** :
  1. Les informations de l'utilisateur sont récupérées depuis Flask.
  2. Les informations sont affichées dans la topbar.
  3. L'utilisateur peut cliquer sur son avatar pour accéder à un menu déroulant.
- **Règles Métier** :
  - Les informations de l'utilisateur doivent être mises à jour en temps réel.
  - L'avatar de l'utilisateur doit être affiché à côté de son nom.

### 2.2. Menu Déroulant
- **Description** : Menu déroulant pour accéder aux actions de l'utilisateur.
- **Composants Alpine.js** :
  - `userMenuState` : Gère l'état du menu déroulant.
- **Flux de Données** :
  1. L'utilisateur clique sur son avatar pour ouvrir le menu déroulant.
  2. Le menu déroulant affiche les actions disponibles (profil, déconnexion).
  3. L'utilisateur clique sur une action pour l'exécuter.
- **Règles Métier** :
  - Le menu déroulant doit être masqué par défaut.
  - Le menu déroulant doit s'ouvrir lorsque l'utilisateur clique sur son avatar.
  - Le menu déroulant doit se fermer lorsque l'utilisateur clique en dehors.

### 2.3. Notifications
- **Description** : Section affichant les notifications de l'utilisateur.
- **Composants Alpine.js** :
  - `notificationsState` : Gère l'état des notifications.
- **Flux de Données** :
  1. Les notifications sont récupérées depuis Flask.
  2. Les notifications sont affichées sous forme de badge.
  3. L'utilisateur peut cliquer sur le badge pour afficher la liste des notifications.
- **Règles Métier** :
  - Les notifications doivent être mises à jour en temps réel.
  - Le badge doit afficher le nombre de notifications non lues.
  - La liste des notifications doit être affichée lorsque l'utilisateur clique sur le badge.

### 2.4. Données de la Topbar
- **Description** : Les données de la topbar sont stockées dans la base de données `app.db` (PickleDB).
- **Collections** :
  - `users` : Stocke les informations des utilisateurs.
  - `notifications` : Stocke les notifications des utilisateurs.

## 3. Composants Alpine.js

| Composant            | Rôle                                      | Props                     | Communication          |
|----------------------|-------------------------------------------|---------------------------|-------------------------|
| userInfoState        | Gère l'état des informations de l'utilisateur. | user: Object              | Appel parent via `$root`|
| userMenuState        | Gère l'état du menu déroulant.            | Aucun                     | Appel parent via `$root`|
| notificationsState   | Gère l'état des notifications.            | notifications: Array      | Appel parent via `$root`|

## 4. Flux de Données

### 4.1. Informations de l'Utilisateur
1. Utilisateur → Accède à la page → Informations de l'utilisateur sont récupérées depuis Flask.
2. Informations de l'utilisateur → Affichées dans la topbar.
3. Utilisateur → Clique sur l'avatar → Menu déroulant s'ouvre.

### 4.2. Menu Déroulant
1. Utilisateur → Clique sur l'avatar → Menu déroulant s'ouvre.
2. Utilisateur → Clique sur une action → Action est exécutée.
3. Utilisateur → Clique en dehors → Menu déroulant se ferme.

### 4.3. Notifications
1. Utilisateur → Accède à la page → Notifications sont récupérées depuis Flask.
2. Notifications → Affichées sous forme de badge.
3. Utilisateur → Clique sur le badge → Liste des notifications s'affiche.

## 5. Règles Métier

### 5.1. Informations de l'Utilisateur
- Les informations de l'utilisateur doivent être mises à jour en temps réel.
- L'avatar de l'utilisateur doit être affiché à côté de son nom.

### 5.2. Menu Déroulant
- Le menu déroulant doit être masqué par défaut.
- Le menu déroulant doit s'ouvrir lorsque l'utilisateur clique sur son avatar.
- Le menu déroulant doit se fermer lorsque l'utilisateur clique en dehors.

### 5.3. Notifications
- Les notifications doivent être mises à jour en temps réel.
- Le badge doit afficher le nombre de notifications non lues.
- La liste des notifications doit être affichée lorsque l'utilisateur clique sur le badge.

## 6. Exemple de Données

### 6.1. Utilisateur
```json
{
  "id": 1,
  "username": "admin",
  "avatar": "/path/to/avatar.jpg",
  "isAdmin": true
}
```

### 6.2. Notifications
```json
{
  "notifications": [
    {
      "id": 1,
      "message": "Nouvelle notification",
      "read": false,
      "createdAt": "2023-01-01T00:00:00Z"
    },
    {
      "id": 2,
      "message": "Autre notification",
      "read": true,
      "createdAt": "2023-01-02T00:00:00Z"
    }
  ]
}
```

## 7. API Backend

### 7.1. Récupération des Informations de l'Utilisateur
- **Endpoint** : `GET /api/user/info`
  - **Réponse** : `{ "status": "success", "user": { "id": number, "username": string, "avatar": string, "isAdmin": boolean } }`

### 7.2. Récupération des Notifications
- **Endpoint** : `GET /api/user/notifications`
  - **Réponse** : `{ "status": "success", "notifications": Array }`

### 7.3. Marquer une Notification comme Lue
- **Endpoint** : `POST /api/user/notifications/read`
  - **Payload** : `{ "notificationId": number }`
  - **Réponse** : `{ "status": "success" }`

## 8. Liens
- [Styleguide](utils/styleguide.md)
- [Scénarios Gherkin](specs/features/topbar.feature)
- [Spécifications techniques](specs/_app/topbar.html.spec)