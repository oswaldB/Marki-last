# Template: simple.html
**Fichier miroir** : `app/templates/simple.html`
**Description** : Layout simple sans authentification. Destiné aux pages publiques de l'application.

---

## 🔧 Structure HTML

### Extension de base.html
```html
{% extends "base.html" %}
```

### Blocs de Contenu
```html
{% block title %}Simple Layout - Marki App{% endblock %}

{% block content %}
<div class="container mx-auto p-4">
    <header class="flex justify-between items-center mb-8">
        <div class="flex items-center">
            <img src="/static/images/marki-logo.png" alt="Marki Logo" class="h-8 mr-4">
            <h1 class="text-2xl font-bold">Marki App</h1>
        </div>
        <nav>
            <ul class="flex space-x-4">
                <li><a href="/" class="text-gray-600 hover:text-gray-900">Accueil</a></li>
                <li><a href="/about" class="text-gray-600 hover:text-gray-900">À propos</a></li>
                <li><a href="/contact" class="text-gray-600 hover:text-gray-900">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {% block simple_content %}{% endblock %}
    </main>
    
    <footer class="mt-8 p-4 bg-gray-100 text-center">
        <p>🎨 Powered by MARKI</p>
    </footer>
</div>
{% endblock %}
```

## 📝 Variables Globales
Aucune variable globale spécifique pour ce template.

## 📋 Flux Principal
1. Afficher l'en-tête avec le logo et la navigation.
2. Afficher le contenu dynamique via le bloc `simple_content`.
3. Afficher le pied de page avec les informations de copyright.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SIMPLE LAYOUT           |
|                                     |
|  +-------------------------------+  |
|  |  🎨 Logo Marki                 |  |
|  +-------------------------------+  |
|  |  📄 Contenu Principal          |  |
|  |  {% block simple_content %}   |  |
|  |  {% endblock %}               |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```