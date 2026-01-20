# Template: superadmin.html
**Fichier miroir** : `app/templates/superadmin.html`
**Base de données** : SQLite (`marki.db`)

## 📝 Description
Template pour la page SuperAdmin de l'application Marki. Il étend le template `simple.html` et inclut un formulaire de protection par mot de passe et des fonctionnalités de gestion des utilisateurs. La page utilise la base de données `marki.db` pour stocker et gérer les informations des utilisateurs.

## 📋 Blocs
- `title` : Titre de la page
- `content` : Contenu principal de la page

## 🎨 Couleurs Utilisées
- `text-text` : Texte principal
- `text-text-light` : Texte secondaire
- `bg-white` : Arrière-plan du formulaire
- `primary` : Bouton de validation
- `success` : Bouton de création
- `secondary` : Bouton de modification
- `bg-bg-light` : Arrière-plan des éléments de liste
- `border-border` : Bordures des champs de formulaire

## 📝 Notes
- Le template utilise les couleurs personnalisées définies dans `base.html`.
- Les boutons changent de couleur au survol pour une meilleure expérience utilisateur.
- Les champs de formulaire ont des effets de focus pour une meilleure accessibilité.
- La page utilise la base de données `marki.db` pour stocker les informations des utilisateurs et les logs des actions.

## 📊 Structure de la Base de Données

### Utilisateurs
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    isAdmin BOOLEAN DEFAULT FALSE,
    isActive BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Logs
```sql
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    action TEXT NOT NULL,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## 🔧 API de Gestion des Utilisateurs

### Routes
- **GET /api/users** : Récupère la liste des utilisateurs.
- **POST /api/users** : Crée un nouvel utilisateur.
- **POST /api/users/<user_id>/activate** : Active un utilisateur.
- **POST /api/users/<user_id>/modify** : Modifie le mot de passe d'un utilisateur.

### Exemple de Réponse (GET /api/users)
```json
{
    "users": [
        {
            "id": 1,
            "username": "admin",
            "isAdmin": true,
            "isActive": true
        }
    ]
}
```

### Exemple de Requête (POST /api/users)
```json
{
    "id": "nouvel_utilisateur",
    "password": "mot_de_passe",
    "isAdmin": true
}
```

### Exemple de Réponse (POST /api/users)
```json
{
    "status": "success",
    "message": "Utilisateur créé avec succès."
}
```
