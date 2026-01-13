# Gestion des Commissions
**Version** : 1.0
**Statut** : En cours

---
## 1. Contexte
Permettre aux utilisateurs de gérer les commissions, y compris la validation, la résolution des conflits, et le règlement des commissions.

## 2. Structure des Données

### 2.1. Collections PickleDB

La base de données `commissions.db` est organisée en collections PickleDB pour stocker les informations relatives aux commissions.

#### Collection `commissions`

Stocke les informations sur les commissions générées pour les techniciens.

**Clé Primaire** : `nfacture` (Numéro de facture, unique)

**Champs** :

| Champ               | Type      | Description                                                                 | Exemple                     |
|---------------------|-----------|-----------------------------------------------------------------------------|-----------------------------|
| `nfacture`          | String    | Numéro de facture unique.                                                   | "FACT-2026-001"           |
| `ndossier`          | String    | Numéro de dossier associé à la facture.                                     | "DOSS-2026-001"          |
| `reference_piece`   | String    | Référence de la pièce associée à la facture.                                | "PIECE-2026-001"         |
| `intervenant`       | String    | Identifiant de l'intervenant associé à la commission.                       | "tech_123"                |
| `montant_ht`        | Float     | Montant total HT de la facture.                                             | 1500.00                     |
| `montant_ttc`       | Float     | Montant total TTC de la facture.                                            | 1800.00                     |
| `date_piece`        | String    | Date de la pièce (format : YYYY-MM-DD).                                     | "2026-01-12"              |
| `lien_facture`      | String    | Lien vers la facture PDF.                                                   | "/path/to/facture.pdf"    |
| `statut`            | String    | Statut de la commission (ex: "valide", "conflit", "archive").           | "valide"                  |
| `date_reglement`    | String    | Date de règlement de la commission (format : YYYY-MM-DD).                   | "2026-01-15"              |
| `conflit_detail`    | String    | Détails du conflit si le statut est "conflit".                              | "Conflit de montant"      |
| `monotech`          | Boolean   | Indique si la facture est associée à un seul technicien.                     | true                       |
| `mono_dossier`      | Boolean   | Indique si la facture est associée à un seul dossier.                       | true                       |

> **Note** : Le champ `statut` est restreint aux valeurs suivantes :
> - `valide` : Commission validée et prête à être réglée.
> - `conflit` : Commission en conflit, nécessite une intervention manuelle.
> - `archive` : Commission archivée, plus active.

## 3. Cas d'Utilisation

### 3.1. Un Seul Intervenant
- **Description** : Si la facture ne contient qu'un seul intervenant, les données sont enregistrées directement dans la table `commissions`.
- **Champs** : Tous les champs sont remplis, et le statut est défini à `valide`.

### 3.2. Plusieurs Intervenants
- **Description** : Si la facture contient plusieurs intervenants, les articles sont croisés avec les types de missions pour déterminer qui a fait quoi.
- **Champs** : Les données sont subdivisées par intervenant, et le statut est défini à `valide`.

### 3.3. Conflit
- **Description** : Si impossible de déterminer les intervenants, les détails sont enregistrés dans `conflit_detail`, et le statut est défini à `conflit`.
- **Champs** : `conflit_detail` contient les informations nécessaires pour résoudre le conflit.

## 4. Écrans

### 4.1. Écran Commissions Valides
- **Description** : Affichage des commissions en deux parties : celles en conflit et celles valides.
- **Fonctionnalités** :
  - **Bouton Réparer** : Ouvre une modale avec la facture PDF pour les commissions en conflit.
  - **Bouton Découper** : Ouvre un drawer pour subdiviser une ligne de commission.
  - **Bouton Archiver** : Change le statut à `archivé`.
  - **Bouton Régler** : Permet de déclarer la date de règlement ou d'enregistrer une date.

### 4.2. Modal de Réparation
- **Description** : Affiche la facture PDF via une API `/api/get-file`.
- **Fonctionnalités** :
  - Affichage de la facture PDF.
  - Bouton pour fermer la modale.

### 4.3. Drawer de Découpage
- **Description** : Permet de subdiviser une ligne de commission.
- **Fonctionnalités** :
  - Formulaire pour subdiviser la ligne.
  - Bouton pour valider la subdivision.

## 5. API Backend

### 5.1. Récupération des Commissions
- **Endpoint** : `GET /api/commissions`
- **Réponse** : Liste des commissions avec leurs statuts.

### 5.2. Récupération d'une Facture PDF
- **Endpoint** : `GET /api/get-file`
- **Paramètres** : `url` (URL de la facture)
- **Réponse** : Fichier PDF de la facture.

### 5.3. Mise à Jour d'une Commission
- **Endpoint** : `PUT /api/commissions/<id>`
- **Payload** : Données de la commission à mettre à jour.
- **Réponse** : Commission mise à jour.

### 5.4. Subdivision d'une Ligne de Commission
- **Endpoint** : `POST /api/commissions/subdivide`
- **Payload** : Données de la ligne à subdiviser.
- **Réponse** : Lignes subdivisées.

## 6. Scripts Backend

### 6.1. Traitement des Commissions
- **Script** : `app/scripts/process_commissions.py`
- **Description** : Traite les commissions des techniciens à partir des factures et des missions associées, en vérifiant la cohérence des données et en gérant les cas particuliers (factures mono-technicien, articles en pack, etc.).
- **Spécifications** : [Voir le script](../scripts/commissions/process_commissions.spec)
- **Exemple d'appel** :
  ```bash
  python app/scripts/process_commissions.py \
      --log "reports/ST-<NUM>-process_commissions.log"
  ```

### 6.2. Récupération des Factures Impayées
- **Script** : `app/scripts/fetch_unpaid_invoices.py`
- **Description** : Récupère les factures impayées depuis une base de données externe et les stocke dans `factures_impayees.db`.
- **Spécifications** : [Voir le script](../scripts/relance_impayees/fetch_unpaid_invoices.spec)
- **Exemple d'appel** :
  ```bash
  python app/scripts/fetch_unpaid_invoices.py \
      --log "reports/ST-<NUM>-fetch_unpaid_invoices.log"
  ```

## 6. Composants Alpine.js

### 6.1. `commission_form.html`
- **Description** : Formulaire pour créer ou modifier une commission.
- **Props** :
  - `commission` : Données de la commission.
- **Fonctions** :
  - `validateField()` : Valide les champs du formulaire.
  - `submitForm()` : Soumet le formulaire.

### 6.2. `commission_list.html`
- **Description** : Liste des commissions avec filtres et actions.
- **Props** :
  - `commissions` : Liste des commissions.
- **Fonctions** :
  - `filterCommissions()` : Filtre les commissions.
  - `openRepairModal()` : Ouvre la modale de réparation.
  - `openSubdivideDrawer()` : Ouvre le drawer de découpage.

### 6.3. `repair_modal.html`
- **Description** : Modale pour réparer une commission en conflit.
- **Props** :
  - `commission` : Données de la commission.
- **Fonctions** :
  - `closeModal()` : Ferme la modale.

### 6.4. `subdivide_drawer.html`
- **Description** : Drawer pour subdiviser une ligne de commission.
- **Props** :
  - `commission` : Données de la commission.
- **Fonctions** :
  - `subdivideLine()` : Subdivise la ligne.
  - `closeDrawer()` : Ferme le drawer.

## 7. Pages Flask

### 7.1. `commissions_valides.html`
- **Description** : Page pour gérer les commissions valides et en conflit.
- **Contexte** :
  - `commissions` : Liste des commissions.

### 7.2. `commissions_conflits.html`
- **Description** : Page pour gérer les commissions en conflit.
- **Contexte** :
  - `commissions` : Liste des commissions en conflit.

## 8. Tests

### 8.1. Scénarios Gherkin
- **Fichier** : `specs/features/commissions.feature`
- **Scénarios** :
  - Création d'une commission valide.
  - Résolution d'un conflit.
  - Subdivision d'une ligne de commission.
  - Archivage d'une commission.
  - Règlement d'une commission.

### 8.2. Tests E2E
- **Fichier** : `tests/e2e/commissions_spec.js`
- **Tests** :
  - Vérification de l'affichage des commissions.
  - Vérification des fonctionnalités des boutons.
  - Vérification des modales et drawers.

## 9. Liens
- [Styleguide](utils/styleguide.md)
- [Scénarios Gherkin](specs/features/commissions.feature)
- [Spécifications techniques](specs/_app/commissions_valides.html.spec)
- [Base de données](bdd/commissions.md)
