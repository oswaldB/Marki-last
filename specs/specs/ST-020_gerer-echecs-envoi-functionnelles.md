# ST-020 : Gérer les échecs d’envoi
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
En cas d’échec d'envoi d'un email, le système envoie un email d’alerte à `email_notification` (défini dans `.env`). Aucun réessai automatique n'est effectué.

## 📜 Règles Métier
- **Alerte en cas d'échec** : En cas d'échec d'envoi, un email d'alerte doit être envoyé à `email_notification`.
- **Pas de réessai automatique** : Aucun réessai automatique ne doit être effectué.

## 📝 Exigences Techniques
- **Gestion des erreurs** : Implémentation de la logique pour gérer les échecs d'envoi.
- **Envoi d'alertes** : Implémentation de la logique pour envoyer un email d'alerte.
- **Configuration** : Utilisation de la variable `email_notification` définie dans `.env`.

## 📋 Flux Principal
1. En cas d'échec d'envoi d'un email, le système envoie un email d'alerte à `email_notification`.
2. Aucun réessai automatique n'est effectué.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] GÉRER ÉCHECS ENVOI       |
|                                     |
|  +-------------------------------+  |
|  |  📋 Échec d'envoi             |  |
|  |  [❌] Email non envoyé        |  |
|  +-------------------------------+  |
|  |  📋 Envoi d'alerte            |  |
|  |  [📧] Alerte envoyée à       |  |
|  |  email_notification          |  |
|  +-------------------------------+  |
|  |  📋 Pas de réessai            |  |
|  |  [🔄] Aucun réessai          |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- En cas d'échec d'envoi, un email d'alerte est envoyé à `email_notification`.
- Aucun réessai automatique n'est effectué.
