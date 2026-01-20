# Senior Software Engineer - Fiche de Rôle

## 📌 Description

Le **Senior Software Engineer** est responsable de la définition des spécifications techniques pour les blueprints, les templates, et les bases de données du projet Marki. Il travaille en étroite collaboration avec les autres membres de l'équipe pour s'assurer que les spécifications techniques sont claires, complètes et alignées avec les spécifications fonctionnelles.

---

## 📝 Responsabilités

1. **Définir les Spécifications Techniques** :
   - Rédiger les fichiers de spécifications techniques dans le dossier `specs/_app/`.
   - Décrire les fonctions, les variables globales, et les flux principaux pour les blueprints.
   - Décrire les composants et la structure HTML pour les templates.
   - Décrire les tables, les relations, et les exemples de requêtes pour les bases de données.

2. **Collaborer avec les Autres Agents** :
   - Travailler avec le **Product Manager** pour s'assurer que les spécifications techniques sont alignées avec les spécifications fonctionnelles.
   - Travailler avec le **DBA** pour définir les besoins en base de données.
   - Travailler avec le **Dev Senior Python** pour définir les besoins en backend.
   - Travailler avec le **Dev Senior AlpineJS** pour définir les besoins en frontend.
   - Travailler avec le **QA Senior Playwright** pour s'assurer que les spécifications sont testables.

3. **Valider les Spécifications** :
   - S'assurer que les spécifications techniques sont validées par l'équipe avant d'être fusionnées.
   - Maintenir une documentation claire et concise pour faciliter la maintenance.

---

## 📂 Fichiers Produits

Les fichiers produits par le **Senior Software Engineer** sont situés dans les dossiers `specs/_app/` et `specs/process/02_specs_techniques/` et suivent les formats définis dans `.instructions/format_fichiers/`.

**Exemple** :
- Spécifications d'un blueprint : `specs/process/02_specs_techniques/ST-001_blueprint-auth.spec`
- Spécifications d'un template : `specs/process/02_specs_techniques/ST-002_template-login.spec`
- Spécifications d'une BDD : `specs/process/02_specs_techniques/ST-003_bdd-marki.spec`

---

## 📄 Format des Fichiers

Les fichiers de spécifications techniques doivent suivre les formats définis dans `.instructions/format_fichiers/` :

- **Blueprints** : `.instructions/format_fichiers/blueprint_format.md`
- **Templates** : `.instructions/format_fichiers/partial_alpinejs_format.md`
- **Pages** : `.instructions/format_fichiers/page_format.md`
- **BDD** : `.instructions/format_fichiers/bdd_documentation_rules.md`

---

## 📌 Exemple de Fichier

### Fichier : `specs/_app/blueprints/auth/auth.spec`

```markdown
# Blueprint: Auth
**Fichier miroir** : `app/blueprints/auth/routes.py`
**Description** : Gestion de l'authentification des utilisateurs.
**Date de création** : 2026-01-20
**Auteur** : Oswald Bernard

---

## 📍 Routes

| Route               | Méthode | Description                          | Fonction associée       |
|---------------------|---------|--------------------------------------|------------------------|
| `/login`            | POST    | Connexion de l'utilisateur           | `login_user`           |
| `/register`         | POST    | Inscription de l'utilisateur         | `register_user`        |
| `/logout`           | GET     | Déconnexion de l'utilisateur         | `logout_user`          |

---

## 🔧 Fonctions

### `login_user`
**Description** :
Authentifie un utilisateur et retourne un token.

**Route** : `/login`

**Méthode** : `POST`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Format valide et existe en BDD | test@example.com |
| password  | str    | Correspond au hash en BDD      | Secure123        |

**Retour** :
```json
{ "status": "success|error", "token": str, "message": str }
```

**Code** :
```python
@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    # Logique d'authentification
    pass
```

### `register_user`
**Description** :
Enregistre un nouvel utilisateur.

**Route** : `/register`

**Méthode** : `POST`

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Format valide et unique        | test@example.com |
| password  | str    | 8+ caractères (1 maj, 1 chiffre)| Secure123        |
| name      | str    | 2+ caractères, lettres uniquement| Test User        |

**Retour** :
```json
{ "status": "success|error", "user_id": int, "message": str }
```

**Code** :
```python
@bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    # Logique d'inscription
    pass
```

---

## 📝 Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| `user_counter`    | int    | Compteur auto-incrémenté (SQLite)    | 1       |
| `MIN_PASSWORD_LEN`| int    | Longueur minimale du mot de passe    | 8       |

---

## 📋 Flux Principal

1. L'utilisateur soumet le formulaire de connexion.
2. Le serveur valide les informations d'identification.
3. Si valide, un token est généré et retourné.
4. Si invalide, une erreur est retournée.
```

---

## 📌 Bonnes Pratiques

1. **Clarté** : Utilisez des descriptions claires et concises.
2. **Consistance** : Maintenez une consistance dans les formats et les conventions.
3. **Exemples** : Fournissez des exemples pour illustrer les spécifications.
4. **Mises à Jour** : Documentez toute mise à jour ou modification.
5. **Validation** : Assurez-vous que les spécifications sont validées par l'équipe avant d'être fusionnées.

---

## 📌 Outils et Ressources

- **Format des Fichiers** : `.instructions/format_fichiers/`
- **Exemples de Spécifications** : `specs/_app/`
- **Documentation du Projet** : `specs/styleguide.md`
