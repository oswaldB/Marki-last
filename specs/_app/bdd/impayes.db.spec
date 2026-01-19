# Base de Données : impayes.db
**Description** : Spécifications pour la base de données SQLite des impayés.

---

## 📊 Tables

### Table `impayes`

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

**Description des champs** :
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

### Table `listes_manuelles`

```sql
CREATE TABLE listes_manuelles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Description des champs** :
- **id** : Identifiant unique de la liste manuelle, auto-incrémenté.
- **nom** : Nom de la liste manuelle.
- **created_at** : Date et heure de création de la liste.

---

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

**Description des champs** :
- **id** : Identifiant unique de l'association, auto-incrémenté.
- **liste_id** : ID de la liste manuelle.
- **impaye_id** : ID de l'impayé associé.

---

### Table `listes_automatiques`

```sql
CREATE TABLE listes_automatiques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    criteres TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Description des champs** :
- **id** : Identifiant unique de la liste automatique, auto-incrémenté.
- **nom** : Nom de la liste automatique.
- **criteres** : Critères de filtrage pour la liste (stockés sous forme de JSON).
- **created_at** : Date et heure de création de la liste.

---

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

**Description des champs** :
- **id** : Identifiant unique de l'association, auto-incrémenté.
- **liste_id** : ID de la liste automatique.
- **impaye_id** : ID de l'impayé associé.

---

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

**Description des champs** :
- **id** : Identifiant unique de la séquence, auto-incrémenté.
- **nom** : Nom de la séquence.
- **templates** : Templates dynamiques de la séquence (stockés sous forme de JSON).
- **is_active** : Indique si la séquence est active.
- **created_at** : Date et heure de création de la séquence.

---

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

**Description des champs** :
- **id** : Identifiant unique de l'association, auto-incrémenté.
- **sequence_id** : ID de la séquence.
- **liste_id** : ID de la liste associée.
- **type_liste** : Type de liste (manuelle ou automatique).

---

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

**Description des champs** :
- **id** : Identifiant unique de l'action, auto-incrémenté.
- **sequence_id** : ID de la séquence.
- **impaye_id** : ID de l'impayé.
- **template** : Template de l'email.
- **date_envoi** : Date d'envoi de l'email.
- **statut** : Statut de l'action (par exemple, "à envoyer", "envoyé", "erreur").

---

## 📝 Notes

- Les tables sont conçues pour gérer les impayés, les listes manuelles et automatiques, les séquences d'emails et les actions de relance.
- Les clés étrangères sont utilisées pour maintenir l'intégrité des données.
- Les champs de type `TEXT` peuvent contenir des données JSON pour une flexibilité accrue.
