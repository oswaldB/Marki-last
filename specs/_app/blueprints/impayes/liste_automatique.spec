# Blueprint: Gestion des listes automatiques
**Fichier miroir** : `app/blueprints/impayes/liste_automatique.py`
**Description** : Blueprint pour gérer les listes automatiques d'impayés.

---

## 🔧 Fonctions

### `creer_liste_automatique()`
**Description** :
- Crée une nouvelle liste automatique d'impayés.
- Définit les critères de filtrage pour la liste.

**Route** :
- **POST /listes-automatiques** : Crée une nouvelle liste automatique.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| nom | str | Nom de la liste automatique | "Liste Auto 1" |
| criteres | dict | Critères de filtrage pour la liste | {"statut": "impayé", "jours_retard": "> 30"} |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `peupler_liste_automatique(liste_id)`
**Description** :
- Peuple une liste automatique avec les impayés correspondant aux critères de filtrage.

**Route** :
- **POST /listes-automatiques/<liste_id>/peupler** : Peuple une liste automatique.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| liste_id | int | ID de la liste automatique à peupler | 1 |

**Retour** :
- Message de succès ou d'erreur au format JSON.

### `supprimer_liste_automatique(liste_id)`
**Description** :
- Supprime une liste automatique.
- Les impayés associés retournent dans le pool général.

**Route** :
- **DELETE /listes-automatiques/<liste_id>** : Supprime une liste automatique.

**Paramètres** :
| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| liste_id | int | ID de la liste automatique à supprimer | 1 |

**Retour** :
- Message de succès ou d'erreur au format JSON.

---

## 📝 Variables Globales

| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| `db` | SQLite | Instance de la base de données SQLite | `sqlite3.connect('marki.db')` |

---

## 📋 Flux Principal

1. **Création d'une liste automatique** :
   - Créer une nouvelle liste automatique.
   - Définir les critères de filtrage.

2. **Peuplement d'une liste automatique** :
   - Sélectionner une liste automatique existante.
   - Peupler la liste avec les impayés correspondant aux critères.

3. **Suppression d'une liste automatique** :
   - Sélectionner une liste automatique existante.
   - Supprimer la liste et retourner les impayés dans le pool général.

---

## 📊 Structure de la Base de Données SQLite

### Table `listes_automatiques`

```sql
CREATE TABLE listes_automatiques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    criteres TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Table `liste_automatique_impayes`

```sql
CREATE TABLE liste_automatique_impayes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liste_id INTEGER NOT NULL,
    impaye_id INTEGER NOT NULL,
    FOREIGN KEY (liste_id) REFERENCES listes_automatiques(id),
    FOREIGN KEY (impaye_id) REFERENCES impayes(id)
);
```

### Explications

- **listes_automatiques** :
  - **id** : Identifiant unique de la liste automatique, auto-incrémenté.
  - **nom** : Nom de la liste automatique.
  - **criteres** : Critères de filtrage pour la liste (stockés sous forme de JSON).
  - **created_at** : Date et heure de création de la liste.

- **liste_automatique_impayes** :
  - **id** : Identifiant unique de l'association, auto-incrémenté.
  - **liste_id** : ID de la liste automatique.
  - **impaye_id** : ID de l'impayé associé.

---

## 🎨 Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT LISTES AUTOMATIQUES |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - creer_liste_automatique()  |  |
|  |  - peupler_liste_automatique()|  |
|  |  - supprimer_liste_automatique() |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - db (SQLite)                |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Créer liste automatique   |  |
|  |  2. Peupler liste automatique |  |
|  |  3. Supprimer liste automatique |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```
