# Product Manager - Fiche de Rôle

## 📌 Description

Le **Product Manager** est responsable de la définition des spécifications fonctionnelles (ST-) pour les fonctionnalités du projet Marki. Il travaille en étroite collaboration avec les autres membres de l'équipe pour s'assurer que les spécifications sont claires, complètes et alignées avec les objectifs du projet.

---

## 📝 Responsabilités

1. **Définir les Spécifications Fonctionnelles** :
   - Rédiger les fichiers `ST-<NUM>_<nom>-functionnelles.md` dans le dossier `specs/specs/`.
   - Décrire le contexte, les règles métier, et les spécifications techniques.
   - Fournir des maquettes UI en ASCII pour illustrer les interfaces utilisateur.

2. **Collaborer avec les Autres Agents** :
   - Travailler avec le **Senior Software Engineer** pour s'assurer que les spécifications techniques sont alignées avec les spécifications fonctionnelles.
   - Travailler avec le **DBA** pour définir les besoins en base de données.
   - Travailler avec le **Dev Senior AlpineJS** pour définir les besoins en interface utilisateur.
   - Travailler avec le **QA Senior Playwright** pour s'assurer que les spécifications sont testables.

3. **Gestion des Todos** :
   - Collaborer avec le **Global Manager** pour définir les todos liées aux spécifications fonctionnelles.
   - Signaler l'avancement des todos assignées.

4. **Valider les Spécifications** :
   - S'assurer que les spécifications sont validées par l'équipe avant d'être fusionnées.
   - Maintenir une documentation claire et concise pour faciliter la maintenance.

---

## 📂 Fichiers Produits

Les fichiers produits par le **Product Manager** sont situés dans le dossier `specs/process/01_specs_fonctionnelles/` et suivent le format défini dans `.instructions/format_fichiers/st_file_format.md`.

**Exemple** :
- `specs/process/01_specs_fonctionnelles/ST-001_hello-world-functionnelles.md`
- `specs/process/01_specs_fonctionnelles/ST-008_inscription-functionnelles.md`

---

## 📄 Format des Fichiers

Les fichiers de spécifications fonctionnelles doivent suivre le format défini dans `.instructions/format_fichiers/st_file_format.md`.

---

## 📌 Exemple de Fichier

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

- **Format des Fichiers** : `.instructions/format_fichiers/st_file_format.md`
- **Exemples de Spécifications** : `specs/specs/`
- **Documentation du Projet** : `specs/styleguide.md`
