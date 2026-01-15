# ST-004 : Layout Simple sans Authentification
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer un layout simple sans authentification. Ce layout est destiné aux pages publiques de l'application.

## 📜 Règles Métier
- **Accessibilité** : Ce layout doit être accessible sans authentification.
- **Simplicité** : Doit être simple et épuré pour une utilisation facile.
- **Logo Marki** : Doit inclure le logo de Marki dans l'en-tête.
- **Responsivité** : Le layout doit être responsive et s'adapter à tous les types d'écrans.

## 📝 Exigences Techniques
- **Intégration avec base.html** : Ce layout doit étendre le template `base.html`.
- **Logo Marki** : Utilisation du logo officiel de Marki dans l'en-tête.
- **Contenu dynamique** : Doit permettre l'affichage de contenu dynamique via un bloc dédié.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SIMPLE LAYOUT           |
|                                     |
|  +-------------------------------+  |
|  |  🎨 Logo Marki                 |  |
|  +-------------------------------+  |
|  |  📄 Contenu Principal          |  |
|  |  {% block content %}          |  |
|  |  {% endblock %}               |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```