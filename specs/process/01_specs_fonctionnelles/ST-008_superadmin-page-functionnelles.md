# ST-008 : Page SuperAdmin
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer une page SuperAdmin pour permettre aux administrateurs principaux de gérer les utilisateurs, y compris la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.

## 📜 Règles Métier
- **Accessibilité** : Cette page est accessible uniquement aux utilisateurs authentifiés avec le rôle `isAdmin`.
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

## 📋 Spécifications Fonctionnelles
- **Protection Frontale** :
  - Un champ de texte doit être présent pour saisir le code de protection.
  - Un bouton "VALIDE" doit être présent pour valider le code saisi.
  - Si le code saisi est correct (`Citron6-Mustang9`), les composants de gestion des utilisateurs doivent être affichés.
  - Si le code saisi est incorrect, un message d'erreur doit être affiché.

- **Création d'un Utilisateur** :
  - Un formulaire doit être présent pour saisir les informations de l'utilisateur (identifiant, mot de passe, rôle).
  - Un bouton "CRÉER" doit être présent pour créer l'utilisateur.
  - Après la création, un message de succès doit être affiché et la liste des utilisateurs doit être mise à jour.

- **Liste des Utilisateurs** :
  - Une datatable doit être présente pour afficher la liste des utilisateurs.
  - La datatable doit être suffisamment large pour afficher toutes les informations des utilisateurs.
  - Chaque ligne de la datatable doit contenir les informations de l'utilisateur (identifiant, rôle, statut).
  - Chaque ligne de la datatable doit contenir deux boutons : "ACTIVER" et "MODIFIER".

- **Activation d'un Utilisateur** :
  - Le bouton "ACTIVER" doit ouvrir un drawer pour confirmer l'activation de l'utilisateur.
  - Le drawer doit contenir un message de confirmation et deux boutons : "CONFIRMER" et "ANNULER".
  - Si l'utilisateur confirme, l'utilisateur doit être activé et un message de succès doit être affiché.

- **Modification d'un Utilisateur** :
  - Le bouton "MODIFIER" doit ouvrir un drawer pour modifier les informations de l'utilisateur.
  - Le drawer doit contenir un formulaire pour modifier les informations de l'utilisateur (identifiant, mot de passe, rôle).
  - Le drawer doit contenir deux boutons : "ENREGISTRER" et "ANNULER".
  - Si l'utilisateur enregistre, les informations de l'utilisateur doivent être mises à jour et un message de succès doit être affiché.

## 🔄 Mises à Jour
- **Modification des Boutons** : Les boutons "ACTIVER" et "MODIFIER" doivent maintenant ouvrir des drawers pour une meilleure expérience utilisateur.
- **Largeur de la Datatable** : La datatable doit être suffisamment large pour afficher toutes les informations des utilisateurs sans troncature.

## 📌 Notes
- La page doit être réactive et s'adapter à différentes tailles d'écran.
- Les drawers doivent être fermés en cliquant en dehors ou en appuyant sur la touche "Échap".
- Les messages de succès et d'erreur doivent être affichés de manière visible et disparaître après quelques secondes.

## 📌 Todo - Qui fait quoi ?

### 01_specs_fonctionnelles
- [] Mettre à jour la fiche ST-008 pour modifier le comportement des boutons activer et modifier avec des drawers @dev
- [] Corriger la largeur de la datatable dans la page superadmin @dev
- [] Placer la fiche ST-008 à l'étape 01_specs_fonctionnelles @dev

### 02_specs_techniques
- [ ] Créer les spécifications techniques pour ST-008 @dev

### 03_redaction_tests
- [ ] Créer les tests pour ST-008 @qa

### 04_developpement_bdd
- [ ] Développer la base de données pour ST-008 @dba

### 05_developpement_back
- [ ] Développer le back pour ST-008 @dev

### 06_developpement_front
- [ ] Développer le front pour ST-008 @dev

### 07_execution_tests
- [ ] Exécuter les tests pour ST-008 @qa

### 08_tests_reussis
- [ ] Valider les tests réussis pour ST-008 @qa

### 09_tests_echoues
- [ ] Corriger les tests échoués pour ST-008 @dev
