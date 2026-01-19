# ST-009 : Synchronisation des impayés

**Date** : 19/01/2026
**Acteurs** : Specificator
**Statut** : À valider

---

## **1. Contexte**
Ce script automatise la synchronisation des impayés entre une base **PostgreSQL (mirroir)** et la base **SQLite locale** de l'application Marki.
Il cible :
- Les **nouveaux impayés** (présents en PostgreSQL mais absents en SQLite).
- Les impayés **marqués comme invalides** (`valide = false` en PostgreSQL) nécessitant une mise à jour en SQLite.

---

## **2. Prérequis**
### **2.1 Environnement**
- Fichier `.env` à la racine du projet avec les variables suivantes :
  ```env
  DB_MIRROIR_HOST=<hôte>
  DB_MIRROIR_PORT=<port>
  DB_MIRROIR_USER=<utilisateur>
  DB_MIRROIR_PASSWORD=<mot_de_passe>
  DB_MIRROIR_NAME=<nom_base>
  ```
- Base SQLite (`marki.db`) avec une table `impayes` contenant les colonnes :
  | Colonne   | Type      | Description                     |
  |-----------|-----------|---------------------------------|
  | id        | INTEGER   | Identifiant unique              |
  | email     | TEXT      | Adresse email du client         |
  | montant   | REAL      | Montant de l'impayé             |
  | date      | TEXT      | Date de l'impayé (format ISO)   |
  | valide    | BOOLEAN   | Statut de validité (true/false) |

### **2.2 Dépendances**
- Python 3.10+
- Bibliothèques : `psycopg2-binary`, `sqlite3`, `python-dotenv`

---

## **3. Spécification fonctionnelle**
### **3.1 Workflow**
1. **Connexion aux bases** :
   - Lecture des credentials PostgreSQL depuis `.env`.
   - Connexion à PostgreSQL et SQLite.
2. **Récupération des données** :
   - Requête PostgreSQL pour identifier :
     - Les impayés **non présents en SQLite** :
       ```sql
       SELECT * FROM impayes_mirror
       WHERE id NOT IN (SELECT id FROM impayes);
       ```
     - Les impayés **invalides en PostgreSQL** mais valides en SQLite :
       ```sql
       SELECT * FROM impayes_mirror
       WHERE valide = false AND id IN (SELECT id FROM impayes WHERE valide = true);
       ```
3. **Synchronisation** :
   - **Insertion** des nouveaux impayés en SQLite.
   - **Mise à jour** du statut `valide` pour les impayés existants.
4. **Logging** :
   - Écriture des actions dans `sync_impayes.log` (format : `[timestamp] ACTION: id=<id>, email=<email>`).
   - Retour console pour Playwright (format JSON structuré).

### **3.2 Règles métier**
- **Conflits** : En cas de doublon sur l'`id`, la donnée PostgreSQL écrase SQLite.
- **Erreurs** : Les échecs de connexion ou de requête doivent être logués et interrompre le script (code de sortie `1`).
- **Performances** : Le script doit traiter **au moins 1000 enregistrements/minute**.

---

## **4. Scénarios Gherkin**
```gherkin
Feature: Synchronisation des impayés entre PostgreSQL et SQLite
  Scenario: Ajout d'un nouvel impayé
    Given Un impayé existe en PostgreSQL avec id=123 et valide=true
    And Cet impayé n'existe pas en SQLite
    When Le script de synchronisation est exécuté
    Then L'impayé est inséré en SQLite avec les mêmes données
    And Un log est généré : "[timestamp] INSERT: id=123, email=client@exemple.com"

  Scenario: Mise à jour d'un impayé invalide
    Given Un impayé existe en SQLite avec id=456, valide=true
    And En PostgreSQL, le même impayé a valide=false
    When Le script de synchronisation est exécuté
    Then La valeur "valide" est mise à jour en SQLite pour id=456
    And Un log est généré : "[timestamp] UPDATE: id=456, valide=false"

  Scenario: Échec de connexion à PostgreSQL
    Given Les credentials PostgreSQL sont invalides
    When Le script est exécuté
    Then Le script s'arrête avec code 1
    And Un log d'erreur est généré : "[timestamp] ERROR: Impossible de se connecter à PostgreSQL"
```

---

## **5. Intégration front-end (Alpine.js)**
**Composant** : `impayes_sync.html` (à créer dans `/app/templates/components/`)
- **Fonctionnalités** :
  - Bouton pour déclencher la synchronisation.
  - Affichage du statut (en cours/terminé/erreur).
  - Lien vers le fichier de log généré.
- **Exemple d'état** :
  ```javascript
  function impayesSyncState() {
    return {
      isSyncing: false,
      lastSync: null,
      error: null,
      async triggerSync() {
        this.isSyncing = true;
        try {
          const response = await fetch("/api/sync-impayes");
          this.lastSync = await response.json();
        } catch (e) {
          this.error = e.message;
        } finally {
          this.isSyncing = false;
        }
      }
    };
  }
  ```

**Route Flask** : `/api/sync-impayes` (méthode `GET`)
- **Réponse attendue** :
  ```json
  {
    "status": "success",
    "stats": {
      "inserted": 5,
      "updated": 2,
      "errors": 0
    },
    "log_path": "/reports/sync_impayes_20260119.log"
  }
  ```

---

## **6. Gestion des emails manquants**
**Composant dédié** : `emails_missing.html` (URL : `/emails-missing`)
- **Données affichées** :
  | Colonne       | Description                          |
  |---------------|--------------------------------------|
  | email         | Adresse email du client              |
  | montant       | Montant de l'impayé                  |
  | date          | Date de l'impayé                     |
  | actions       | Bouton "Renvoyer l'email"            |

---

## **7. Livrables attendus**
| Acteur         | Livrable                                  | Emplacement                     |
|----------------|-------------------------------------------|---------------------------------|
| Specificator   | Ce fichier de spécification              | `/specs/specs/ST-009_...md`     |
| Codifia        | Script Python (`sync_impayes.py`)         | `/app/scripts/`                 |
| Codifia        | Composants Alpine.js                     | `/app/templates/components/`    |
| Codifia        | Route Flask (`/api/sync-impayes`)         | `/app/routes.py`                |
| RedacTestor    | Tests unitaires (pytest)                  | `/tests/test_sync_impayes.py`   |
| TravauxFini    | Rapport d'exécution                      | `/reports/sync_impayes_*.log`   |