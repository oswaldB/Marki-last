# Blueprint: Synchronisation des impayés
**Fichier miroir** : `app/blueprints/impayes/synchronisation.py`
**Description** : Blueprint pour synchroniser les impayés depuis Marki Mirroir vers la base de données locale.

---

## 🔧 Fonctions

### `synchroniser_impayes()`
**Description** :
- Synchronise les données des impayés depuis Marki Mirroir.
- Met à jour la table `impayées` avec les données récupérées.
- Identifie les impayés avec des emails manquants.

**Route** :
- **GET /synchroniser-impayes** : Lance la synchronisation des impayés.

**Retour** :
- Message de succès ou d'erreur au format JSON.
- Liste des impayés avec emails manquants.

### `get_impayes_manquants()`
**Description** :
- Récupère la liste des impayés avec des emails manquants.
- Affiche une page dédiée pour la mise à jour manuelle.

**Route** :
- **GET /impayes-manquants** : Affiche la page des impayés avec emails manquants.

**Retour** :
- Rend le template `impayes_manquants.html` avec la liste des impayés concernés.

---

## 📝 Variables Globales

| Nom | Type | Description | Exemple |
|-----|------|-------------|---------|
| `MARKI_MIRROIR_API_URL` | str | URL de l'API Marki Mirroir | `https://api.markimirroir.com/impayes` |
| `MARKI_MIRROIR_API_KEY` | str | Clé d'API pour l'authentification | `abc123xyz` |

---

## 📋 Flux Principal

1. **Synchronisation des impayés** :
   - Établir une connexion à l'API Marki Mirroir.
   - Récupérer les données des impayés.
   - Mettre à jour la table `impayées` avec les données récupérées.
   - Identifier les impayés avec des emails manquants.

2. **Affichage des impayés manquants** :
   - Récupérer la liste des impayés avec emails manquants.
   - Afficher la page dédiée pour la mise à jour manuelle.

---

## 📊 Structure de la Base de Données SQLite

### Table `impayées`

```sql
CREATE TABLE impayes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference TEXT UNIQUE NOT NULL,
    montant REAL NOT NULL,
    date_echeance TEXT NOT NULL,
    statut TEXT NOT NULL,
    email_particulier TEXT,
    email_apporteur TEXT,
    jours_retard INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Explications

- **id** : Identifiant unique de l'impayé, auto-incrémenté.
- **reference** : Référence unique de l'impayé.
- **montant** : Montant de l'impayé.
- **date_echeance** : Date d'échéance de l'impayé.
- **statut** : Statut de l'impayé (par exemple, "impayé", "partiellement payé", "payé").
- **email_particulier** : Email du particulier (peut être NULL).
- **email_apporteur** : Email de l'apporteur (peut être NULL).
- **jours_retard** : Nombre de jours de retard.
- **created_at** : Date et heure de création de l'entrée.

---

## 🎨 Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] BLUEPRINT IMPAYÉS        |
|                                     |
|  +-------------------------------+  |
|  |  📋 Fonctions                  |  |
|  |  - synchroniser_impayes()     |  |
|  |  - get_impayes_manquants()    |  |
|  +-------------------------------+  |
|  |  📊 Variables Globales         |  |
|  |  - MARKI_MIRROIR_API_URL      |  |
|  |  - MARKI_MIRROIR_API_KEY      |  |
|  +-------------------------------+  |
|  |  📋 Flux Principal             |  |
|  |  1. Synchroniser impayés      |  |
|  |  2. Afficher impayés          |  |
|  |     manquants                 |  |
|  +-------------------------------+  |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```
