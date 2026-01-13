# Sidebar
**Version** : 1.0
**Statut** : En cours

---
## 1. Contexte
La sidebar est un composant principal du layout `app-layout.html`. Elle contient les liens de navigation principaux de l'application et est inspirée de Flowbite pour offrir une expérience utilisateur cohérente et professionnelle.

## 2. Structure de la Sidebar

### 2.1. Toggle Sidebar
- **Description** : Bouton pour ouvrir/fermer la sidebar sur les écrans mobiles.
- **Composants Alpine.js** :
  - `sidebarToggleState` : Gère l'état du bouton de toggle.
- **Flux de Données** :
  1. L'utilisateur clique sur le bouton de toggle.
  2. La sidebar s'ouvre ou se ferme en fonction de son état actuel.
- **Règles Métier** :
  - Le bouton de toggle doit être visible uniquement sur les écrans mobiles (< 1024px).
  - Le bouton de toggle doit être masqué sur les écrans larges (>= 1024px).

### 2.2. Liens de Navigation
- **Description** : Liste des liens de navigation principaux.
- **Composants Alpine.js** :
  - `navigationLinksState` : Gère l'état des liens de navigation.
- **Flux de Données** :
  1. Les liens de navigation sont récupérés depuis Flask.
  2. Les liens sont affichés dans la sidebar.
  3. L'utilisateur clique sur un lien pour naviguer vers la page correspondante.
- **Règles Métier** :
  - Les liens de navigation doivent être mis à jour en fonction des permissions de l'utilisateur.
  - Les liens doivent être affichés sous forme de liste verticale.
  - Les liens actifs doivent être mis en évidence.

### 2.3. Footer de la Sidebar
- **Description** : Section en bas de la sidebar contenant des informations supplémentaires.
- **Composants Alpine.js** :
  - `sidebarFooterState` : Gère l'état du footer de la sidebar.
- **Flux de Données** :
  1. Le footer de la sidebar est affiché en bas de la sidebar.
  2. Le footer contient des informations supplémentaires comme la version de l'application.
- **Règles Métier** :
  - Le footer de la sidebar doit être visible en bas de la sidebar.
  - Le footer doit contenir des informations supplémentaires comme la version de l'application.

### 2.4. Données de la Sidebar
- **Description** : Les données de la sidebar sont stockées dans la base de données `app.db` (PickleDB).
- **Collections** :
  - `navigation_links` : Stocke les liens de navigation.
  - `sidebar_footer` : Stocke les informations du footer.

## 3. Composants Alpine.js

| Composant               | Rôle                                      | Props                     | Communication          |
|-------------------------|-------------------------------------------|---------------------------|-------------------------|
| sidebarToggleState      | Gère l'état du bouton de toggle.          | Aucun                     | Appel parent via `$root`|
| navigationLinksState    | Gère l'état des liens de navigation.      | links: Array              | Appel parent via `$root`|
| sidebarFooterState      | Gère l'état du footer de la sidebar.      | Aucun                     | Appel parent via `$root`|

## 4. Flux de Données

### 4.1. Toggle Sidebar
1. Utilisateur → Clique sur le bouton de toggle → Sidebar s'ouvre/ferme.

### 4.2. Liens de Navigation
1. Utilisateur → Accède à la page → Liens de navigation sont récupérés depuis Flask.
2. Liens de navigation → Affichés dans la sidebar.
3. Utilisateur → Clique sur un lien → Navigation vers la page correspondante.

### 4.3. Footer de la Sidebar
1. Utilisateur → Accède à la page → Footer de la sidebar est affiché.

## 5. Règles Métier

### 5.1. Toggle Sidebar
- Le bouton de toggle doit être visible uniquement sur les écrans mobiles.
- Le bouton de toggle doit être masqué sur les écrans larges.

### 5.2. Liens de Navigation
- Les liens de navigation doivent être mis à jour en fonction des permissions de l'utilisateur.
- Les liens doivent être affichés sous forme de liste verticale.
- Les liens actifs doivent être mis en évidence.

### 5.3. Footer de la Sidebar
- Le footer de la sidebar doit être visible en bas de la sidebar.
- Le footer doit contenir des informations supplémentaires comme la version de l'application.

## 6. Exemple de Données

### 6.1. Liens de Navigation
```json
{
  "links": [
    {
      "id": 1,
      "label": "Tableau de bord",
      "url": "/dashboard",
      "icon": "home",
      "isActive": true
    },
    {
      "id": 2,
      "label": "Utilisateurs",
      "url": "/settings/team",
      "icon": "users",
      "isActive": false
    }
  ]
}
```

### 6.2. Footer de la Sidebar
```json
{
  "version": "1.0.0",
  "copyright": "© 2023 Marki"
}
```

## 7. API Backend

### 7.1. Récupération des Liens de Navigation
- **Endpoint** : `GET /api/navigation/links`
  - **Réponse** : `{ "status": "success", "links": Array }`

## 8. Liens
- [Styleguide](utils/styleguide.md)
- [Scénarios Gherkin](specs/features/sidebar.feature)
- [Spécifications techniques](specs/_app/sidebar.html.spec)