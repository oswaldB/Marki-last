# ST-019 : Envoyer les emails quotidiens
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
À 18h chaque jour, le système vérifie les impayés dans `relances-actions`. Si le statut est "impayé", le système envoie l’email et met à jour le statut.

## 📜 Règles Métier
- **Envoi automatique** : Les emails doivent être envoyés automatiquement à 18h chaque jour.
- **Vérification du statut** : Seuls les impayés avec un statut "impayé" doivent recevoir un email.
- **Mise à jour du statut** : Le statut doit être mis à jour après l'envoi de l'email.

## 📝 Exigences Techniques
- **Planification** : Utilisation d'un planificateur de tâches pour exécuter l'envoi à 18h.
- **Vérification du statut** : Implémentation de la logique pour vérifier le statut des impayés.
- **Envoi d'emails** : Implémentation de la logique pour envoyer les emails.
- **Mise à jour du statut** : Implémentation de la logique pour mettre à jour le statut après l'envoi.

## 📋 Flux Principal
1. À 18h, le système vérifie les impayés dans `relances-actions`.
2. Pour chaque impayé avec un statut "impayé", le système envoie l’email.
3. Le système met à jour le statut de l'impayé après l'envoi.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] ENVOI EMAILS QUOTIDIENS  |
|                                     |
|  +-------------------------------+  |
|  |  📋 Planification             |  |
|  |  [🕒] Heure: 18h              |  |
|  +-------------------------------+  |
|  |  📋 Vérification du statut    |  |
|  |  [📋] Statut: Impayé          |  |
|  +-------------------------------+  |
|  |  📋 Envoi d'emails            |  |
|  |  [📧] Email envoyé            |  |
|  +-------------------------------+  |
|  |  📋 Mise à jour du statut     |  |
|  |  [📋] Statut: Envoyé          |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les emails sont envoyés automatiquement à 18h chaque jour.
- Seuls les impayés avec un statut "impayé" reçoivent un email.
- Le statut est mis à jour après l'envoi de l'email.
