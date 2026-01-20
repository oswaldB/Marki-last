# ST-001 : Page Hello World - Spécifications Techniques
**Date** : 2024-10-04
**Version** : 1.0
**Auteur** : Mistral Vibe

---

## 📋 Vue d'ensemble
Ce document décrit les spécifications techniques pour l'implémentation de la page Hello World (ST-001).

## 🔧 Architecture Technique

### Backend (Flask)
- **Route** : `/hello`
- **Méthode** : GET
- **Contrôleur** : `hello_world()` dans `app/blueprints/hello/routes.py`
- **Template** : `hello_world.html` dans `app/templates/`
- **Statut HTTP** : 200 OK

### Frontend
- **Framework** : HTML5 + CSS3 (vanilla, pas de framework JS requis)
- **Responsive** : Utilisation de media queries pour mobile/desktop
- **Assets** :
  - Logo : `/static/images/marki-logo.png`
  - CSS : Intégré directement dans le template ou via fichier dédié

### Structure des fichiers
```
app/
├── blueprints/
│   └── hello/
│       ├── __init__.py
│       └── routes.py
├── templates/
│   └── hello_world.html
└── static/
    └── images/
        └── marki-logo.png
```

## 🛠️ Implémentation Détaillée

### 1. Route Backend (`app/blueprints/hello/routes.py`)
```python
from flask import Blueprint, render_template

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello')
def hello_world():
    """Route pour afficher la page Hello World"""
    return render_template('hello_world.html')
```

### 2. Template Frontend (`app/templates/hello_world.html`)
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marki - Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background-color: #f5f5f5;
        }
        
        .logo {
            position: absolute;
            top: 20px;
            left: 20px;
            width: 120px;
        }
        
        .content {
            text-align: center;
            padding: 20px;
        }
        
        h1 {
            font-size: 3rem;
            font-weight: 700;
            color: #2c3e50;
            margin: 0;
        }
        
        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
            
            .logo {
                width: 80px;
                top: 10px;
                left: 10px;
            }
        }
    </style>
</head>
<body>
    <img src="/static/images/marki-logo.png" alt="Marki Logo" class="logo">
    
    <div class="content">
        <h1>Hello World</h1>
    </div>
</body>
</html>
```

### 3. Intégration du Blueprint
Modifier `app/__init__.py` pour enregistrer le blueprint :
```python
from app.blueprints.hello import hello_bp

app.register_blueprint(hello_bp)
```

## 📊 Critères de Validation Techniques

1. **Backend**
   - La route `/hello` répond avec un statut 200
   - Le template `hello_world.html` est correctement rendu
   - Pas d'erreurs serveur

2. **Frontend**
   - Le texte "Hello World" est visible avec `font-weight: 700`
   - Le logo est affiché avec l'attribut `alt="Marki Logo"`
   - La page est responsive (testé sur mobile et desktop)
   - Pas d'erreurs console

3. **Performances**
   - Temps de chargement < 500ms
   - Taille de la page < 50KB

## 🔄 Dépendances
- Flask >= 2.0
- Python >= 3.8

## 📝 Notes
- Aucune base de données requise pour cette page
- Aucune authentification requise
- La page doit être accessible publiquement

---

**Statut** : Prêt pour implémentation
**Prochaine étape** : Développement BDD (ST-001_hello-world-bdd.md)