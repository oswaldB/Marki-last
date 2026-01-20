# ST-008 : Page SuperAdmin
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer une page SuperAdmin pour permettre aux administrateurs principaux de gérer les utilisateurs, y compris la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.

## 📜 Règles Métier
- **Accessibilité** : Cette
- **Protection Frontale** : La page doit inclure une protection frontale où les composants de gestion des utilisateurs ne sont visibles que si l'utilisateur entre le code `Citron6-Mustang9` dans un champ dédié.
- **Gestion des Utilisateurs** : Permettre la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.
- **Réactivité** : La page doit être réactive et utiliser Alpine.js pour les interactions utilisateur.
- **Layout** : Utiliser le layout simple public pour cette page.

## 📝 Exigences Techniques
- **Authentification** : Utilisation de Flask-Login pour vérifier que l'utilisateur est authentifié et a le rôle `isAdmin`.
- **Protection Frontale** : Utilisation de Alpine.js pour gérer la visibilité des composants en fonction du code saisi.
- **API de Gestion des Utilisateurs** : Utilisation d'API pour gérer les utilisateurs (création, activation, modification du mot de passe).
- **Base de Données** : Utilisation de PickleDB pour stocker les informations des utilisateurs.
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