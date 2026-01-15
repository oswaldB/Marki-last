# ST-012 : Gestion des Assets Publics
**Date** : 2026-01-16
**Auteur** : Product Manager

---
## Contexte
Le système de gestion des assets publics permet de servir efficacement les fichiers statiques (images, CSS, JS, polices) nécessaires à l'interface utilisateur. Une gestion optimisée des assets améliore les performances, la maintenabilité et l'expérience utilisateur.

## Objectifs
- Centraliser la gestion des fichiers statiques
- Optimiser les temps de chargement
- Faciliter la maintenance et les mises à jour
- Assurer la compatibilité avec les environnements de développement et production

## Architecture des Assets

### Structure des Dossiers
```
app/
└── static/
    ├── images/
    │   ├── logo.png
    │   ├── favicon.ico
    │   └── ...
    ├── css/
    │   └── custom.css
    ├── js/
    │   └── custom.js
    └── fonts/
        └── ...
```

### Règles de Nommage
- Noms en minuscules avec tirets (kebab-case)
- Préfixes pour les versions : `logo-v1.png`, `logo-v2.png`
- Pas d'espaces ni de caractères spéciaux
- Extensions en minuscules

## Configuration Flask

### Configuration de Base
```python
# Dans app/__init__.py ou configuration Flask
app = Flask(__name__, 
            static_folder='static',
            static_url_path='/static')
```

### Configuration Avancée
```python
# Pour la production
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600  # Cache 1 heure
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
```

## Bonnes Pratiques

### Organisation
1. **Images** : `static/images/` - Tous les fichiers image (PNG, JPEG, SVG, WebP)
2. **CSS** : `static/css/` - Feuilles de style personnalisées
3. **JavaScript** : `static/js/` - Scripts personnalisés
4. **Polices** : `static/fonts/` - Fichiers de polices
5. **Vendors** : `static/vendor/` - Bibliothèques tierces

### Optimisation
- Compression des images (WebP recommandé)
- Minification des CSS/JS
- Utilisation des CDN pour les bibliothèques populaires
- Cache longue durée avec versioning

### Référencement dans les Templates
```html
<!-- Images -->
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">

<!-- CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">

<!-- JS -->
<script src="{{ url_for('static', filename='js/custom.js') }}"></script>
```

## Migration depuis l'Ancien Système

### Ancienne Structure (à éviter)
```
app/public/logo.png  # ❌ Ancienne localisation
```

### Nouvelle Structure (recommandée)
```
app/static/images/logo.png  # ✅ Nouvelle localisation
```

### Étapes de Migration
1. Créer le dossier `app/static/images/`
2. Déplacer `app/public/logo.png` vers `app/static/images/logo.png`
3. Mettre à jour les références dans les templates
4. Tester le rendu visuel
5. Supprimer l'ancien dossier `public/` (après validation)

## Gestion des Versions

### Stratégie de Versioning
- Utiliser des noms de fichiers versionnés : `logo-v1.png`, `logo-v2.png`
- Mettre à jour les références dans les templates
- Conserver les anciennes versions pendant 30 jours

### Exemple
```html
<!-- Version 1 -->
<img src="{{ url_for('static', filename='images/logo-v1.png') }}" alt="Logo">

<!-- Version 2 (nouvelle) -->
<img src="{{ url_for('static', filename='images/logo-v2.png') }}" alt="Logo">
```

## Sécurité

### Mesures de Sécurité
- Ne jamais servir de fichiers sensibles via le dossier static
- Valider les types de fichiers uploadés
- Limiter les extensions autorisées
- Désactiver l'exécution de code dans le dossier static

### Extensions Autorisées
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 
                     'css', 'js', 'woff', 'woff2', 'ttf', 'eot',
                     'ico', 'json'}
```

## Performance

### Optimisations Recommandées
1. **Cache** : Configurer des headers de cache appropriés
2. **CDN** : Utiliser un CDN pour les assets statiques
3. **Compression** : Activer la compression GZIP/Brotli
4. **Lazy Loading** : Pour les images hors écran
5. **Responsive Images** : Utiliser `srcset` pour différentes tailles

### Exemple de Cache
```python
from flask import send_from_directory
from werkzeug.middleware.shared_data import SharedDataMiddleware

# Cache pour 1 an (31536000 secondes)
app.add_url_rule('/static/<path:filename>', 'static', 
                build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/static': app.static_folder
})
```

## Tests

### Tests Requis
- Vérification que tous les assets sont accessibles
- Test des performances de chargement
- Validation des headers de cache
- Test de l'affichage correct des images
- Vérification des chemins dans les templates

### Exemple de Test Cypress
```javascript
describe('Assets Management', () => {
  it('Should load logo correctly', () => {
    cy.visit('/superadmin');
    cy.get('img[alt="Logo Marki"]').should('be.visible');
    cy.get('img[alt="Logo Marki"]').should('have.attr', 'src')
      .should('include', '/static/images/logo.png');
  });

  it('Should have proper cache headers', () => {
    cy.request('/static/images/logo.png')
      .its('headers')
      .its('cache-control')
      .should('include', 'public, max-age=');
  });
});
```

## Documentation

### Pour les Développeurs
- Toujours utiliser `url_for('static', filename='...')`
- Ne jamais coder en dur les chemins statiques
- Documenter les nouveaux assets dans `specs/bdd/assets.md`
- Suivre les conventions de nommage

### Pour les Designers
- Fournir les assets dans les formats optimisés
- Spécifier les dimensions et poids maximaux
- Utiliser des noms descriptifs
- Fournir les assets en WebP si possible

## Évolutions Futures
- Implémentation d'un système de CDN
- Automatisation de l'optimisation des images
- Génération automatique des sprites CSS
- Support des images responsives avancées
- Intégration avec des outils de build (Webpack, Vite)