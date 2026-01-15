# Template: login.html
**Fichier miroir** : `app/templates/login.html`
**Description** : Page de connexion pour permettre aux utilisateurs de s'authentifier et d'accéder aux parties protégées de l'application.

---

## 🔧 Structure HTML

### Extension de base.html
```html
{% extends "base.html" %}
```

### Blocs de Contenu
```html
{% block title %}Connexion - Marki App{% endblock %}

{% block content %}
<div class="container mx-auto p-4">
    <div class="flex justify-center items-center h-screen">
        <div class="w-full max-w-md">
            <div class="text-center mb-8">
                <img src="/static/images/marki-logo.png" alt="Marki Logo" class="h-16 mx-auto mb-4">
                <h1 class="text-2xl font-bold">Connexion</h1>
            </div>
            
            <form x-data="loginForm()" @submit.prevent="submitForm" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="id">
                        Identifiant
                    </label>
                    <input x-model="id" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="id" type="text" placeholder="Identifiant" required>
                    <div x-text="idError" class="text-red-500 text-xs italic"></div>
                </div>
                
                <div class="mb-6">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                        Mot de passe
                    </label>
                    <input x-model="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" required>
                    <div x-text="passwordError" class="text-red-500 text-xs italic"></div>
                </div>
                
                <div class="flex items-center justify-between">
                    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                        Se connecter
                    </button>
                    <a class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="/forgot-password">
                        Mot de passe oublié ?
                    </a>
                </div>
                
                <div class="mt-4 text-center">
                    <button @click="openDrawer" class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" type="button">
                        S'inscrire
                    </button>
                </div>
                
                {% if error %}
                <div class="mt-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ error }}</span>
                </div>
                {% endif %}
            </form>
        </div>
    </div>
</div>

<!-- Drawer d'Inscription -->
<div x-show="isDrawerOpen" @click.away="closeDrawer" class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4" style="display: none;">
    <div class="bg-white rounded-lg shadow-xl w-full max-w-md" @click.stop>
        <div class="p-6">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-xl font-bold">Inscription</h2>
                <button @click="closeDrawer" class="text-gray-500 hover:text-gray-700">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            <div class="mb-4">
                <p class="text-gray-700">
                    Merci de contacter votre administrateur principal pour créer un compte.
                </p>
                <p class="text-gray-700 mt-2">
                    Si vous êtes l'administrateur principal, veuillez envoyer un email à :
                </p>
                <a href="mailto:contact@markidiags.com" class="text-blue-500 hover:text-blue-700">
                    contact@markidiags.com
                </a>
            </div>
        </div>
    </div>
</div>

<!-- Drawer Mot de Passe Oublié -->
<div x-show="isForgotPasswordDrawerOpen" @click.away="closeForgotPasswordDrawer" class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4" style="display: none;">
    <div class="bg-white rounded-lg shadow-xl w-full max-w-md" @click.stop>
        <div class="p-6">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-xl font-bold">Mot de Passe Oublié</h2>
                <button @click="closeForgotPasswordDrawer" class="text-gray-500 hover:text-gray-700">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            <div class="mb-4">
                <p class="text-gray-700">
                    Merci de contacter votre administrateur principal pour réinitialiser votre mot de passe.
                </p>
                <p class="text-gray-700 mt-2">
                    Si vous êtes l'administrateur principal, veuillez envoyer un email à :
                </p>
                <a href="mailto:contact@markidiags.com" class="text-blue-500 hover:text-blue-700">
                    contact@markidiags.com
                </a>
            </div>
        </div>
    </div>
</div>

{% endblock %}
```

### Script Alpine.js
```html
<script>
function loginForm() {
    return {
        id: '',
        password: '',
        idError: '',
        passwordError: '',
        isDrawerOpen: false,
        isForgotPasswordDrawerOpen: false,
        
        openDrawer() {
            this.isDrawerOpen = true;
        },
        
        closeDrawer() {
            this.isDrawerOpen = false;
        },
        
        openForgotPasswordDrawer() {
            this.isForgotPasswordDrawerOpen = true;
        },
        
        closeForgotPasswordDrawer() {
            this.isForgotPasswordDrawerOpen = false;
        },
        
        validateId() {
            if (!this.id) {
                this.idError = 'L\'identifiant est requis.';
                return false;
            }
            this.idError = '';
            return true;
        },
        
        validatePassword() {
            if (!this.password) {
                this.passwordError = 'Le mot de passe est requis.';
                return false;
            }
            if (this.password.length < 8) {
                this.passwordError = 'Le mot de passe doit contenir au moins 8 caractères.';
                return false;
            }
            this.passwordError = '';
            return true;
        },
        
        submitForm() {
            if (this.validateId() && this.validatePassword()) {
                // Soumettre le formulaire
                this.$el.submit();
            }
        }
    };
}
</script>
```

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| error     | str    | Message d'erreur en cas d'échec de la connexion | "Identifiant ou mot de passe incorrect." |

## 📋 Flux Principal
1. Afficher le formulaire de connexion avec les champs pour l'identifiant et le mot de passe.
2. Valider les champs du formulaire avec Alpine.js.
3. Soumettre le formulaire à l'API `/api/login` pour l'authentification.
4. Utiliser Flask-Login pour gérer la session utilisateur.
5. En cas de succès, rediriger l'utilisateur vers `/app/dashboard` par défaut ou vers la page spécifiée dans le paramètre `?redirect=/path`.
6. En cas d'échec, afficher un message d'erreur.
7. Afficher un drawer informatif pour l'inscription lorsque l'utilisateur clique sur le lien "S'inscrire".
8. Afficher un drawer informatif pour le mot de passe oublié lorsque l'utilisateur clique sur le lien "Mot de passe oublié ?".

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] LOGIN PAGE              |
|                                     |
|  +-------------------------------+  |
|  |  🎨 Logo Marki                 |  |
|  +-------------------------------+  |
|  |  📧 Identifiant                |  |
|  |  ________________________     |  |
|  |  🔒 Mot de passe              |  |
|  |  ________________________     |  |
|  |  [🖱 Bouton] SE CONNECTER      |  |
|  |  [🔗 Lien] Mot de passe oublié |  |
|  |  [🔗 Lien] S'inscrire         |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

## 📄 Drawer d'Inscription
```
+-------------------------------------+
|  🏗 [MARKI] DRAWER INSCRIPTION      |
|                                     |
|  +-------------------------------+  |
|  |  📄 Informations               |  |
|  |  Merci de contacter votre     |  |
|  |  administrateur principal.    |  |
|  |  Si vous êtes l'administrateur|  |
|  |  principal, veuillez envoyer  |  |
|  |  un email à :                |  |
|  |  contact@markidiags.com       |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

## 📄 Drawer Mot de Passe Oublié
```
+-------------------------------------+
|  🏗 [MARKI] DRAWER MOT DE PASSE     |
|  OUBLIÉ                            |
|                                     |
|  +-------------------------------+  |
|  |  📄 Informations               |  |
|  |  Merci de contacter votre     |  |
|  |  administrateur principal.    |  |
|  |  Si vous êtes l'administrateur|  |
|  |  principal, veuillez envoyer  |  |
|  |  un email à :                |  |
|  |  contact@markidiags.com       |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```