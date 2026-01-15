# ST-005 : Layout Simple avec Authentification
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer un layout simple avec authentification. Ce layout est destiné aux pages nécessitant une authentification mais sans la complexité d'un dashboard.

## 📜 Règles Métier
- **Authentification** : L'accès à ce layout doit être restreint aux utilisateurs authentifiés. Utilisation de Flask-Login pour gérer l'authentification.
- **Redirection** : Si l'utilisateur n'est pas authentifié, il doit être redirigé vers `/login`.
- **Simplicité** : Doit être simple et épuré pour une utilisation facile.
- **Responsivité** : Le layout doit être responsive et s'adapter à tous les types d'écrans.

## 📝 Exigences Techniques
- **Authentification** : Utilisation de Flask-Login pour vérifier l'état de connexion de l'utilisateur.
- **Redirection** : Utilisation de Flask-Login pour rediriger les utilisateurs non authentifiés vers `/login`.
- **Intégration avec base.html** : Ce layout doit étendre le template `base.html`.
- **Contenu dynamique** : Doit permettre l'affichage de contenu dynamique via un bloc dédié.

## 📋 Flux Principal
1. Vérifier l'état de connexion de l'utilisateur avec Flask-Login.
2. Si l'utilisateur n'est pas authentifié, rediriger vers `/login`.
3. Afficher l'en-tête avec le logo et la navigation.
4. Afficher le contenu dynamique via le bloc `auth_content`.
5. Afficher le pied de page avec les informations de copyright.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SIMPLE AUTH LAYOUT      |
|                                     |
|  +-------------------------------+  |
|  |  📄 Contenu Principal          |  |
|  |  {% block auth_content %}     |  |
|  |  {% endblock %}               |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```