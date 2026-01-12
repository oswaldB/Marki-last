# Script : Récupération des Pièces Non Réglées
**Fichier** : `app/scripts/fetch_unpaid_pieces.py`
**Description** : Script pour récupérer les pièces non réglées depuis une base de données PostgreSQL externe et les importer dans la base SQLite locale.

---
## Contexte
Ce script permet de synchroniser les pièces non réglées depuis une base de données PostgreSQL externe vers la base SQLite locale utilisée par l'application. Cela permet de centraliser les données et de faciliter leur gestion.

---
## Entrées
- **Base de données PostgreSQL externe** :
  - Les informations de connexion sont définies dans le fichier `.env` :
    - `POSTGRES_HOST` : Hôte de la base de données PostgreSQL.
    - `POSTGRES_PORT` : Port de la base de données PostgreSQL.
    - `POSTGRES_DB` : Nom de la base de données PostgreSQL.
    - `POSTGRES_USER` : Utilisateur de la base de données PostgreSQL.
    - `POSTGRES_PASSWORD` : Mot de passe de la base de données PostgreSQL.
  - Table : `pieces` (ou autre table spécifiée)

- **Base de données SQLite locale** :
  - Fichier : `app/blueprints/commissions.db`
  - Table : `commissions`

---
## Sorties
- **Base de données SQLite mise à jour** : Les pièces non réglées sont ajoutées à la table `commissions` avec un statut `valide`.
- **Fichier de log** : `reports/ST-<NUM>-fetch_unpaid_pieces.log`
  - Contient les détails de l'exécution (nombre de pièces récupérées, erreurs éventuelles, etc.).

---
## Étapes
1. **Connexion à la base PostgreSQL externe** :
   - Établir une connexion sécurisée à la base PostgreSQL.
   - Vérifier que la connexion est réussie.

2. **Récupération des pièces non réglées** :
   - Exécuter une requête pour sélectionner les pièces non réglées (par exemple, où `date_reglement` est `NULL` ou `statut` est `non_regele`).
   - Filtrer les pièces selon les critères définis (par exemple, `montant_ht > 0`).

3. **Transformation des données** :
   - Adapter les données récupérées au format de la table `commissions` (par exemple, mapper les champs `nfacture`, `ndossier`, etc.).
   - Définir le statut à `valide` pour les pièces importées.

4. **Insertion dans la base SQLite locale** :
   - Vérifier que la table `commissions` existe dans la base SQLite.
   - Insérer les pièces récupérées dans la table `commissions`.
   - Gérer les doublons (par exemple, éviter d'insérer une pièce déjà présente).

5. **Génération du rapport** :
   - Écrire un rapport dans le fichier de log avec les détails de l'exécution.
   - Inclure le nombre de pièces récupérées, les erreurs éventuelles, et les avertissements.

---
## Règles Métier
- **Pièces non réglées** : Seules les pièces avec un statut `non_regele` ou une `date_reglement` nulle sont récupérées.
- **Montant valide** : Le `montant_ht` doit être supérieur à 0.
- **Unicité des pièces** : Une pièce ne doit pas être dupliquée dans la base SQLite (vérification via `nfacture` ou `reference_piece`).
- **Statut par défaut** : Les pièces importées ont un statut `valide` par défaut.

---
## Exemple de Requête PostgreSQL
```sql
SELECT 
    nfacture,
    ndossier,
    reference_piece,
    intervenant,
    montant_ht,
    montant_ttc,
    date_piece,
    lien_facture
FROM pieces
WHERE date_reglement IS NULL AND montant_ht > 0;
```

---
## Exemple d'Appel
```bash
python app/scripts/fetch_unpaid_pieces.py \
    --log "reports/ST-<NUM>-fetch_unpaid_pieces.log"
```

> **Note** : Les informations de connexion à la base de données PostgreSQL sont lues depuis le fichier `.env`.

---
## Schéma SQL Associé
```sql
-- specs/bdd/commissions.sql
CREATE TABLE commissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nfacture TEXT NOT NULL,
    ndossier TEXT NOT NULL,
    reference_piece TEXT NOT NULL,
    intervenant TEXT NOT NULL,
    montant_ht REAL NOT NULL,
    montant_ttc REAL NOT NULL,
    date_piece TEXT NOT NULL,
    lien_facture TEXT NOT NULL,
    statut TEXT NOT NULL DEFAULT 'valide' CHECK (statut IN ('valide', 'conflit', 'archive')),
    date_reglement TEXT,
    conflit_detail TEXT,
    monotech BOOLEAN DEFAULT FALSE,
    mono_dossier BOOLEAN DEFAULT FALSE
);
```

---
## Liens
- [Spécifications fonctionnelles](../md/commissions_specs.md)
- [Scénarios Gherkin](../features/commissions.feature)

---
## Notes Techniques
- **Gestion des erreurs** : Le script doit gérer les erreurs de connexion, les requêtes SQL échouées, et les problèmes d'insertion.
- **Sécurité** : Les informations de connexion à la base PostgreSQL sont sécurisées via le fichier `.env`.
- **Performance** : Optimiser les requêtes pour éviter de surcharger la base PostgreSQL.
