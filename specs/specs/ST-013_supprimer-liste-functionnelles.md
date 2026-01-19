# ST-013 : Supprimer une liste
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de supprimer une liste (manuelle ou automatique). Les impayés associés à la liste retournent dans le pool général.

## 📜 Règles Métier
- **Suppression de liste** : Les utilisateurs doivent pouvoir supprimer une liste.
- **Retour au pool général** : Les impayés associés à la liste doivent retourner dans le pool général.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la suppression des listes.
- **Gestion des impayés** : Implémentation de la logique pour retourner les impayés dans le pool général.

## 📋 Flux Principal
1. Accéder à l'interface de gestion des listes.
2. Sélectionner une liste à supprimer.
3. Confirmer la suppression.
4. Retourner les impayés associés dans le pool général.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SUPPRIMER LISTE          |
|                                     |
|  +-------------------------------+  |
|  |  📋 Liste existante            |  |
|  |  [📋] Liste 1                 |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] SUPPRIMER        |  |
|  +-------------------------------+  |
|  |  📋 Confirmation              |  |
|  |  Êtes-vous sûr de vouloir    |  |
|  |  supprimer cette liste ?     |  |
|  |  [🖱 Bouton] OUI             |  |
|  |  [🖱 Bouton] NON             |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent supprimer une liste.
- Les impayés associés retournent dans le pool général.
- La suppression est confirmée avant d'être exécutée.
