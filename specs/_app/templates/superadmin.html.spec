# Template: superadmin.html
**Fichier miroir** : `app/templates/superadmin.html`
**Description** : Page SuperAdmin pour permettre aux administrateurs principaux de gérer les utilisateurs, y compris la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.

---

## 🔧 Structure HTML

### Extension de simple.html
```html
{% extends "simple.html" %}
```

### Blocs de Contenu
```html
{% block title %}SuperAdmin - Marki App{% endblock %}

{% block simple_content %}
<div class="container mx-auto p-4">
    <div class="flex justify-center items-center h-screen">
        <div class="w-full max-w-md">
            <div class="text-center mb-8">
                <img src="/static/images/marki-logo.png" alt="Marki Logo" class="h-16 mx-auto mb-4">
                <h1 class="text-2xl font-bold">SuperAdmin</h1>
            </div>
            
            <div x-data="superAdminPage()" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="protection-code">
                        Code de Protection
                    </label>
                    <input x-model="protectionCode" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="protection-code" type="text" placeholder="Entrez le code de protection">
                    <button @click="validateProtectionCode" class="mt-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                        Valider
                    </button>
                </div>
                
                <div x-show="isProtectedContentVisible" class="mt-8">
                    <h2 class="text-xl font-bold mb-4">Gestion des Utilisateurs</h2>
                    
                    <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2" for="user-id">
                            Identifiant
                        </label>
                        <input x-model="newUser.id" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="user-id" type="text" placeholder="Identifiant">
                    </div>
                    
                    <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2" for="user-password">
                            Mot de passe
                        </label>
                        <input x-model="newUser.password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="user-password" type="password" placeholder="Mot de passe">
                    </div>
                    
                    <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2">
                            Rôle
                        </label>
                        <label class="inline-flex items-center">
                            <input x-model="newUser.isAdmin" type="checkbox" class="form-checkbox">
                            <span class="ml-2">isAdmin</span>
                        </label>
                    </div>
                    
                    <button @click="createUser" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                        Créer
                    </button>
                    
                    <div class="mt-8">
                        <h2 class="text-xl font-bold mb-4">Liste des Utilisateurs</h2>
                        
                        <template x-for="user in users" :key="user.id">
                            <div class="mb-4 p-4 bg-gray-100 rounded">
                                <div class="flex justify-between items-center">
                                    <div>
                                        <p class="font-bold">Identifiant: <span x-text="user.id"></span></p>
                                        <p>Rôle: <span x-text="user.isAdmin ? 'Admin' : 'Utilisateur'"></span></p>
                                    </div>
                                    <div>
                                        <button @click="activateUser(user.id)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded focus:outline-none focus:shadow-outline mr-2" type="button">
                                            Activer
                                        </button>
                                        <button @click="modifyUser(user.id)" class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-1 px-2 rounded focus:outline-none focus:shadow-outline" type="button">
                                            Modifier
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Script Alpine.js
```html
<script>
function superAdminPage() {
    return {
        protectionCode: '',
        isProtectedContentVisible: false,
        newUser: {
            id: '',
            password: '',
            isAdmin: false
        },
        users: [],
        
        validateProtectionCode() {
            if (this.protectionCode === 'Citron6-Mustang9') {
                this.isProtectedContentVisible = true;
                this.loadUsers();
            } else {
                alert('Mot de passe de protection incorrect.');
            }
        },
        
        async loadUsers() {
            try {
                const response = await fetch('/api/users');
                const data = await response.json();
                this.users = data.users;
            } catch (error) {
                console.error('Erreur lors du chargement des utilisateurs:', error);
            }
        },
        
        async createUser() {
            try {
                const response = await fetch('/api/users', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.newUser)
                });
                const data = await response.json();
                if (data.status === 'success') {
                    alert('Utilisateur créé avec succès.');
                    this.newUser = { id: '', password: '', isAdmin: false };
                    this.loadUsers();
                } else {
                    alert('Erreur lors de la création de l\'utilisateur.');
                }
            } catch (error) {
                console.error('Erreur lors de la création de l\'utilisateur:', error);
            }
        },
        
        async activateUser(userId) {
            try {
                const response = await fetch(`/api/users/${userId}/activate`, {
                    method: 'POST'
                });
                const data = await response.json();
                if (data.status === 'success') {
                    alert('Utilisateur activé avec succès.');
                    this.loadUsers();
                } else {
                    alert('Erreur lors de l\'activation de l\'utilisateur.');
                }
            } catch (error) {
                console.error('Erreur lors de l\'activation de l\'utilisateur:', error);
            }
        },
        
        async modifyUser(userId) {
            try {
                const newPassword = prompt('Entrez le nouveau mot de passe:');
                if (newPassword) {
                    const response = await fetch(`/api/users/${userId}/modify`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ password: newPassword })
                    });
                    const data = await response.json();
                    if (data.status === 'success') {
                        alert('Mot de passe modifié avec succès.');
                        this.loadUsers();
                    } else {
                        alert('Erreur lors de la modification du mot de passe.');
                    }
                }
            } catch (error) {
                console.error('Erreur lors de la modification du mot de passe:', error);
            }
        }
    };
}
</script>
```

## 📝 Variables Globales
| Nom       | Type   | Description                          | Exemple          |
|-----------|--------|--------------------------------------|------------------|
| protectionCode | str | Code de protection pour afficher les composants de gestion des utilisateurs | "Citron6-Mustang9" |
| isProtectedContentVisible | bool | Indique si les composants de gestion des utilisateurs sont visibles | true |
| newUser | dict | Nouveau utilisateur à créer | { "id": "user1", "password": "password123", "isAdmin": true } |
| users | list | Liste des utilisateurs | [{ "id": "user1", "isAdmin": true }, { "id": "user2", "isAdmin": false }] |

## 📋 Flux Principal
1. Afficher le champ de mot de passe de protection.
2. Valider le mot de passe de protection avec Alpine.js.
3. Si le mot de passe est correct (`Citron6-Mustang9`), afficher les composants de gestion des utilisateurs.
4. Charger la liste des utilisateurs depuis l'API.
5. Permettre la création, l'activation, et la modification des mots de passe des utilisateurs administrateurs.
6. Utiliser Alpine.js pour les interactions utilisateur et les appels API.

## 🎨 Maquette ASCII
```
+-------------------------------------+
|  🏗 [MARKI] SUPERADMIN PAGE         |
|                                     |
|  +-------------------------------+  |
|  |  🔒 Code de Protection          |  |
|  |  ________________________     |  |
|  |  [🖱 Bouton] VALIDER            |  |
|  +-------------------------------+  |
|  |  📄 Gestion des Utilisateurs   |  |
|  |  (visible après validation)   |  |
|  |  +---------------------------+  |
|  |  |  📧 Identifiant            |  |
|  |  |  ________________________ |  |
|  |  |  🔒 Mot de passe           |  |
|  |  |  ________________________ |  |
|  |  |  📋 Rôle                   |  |
|  |  |  [✓] isAdmin              |  |
|  |  |  [🖱 Bouton] CRÉER        |  |
|  |  +---------------------------+  |
|  |  📄 Liste des Utilisateurs   |  |
|  |  (visible après validation)   |  |
|  |  +---------------------------+  |
|  |  |  📋 Utilisateur 1          |  |
|  |  |  [🖱 Bouton] ACTIVER      |  |
|  |  |  [🖱 Bouton] MODIFIER     |  |
|  |  +---------------------------+  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```