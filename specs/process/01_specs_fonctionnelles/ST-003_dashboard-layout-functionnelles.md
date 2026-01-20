# ST-003 : Layout Dashboard avec Sidebar et Topbar
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer un layout de type dashboard avec une sidebar et une topbar. Ce layout nécessite une authentification pour être accessible.

## 📜 Règles Métier
- **Authentification** : L'accès à ce layout doit être restreint aux utilisateurs authentifiés. Utilisation de Flask-Login pour gérer l'authentification.
- **Redirection** : Si l'utilisateur n'est pas authentifié, il doit être redirigé vers `/login`.
- **Sidebar** : Doit contenir les liens de navigation principaux.
- **Topbar** : Doit contenir les informations de l'utilisateur et les options de déconnexion.
- **Responsivité** : Le layout doit être responsive et s'adapter à tous les types d'écrans.

## 📝 Exigences Techniques
- **Authentification** : Utilisation de Flask-Login pour vérifier l'état de connexion de l'utilisateur.
- **Redirection** : Utilisation de Flask-Login pour rediriger les utilisateurs non authentifiés vers `/login`.
- **Sidebar** : Utilisation de composants Alpine.js pour une gestion réactive.
- **Topbar** : Affichage des informations de l'utilisateur et options de déconnexion.
- **Intégration avec base.html** : Ce layout doit étendre le template `base.html`.

## 📋 Flux Principal
1. Vérifier l'état de connexion de l'utilisateur avec Flask-Login.
2. Si l'utilisateur n'est pas authentifié, rediriger vers `/login`.
3. Afficher la sidebar avec les liens de navigation.
4. Afficher la topbar avec les informations de l'utilisateur.
5. Afficher le contenu dynamique via le bloc `dashboard_content`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] DASHBOARD LAYOUT         |
|                                     |
|  +-------------------------------+  |
|  |  📱 Sidebar                    |  |
|  |  - Accueil                    |  |
|  |  - Tableau de bord            |  |
|  |  - Profil                     |  |
|  |  - Déconnexion                |  |
|  +-------------------------------+  |
|                                     |
|  +-------------------------------+  |
|  |  📊 Topbar                     |  |
|  |  Utilisateur: John Doe        |  |
|  |  [🔒 Déconnexion]             |  |
|  +-------------------------------+  |
|                                     |
|  {% block content %}{% endblock %}  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```