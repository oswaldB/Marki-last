# Structure d'une Page avec Alpine.js (Méthode Steroids Studio)

## 📄 Structure de Base

### 1. **Div Principal avec `x-data`**
Toute page commence par un `div` avec un état local défini par `x-data`.

```html
<div x-data="pageNomState()">
  <!-- Contenu de la page -->
</div>
```

### 2. **Utilisation de `x-ref`**
Les références aux éléments DOM sont définies avec `x-ref`.

```html
<input x-ref="emailInput" type="email">
```

### 3. **Accès aux États des Composants**
Pour accéder ou modifier l'état d'un composant inclus, utilisez `$refs`.

```html
<div x-data="parentState()">
  <div x-data="childState()" x-ref="childComponent"></div>
  
  <button @click="$refs.childComponent.state.value = 'new value'">Update Child</button>
  
  <script>
    function parentState() {
      return {
        updateChild() {
          this.$refs.childComponent.state.value = 'new value';
        }
      };
    }
    
    function childState() {
      return {
        value: ''
      };
    }
  </script>
</div>
```

### 2. **Includes dans le Div**
Les includes (composants réutilisables) sont placés à l'intérieur de ce `div`.

```html
<div x-data="pageNomState()">
  {% include 'partials/header.html' %}
  {% include 'partials/footer.html' %}
</div>
```

### 3. **Script Alpine.js**
Le script définissant l'état et les fonctions est placé à la fin du `div`.

```html
<div x-data="pageNomState()">
  <!-- Contenu de la page -->
  
  <script>
    function pageNomState() {
      return {
        // État local
        email: '',
        password: '',
        
        // Fonctions
        validateEmail() {
          // Logique de validation
        },
        
        submitForm() {
          // Logique de soumission
        }
      };
    }
  </script>
</div>
```

## 📋 Exemple Complet

### Fichier de Spécifications (`/specs/_app/templates/login.html.spec`)
```markdown
# Template: login
**Fichier miroir** : `app/templates/login.html`

---
## 🎯 Objectif
Créer une page de connexion avec validation dynamique.

## 📜 Structure HTML
```html
<div x-data="loginFormState()">
  {% include 'partials/header.html' %}
  
  <input x-model="email" type="email" placeholder="Email">
  <div x-text="emailError"></div>
  
  <input x-model="password" type="password" placeholder="Password">
  <div x-text="passwordError"></div>
  
  <button @click="submitForm">Login</button>
  
  {% include 'partials/footer.html' %}
  
  <script>
    function loginFormState() {
      return {
        email: '',
        password: '',
        emailError: '',
        passwordError: '',
        
        validateEmail() {
          this.emailError = !this.email.includes('@') ? 'Email invalide' : '';
        },
        
        validatePassword() {
          this.passwordError = this.password.length < 8 ? 'Mot de passe trop court' : '';
        },
        
        submitForm() {
          this.validateEmail();
          this.validatePassword();
          
          if (!this.emailError && !this.passwordError) {
            // Logique de soumission
          }
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
<button class="marki-button">Login</button>
```

### Input Marki
```html
<input class="marki-input" type="email" placeholder="Email">
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

## 📊 Exemple de Page Complète

### Fichier de Spécifications (`/specs/_app/templates/login.html.spec`)
```markdown
# Template: login
**Fichier miroir** : `app/templates/login.html`

---
## 🎯 Objectif
Créer une page de connexion avec validation dynamique.

## 📜 Structure HTML
```html
<div x-data="loginFormState()">
  {% include 'partials/header.html' %}
  
  <div class="marki-logo-container">
    <img src="/static/images/marki-logo.png" alt="Marki" class="marki-logo">
  </div>
  
  <input x-model="email" type="email" placeholder="Email" class="marki-input">
  <div x-text="emailError" class="marki-error"></div>
  
  <input x-model="password" type="password" placeholder="Password" class="marki-input">
  <div x-text="passwordError" class="marki-error"></div>
  
  <button @click="submitForm" class="marki-button">Login</button>
  
  {% include 'partials/footer.html' %}
  
  <script>
    function loginFormState() {
      return {
        email: '',
        password: '',
        emailError: '',
        passwordError: '',
        
        validateEmail() {
          this.emailError = !this.email.includes('@') ? 'Email invalide' : '';
        },
        
        validatePassword() {
          this.passwordError = this.password.length < 8 ? 'Mot de passe trop court' : '';
        },
        
        submitForm() {
          this.validateEmail();
          this.validatePassword();
          
          if (!this.emailError && !this.passwordError) {
            // Logique de soumission
          }
        }
      };
    }
  </script>
</div>
```
