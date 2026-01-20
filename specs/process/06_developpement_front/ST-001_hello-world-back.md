# ST-001 : Page Hello World - Développement Backend
**Date** : 2024-10-04
**Version** : 1.0
**Auteur** : Mistral Vibe

---

## 📋 Vue d'ensemble
Ce document décrit le développement backend pour la page Hello World (ST-001).

## 🔧 Implémentation Backend

### 1. Structure des fichiers
```
app/
├── blueprints/
│   └── hello/
│       ├── __init__.py
│       └── routes.py
└── templates/
    └── hello_world.html
```

### 2. Création du Blueprint

#### `app/blueprints/hello/__init__.py`
```python
from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

from . import routes
```

#### `app/blueprints/hello/routes.py`
```python
from flask import render_template
from . import hello_bp

@hello_bp.route('/hello')
def hello_world():
    """
    Route pour afficher la page Hello World
    
    Returns:
        Rendered template: hello_world.html
    """
    return render_template('hello_world.html')
```

### 3. Intégration du Blueprint

Modifier `app/__init__.py` pour enregistrer le blueprint :
```python
from app.blueprints.hello import hello_bp

app.register_blueprint(hello_bp)
```

### 4. Template

#### `app/templates/hello_world.html`
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

## 📊 Tests Backend

### Vérification de la route
```bash
# Démarrer le serveur
python3 app.py

# Tester la route avec curl
curl -I http://127.0.0.1:5000/hello

# Résultat attendu:
# HTTP/1.1 200 OK
# Content-Type: text/html; charset=utf-8
```

### Vérification du template
```python
# Dans un shell Python
from flask import Flask
app = Flask(__name__)
app.config['TESTING'] = True

with app.test_client() as client:
    response = client.get('/hello')
    print(response.status_code)  # Doit afficher 200
    print('Hello World' in response.data.decode())  # Doit afficher True
```

## 🔄 Dépendances
- Flask >= 2.0
- Python >= 3.8

## 📝 Notes
- Aucune base de données requise
- Aucune authentification requise
- La route est publique

---

**Statut** : Prêt pour développement front
**Prochaine étape** : Développement front (ST-001_hello-world-front.md)