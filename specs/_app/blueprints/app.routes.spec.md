# Routes : App
**Fichier cible** : `app/blueprints/app/routes.py`

---

## **Endpoints**

| URL                | Méthode | Paramètres          | Retour       | Description                     |
|--------------------|---------|---------------------|--------------|---------------------------------|
| `/`                | GET     | -                   | HTML         | Page d'accueil (redirige vers dashboard). |
| `/dashboard`       | GET     | -                   | HTML         | Dashboard principal.           |
| `/api/user/info`   | GET     | -                   | JSON         | Infos utilisateur pour Alpine.js. |

---

## **Exemple d'Implémentation**
```python
from flask import Blueprint, redirect, url_for, jsonify, render_template

bp = Blueprint('app', __name__)

@bp.route('/')
def index():
    return redirect(url_for('app.dashboard'))

@bp.route('/dashboard')
def dashboard():
    return render_template('app-layout.html')

@bp.route('/api/user/info')
def user_info():
    # Récupérer les infos utilisateur depuis la session ou la base de données
    user_data = {
        'username': 'admin',  # Exemple
        'email': 'admin@example.com',
        'isAdmin': True
    }
    return jsonify({'user': user_data})
