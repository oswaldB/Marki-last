# ST-016 : Activer une séquence
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) d'activer une séquence d’emails. L'activation génère les actions dans `relances-actions` pour tous les impayés de la liste associée, en remplaçant les variables des templates par les valeurs réelles.

## 📜 Règles Métier
- **Activation de séquence** : Les utilisateurs doivent pouvoir activer une séquence.
- **Génération des actions** : L'activation doit générer les actions dans `relances-actions` pour tous les impayés de la liste associée.
- **Remplacement des variables** : Les variables des templates doivent être remplacées par les valeurs réelles.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour l'activation des séquences.
- **Génération des actions** : Implémentation de la logique pour générer les actions dans `relances-actions`.
- **Remplacement des variables** : Implémentation de la logique pour remplacer les variables des templates.

## 📋 Flux Principal
1. Accéder à l'interface d'activation des séquences.
2. Sélectionner une séquence associée à une liste.
3. Activer la séquence.
4. Générer les actions dans `relances-actions` pour tous les impayés de la liste.
5. Remplacer les variables des templates par les valeurs réelles.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] ACTIVER SÉQUENCE         |
|                                     |
|  +-------------------------------+  |
|  |  📋 Séquence existante         |  |
|  |  [📋] Séquence 1              |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] ACTIVER          |  |
|  +-------------------------------+  |
|  |  📋 Confirmation              |  |
|  |  Êtes-vous sûr de vouloir    |  |
|  |  activer cette séquence ?    |  |
|  |  [🖱 Bouton] OUI             |  |
|  |  [🖱 Bouton] NON             |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent activer une séquence.
- Les actions sont générées dans `relances-actions` pour tous les impayés de la liste.
- Les variables des templates sont remplacées par les valeurs réelles.
- L'activation est confirmée avant d'être exécutée.
