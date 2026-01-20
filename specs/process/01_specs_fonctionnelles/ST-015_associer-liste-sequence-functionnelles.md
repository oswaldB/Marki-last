# ST-015 : Associer une liste à une séquence
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) d'associer une liste (manuelle ou automatique) à une séquence d’emails.

## 📜 Règles Métier
- **Association de liste et séquence** : Les utilisateurs doivent pouvoir associer une liste à une séquence.
- **Gestion des associations** : Les utilisateurs doivent pouvoir gérer les associations existantes.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour l'association des listes et séquences.
- **Gestion des associations** : Implémentation de la logique pour associer une liste à une séquence.

## 📋 Flux Principal
1. Accéder à l'interface d'association des listes et séquences.
2. Sélectionner une liste existante.
3. Sélectionner une séquence existante.
4. Associer la liste à la séquence.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] ASSOCIER LISTE SÉQUENCE  |
|                                     |
|  +-------------------------------+  |
|  |  📋 Liste existante            |  |
|  |  [📋] Liste 1                 |  |
|  +-------------------------------+  |
|  |  📋 Séquence existante         |  |
|  |  [📋] Séquence 1              |  |
|  +-------------------------------+  |
|  |  [🖱 Bouton] ASSOCIER         |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent associer une liste à une séquence.
- Les associations sont enregistrées et accessibles.
- Les utilisateurs peuvent gérer les associations existantes.
