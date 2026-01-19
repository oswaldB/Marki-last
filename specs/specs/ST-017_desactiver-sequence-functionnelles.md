# ST-017 : Désactiver une séquence
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de désactiver une séquence d’emails. La désactivation supprime toutes les actions non envoyées dans `relances-actions` pour cette séquence.

## 📜 Règles Métier
- **Désactivation de séquence** : Les utilisateurs doivent pouvoir désactiver une séquence.
- **Suppression des actions non envoyées** : La désactivation doit supprimer toutes les actions non envoyées dans `relances-actions`.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la désactivation des séquences.
- **Suppression des actions** : Implémentation de la logique pour supprimer les actions non envoyées.

## 📋 Flux Principal
1. Accéder à l'interface de désactivation des séquences.
2. Sélectionner une séquence active.
3. Désactiver la séquence.
4. Supprimer toutes les actions non envoyées dans `relances-actions`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] DÉSACTIVER SÉQUENCE      |
|                                     |
|  +-------------------------------+  |
|  |  📋 Séquence existante         |  |
|  |  [📋] Séquence 1              |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] DÉSACTIVER       |  |
|  +-------------------------------+  |
|  |  📋 Confirmation              |  |
|  |  Êtes-vous sûr de vouloir    |  |
|  |  désactiver cette séquence ? |  |
|  |  [🖱 Bouton] OUI             |  |
|  |  [🖱 Bouton] NON             |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent désactiver une séquence.
- Les actions non envoyées sont supprimées dans `relances-actions`.
- La désactivation est confirmée avant d'être exécutée.
