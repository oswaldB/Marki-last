# Spécifications des Tests pour les Relances des Factures Impayées

## 1. Contexte
- **Objectif** : Vérifier le bon fonctionnement des fonctionnalités de relance des factures impayées.
- **Portée** : Tests unitaires, tests d'intégration et tests end-to-end.

## 2. Scénarios de Test

### 2.1. Tests Unitaires

#### 2.1.1. Récupération des Factures Impayées
- **Description** : Vérifier que les factures impayées sont correctement récupérées depuis la base de données.
- **Préconditions** :
  - Base de données `factures_impayees.db` initialisée avec des données de test.
- **Étapes** :
  1. Exécuter `fetch_unpaid_invoices`.
  2. Vérifier que les factures impayées sont correctement récupérées.
- **Résultat attendu** :
  - Les factures impayées sont récupérées et stockées dans `factures_impayees.db`.

#### 2.1.2. Population des Relances
- **Description** : Vérifier que les relances sont correctement générées et stockées.
- **Préconditions** :
  - Base de données `campagnes.db` initialisée avec des campagnes de test.
  - Base de données `relances.db` initialisée.
- **Étapes** :
  1. Exécuter `populate_relances`.
  2. Vérifier que les relances sont correctement générées et stockées.
- **Résultat attendu** :
  - Les relances sont générées et stockées dans `relances.db`.

### 2.2. Tests d'Intégration

#### 2.2.1. Envoi des Relances
- **Description** : Vérifier que les relances sont correctement envoyées par email.
- **Préconditions** :
  - Base de données `relances.db` initialisée avec des relances de test.
  - Serveur SMTP configuré pour les tests.
- **Étapes** :
  1. Exécuter l'endpoint `/api/relances/<id>/envoi`.
  2. Vérifier que les relances sont correctement envoyées.
- **Résultat attendu** :
  - Les relances sont envoyées et le statut est mis à jour dans `relances.db`.

#### 2.2.2. Archivage des Relances
- **Description** : Vérifier que les relances sont correctement archivées.
- **Préconditions** :
  - Base de données `relances.db` initialisée avec des relances de test.
- **Étapes** :
  1. Exécuter l'endpoint `/api/relances/<id>/archive`.
  2. Vérifier que les relances sont correctement archivées.
- **Résultat attendu** :
  - Les relances sont archivées et le statut est mis à jour dans `relances.db`.

### 2.3. Tests End-to-End

#### 2.3.1. Workflow Complet
- **Description** : Vérifier le workflow complet depuis la récupération des factures impayées jusqu'à l'envoi des relances.
- **Préconditions** :
  - Base de données `factures_impayees.db` initialisée avec des données de test.
  - Base de données `campagnes.db` initialisée avec des campagnes de test.
  - Base de données `relances.db` initialisée.
  - Serveur SMTP configuré pour les tests.
- **Étapes** :
  1. Exécuter `fetch_unpaid_invoices`.
  2. Exécuter `populate_relances`.
  3. Exécuter l'endpoint `/api/relances/<id>/envoi`.
  4. Vérifier que le workflow complet est correctement exécuté.
- **Résultat attendu** :
  - Le workflow complet est correctement exécuté et les relances sont envoyées.

## 3. Règles Métier

### 3.1. Validation des Données
- **Description** : Vérifier que les données sont correctement validées.
- **Préconditions** :
  - Base de données `factures_impayees.db` initialisée avec des données de test.
- **Étapes** :
  1. Exécuter `fetch_unpaid_invoices` avec des données invalides.
  2. Vérifier que les données invalides sont correctement détectées.
- **Résultat attendu** :
  - Les données invalides sont correctement détectées et les erreurs sont correctement gérées.

### 3.2. Gestion des Erreurs
- **Description** : Vérifier que les erreurs sont correctement gérées.
- **Préconditions** :
  - Base de données `factures_impayees.db` initialisée avec des données de test.
- **Étapes** :
  1. Exécuter `fetch_unpaid_invoices` avec une connexion échouée.
  2. Vérifier que les erreurs sont correctement gérées.
- **Résultat attendu** :
  - Les erreurs sont correctement gérées et les messages d'erreur sont correctement affichés.

## 4. Liens Vers les Spécifications Techniques

- [Routes](/_app/blueprints/relance.routes.spec.md)
- [Modèles](/_app/blueprints/relance.models.spec.md)
- [Composants](/_app/blueprints/relance/templates/partials/)
- [Scripts](/_app/blueprints/relance/scripts/)