# ST-008 : Page SuperAdmin
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer une page SuperAdmin pour permettre aux administrateurs principaux de gérer les utilisateurs, y compris la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs. La page est accessible à tous, mais les fonctionnalités d'administration sont protégées par un mot de passe.

## 📜 Règles Métier
- **Accessibilité** : Cette page doit être accessible à tous les utilisateurs, sans authentification requise.
- **Protection Frontale** : La page doit inclure une protection frontale où les composants de gestion des utilisateurs ne sont visibles que si l'utilisateur entre le mot de passe `Citron6-Mustang9` dans un champ dédié.
- **Gestion des Utilisateurs** : Permettre la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.
- **Réactivité** : La page doit être réactive et utiliser Alpine.js pour les interactions utilisateur.
- **Layout** : Utiliser le layout simple public pour cette page.

## 📝 Exigences Techniques
- **Protection Frontale** : Utilisation de Alpine.js pour gérer la visibilité des composants en fonction du mot de passe saisi.
- **API de Gestion des Utilisateurs** : Utilisation d'API pour gérer les utilisateurs (création, activation, modification du mot de passe).
- **Base de Données** : Utilisation de SQLite pour stocker les informations des utilisateurs.
- **Réactivité** : Utilisation de Alpine.js pour les interactions utilisateur et les appels API.

## 🎨 Maquette ASCII
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

## 📋 Flux Principal
1. Afficher le champ de mot de passe de protection.
2. Valider le mot de passe de protection avec Alpine.js.
3. Si le mot de passe est correct (`Citron6-Mustang9`), afficher les composants de gestion des utilisateurs.
4. Charger la liste des utilisateurs depuis l'API.
5. Permettre la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.
6. Utiliser Alpine.js pour les interactions utilisateur et les appels API.