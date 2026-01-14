# Template : Base (ST-001)
**Fichier cible** : `app/templates/base.html`

---

## **Description**
Template de base commun à toutes les pages. Définit la structure HTML, le système de couleurs Tailwind, Alpine.js et Heroicons.

---

## **Structure**
```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Marki - Gestion des Commissions{% endblock %}</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Alpine.js -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  
  <!-- Heroicons (SVG Sprites) -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/heroicons@2.0.0/24/outline/index.css">
  
  {% block head %}{% endblock %}
</head>

<body class="bg-bg-light text-text font-inter">
  {% block content %}{% endblock %}
  {% block scripts %}{% endblock %}
</body>
</html>
```

---

## **Couleurs Personnalisées**
À ajouter dans la config Tailwind ou en CSS personnalisé:

```javascript
{
  "colors": {
    "primary": "#509EE3",
    "primary-dark": "#236CB9",
    "secondary": "#6D5DCF",
    "success": "#4CAF50",
    "error": "#F44336",
    "text": "#333333",
    "text-light": "#666666",
    "border": "#CCCCCC",
    "bg-light": "#F5F7FA"
  }
}
```

---

## **Blocs Hérités**
- `{% block title %}` : Titre de la page
- `{% block head %}` : Ressources supplémentaires (styles, meta, etc.)
- `{% block content %}` : Contenu principal
- `{% block scripts %}` : Scripts supplémentaires
