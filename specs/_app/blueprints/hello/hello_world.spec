# Blueprint: Hello World
**Fichier miroir** : `app/blueprints/hello/hello_world.py`

---

## 🔧 Fonctions

### `hello_world()`
**Description** :
- Affiche une page simple avec le texte "Hello World".
- Inclut le logo Marki.
- La page est accessible via l'URL `/`.

**Retour** :
- Rend le template `hello_world.html` avec les données nécessaires.

## 📝 Variables Globales
Aucune variable globale nécessaire pour cette page.

## 📋 Flux Principal
1. L'utilisateur accède à l'URL `/`.
2. La fonction `hello_world()` est appelée.
3. Le template `hello_world.html` est rendu avec le texte "Hello World" et le logo Marki.

## 🎨 Éléments UI
- Logo Marki : `/static/logo.png`.
- Texte "Hello World" : centré et en gras.
- Couleurs : conformes à la charte Marki.
