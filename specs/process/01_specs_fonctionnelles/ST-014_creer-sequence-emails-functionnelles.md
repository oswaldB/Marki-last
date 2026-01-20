# ST-014 : Créer une séquence d’emails
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de créer une séquence d’emails avec des templates dynamiques et des délais. Les prompts ChatGPT sont proposés pour aider à rédiger les templates.

## 📜 Règles Métier
- **Création de séquence** : Les utilisateurs doivent pouvoir créer une séquence d’emails.
- **Templates dynamiques** : Les templates doivent supporter des variables dynamiques (par exemple, `{{variable}}`).
- **Délais** : Les utilisateurs doivent pouvoir définir des délais pour l'envoi des emails.
- **Prompts ChatGPT** : Des prompts ChatGPT doivent être proposés pour aider à rédiger les templates.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la gestion des séquences d’emails.
- **Templates dynamiques** : Implémentation de templates dynamiques avec des variables.
- **Délais** : Implémentation de la gestion des délais pour l'envoi des emails.
- **Prompts ChatGPT** : Intégration de prompts ChatGPT pour aider à la rédaction.

## 📋 Flux Principal
1. Accéder à l'interface de création de séquence d’emails.
2. Définir les templates dynamiques avec des variables.
3. Définir les délais pour l'envoi des emails.
4. Utiliser les prompts ChatGPT pour aider à la rédaction.
5. Enregistrer la séquence d’emails.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] CRÉER SÉQUENCE EMAILS    |
|                                     |
|  +-------------------------------+  |
|  |  📋 Template dynamique         |  |
|  |  [📝] Contenu:                |  |
|  |  Bonjour {{nom}},           |  |
|  |  Votre impayé est de        |  |
|  |  {{montant}} euros.         |  |
|  +-------------------------------+  |
|  |  📋 Délais                    |  |
|  |  [📅] Date: 2026-01-18       |  |
|  +-------------------------------+  |
|  |  📋 Prompts ChatGPT           |  |
|  |  [🖱 Bouton] GÉNÉRER        |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] ENREGISTRER     |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent créer une séquence d’emails.
- Les templates dynamiques sont supportés.
- Les délais pour l'envoi des emails sont définis.
- Les prompts ChatGPT aident à la rédaction des templates.
- La séquence d’emails est enregistrée et accessible.
