# Script : Traitement des Commissions des Techniciens
**Fichier** : `app/scripts/process_commissions.py`
**Description** : Script pour calculer et enregistrer les commissions des techniciens à partir des factures et des missions associées, en vérifiant la cohérence des données et en gérant les cas particuliers (factures mono-technicien, articles en pack, etc.).

---
## Contexte
Ce script permet de traiter les factures et les missions associées pour calculer les commissions des techniciens. Il gère les cas particuliers tels que les factures mono-technicien, les articles en pack, et les incohérences entre les articles et les missions.

---
## Entrées
- **Base de données PostgreSQL externe** :
  - Les informations de connexion sont définies dans le fichier `.env` :
    - `POSTGRES_HOST` : Hôte de la base de données PostgreSQL.
    - `POSTGRES_PORT` : Port de la base de données PostgreSQL.
    - `POSTGRES_DB` : Nom de la base de données PostgreSQL.
    - `POSTGRES_USER` : Utilisateur de la base de données PostgreSQL.
    - `POSTGRES_PASSWORD` : Mot de passe de la base de données PostgreSQL.
  - Tables : `(GCO) GcoPiece`, `(GCO) GcoPieceVente`, `(GCO) GcoArticle`, `(ADN_DIAG) Mission`, `(ADN_RG)Employe`

- **Base de données SQLite locale** :
  - Fichier : `app/blueprints/commissions.db`
  - Table : `commissions`

---
## Sorties
- **Base de données SQLite mise à jour** : Les commissions des techniciens sont enregistrées dans la table `commissions` avec un statut approprié (`valide`, `conflit`, ou `archive`).
- **Fichier de log** : `reports/ST-<NUM>-process_commissions.log`
  - Contient les détails de l'exécution (nombre de factures traitées, erreurs éventuelles, conflits, etc.).

---
## Étapes
1. **Déclencheurs** :
   - Le script peut être déclenché de deux manières :
     - **Route** : Lorsqu’une requête est envoyée à l’URL `/api/process-commissions` avec un paramètre `nfacture` (numéro de facture).
     - **Planification** : Tous les jours à 6h00, 14h00 et 17h00 (via un cron ou un planificateur de tâches).

2. **Récupération des données initiales** :
   - **Facture (GCO Piece)** : Récupérer les informations de base de la facture (numéro, référence, dates, montant HT, validité, ID de la pièce).
   - **Articles de la facture (GCO PieceVente)** : Lister tous les articles associés à la facture, avec leur prix unitaire HT, montant HT et ID métier (lien vers le dossier/mission).
   - **Vérification des articles** : Si la facture ne contient aucun article, mettre le statut à `conflit` avec le message `"Pas d'article dans la facture"`.
   - **Détails des articles (GCO Article)** : Pour chaque article, récupérer ses détails (intitulé, catégorie, type, si c’est un pack, etc.).
   - **Traitement des packs** : Si l’article est un pack, récupérer la répartition des prix entre les articles du pack et recalculer les prix unitaire et montant HT.

3. **Récupération des missions associées** :
   - **Lien entre article et mission (GCO PieceMetier)** : Trouver les `idmetier` (IDs des dossiers/missions) liés à la facture.
   - **Techniciens et catégories de mission (ADN_DIAG Mission)** : Pour chaque `idmetier`, récupérer l’ID du technicien, la catégorie et le type de mission, le nom du technicien, et l’ID du dossier.
   - **Vérification de la cohérence des techniciens** : Vérifier si tous les articles de la facture sont associés au même technicien (`dossierMonoTech = true`).
   - **Agrégation des missions par dossier** : Regrouper les missions par `idDossier` et `factureMonoTech` (oui/non).

4. **Vérification de la correspondance articles/missions** :
   - **Comparaison du nombre d’articles et de missions** : Si le nombre d’articles ≠ nombre de missions, mettre le statut à `conflit` avec le message `"Impossible d'associer les articles de la facture avec les missions"`.
   - **Association des articles aux missions** : Pour chaque mission, calculer le montant total HT des articles qui lui correspondent (même catégorie et type).
   - **Vérification des missions éligibles** : Si aucune mission éligible n’est trouvée, la facture est ignorée.

5. **Préparation des données pour l’enregistrement** :
   - **Construction du payload final** : Préparer les données pour l’enregistrement dans la base SQLite, incluant les champs principaux tels que `nfacture`, `techniciens`, `datepiece`, `totalhtnet`, `valide`, `dossier`, `factureMonoTech`, `url`, `statut`, `articles`, et `missions`.

6. **Enregistrement dans SQLite** :
   - **Création ou mise à jour de l’entrée** : Si la facture n’existe pas dans la base SQLite, une nouvelle entrée est créée dans la table `commissions`. Si la facture existe déjà, l’entrée est mise à jour.
   - **Gestion des conflits** : Les détails des conflits sont enregistrés dans le champ `conflit_detail`.

---
## Règles Métier
- **Facture sans article** : Mettre le statut à `conflit` avec le message `"Pas d'article dans la facture"`.
- **Facture mono-technicien** : Si tous les articles de la facture sont associés au même technicien, marquer la facture comme `monotech = true`.
- **Articles en pack** : Répartir les montants HT selon les règles du pack.
- **Incohérence articles/missions** : Mettre le statut à `conflit` avec le message `"Impossible d'associer les articles de la facture avec les missions"`.
- **Facture multi-technicien** : Si plusieurs techniciens sont impliqués, marquer la facture comme `monotech = false`.
- **Statut par défaut** : Les factures traitées sans conflit ont un statut `valide`.

---
## Exemple de Requêtes PostgreSQL
### Récupération de la facture
```sql
SELECT
    p."nfacture",
    p."refpiece",
    p."datecre",
    p."datepiece",
    p."totalhtnet",
    p."valide",
    p."idpiece"
FROM
    "public"."(GCO) GcoPiece" p
WHERE
    p."nfacture" = '{{ $json.query.nfacture }}';
```

### Récupération des articles de la facture
```sql
SELECT
    "public"."(GCO) GcoPieceVente"."idpiece" AS "idpiece",
    "public"."(GCO) GcoPieceVente"."idarticle" AS "idarticle",
    "public"."(GCO) GcoPieceVente"."puhtnet" AS "puhtnet",
    "public"."(GCO) GcoPieceVente"."montantht" AS "montantht",
    "public"."(GCO) GcoPieceVente"."idmetier" AS "idmetier"
FROM
    "public"."(GCO) GcoPieceVente"
WHERE
    "public"."(GCO) GcoPieceVente"."idpiece" = {{ $json.idpiece }}
```

### Récupération des détails des articles
```sql
SELECT
    "public"."(GCO) GcoArticle".*,
FROM
    "public"."(GCO) GcoArticle"
WHERE
    "public"."(GCO) GcoArticle"."idarticle" = {{ $json.idarticle }}
```

### Récupération des missions associées
```sql
SELECT
    "public"."(ADN_DIAG) Mission"."idMission" AS "idMission",
    "public"."(ADN_DIAG) Mission"."idIntervenant" AS "idIntervenant",
    "public"."(ADN_DIAG) Mission"."idCategorieMission" AS "idCategorieMission",
    "public"."(ADN_DIAG) Mission"."idTypeMission" AS "idTypeMission",
    CONCAT(
        "(adn RG)Employe - IdIntervenant"."prenom",
        ' ',
        "(adn RG)Employe - IdIntervenant"."nom"
    ) AS "tech",
    "public"."(ADN_DIAG) Mission"."idDossier" AS "idDossier"
FROM
    "public"."(ADN_DIAG) Mission"
LEFT JOIN "public"."(ADN_RG)Employe" AS "(adn RG)Employe - IdIntervenant"
    ON "public"."(ADN_DIAG) Mission"."idIntervenant" = "(adn RG)Employe - IdIntervenant"."idEmploye"
WHERE
    "public"."(ADN_DIAG) Mission"."idDossier" = {{ $json.idmetier }}
```

---
## Exemple d'Appel
```bash
python app/scripts/process_commissions.py \
    --log "reports/ST-<NUM>-process_commissions.log"
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

> **Enum des statuts** :
> - `valide` : La commission est validée et prête à être réglée.
> - `conflit` : La commission est en conflit et nécessite une intervention manuelle.
> - `archive` : La commission est archivée et n'est plus active.

---
## Liens
- [Spécifications fonctionnelles](../md/commissions_specs.md)
- [Scénarios Gherkin](../features/commissions.feature)

---
## Notes Techniques
- **Gestion des erreurs** : Le script doit gérer les erreurs de connexion, les requêtes SQL échouées, et les problèmes d'insertion.
- **Sécurité** : Les informations de connexion à la base PostgreSQL sont sécurisées via le fichier `.env`.
- **Performance** : Optimiser les requêtes pour éviter de surcharger la base PostgreSQL.
- **Gestion des packs** : La logique de répartition des prix doit être validée avec les règles métiers.
- **Doublons** : Vérifier que la facture n’a pas déjà été traitée pour éviter les doublons.
