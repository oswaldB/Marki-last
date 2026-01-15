# Template: dashboard.html
**Fichier miroir** : `app/templates/dashboard.html`
**Description** : Layout de type dashboard avec sidebar et topbar. Nécessite une authentification.

---

## 🔧 Structure HTML

### Extension de base.html
```html
{% extends "base.html" %}
```

### Blocs de Contenu
```html
{% block title %}Dashboard - Marki App{% endblock %}

{% block content %}
<div class="flex h-screen">
    <!-- Sidebar -->
    <div class="w-64 bg-gray-800 text-white">
        <div class="p-4">
            <h1 class="text-xl font-bold">Marki Dashboard</h1>
        </div>
        <nav class="p-4">
            <ul>
                <li class="mb-2"><a href="/dashboard" class="text-gray-300 hover:text-white">Accueil</a></li>
                <li class="mb-2"><a href="/dashboard/profile" class="text-gray-300 hover:text-white">Profil</a></li>
                <li class="mb-2"><a href="/logout" class="text-gray-300 hover:text-white">Déconnexion</a></li>
            </ul>
        </nav>
    </div>
    
    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
        <!-- Topbar -->
        <div class="bg-white shadow p-4">
            <div class="flex justify-between items-center">
                <h2 class="text-lg font-semibold">Tableau de bord</h2>
                <div>
                    <span class="mr-4">Utilisateur: {{ user.name }}</span>
                    <a href="/logout" class="bg-red-500 text-white px-4 py-2 rounded">Déconnexion</a>
                </div>
            </div>
        </div>
        
        <!-- Content -->
        <div class="flex-1 p-4">
            {% block dashboard_content %}{% endblock %}
        </div>
    </div>
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
3. Afficher la sidebar avec les liens de navigation.
4. Afficher la topbar avec les informations de l'utilisateur.
5. Afficher le contenu dynamique via le bloc `dashboard_content`.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] DASHBOARD LAYOUT         |
|                                     |
|  +-------------------------------+  |
|  |  📱 Sidebar                    |  |
|  |  - Accueil                    |  |
|  |  - Tableau de bord            |  |
|  |  - Profil                     |  |
|  |  - Déconnexion                |  |
|  +-------------------------------+  |
|                                     |
|  +-------------------------------+  |
|  |  📊 Topbar                     |  |
|  |  Utilisateur: John Doe        |  |
|  |  [🔒 Déconnexion]             |  |
|  +-------------------------------+  |
|                                     |
|  {% block dashboard_content %}    |
|  {% endblock %}                   |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```