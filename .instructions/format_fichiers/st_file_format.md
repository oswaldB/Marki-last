# Format des Fichiers ST- (Spécifications Techniques)

Ce document définit le format et les conventions pour les fichiers de spécifications techniques (ST-) dans le projet Marki.

---

## 📂 Structure des Dossiers

Les fichiers de spécifications techniques doivent être organisés dans le dossier `specs/specs/` selon la structure suivante :

```bash
specs/
└── specs/
    ├── ST-<NUM>_<nom>-functionnelles.md  # Spécifications fonctionnelles
    └── ...
```

**Exemple** :
- `specs/specs/ST-001_hello-world-functionnelles.md`
- `specs/specs/ST-008_superadmin-page-functionnelles.md`

---

## 📄 Format du Fichier

### Nom du Fichier

Les fichiers de spécifications techniques doivent être nommés selon le format suivant :
- `ST-<NUM>_<nom>-functionnelles.md`

**Exemple** :
- `ST-001_hello-world-functionnelles.md`
- `ST-008_superadmin-page-functionnelles.md`

### Contenu du Fichier

Chaque fichier de spécifications techniques doit contenir les sections suivantes :

#### 1. **En-tête**
```markdown
# ST-<NUM> : <Titre de la Spécification>
**Date** : <YYYY-MM-DD>
**UI** : <Description de l'intégration UI, le cas échéant>.
```

**Exemple** :
```markdown
# ST-008 : Inscription Utilisateur
**Date** : 2026-01-16
**UI** : Intégration des logos et couleurs Marki.
```

#### 2. **Contexte**
Cette section doit décrire le contexte et l'objectif de la spécification.

```markdown
## 🎯 Contexte
<Description du contexte et de l'objectif de la spécification.>
```

**Exemple** :
```markdown
## 🎯 Contexte
Permettre une inscription en **< 30s** avec validation SQLite.
```

#### 3. **Règles Métier**
Cette section doit lister les règles métier à respecter.

```markdown
## 📜 Règles Métier
- <Règle 1>
- <Règle 2>
- <Règle 3>
```

**Exemple** :
```markdown
## 📜 Règles Métier
- Email : format valide + unique (SQLite).
- Mot de passe : 8+ caractères (1 maj, 1 chiffre).
- Nom : 2+ caractères, lettres uniquement.
```

#### 4. **Spécifications Techniques**
Cette section doit décrire les spécifications techniques détaillées, y compris les fonctions, les variables, et les flux.

```markdown
## 🔧 Spécifications Techniques

### Fonctions

#### `<Nom de la Fonction>`
**Description** :
<Description de la fonction.>

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| <param1>  | <type> | <validation>                   | <exemple>        |
| <param2>  | <type> | <validation>                   | <exemple>        |

**Retour** :
<Description du retour.>

**Exemple** :
```json
{ "status": "success|error", "message": str }
```

### Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| <variable1>       | <type> | <description>                        | <exemple>|
| <variable2>       | <type> | <description>                        | <exemple>|

### Flux Principal

1. <Étape 1>
2. <Étape 2>
3. <Étape 3>
```

**Exemple** :
```markdown
## 🔧 Spécifications Techniques

### Fonctions

#### `validate_email(email: str) -> bool`
**Description** :
Valide le format de l'email (regex: `^[^\s@]+@[^\s@]+\.[^\s@]+$`).
Vérifie l'unicité via SQLite (`db.getall()`).

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Regex + unicité SQLite         | test@example.com |

**Retour** :
`True` si valide et unique, `False` sinon.

#### `create_user(email: str, password: str, name: str) -> dict`
**Description** :
Hache le mot de passe (SHA-256).
Incrémente `user_counter` dans SQLite.
Stocke l'utilisateur sous la clé `user:<id>`.

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Regex + unicité SQLite         | test@example.com |
| password  | str    | 8+ chars (1 maj, 1 chiffre)     | Secure123        |
| name      | str    | 2+ chars, lettres uniquement   | Test User        |

**Retour** :
```json
{ "status": "success|error", "user_id": int, "message": str }
```

### Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| `user_counter`    | int    | Compteur auto-incrémenté (SQLite)    | 1       |
| `MIN_PASSWORD_LEN`| int    | Longueur minimale du mot de passe    | 8       |

### Flux Principal

1. Valider `email` et `password`.
2. Hacher le mot de passe.
3. Incrémenter `user_counter` et stocker dans SQLite :
   ```python
   # Pseudo-code (NE PAS COPIER DANS /app/)
   user_id = db.incr('user_counter')
   db.set(f'user:{user_id}', { 'email': email, 'password': hashed_password, 'name': name })
   ```
```

#### 5. **Maquettes UI**
Cette section doit inclure des maquettes ASCII ou des descriptions des interfaces utilisateur.

```markdown
## 🎨 Maquettes UI

### Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] INSCRIPTION              |
|                                     |
|  📧 Email     : ________________     |
|  🔒 Mot de passe : ________________  |
|  👤 Nom       : ________________     |
|                                     |
|  [🖱 Bouton] S'INSCRIRE              |
|  [🔗 Lien] Annuler                   |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

### Description

<Description des éléments de l'interface utilisateur.>
```

**Exemple** :
```markdown
## 🎨 Maquettes UI

### Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] INSCRIPTION              |
|                                     |
|  📧 Email     : ________________     |
|  🔒 Mot de passe : ________________  |
|  👤 Nom       : ________________     |
|                                     |
|  [🖱 Bouton] S'INSCRIRE              |
|  [🔗 Lien] Annuler                   |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

### Description

- **Logo Marki** : En-tête avec le logo Marki.
- **Champs** : Email, mot de passe, et nom.
- **Bouton** : Bouton d'inscription.
- **Lien** : Lien pour annuler.
- **Pied de page** : Powered by MARKI.
```

---

## 📝 Bonnes Pratiques

1. **Clarté** : Utilisez des descriptions claires et concises.
2. **Consistance** : Maintenez une consistance dans les formats et les conventions.
3. **Exemples** : Fournissez des exemples pour illustrer les spécifications.
4. **Mises à Jour** : Documentez toute mise à jour ou modification.
5. **Validation** : Assurez-vous que les spécifications sont validées par l'équipe avant d'être fusionnées.

---

## 📌 Exemple Complet

### Fichier : `specs/specs/ST-008_inscription-functionnelles.md`
```markdown
# ST-008 : Inscription Utilisateur
**Date** : 2026-01-16
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte

Permettre une inscription en **< 30s** avec validation SQLite.

---

## 📜 Règles Métier

- Email : format valide + unique (SQLite).
- Mot de passe : 8+ caractères (1 maj, 1 chiffre).
- Nom : 2+ caractères, lettres uniquement.

---

## 🔧 Spécifications Techniques

### Fonctions

#### `validate_email(email: str) -> bool`
**Description** :
Valide le format de l'email (regex: `^[^\s@]+@[^\s@]+\.[^\s@]+$`).
Vérifie l'unicité via SQLite (`db.getall()`).

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Regex + unicité SQLite         | test@example.com |

**Retour** :
`True` si valide et unique, `False` sinon.

#### `create_user(email: str, password: str, name: str) -> dict`
**Description** :
Hache le mot de passe (SHA-256).
Incrémente `user_counter` dans SQLite.
Stocke l'utilisateur sous la clé `user:<id>`.

**Paramètres** :
| Nom       | Type   | Validation                     | Exemple          |
|-----------|--------|--------------------------------|------------------|
| email     | str    | Regex + unicité SQLite         | test@example.com |
| password  | str    | 8+ chars (1 maj, 1 chiffre)     | Secure123        |
| name      | str    | 2+ chars, lettres uniquement   | Test User        |

**Retour** :
```json
{ "status": "success|error", "user_id": int, "message": str }
```

### Variables Globales

| Nom               | Type   | Description                          | Exemple |
|-------------------|--------|--------------------------------------|---------|
| `user_counter`    | int    | Compteur auto-incrémenté (SQLite)    | 1       |
| `MIN_PASSWORD_LEN`| int    | Longueur minimale du mot de passe    | 8       |

### Flux Principal

1. Valider `email` et `password`.
2. Hacher le mot de passe.
3. Incrémenter `user_counter` et stocker dans SQLite :
   ```python
   # Pseudo-code (NE PAS COPIER DANS /app/)
   user_id = db.incr('user_counter')
   db.set(f'user:{user_id}', { 'email': email, 'password': hashed_password, 'name': name })
   ```

---

## 🎨 Maquettes UI

### Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] INSCRIPTION              |
|                                     |
|  📧 Email     : ________________     |
|  🔒 Mot de passe : ________________  |
|  👤 Nom       : ________________     |
|                                     |
|  [🖱 Bouton] S'INSCRIRE              |
|  [🔗 Lien] Annuler                   |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

### Description

- **Logo Marki** : En-tête avec le logo Marki.
- **Champs** : Email, mot de passe, et nom.
- **Bouton** : Bouton d'inscription.
- **Lien** : Lien pour annuler.
- **Pied de page** : Powered by MARKI.
```

---

## 📌 Notes Supplémentaires

- Les spécifications techniques doivent être synchronisées avec les fichiers de spécifications dans `specs/_app/`.
- Toute modification doit être validée par l'équipe avant d'être fusionnée.
