# ST-012 : Créer une liste automatique
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de créer une liste automatique d'impayés via un écran dédié. La liste est peuplée automatiquement depuis la table `impayées` en fonction de critères définis (par exemple, `statut = "impayé" AND jours_retard > 30`).

## 📜 Règles Métier
- **Création de liste automatique** : Les utilisateurs doivent pouvoir créer une liste automatique.
- **Critères de filtrage** : Les utilisateurs doivent pouvoir définir des critères de filtrage pour la liste.
- **Peuplement automatique** : La liste doit être peuplée automatiquement depuis la table `impayées`.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la gestion des listes automatiques.
- **Critères de filtrage** : Implémentation de critères de filtrage pour la création de listes.
- **Script de peuplement** : Création d'un script pour peupler automatiquement la liste depuis `impayées`.

## 📋 Flux Principal
1. Accéder à l'interface de création de liste automatique.
2. Définir les critères de filtrage (par exemple, `statut = "impayé" AND jours_retard > 30`).
3. Enregistrer la liste automatique.
4. Exécuter le script de peuplement pour remplir la liste.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] CRÉER LISTE AUTOMATIQUE  |
|                                     |
|  +-------------------------------+  |
|  |  📋 Critères de filtrage       |  |
|  |  Statut: [📋] Impayé           |  |
|  |  Jours de retard: > [30]      |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] ENREGISTRER     |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] PEUPLER          |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent créer une liste automatique.
- Les utilisateurs peuvent définir des critères de filtrage pour la liste.
- La liste est peuplée automatiquement depuis la table `impayées`.
- La liste automatique est enregistrée et accessible.
