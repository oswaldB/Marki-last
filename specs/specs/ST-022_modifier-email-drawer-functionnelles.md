# ST-022 : Modifier un email via un drawer
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de modifier un email (contenu, date, destinataire) via un drawer depuis le calendrier. Les variables du template sont recalculées si nécessaire.

## 📜 Règles Métier
- **Modification d'email** : Les utilisateurs doivent pouvoir modifier un email via un drawer.
- **Recalcul des variables** : Les variables du template doivent être recalculées si nécessaire.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'un drawer pour la modification des emails.
- **Gestion des modifications** : Implémentation de la logique pour modifier un email.
- **Recalcul des variables** : Implémentation de la logique pour recalculer les variables du template.

## 📋 Flux Principal
1. Accéder au calendrier des relances.
2. Sélectionner un email à modifier.
3. Ouvrir le drawer de modification.
4. Modifier le contenu, la date ou le destinataire.
5. Enregistrer les modifications.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] MODIFIER EMAIL DRAWER    |
|                                     |
|  +-------------------------------+  |
|  |  📅 Calendrier interactif     |  |
|  |  [📧] Email 1                |  |
|  |  [🖱 Bouton] MODIFIER        |  |
|  +-------------------------------+  |
|  |  📋 Drawer de modification    |  |
|  |  [📝] Contenu:                |  |
|  |  Bonjour {{nom}},           |  |
|  |  [📅] Date: 2026-01-18       |  |
|  |  [📧] Destinataire:           |  |
|  |  email@example.com          |  |
|  |  [🖱 Bouton] ENREGISTRER     |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent modifier un email via un drawer.
- Les variables du template sont recalculées si nécessaire.
- Les modifications sont enregistrées et accessibles.
