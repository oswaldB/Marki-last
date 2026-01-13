# Spécifications Fonctionnelles : Relance des Factures Impayées

**Blueprint** : `relance-impayees`
**Version** : 2.0
**Date** : 2024-10-15

---

## Introduction

Ce blueprint permet de gérer les relances des factures impayées. Il inclut des fonctionnalités pour créer des campagnes de relance, gérer des listes de factures impayées, et envoyer des notifications par email ou SMS. Le système est conçu pour automatiser les relances tout en permettant une intervention manuelle si nécessaire.

---

## Bases de Données

### 1. `campagnes.db` (PickleDB)
- **Collection** : `campagnes`
- **Description** : Stocke les campagnes de relance, incluant les séquences d'emails et les critères de sélection des factures.
- **Structure** :
  - `id` : Identifiant unique de la campagne.
  - `nom` : Nom de la campagne.
  - `description` : Description de la campagne.
  - `statut` : Statut de la campagne (ex: "active", "completed").
  - `date_creation` : Date de création de la campagne.
  - `nombre_relances` : Nombre de relances effectuées.
  - `type` : Type de campagne ("automatique" ou "manuelle").
  - `sequence` : Séquence d'emails associée à la campagne.
  - `critères` : Critères de sélection des factures.

### 2. `relances.db` (PickleDB)
- **Collection** : `relances`
- **Description** : Stocke les factures et leurs relances associées.
- **Structure** :
  - `id` : Identifiant unique de la facture.
  - `numero_facture` : Numéro de la facture.
  - `montant` : Montant total de la facture.
  - `date_echeance` : Date d'échéance de la facture.
  - `reste_a_payer` : Montant restant à payer.
  - `statut` : Statut de la facture (ex: "impayee", "partially_paid").
  - `proprietaire_prenom` : Prénom du propriétaire.
  - `proprietaire_nom` : Nom du propriétaire.
  - `proprietaire_email` : Adresse email du propriétaire.
  - `apporteur_affaire_prenom` : Prénom de l'apporteur d'affaires.
  - `apporteur_affaire_nom` : Nom de l'apporteur d'affaires.
  - `apporteur_affaire_email` : Adresse email de l'apporteur d'affaires.
  - `notaire_prenom` : Prénom du notaire.
  - `notaire_nom` : Nom du notaire.
  - `notaire_email` : Adresse email du notaire.
  - `payeur` : Indique qui est responsable du paiement ("proprietaire", "notaire", ou "apporteur_affaire").
  - `relances` : Liste des relances associées à la facture.

### 3. `factures_impayees.db` (PickleDB)
- **Collection** : `factures_impayees`
- **Description** : Stocke les factures impayées (source pour les campagnes automatiques).
- **Structure** :
  - `id` : Identifiant unique de la facture.
  - `numero_facture` : Numéro de la facture.
  - `montant` : Montant total de la facture.
  - `date_echeance` : Date d'échéance de la facture.
  - `reste_a_payer` : Montant restant à payer.
  - `statut` : Statut de la facture (ex: "impayee").
  - `proprietaire_prenom` : Prénom du propriétaire.
  - `proprietaire_nom` : Nom du propriétaire.
  - `proprietaire_email` : Adresse email du propriétaire.
  - `apporteur_affaire_prenom` : Prénom de l'apporteur d'affaires.
  - `apporteur_affaire_nom` : Nom de l'apporteur d'affaires.
  - `apporteur_affaire_email` : Adresse email de l'apporteur d'affaires.
  - `notaire_prenom` : Prénom du notaire.
  - `notaire_nom` : Nom du notaire.
  - `notaire_email` : Adresse email du notaire.
  - `payeur` : Indique qui est responsable du paiement ("proprietaire", "notaire", ou "apporteur_affaire").
  - `date_ajout` : Date d'ajout à la base des factures impayées.

### 4. `app.db` (PickleDB)
- **Collection** : `users`
- **Description** : Stocke les informations des utilisateurs.
- **Structure** :
  - `id` : Identifiant unique de l'utilisateur.
  - `username` : Nom d'utilisateur.
  - `email` : Adresse email de l'utilisateur.
  - `isAdmin` : Indique si l'utilisateur est un administrateur.

### 5. `app.db` (PickleDB)
- **Collection** : `notifications`
- **Description** : Stocke les notifications des utilisateurs.
- **Structure** :
  - `id` : Identifiant unique de la notification.
  - `user_id` : Identifiant de l'utilisateur associé à la notification.
  - `message` : Message de la notification.
  - `read` : Indique si la notification a été lue.
  - `createdAt` : Date de création de la notification.

---

## Pages et Fonctionnalités

### 1. Dashboard & Calendrier

#### Résumé des campagnes
- **Description** : Afficher un résumé des campagnes actives et pausées.
- **Fonctionnalités** :
  - Statistiques (taux d’ouverture, relances réussies/échouées). Les statistiques sont stockées dans la collection `campagnes` de `campagnes.db`.

#### Calendrier des envois
- **Description** : Afficher un calendrier des emails/SMS envoyés et à envoyer.
- **Fonctionnalités** :
  - Filtres par campagne, date, statut, numéro de dossier, et numéro de facture.
  - Recherche libre pour faciliter la navigation.
  - Marquer manuellement une relance comme envoyée/échouée.
  - Visualiser les détails d’un envoi (contenu, destinataire, statut).
  - Modifier les messages via un drawer.

### 2. Campagnes de Relances

#### Gestion des campagnes
- **Description** : Créer, éditer, et gérer des campagnes de relance.
- **Fonctionnalités** :
  - Créer/éditer une campagne (nom, description, statut actif/pause, critères de sélection des factures, et séquence d'emails).
  - Mettre en pause/reprendre une campagne.
  - Supprimer une campagne.
  - Lister toutes les campagnes (statut, date de création, nombre de relances).

#### Séquences de relance
- **Description** : Définir des séquences d’emails/SMS pour les campagnes.
- **Fonctionnalités** :
  - Définir une séquence (contenu, délais entre chaque envoi, variables dynamiques).
  - Associer une séquence à une campagne.
  - Prévisualiser une séquence avant activation.
  - Générer les emails/SMS à envoyer pour une campagne active (tous les jours à 18h).
  - Utiliser des variables dynamiques dans les messages (ex: `{{table.column}}`).
  - Générer un email avec ChatGPT en utilisant les variables dynamiques.
  - Afficher le prompt utilisé pour générer l'email.

### 3. Critères de Sélection

#### Critères automatiques
- **Description** : Définir des critères automatiques pour sélectionner les factures à relancer.
- **Fonctionnalités** :
  - Filtres : montant, date d’échéance, client, etc.
  - Planifier le peuplement automatique des factures tous les jours à 17h.
  - Afficher les factures sans email valide dans un tableau dédié.

#### Critères manuels
- **Description** : Sélectionner manuellement les factures à relancer.
- **Fonctionnalités** :
  - Ajout/suppression de factures.
  - Rafraîchir manuellement la liste des factures impayées (bouton "Réparer").

### 4. Gestion des Factures Impayées

#### Récupération des factures
- **Description** : Récupérer les factures impayées depuis une base de données externe.
- **Fonctionnalités** :
  - Exécuter une requête SQL pour obtenir les factures impayées.
  - Synchroniser les statuts des factures (payé/impayé) avant chaque envoi de relance.

---

## Use Cases

### UC1 : Afficher un résumé des campagnes actives/pausées, statistiques
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut voir un résumé des campagnes actives et pausées, ainsi que des statistiques sur les relances.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Les statistiques sont affichées.

### UC2 : Notifier l’utilisateur en cas d’email manquant ou d’échec d’envoi
- **Acteur** : Système
- **Description** : Le système notifie l’utilisateur en cas d’email manquant ou d’échec d’envoi via un système de notifications internes.
- **Préconditions** : Une relance a échoué ou un email est manquant.
- **Postconditions** : L’utilisateur est notifié via une alerte dans l'interface.

### UC4 : Afficher un calendrier des emails/SMS envoyés et à envoyer
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut voir un calendrier des emails/SMS envoyés et à envoyer.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Le calendrier est affiché.

### UC5 : Marquer manuellement une relance comme envoyée/échouée
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut marquer manuellement une relance comme envoyée ou échouée.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La relance est marquée.

### UC6 : Visualiser les détails d’un envoi
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut visualiser les détails d’un envoi (contenu, destinataire, statut).
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Les détails sont affichés.

### UC7 : Modifier les messages via un drawer
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut modifier les messages des relances via un drawer.
- **Préconditions** : L’utilisateur est connecté et a sélectionné une relance.
- **Postconditions** : Le message est modifié.

### UC7 : Créer/éditer une campagne de relance
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut créer ou éditer une campagne de relance.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La campagne est créée ou modifiée.

### UC8 : Mettre en pause/reprendre une campagne
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut mettre en pause ou reprendre une campagne.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La campagne est mise en pause ou reprise.

### UC9 : Supprimer une campagne
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut supprimer une campagne.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La campagne est supprimée.

### UC10 : Lister toutes les campagnes
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut lister toutes les campagnes.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Les campagnes sont listées.

### UC11 : Définir une séquence d’emails/SMS
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut définir une séquence d’emails/SMS.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La séquence est définie.

### UC12 : Définir une séquence dans une campagne
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut définir une séquence d'emails directement dans une campagne.
- **Préconditions** : L’utilisateur est connecté et a créé une campagne.
- **Postconditions** : La séquence est définie dans la campagne.

### UC13 : Prévisualiser une séquence avant activation
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut prévisualiser une séquence avant activation.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La séquence est prévisualisée.

### UC14 : Utiliser des variables dynamiques dans les messages
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut utiliser des variables dynamiques dans les messages des séquences (ex: `{{table.column}}`).
- **Préconditions** : L’utilisateur est connecté et a défini une séquence.
- **Postconditions** : Les variables sont remplacées par les valeurs correspondantes.

### UC15 : Générer un template d'email avec ChatGPT
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut générer un template d'email avec ChatGPT en utilisant les variables dynamiques.
- **Préconditions** : L’utilisateur est connecté et a défini une séquence.
- **Postconditions** : Un template d'email est généré avec les variables dynamiques.

### UC16 : Afficher le prompt ChatGPT
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut afficher le prompt utilisé pour générer le template d'email avec ChatGPT.
- **Préconditions** : L’utilisateur est connecté et a généré un email avec ChatGPT.
- **Postconditions** : Le prompt est affiché.

### UC14 : Générer les emails/SMS à envoyer pour une campagne active
- **Acteur** : Système
- **Description** : Le système génère les emails/SMS à envoyer pour une campagne active et les stocke dans `relances.db`.
- **Préconditions** : La campagne est active.
- **Postconditions** : Les emails/SMS sont générés et stockés dans `relances.db`.

### UC15 : Vérifier le statut des factures avant envoi
- **Acteur** : Système
- **Description** : Le système vérifie le statut des factures avant envoi.
- **Préconditions** : Une relance est sur le point d’être envoyée.
- **Postconditions** : Le statut des factures est vérifié.

### UC16 : Envoyer les relances
- **Acteur** : Système
- **Description** : Le système envoie les relances.
- **Préconditions** : Les relances sont générées.
- **Postconditions** : Les relances sont envoyées.

### UC17 : Définir des critères automatiques pour une campagne
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut définir des critères automatiques pour sélectionner les factures à relancer dans une campagne.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Les critères sont définis et les factures sont sélectionnées automatiquement.

### UC18 : Planifier le peuplement automatique des listes
- **Acteur** : Système
- **Description** : Le système planifie le peuplement automatique des listes.
- **Préconditions** : La liste est créée.
- **Postconditions** : La liste est peuplée.

### UC19 : Afficher les factures sans email valide
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut voir les factures sans email valide.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Les factures sont affichées.

### UC20 : Sélectionner manuellement des factures pour une campagne
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut sélectionner manuellement les factures à relancer dans une campagne.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : Les factures sont sélectionnées et ajoutées à la campagne.

### UC21 : Rafraîchir manuellement la liste des factures impayées
- **Acteur** : Utilisateur
- **Description** : L’utilisateur peut rafraîchir manuellement la liste des factures impayées.
- **Préconditions** : L’utilisateur est connecté.
- **Postconditions** : La liste est rafraîchie.

### UC22 : Récupérer les factures impayées via une requête SQL
- **Acteur** : Système
- **Description** : Le système récupère les factures impayées via une requête SQL.
- **Préconditions** : La requête est configurée.
- **Postconditions** : Les factures sont récupérées.

### UC23 : Synchroniser les statuts des factures
- **Acteur** : Système
- **Description** : Le système synchronise les statuts des factures.
- **Préconditions** : Les factures sont récupérées.
- **Postconditions** : Les statuts sont synchronisés.

---

## Règles Métier

1. **Relances** :
   - Une relance ne doit pas être envoyée si la facture est déjà payée.
   - Les relances doivent être envoyées selon les délais définis dans la séquence.
   - Les emails/SMS doivent contenir des variables dynamiques (nom du client, montant dû, etc.).

2. **Campagnes** :
   - Une campagne ne peut être supprimée que si elle est en pause.
   - Une campagne ne peut être activée que si elle inclut des critères de sélection et une séquence d'emails.

3. **Critères de Sélection** :
   - Les critères automatiques sont appliqués tous les jours à 17h pour sélectionner les factures.
   - Les critères manuels peuvent être rafraîchis manuellement.

4. **Factures** :
   - Les factures impayées sont récupérées via une requête SQL sur une base de données externe.
   - Les statuts des factures sont synchronisés avant chaque envoi de relance.

---

## Intégrations

- **Service d’emailing/SMS** : Pour l’envoi des relances.
- **Base de données externe** : Pour la récupération des factures impayées.

---

## Exigences Techniques

- **Frontend** : Alpine.js, Tailwind CSS.
- **Backend** : Python, Flask.
- **Base de données** : PickleDB (pour les données locales), requêtes SQL pour la base externe.

---

## Liens

- [Spécifications des scripts backend](scripts/relance_impayees/)
- [Schéma SQL](bdd/relance_impayees.sql)
- [Scénarios Gherkin](features/relance_impayees.feature)
