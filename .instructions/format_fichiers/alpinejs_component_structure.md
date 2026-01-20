# Structure d'un Composant Alpine.js avec Injection Include (Méthode Steroids Studio)

## 📄 Structure de Base

### 1. **Div Principal avec `x-data`**
Un composant Alpine.js commence par un `div` avec un état local défini par `x-data`.

```html
<div x-data="componentNomState()">
  <!-- Contenu du composant -->
</div>
```

### 2. **Utilisation de `x-ref`**
Les références aux éléments DOM sont définies avec `x-ref`.

```html
<input x-ref="componentInput" type="text">
```

### 2. **Injection Include**
Les includes (composants réutilisables) sont injectés à l'intérieur de ce `div`.

```html
<div x-data="componentNomState()">
  {% include 'partials/subcomponent.html' %}
</div>
```

### 3. **Script Alpine.js**
Le script définissant l'état et les fonctions est placé à la fin du `div`.

```html
<div x-data="componentNomState()">
  <!-- Contenu du composant -->
  
  <script>
    function componentNomState() {
      return {
        // État local
        value: '',
        
        // Fonctions
        validate() {
          // Logique de validation
        }
      };
    }
  </script>
</div>
```

## 📋 Exemple Complet

### Fichier de Spécifications (`/specs/_app/templates/partials/form_component.html.spec`)
```markdown
# Template: form_component
**Fichier miroir** : `app/templates/partials/form_component.html`

---
## 🎯 Objectif
Créer un composant de formulaire réutilisable avec validation dynamique.

## 📜 Structure HTML
```html
<div x-data="formComponentState()">
  {% include 'partials/input_field.html' %}
  
  <div x-text="errorMessage"></div>
  
  <button @click="submit">Submit</button>
  
  <script>
    function formComponentState() {
      return {
        errorMessage: '',
        
        submit() {
          // Logique de soumission
        }
      };
    }
  </script>
</div>
```

## 🎨 Intégration Marki

### Logo Marki
```html
<div class="marki-logo-container">
  <img src="/static/images/marki-logo.png" alt="Marki" class="marki-logo">
</div>
```

### Bouton Marki
```html
<button class="marki-button">Submit</button>
```

### Input Marki
```html
<input class="marki-input" type="text" placeholder="Value">
```

## 📌 Utilisation de Tailwind CSS

Les classes CSS utilisées sont basées sur **Tailwind CSS en CDN**. Aucune classe maison n'est utilisée.

### Exemple d'utilisation de Tailwind
```html
<div class="p-4 bg-gray-100 rounded-lg">
  <input class="w-full p-2 border rounded" type="text" placeholder="Enter text">
  <button class="mt-2 px-4 py-2 bg-blue-500 text-white rounded">Submit</button>
</div>
```

### Avantages
- **Pas de classes personnalisées** : Tout est géré par Tailwind.
- **CDN** : Pas besoin de build ou de configuration.
- **Consistance** : Utilisation des mêmes classes dans tout le projet.

## 📊 Exemple de Composant Complet

### Fichier de Spécifications (`/specs/_app/templates/partials/form_component.html.spec`)
```markdown
# Template: form_component
**Fichier miroir** : `app/templates/partials/form_component.html`

---
## 🎯 Objectif
Créer un composant de formulaire réutilisable avec validation dynamique.

## 📜 Structure HTML
```html
<div x-data="formComponentState()">
  <div class="marki-logo-container">
    <img src="/static/images/marki-logo.png" alt="Marki" class="marki-logo">
  </div>
  
  {% include 'partials/input_field.html' %}
  
  <div x-text="errorMessage" class="marki-error"></div>
  
  <button @click="submit" class="marki-button">Submit</button>
  
  <script>
    function formComponentState() {
      return {
        errorMessage: '',
        
        submit() {
          // Logique de soumission
        }
      };
    }
  </script>
</div>
```

## 📝 Script Alpine.js
```javascript
function formComponentState() {
  return {
    errorMessage: '',
    
    submit() {
      // Logique de soumission
    }
  };
}
```

## 📊 Exemple de Composant Complet

### Fichier de Spécifications (`/specs/_app/templates/partials/form_component.html.spec`)
```markdown
# Template: form_component
**Fichier miroir** : `app/templates/partials/form_component.html`

---
## 🎯 Objectif
Créer un composant de formulaire réutilisable avec validation dynamique.

## 📜 Structure HTML
```html
<div x-data="formComponentState()">
  <div class="marki-logo-container">
    <img src="/static/images/marki-logo.png" alt="Marki" class="marki-logo">
  </div>
  
  {% include 'partials/input_field.html' %}
  
  <div x-text="errorMessage" class="marki-error"></div>
  
  <button @click="submit" class="marki-button">Submit</button>
  
  <script>
    function formComponentState() {
      return {
        errorMessage: '',
        
        submit() {
          // Logique de soumission
        }
      };
    }
  </script>
</div>
```

## 📝 Script Alpine.js
```javascript
function formComponentState() {
  return {
    errorMessage: '',
    
    submit() {
      // Logique de soumission
    }
  };
}
```
