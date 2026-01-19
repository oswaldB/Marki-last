# ST-018 : Modifier une séquence
**Date** : 2026-01-18
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Permettre aux utilisateurs (PM/Dev) de modifier une séquence d’emails existante. Les changements ne s’appliquent pas aux actions déjà générées.

## 📜 Règles Métier
- **Modification de séquence** : Les utilisateurs doivent pouvoir modifier une séquence existante.
- **Non-rétroactivité** : Les changements ne doivent pas s’appliquer aux actions déjà générées.

## 📝 Exigences Techniques
- **Interface utilisateur** : Création d'une interface pour la modification des séquences.
- **Gestion des modifications** : Implémentation de la logique pour modifier une séquence sans affecter les actions déjà générées.

## 📋 Flux Principal
1. Accéder à l'interface de modification des séquences.
2. Sélectionner une séquence existante.
3. Modifier les templates ou les délais.
4. Enregistrer les modifications.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] MODIFIER SÉQUENCE        |
|                                     |
|  +-------------------------------+  |
|  |  📋 Séquence existante         |  |
|  |  [📋] Séquence 1              |  |
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
|  |  [🖱 Bouton] ENREGISTRER     |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📊 Critères de Validation
- Les utilisateurs peuvent modifier une séquence existante.
- Les modifications ne s’appliquent pas aux actions déjà générées.
- Les modifications sont enregistrées et accessibles.
