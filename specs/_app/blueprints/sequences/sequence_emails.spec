# Blueprint: Gestion des séquences d'emails
**Fichier miroir** : `app/blueprints/sequences/sequence_emails.py`
**Description** : Blueprint pour gérer les séquences d'emails.

---

## 🔧 Fonctions

### `creer_sequence()`
**Description** :
- Crée une nouvelle séquence d'emails.
- Définit les templates dynamiques et les délais.

**Route** :
- **POST /sequences** : Crée une nouvelle séquence.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| nom | str | Nom de la séquence | "Séquence 1" |
| templates | list | Liste des templates dynamiques | [{"contenu": "Bonjour {{nom}}", "delai": 1}] |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `modifier_sequence(sequence_id)`
**Description** :
- Modifie une séquence d'emails existante.
- Les changements ne s'appliquent pas aux actions déjà générées.

**Route** :
- **PUT /sequences/<sequence_id>** : Modifie une séquence.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| sequence_id | int | ID de la séquence à modifier | 1 |
| templates | list | Liste des templates dynamiques | [{"contenu": "Bonjour {{nom}}", "delai": 1}] |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `associer_liste_sequence(liste_id, sequence_id)`
**Description** :
- Associe une liste (manuelle ou automatique) à une séquence.

**Route** :
- **POST /sequences/<sequence_id>/associer-liste** : Associe une liste à une séquence.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| sequence_id | int | ID de la séquence | 1 |
| liste_id | int | ID de la liste à associer | 1 |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `activer_sequence(sequence_id)`
**Description** :
- Active une séquence d'emails.
- Génère les actions dans `relances-actions` pour tous les impayés de la liste associée.

**Route** :
- **POST /sequences/<sequence_id>/activer** : Active une séquence.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| sequence_id | int | ID de la séquence à activer | 1 |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `desactiver_sequence(sequence_id)`
**Description** :
- Désactive une séquence d'emails.
- Supprime toutes les actions non envoyées dans `relances-actions`.

**Route** :
- **POST /sequences/<sequence_id>/desactiver** : Désactive une séquence.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| sequence_id | int | ID de la séquence à désactiver | 1 |

**Retour** :
- Message de succès ou d'erreur au format JSON.

---

## 📝 Variables Globales

| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| `db` | SQLite | Instance de la base de données SQLite | `sqlite3.connect('marki.db')` |

---

## 📋 Flux Principal

1. **Création d'une séquence** :
   - Créer une nouvelle séquence.
   - Définir les templates dynamiques et les délais.

2. **Modification d'une séquence** :
   - Sélectionner une séquence existante.
   - Modifier les templates ou les délais.

3. **Association d'une liste à une séquence** :
   - Sélectionner une liste et une séquence.
   - Associer la liste à la séquence.

4. **Activation d'une séquence** :
   - Sélectionner une séquence associée à une liste.
   - Activer la séquence et générer les actions.

5. **Désactivation d'une séquence** :
   - Sélectionner une séquence active.
   - Désactiver la séquence et supprimer les actions non envoyées.

---

## 📊 Structure de la Base de Données SQLite

### Table `sequences`

```sql
CREATE TABLE sequences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    templates TEXT NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Table `sequence_listes`

```sql
CREATE TABLE sequence_listes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER NOT NULL,
    liste_id INTEGER NOT NULL,
    type_liste TEXT NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequences(id)
);
```

### Table `relances_actions`

```sql
CREATE TABLE relances_actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    template TEXT NOT NULL,
    date_envoi TEXT NOT NULL,
    statut TEXT NOT NULL,
    FOREIGN KEY (sequence_id) REFERENCES sequences(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications

- **sequences** :
  - **id** : Identifiant unique de la séquence, auto-incrémenté.
  - **nom** : Nom de la séquence.
  - **templates** : Templates dynamiques de la séquence (stockés sous forme de JSON).
  - **is_active** : Indique si la séquence est active.
  - **created_at** : Date et heure de création de la séquence.

- **sequence_listes** :
  - **id** : Identifiant unique de l'association, auto-incrémenté.
  - **sequence_id** : ID de la séquence.
  - **liste_id** : ID de la liste associée.
  - **type_liste** : Type de liste (manuelle ou automatique).

- **relances_actions** :
  - **id** : Identifiant unique de l'action, auto-incrémenté.
  - **sequence_id** : ID de la séquence.
  - **impaye_id** : ID de l'impayé.
  - **template** : Template de l'email.
  - **date_envoi** : Date d'envoi de l'email.
  - **statut** : Statut de l'action (par exemple, "à envoyer", "envoyé", "erreur").

---

## 🎨 Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT SÉQUENCES EMAILS |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - creer_sequence()           |  |
|  |  - modifier_sequence()         |  |
|  |  - associer_liste_sequence()   |  |
|  |  - activer_sequence()          |  |
|  |  - desactiver_sequence()       |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - db (SQLite)                |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Créer séquence            |  |
|  |  2. Modifier séquence         |  |
|  |  3. Associer liste            |  |
|  |  4. Activer séquence          |  |
|  |  5. Désactiver séquence       |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```
