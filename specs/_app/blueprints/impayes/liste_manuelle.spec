# Blueprint: Gestion des listes manuelles
**Fichier miroir** : `app/blueprints/impayes/liste_manuelle.py`
**Description** : Blueprint pour gérer les listes manuelles d'impayés.

---

## 🔧 Fonctions

### `creer_liste_manuelle()`
**Description** :
- Crée une nouvelle liste manuelle d'impayés.
- Permet l'ajout d'impayés en batch.

**Route** :
- **POST /listes-manuelles** : Crée une nouvelle liste manuelle.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| nom | str | Nom de la liste manuelle | "Liste 1" |
| impayes_ids | list | Liste des IDs des impayés à ajouter | [1, 2, 3] |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `modifier_liste_manuelle(liste_id)`
**Description** :
- Modifie une liste manuelle existante.
- Permet l'ajout ou la suppression d'impayés en batch.

**Route** :
- **PUT /listes-manuelles/<liste_id>** : Modifie une liste manuelle.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| liste_id | int | ID de la liste manuelle à modifier | 1 |
| impayes_ids | list | Liste des IDs des impayés à ajouter ou supprimer | [1, 2, 3] |
| action | str | Action à effectuer (ajouter/supprimer) | "ajouter" |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `supprimer_liste_manuelle(liste_id)`
**Description** :
- Supprime une liste manuelle.
- Les impayés associés retournent dans le pool général.

**Route** :
- **DELETE /listes-manuelles/<liste_id>** : Supprime une liste manuelle.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| liste_id | int | ID de la liste manuelle à supprimer | 1 |

**Retour** :
- Message de succès ou d'erreur au format JSON.

---

## 📝 Variables Globales

| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| `db` | SQLite | Instance de la base de données SQLite | `sqlite3.connect('marki.db')` |

---

## 📋 Flux Principal

1. **Création d'une liste manuelle** :
   - Créer une nouvelle liste manuelle.
   - Ajouter des impayés en batch.

2. **Modification d'une liste manuelle** :
   - Sélectionner une liste manuelle existante.
   - Ajouter ou supprimer des impayés en batch.

3. **Suppression d'une liste manuelle** :
   - Sélectionner une liste manuelle existante.
   - Supprimer la liste et retourner les impayés dans le pool général.

---

## 📊 Structure de la Base de Données SQLite

### Table `listes_manuelles`

```sql
CREATE TABLE listes_manuelles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Table `liste_manuelle_impayes`

```sql
CREATE TABLE liste_manuelle_impayes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liste_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    FOREIGN KEY (liste_id) REFERENCES listes_manuelles(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications

- **listes_manuelles** :
  - **id** : Identifiant unique de la liste manuelle, auto-incrémenté.
  - **nom** : Nom de la liste manuelle.
  - **created_at** : Date et heure de création de la liste.

- **liste_manuelle_impayes** :
  - **id** : Identifiant unique de l'association, auto-incrémenté.
  - **liste_id** : ID de la liste manuelle.
  - **impaye_id** : ID de l'impayé associé.

---

## 🎨 Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT LISTES MANUELLES |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - creer_liste_manuelle()     |  |
|  |  - modifier_liste_manuelle()  |  |
|  |  - supprimer_liste_manuelle() |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - db (SQLite)                |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Créer liste manuelle     |  |
|  |  2. Modifier liste manuelle  |  |
|  |  3. Supprimer liste manuelle  |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```
