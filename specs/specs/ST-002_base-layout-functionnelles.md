# ST-002 : Base Layout avec Tailwind et Alpine.js
**Date** : 2024-10-04
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte
Créer un fichier `base.html` qui servira de template de base pour toutes les pages de l'application. Ce fichier doit inclure les dépendances nécessaires pour Tailwind CSS et Alpine.js en CDN.

## 📜 Règles Métier
- **Tailwind CSS** : Doit être chargé via CDN pour une utilisation rapide et sans configuration.
- **Alpine.js** : Doit être chargé via CDN pour une gestion réactive des composants.
- **Lucid Icons** : Doit être chargé via CDN pour une utilisation facile des icônes.
- **Structure HTML** : Doit inclure les balises de base pour une page HTML5.
- **Responsivité** : Le layout doit être responsive et s'adapter à tous les types d'écrans.

## 📝 Exigences Techniques
- **Balises HTML5** : Utilisation de `<!DOCTYPE html>`, `<html>`, `<head>`, et `<body>`.
- **CDN Tailwind** : Utilisation du CDN officiel de Tailwind CSS.
- **CDN Alpine.js** : Utilisation du CDN officiel de Alpine.js.
- **CDN Lucid Icons** : Utilisation du CDN officiel de Lucid Icons.
- **Meta Tags** : Inclusion des balises meta pour le viewport et le charset.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BASE LAYOUT             |
|                                     |
|  <!DOCTYPE html>                    |
|  <html>                             |
|  <head>                             |
|  <meta charset="UTF-8">            |
|  <meta name="viewport" ...>        |
|  <script src="CDN Tailwind">      |
|  <script src="CDN Alpine.js">     |
|  <link href="CDN Lucid Icons">    |
|  </head>                            |
|  <body>                             |
|  {% block content %}{% endblock %}  |
|  </body>                            |
|  </html>                            |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```