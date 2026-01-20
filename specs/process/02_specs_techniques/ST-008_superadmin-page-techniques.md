# ST-008 : Page SuperAdmin
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte

Créer une page SuperAdmin pour permettre aux administrateurs principaux de gérer les utilisateurs, y compris la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.

---

## 📜 Règles Métier

- **Accessibilité** : Cette page est accessible uniquement aux utilisateurs authentifiés avec le rôle `isAdmin`.
- **Protection Frontale** : La page doit inclure une protection frontale où les composants de gestion des utilisateurs ne sont visibles que si l'utilisateur entre le code `Citron6-Mustang9` dans un champ dédié.
- **Gestion des Utilisateurs** : Permettre la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.
- **Réactivité** : La page doit être réactive et utiliser Alpine.js pour les interactions utilisateur.
- **Layout** : Utiliser le layout simple public pour cette page.

---

## 🔧 Spécifications Techniques

### Fonctions

#### `validateProtectionCode(code: str) -> bool`
**Description** :
Valide le code de protection saisi par l'utilisateur.

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| code      | str    | Doit être égal à `Citron6-Mustang9` | Citron6-Mustang9 |

**Retour** :
`True` si le code est valide, `False` sinon.

#### `loadUsers() -> list`
**Description** :
Charge la liste des utilisateurs depuis l'API.

**Retour** :
Une liste d'objets utilisateurs.

**Exemple** :
```json
[
    {
        "id": "user1",
        "isAdmin": true
    },
    {
        "id": "user2",
        "isAdmin": false
    }
]
```

#### `createUser(user: dict) -> dict`
**Description** :
Crée un nouvel utilisateur via l'API.

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| user      | dict   | Doit contenir `id`, `password`, et `isAdmin` | {"id": "user1", "password": "password123", "isAdmin": true} |

**Retour** :
```json
{ "status": "success|error", "message": str }
```

#### `activateUser(userId: str) -> dict`
**Description** :
Active un utilisateur via l'API.

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| userId    | str    | Doit être un identifiant valide | user1 |

**Retour** :
```json
{ "status": "success|error", "message": str }
```

#### `modifyUser(userId: str, password: str) -> dict`
**Description** :
Modifie le mot de passe d'un utilisateur via l'API.

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| userId    | str    | Doit être un identifiant valide | user1 |
| password  | str    | Doit être un mot de passe valide | newpassword123 |

**Retour** :
```json
{ "status": "success|error", "message": str }
```

### Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| `protectionCode`  | str    | Code de protection saisi par l'utilisateur | Citron6-Mustang9 |
| `isProtectedContentVisible` | bool | Indique si le contenu protégé est visible | true |
| `newUser`         | dict   | Nouveau utilisateur à créer | {"id": "", "password": "", "isAdmin": false} |
| `users`           | list   | Liste des utilisateurs | [{"id": "user1", "isAdmin": true}] |
| `isActivateDrawerOpen` | bool | Indique si le drawer d'activation est ouvert | false |
| `isModifyDrawerOpen` | bool | Indique si le drawer de modification est ouvert | false |
| `currentUserId`   | str    | Identifiant de l'utilisateur courant | user1 |
| `newPassword`     | str    | Nouveau mot de passe saisi | newpassword123 |

### Flux Principal

1. **Validation du Code de Protection** :
   - L'utilisateur saisit le code de protection.
   - Le code est validé via `validateProtectionCode`.
   - Si le code est valide, le contenu protégé est affiché.

2. **Création d'un Utilisateur** :
   - L'utilisateur saisit les informations du nouvel utilisateur.
   - Les informations sont envoyées via `createUser`.
   - Si la création est réussie, la liste des utilisateurs est mise à jour.

3. **Activation d'un Utilisateur** :
   - L'utilisateur clique sur le bouton "Activer".
   - Le drawer d'activation est ouvert.
   - L'utilisateur confirme l'activation.
   - L'utilisateur est activé via `activateUser`.
   - Si l'activation est réussie, la liste des utilisateurs est mise à jour.

4. **Modification d'un Utilisateur** :
   - L'utilisateur clique sur le bouton "Modifier".
   - Le drawer de modification est ouvert.
   - L'utilisateur saisit le nouveau mot de passe.
   - Le mot de passe est modifié via `modifyUser`.
   - Si la modification est réussie, la liste des utilisateurs est mise à jour.

---

## 🎨 Maquettes UI

### Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] SUPERADMIN PAGE         |
|                                     |
|  +-------------------------------+  |
|  |  🔒 Code de Protection          |  |
|  |  ________________________     |  |
|  |  [🖱 Bouton] VALIDER            |  |
|  +-------------------------------+  |
|  |  📄 Gestion des Utilisateurs   |  |
|  |  (visible après validation)   |  |
|  |  +---------------------------+  |
|  |  |  📧 Identifiant            |  |
|  |  |  ________________________ |  |
|  |  |  🔒 Mot de passe           |  |
|  |  |  ________________________ |  |
|  |  |  📋 Rôle                   |  |
|  |  |  [✓] isAdmin              |  |
|  |  |  [🖱 Bouton] CRÉER        |  |
|  |  +---------------------------+  |
|  |  📄 Liste des Utilisateurs   |  |
|  |  (visible après validation)   |  |
|  |  +---------------------------+  |
|  |  |  📋 Utilisateur 1          |  |
|  |  |  [🖱 Bouton] ACTIVER      |  |
|  |  |  [🖱 Bouton] MODIFIER     |  |
|  |  +---------------------------+  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

### Description

- **Logo Marki** : En-tête avec le logo Marki.
- **Champs** : Code de protection, identifiant, mot de passe, et rôle.
- **Boutons** : Boutons pour valider le code de protection, créer un utilisateur, activer un utilisateur, et modifier un utilisateur.
- **Liste des Utilisateurs** : Tableau affichant la liste des utilisateurs avec des boutons pour activer et modifier chaque utilisateur.
- **Drawers** : Drawers pour confirmer l'activation et modifier le mot de passe d'un utilisateur.
- **Pied de page** : Powered by MARKI.

---

## 📌 Notes Supplémentaires

- Les spécifications techniques doivent être synchronisées avec les fichiers de spécifications dans `specs/_app/`.
- Toute modification doit être validée par l'équipe avant d'être fusionnée.
