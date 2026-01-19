# ST-009 : Synchroniser les impayés depuis Marki Mirroir
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Synchroniser les données des impayés depuis Marki Mirroir vers la table `impayées` de la base de données locale. Les impayés avec des emails manquants (particulier/apporteur) sont listés sur une page dédiée pour mise à jour manuelle.

## 📜 Règles Métier
- **Synchronisation automatique** : Les données doivent être synchronisées automatiquement depuis Marki Mirroir.
- **Gestion des emails manquants** : Les impayés avec des emails manquants doivent être listés sur une page dédiée.
- **Mise à jour manuelle** : Les emails manquants doivent être mis à jour manuellement dans Marki Mirroir.

## 📝 Exigences Techniques
- **Connexion à Marki Mirroir** : Utilisation d'une API ou d'un script pour se connecter à Marki Mirroir.
- **Synchronisation des données** : Récupération des données des impayés et mise à jour de la table `impayées`.
- **Page dédiée** : Création d'une page pour lister les impayés avec des emails manquants.

## 📋 Flux Principal
1. Établir une connexion à Marki Mirroir.
2. Récupérer les données des impayés.
3. Mettre à jour la table `impayées` avec les données récupérées.
4. Identifier les impayés avec des emails manquants.
5. Générer une page dédiée pour la mise à jour manuelle des emails manquants.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SYNCHRONISATION          |
|                                     |
|  +-------------------------------+  |
|  |  📊 Synchronisation            |  |
|  |  [🖱 Bouton] SYNCHRONISER     |  |
|  +-------------------------------+  |
|  |  📋 Impayés avec emails        |  |
|  |  manquants                    |  |
|  |  +---------------------------+  |
|  |  |  📧 Impayé 1                |  |
|  |  |  [🖱 Bouton] METTRE À JOUR  |  |
|  |  +---------------------------+  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les données des impayés sont synchronisées depuis Marki Mirroir.
- La table `impayées` est mise à jour avec les données récupérées.
- Les impayés avec des emails manquants sont listés sur une page dédiée.
- La page dédiée permet la mise à jour manuelle des emails manquants.
