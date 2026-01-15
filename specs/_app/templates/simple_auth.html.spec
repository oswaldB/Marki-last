# Template: simple_auth.html
**Fichier miroir** : `app/templates/simple_auth.html`
**Description** : Layout simple avec authentification. Destiné aux pages nécessitant une authentification mais sans la complexité d'un dashboard.

---

## 🔧 Structure HTML

### Extension de base.html
```html
{% extends "base.html" %}
```

### Blocs de Contenu
```html
{% block title %}Simple Auth Layout - Marki App{% endblock %}

{% block content %}
<div class="container mx-auto p-4">
    <header class="flex justify-between items-center mb-8">
        <h1 class="text-2xl font-bold">Marki App</h1>
        <nav>
            <ul class="flex space-x-4">
                <li><a href="/dashboard" class="text-gray-600 hover:text-gray-900">Dashboard</a></li>
                <li><a href="/profile" class="text-gray-600 hover:text-gray-900">Profil</a></li>
                <li><a href="/logout" class="text-gray-600 hover:text-gray-900">Déconnexion</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {% block auth_content %}{% endblock %}
    </main>
    
    <footer class="mt-8 p-4 bg-gray-100 text-center">
        <p>🎨 Powered by MARKI</p>
    </footer>
</div>
{% endblock %}
```

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| user      | dict   | Informations de l'utilisateur connecté | { "name": "John Doe", "email": "john@example.com" } |

## 📋 Flux Principal
1. Vérifier l'état de connexion de l'utilisateur avec Flask-Login.
2. Si l'utilisateur n'est pas authentifié, rediriger vers `/login`.
3. Afficher l'en-tête avec le logo et la navigation.
4. Afficher le contenu dynamique via le bloc `auth_content`.
5. Afficher le pied de page avec les informations de copyright.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SIMPLE AUTH LAYOUT      |
|                                     |
|  +-------------------------------+  |
|  |  📄 Contenu Principal          |  |
|  |  {% block auth_content %}     |  |
|  |  {% endblock %}               |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```