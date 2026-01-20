# ST-010 : Créer une liste manuelle
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de créer une liste manuelle d'impayés via des filtres ou en ajoutant/supprimant des impayés en batch.

## 📜 Règles Métier
- **Création de liste** : Les utilisateurs doivent pouvoir créer une liste manuelle.
- **Ajout/Suppression en batch** : Les utilisateurs doivent pouvoir ajouter ou supprimer des impayés en batch.
- **Filtres** : Les utilisateurs doivent pouvoir appliquer des filtres pour créer la liste.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la gestion des listes manuelles.
- **Sélection multiple** : Permettre la sélection multiple d'impayés pour l'ajout/suppression en batch.
- **Filtres** : Implémentation de filtres pour faciliter la création de listes.

## 📋 Flux Principal
1. Accéder à l'interface de création de liste manuelle.
2. Appliquer des filtres ou sélectionner des impayés manuellement.
3. Ajouter ou supprimer des impayés en batch.
4. Enregistrer la liste manuelle.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] CRÉER LISTE MANUELLE     |
|                                     |
|  +-------------------------------+  |
|  |  📋 Filtres                    |  |
|  |  [🖱 Bouton] APPLIQUER        |  |
|  +-------------------------------+  |
|  |  📋 Impayés disponibles        |  |
|  |  [✓] Impayé 1                |  |
|  |  [✓] Impayé 2                |  |
|  |  [🖱 Bouton] AJOUTER          |  |
|  +-------------------------------+  |
|  |  📋 Liste manuelle            |  |
|  |  [✓] Impayé 1                |  |
|  |  [🖱 Bouton] SUPPRIMER        |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] ENREGISTRER     |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent créer une liste manuelle.
- Les utilisateurs peuvent ajouter/supprimer des impayés en batch.
- Les utilisateurs peuvent appliquer des filtres pour créer la liste.
- La liste manuelle est enregistrée et accessible.
