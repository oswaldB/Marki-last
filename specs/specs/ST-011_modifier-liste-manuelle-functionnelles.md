# ST-011 : Modifier une liste manuelle
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de modifier une liste manuelle existante, y compris l'application de filtres, la modification du nom, et l'ajout/suppression d'impayés en batch.

## 📜 Règles Métier
- **Modification de liste** : Les utilisateurs doivent pouvoir modifier une liste manuelle existante.
- **Ajout/Suppression en batch** : Les utilisateurs doivent pouvoir ajouter ou supprimer des impayés en batch.
- **Filtres** : Les utilisateurs doivent pouvoir appliquer des filtres pour modifier la liste.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la modification des listes manuelles.
- **Sélection multiple** : Permettre la sélection multiple d'impayés pour l'ajout/suppression en batch.
- **Filtres** : Implémentation de filtres pour faciliter la modification de listes.

## 📋 Flux Principal
1. Accéder à l'interface de modification de liste manuelle.
2. Sélectionner une liste manuelle existante.
3. Appliquer des filtres ou sélectionner des impayés manuellement.
4. Ajouter ou supprimer des impayés en batch.
5. Enregistrer les modifications.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] MODIFIER LISTE MANUELLE  |
|                                     |
|  +-------------------------------+  |
|  |  📋 Liste existante            |  |
|  |  [📋] Liste 1                 |  |
|  +-------------------------------+  |
|  |  📋 Filtres                    |  |
|  |  [🖱 Bouton] APPLIQUER        |  |
|  +-------------------------------+  |
|  |  📋 Impayés disponibles        |  |
|  |  [✓] Impayé 1                |  |
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
- Les utilisateurs peuvent modifier une liste manuelle existante.
- Les utilisateurs peuvent ajouter/supprimer des impayés en batch.
- Les utilisateurs peuvent appliquer des filtres pour modifier la liste.
- Les modifications sont enregistrées et accessibles.
