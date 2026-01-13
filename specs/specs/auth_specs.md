# Authentification et Gestion des Utilisateurs
**Version** : 1.0
**Statut** : En cours

---
## 1. Contexte
Permettre aux utilisateurs de s'authentifier, de créer un compte, de récupérer un mot de passe perdu, et de gérer les utilisateurs (pour les administrateurs).

## 2. Pages et Fonctionnalités

### 2.1. Page de Login (`/auth/login`)
- **Description** : Permet aux utilisateurs de se connecter avec leur identifiant et mot de passe.
- **Composants Alpine.js** :
  - `loginFormState` : Gère le formulaire de connexion.
- **Flux de Données** :
  1. L'utilisateur saisit son identifiant et mot de passe.
  2. Le formulaire est soumis à Flask.
  3. Flask vérifie les informations d'identification.
  4. Si valide, l'utilisateur est redirigé vers la page d'accueil.
  5. Si invalide, un message d'erreur est affiché.
- **Règles Métier** :
  - L'identifiant doit être unique.
  - Le mot de passe doit être haché avant d'être stocké.
  - Si l'utilisateur est bloqué, un message d'erreur est affiché.

### 2.2. Page de Création de Compte (`/auth/register`)
- **Description** : Permet aux utilisateurs de créer un compte avec un identifiant et un mot de passe.
- **Composants Alpine.js** :
  - `registerFormState` : Gère le formulaire de création de compte.
- **Flux de Données** :
  1. L'utilisateur saisit son identifiant et mot de passe.
  2. Le formulaire est soumis à Flask.
  3. Flask vérifie que l'identifiant est unique.
  4. Si valide, le compte est créé et l'utilisateur est redirigé vers la page de login.
  5. Si invalide, un message d'erreur est affiché.
- **Règles Métier** :
  - L'identifiant doit être unique.
  - Le mot de passe doit être haché avant d'être stocké.
  - Le mot de passe doit avoir une longueur minimale de 8 caractères.

### 2.3. Page de Mot de Passe Perdu (`/auth/forgot_password`)
- **Description** : Permet aux utilisateurs de récupérer leur mot de passe.
- **Composants Alpine.js** :
  - `forgotPasswordFormState` : Gère le formulaire de récupération de mot de passe.
- **Flux de Données** :
  1. L'utilisateur saisit son identifiant.
  2. Le formulaire est soumis à Flask.
  3. Flask génère un nouveau mot de passe temporaire.
  4. Le mot de passe temporaire est affiché à l'utilisateur.
  5. L'utilisateur est redirigé vers la page de login.
- **Règles Métier** :
  - Le mot de passe temporaire doit être généré aléatoirement.
  - Le mot de passe temporaire doit être haché avant d'être stocké.

### 2.4. Page de Gestion des Utilisateurs (`/settings/team`)
- **Description** : Permet aux administrateurs de gérer les utilisateurs (bloquer, débloquer, changer le mot de passe, ajouter des collaborateurs) en utilisant des drawers plutôt que des popups. Cette page utilise le layout `app-layout.html` qui inclut un dashboard avec une sidebar, une topbar et un espace de contenu.
- **Layout** : `app-layout.html` (inspiré de Flowbite pour le design du dashboard).
- **Icônes** : Heroicons pour les icônes de la sidebar et des actions.
- **Blueprint** : `app` pour les routes principales de l'application.
- **Composants Alpine.js** :
  - `teamManagementState` : Gère la liste des utilisateurs et les actions administratives.
  - `addCollaboratorFormState` : Gère le formulaire d'ajout de collaborateurs dans un drawer.
  - `changePasswordFormState` : Gère le formulaire de changement de mot de passe dans un drawer.
- **Flux de Données** :
  1. L'administrateur accède à la page `/settings/team`.
  2. Flask renvoie la liste des utilisateurs.
  3. L'administrateur peut ouvrir un drawer pour ajouter un collaborateur ou changer le mot de passe d'un utilisateur.
  4. Les modifications sont soumises à Flask.
  5. Flask met à jour la base de données.
- **Règles Métier** :
  - Seuls les utilisateurs avec `isAdmin = true` peuvent accéder à cette page.
  - Les actions administratives sont enregistrées dans la base de données.
  - L'identifiant du collaborateur doit être unique.
  - Le mot de passe du collaborateur doit avoir une longueur minimale de 8 caractères.

### 2.5. Page SuperAdmin (`/superadmin`)
- **Description** : Permet de créer le premier utilisateur administrateur avec un mot de passe spécifique.
- **Composants Alpine.js** :
  - `superAdminFormState` : Gère le formulaire de création du premier administrateur.
- **Flux de Données** :
  1. L'utilisateur accède à la page `/superadmin`.
  2. L'utilisateur saisit le mot de passe `Citron6-Mustang8`.
  3. Le formulaire est soumis à Flask.
  4. Flask vérifie le mot de passe.
  5. Si valide, l'utilisateur est redirigé vers la page de création de compte pour créer le premier administrateur.
  6. Si invalide, un message d'erreur est affiché.
- **Règles Métier** :
  - Le mot de passe `Citron6-Mustang8` est requis pour accéder à cette page.
  - Une fois le premier administrateur créé, cette page devient inaccessible.

## 3. Composants Alpine.js
| Composant               | Rôle                                      | Props                     | Communication          |
|-------------------------|-------------------------------------------|---------------------------|-------------------------|
| loginFormState          | Gère le formulaire de connexion.           | Aucun                     | Appel parent via `$root`|
| registerFormState       | Gère le formulaire de création de compte. | Aucun                     | Appel parent via `$root`|
| forgotPasswordFormState | Gère le formulaire de récupération de mot de passe. | Aucun                     | Appel parent via `$root`|
| teamManagementState     | Gère la liste des utilisateurs et les actions administratives. | users: Array              | Appel parent via `$root`|
| superAdminFormState     | Gère le formulaire de création du premier administrateur. | Aucun                     | Appel parent via `$root`|

## 4. Flux de Données

### 4.1. Login
1. Utilisateur → Saisie identifiant/mot de passe → Soumission → Flask → Vérification → Redirection ou erreur.

### 4.2. Création de Compte
1. Utilisateur → Saisie identifiant/mot de passe → Soumission → Flask → Vérification → Création → Redirection ou erreur.

### 4.3. Mot de Passe Perdu
1. Utilisateur → Saisie identifiant → Soumission → Flask → Génération mot de passe temporaire → Affichage → Redirection.

### 4.4. Gestion des Utilisateurs
1. Administrateur → Accès à `/settings/team` → Flask → Liste des utilisateurs → Actions administratives → Soumission → Flask → Mise à jour.

### 4.5. SuperAdmin
1. Utilisateur → Saisie mot de passe `Citron6-Mustang8` → Soumission → Flask → Vérification → Redirection ou erreur.

## 5. Règles Métier

### 5.1. Login
- L'identifiant doit être unique.
- Le mot de passe doit être haché avant d'être stocké.
- Si l'utilisateur est bloqué, un message d'erreur est affiché.

### 5.2. Création de Compte
- L'identifiant doit être unique.
- Le mot de passe doit être haché avant d'être stocké.
- Le mot de passe doit avoir une longueur minimale de 8 caractères.

### 5.3. Mot de Passe Perdu
- Le mot de passe temporaire doit être généré aléatoirement.
- Le mot de passe temporaire doit être haché avant d'être stocké.

### 5.4. Gestion des Utilisateurs
- Seuls les utilisateurs avec `isAdmin = true` peuvent accéder à cette page.
- Les actions administratives sont enregistrées dans la base de données.

### 5.5. SuperAdmin
- Le mot de passe `Citron6-Mustang8` est requis pour accéder à cette page.
- Une fois le premier administrateur créé, cette page devient inaccessible.

## 6. Exemple de Données

### 6.1. Utilisateur
```json
{
  "id": 1,
  "username": "admin",
  "password": "hashed_password",
  "isAdmin": true,
  "isBlocked": false
}
```

### 6.2. Mot de Passe Temporaire
```json
{
  "username": "user1",
  "tempPassword": "temp_hashed_password"
}
```

## 7. API Backend

### 7.1. Login
- **Endpoint** : `POST /api/auth/login`
  - **Payload** : `{ "username": string, "password": string }`
  - **Réponse** : `{ "status": "success", "user": { "id": number, "username": string, "isAdmin": boolean } }`

### 7.2. Création de Compte
- **Endpoint** : `POST /api/auth/register`
  - **Payload** : `{ "username": string, "password": string }`
  - **Réponse** : `{ "status": "success", "user": { "id": number, "username": string } }`

### 7.3. Mot de Passe Perdu
- **Endpoint** : `POST /api/auth/forgot_password`
  - **Payload** : `{ "username": string }`
  - **Réponse** : `{ "status": "success", "tempPassword": string }`

### 7.4. Gestion des Utilisateurs
- **Endpoint** : `GET /api/settings/team`
  - **Réponse** : `{ "status": "success", "users": Array }`
- **Endpoint** : `POST /api/settings/team/block`
  - **Payload** : `{ "userId": number }`
  - **Réponse** : `{ "status": "success" }`
- **Endpoint** : `POST /api/settings/team/unblock`
  - **Payload** : `{ "userId": number }`
  - **Réponse** : `{ "status": "success" }`
- **Endpoint** : `POST /api/settings/team/change_password`
  - **Payload** : `{ "userId": number, "newPassword": string }`
  - **Réponse** : `{ "status": "success" }`

### 7.5. SuperAdmin
- **Endpoint** : `POST /api/superadmin`
  - **Payload** : `{ "password": string }`
  - **Réponse** : `{ "status": "success" }`

## 8. Liens
- [Styleguide](utils/styleguide.md)
- [Scénarios Gherkin](specs/features/auth_login.feature)
- [Spécifications techniques](specs/_app/auth_login.html.spec)
