# Template: base.html
**Fichier miroir** : `app/templates/base.html`
**Description** : Template de base pour toutes les pages de l'application.

---

## 🔧 Structure HTML

### Balises de Base
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Marki App{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

### CDN Tailwind CSS
**Description** : Intégration de Tailwind CSS via CDN pour une utilisation rapide et sans configuration.
**Code** :
```html
<script src="https://cdn.tailwindcss.com"></script>
```

### CDN Alpine.js
**Description** : Intégration de Alpine.js via CDN pour une gestion réactive des composants.
**Code** :
```html
<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
```

### CDN Lucid Icons
**Description** : Intégration de Lucid Icons via CDN pour une utilisation facile des icônes.
**Code** :
```html
<link href="https://unpkg.com/lucide@latest/dist/lucide.css" rel="stylesheet">
```

## 📝 Variables Globales
Aucune variable globale spécifique pour ce template.

## 📋 Flux Principal
1. Charger les dépendances CSS et JS via CDN.
2. Afficher le contenu dynamique via le bloc `content`.
3. Permettre la personnalisation du titre via le bloc `title`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] BASE LAYOUT             |
|                                     |
|  <!DOCTYPE html>                    |
|  <html lang="fr">                  |
|  <head>                             |
|  <meta charset="UTF-8">            |
|  <meta name="viewport" ...>        |
|  <title>{% block title %}</title>   |
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