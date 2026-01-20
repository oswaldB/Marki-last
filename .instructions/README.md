# Méthodologie de Développement - Steroids Studio

Ce document décrit la méthodologie de développement utilisée par l'équipe de Steroids Studio pour le projet Marki. Il explique comment l'équipe est organisée, comment les tâches sont gérées, et comment les livrables sont validés et déployés.

---

## 📌 Organisation de l'Équipe

L'équipe de développement de Steroids Studio est organisée en plusieurs rôles spécialisés, chacun ayant des responsabilités spécifiques. Voici les rôles et leurs responsabilités :

### 1. **Product Manager**
- **Responsabilités** :
  - Définir les spécifications fonctionnelles (ST-) pour les fonctionnalités du projet.
  - Collaborer avec les autres membres de l'équipe pour s'assurer que les spécifications sont claires et alignées avec les objectifs du projet.
  - Valider les spécifications avant qu'elles ne soient fusionnées.
- **Livrables** :
  - Fichiers de spécifications fonctionnelles dans `specs/process/01_specs_fonctionnelles/`.
- **Documentation** :
  - Voir `.instructions/product_manager/README.md`.

### 2. **Senior Software Engineer**
- **Responsabilités** :
  - Définir les spécifications techniques pour les blueprints, les templates, et les bases de données.
  - Collaborer avec les autres membres de l'équipe pour s'assurer que les spécifications techniques sont alignées avec les spécifications fonctionnelles.
  - Valider les spécifications techniques avant qu'elles ne soient fusionnées.
- **Livrables** :
  - Fichiers de spécifications techniques dans `specs/_app/` et `specs/process/02_specs_techniques/`.
- **Documentation** :
  - Voir `.instructions/senior_software_engineer/README.md`.

### 3. **DBA (Database Administrator)**
- **Responsabilités** :
  - Définir et gérer les bases de données du projet.
  - Collaborer avec les autres membres de l'équipe pour s'assurer que les bases de données sont bien structurées et optimisées.
  - Valider les spécifications des bases de données avant qu'elles ne soient fusionnées.
- **Livrables** :
  - Fichiers de spécifications des bases de données dans `specs/_app/bdd/` et `specs/process/04_developpement_bdd/`.
- **Documentation** :
  - Voir `.instructions/dba/README.md`.

### 4. **Dev Senior Python**
- **Responsabilités** :
  - Développer le backend de l'application en utilisant Python et Flask.
  - Implémenter les blueprints et les routes définis dans les spécifications techniques.
  - Valider le code backend avant qu'il ne soit fusionné.
- **Livrables** :
  - Code backend dans `app/`.
- **Documentation** :
  - Voir `.instructions/dev_senior_python/README.md`.

### 5. **Dev Senior AlpineJS**
- **Responsabilités** :
  - Développer le frontend de l'application en utilisant Alpine.js et Tailwind CSS.
  - Implémenter les templates et les partials définis dans les spécifications techniques.
  - Valider le code frontend avant qu'il ne soit fusionné.
- **Livrables** :
  - Code frontend dans `app/templates/`.
- **Documentation** :
  - Voir `.instructions/dev_senior_alpinejs/README.md`.

### 6. **QA Senior Playwright**
- **Responsabilités** :
  - Définir et exécuter les tests pour l'application en utilisant Playwright.
  - Collaborer avec les autres membres de l'équipe pour s'assurer que les tests sont bien structurés et alignés avec les spécifications.
  - Valider les tests avant qu'ils ne soient fusionnés.
- **Livrables** :
  - Fichiers de tests dans `tests/` et `specs/process/03_redaction_tests/`.
- **Documentation** :
  - Voir `.instructions/qa_senior_playwright/README.md`.

### 7. **Global Manager**
- **Responsabilités** :
  - Coordonner et gérer globalement le projet.
  - Organiser les réunions et les revues de code.
  - Valider les livrables avant qu'ils ne soient fusionnés.
  - Gérer les todos et le serveur.
- **Livrables** :
  - Validation des livrables et gestion des todos.
- **Documentation** :
  - Voir `.instructions/global_manager/README.md`.

---

## 📌 Processus de Développement

Le processus de développement de Steroids Studio est structuré en plusieurs étapes, chacune correspondant à un sous-dossier dans `specs/process/`. Voici les étapes du processus :

### 1. **Spécifications Fonctionnelles (01_specs_fonctionnelles)**
- **Description** :
  - Le Product Manager définit les spécifications fonctionnelles pour les fonctionnalités du projet.
  - Les spécifications fonctionnelles sont rédigées dans des fichiers `ST-<NUM>_<nom>-functionnelles.md`.
- **Livrables** :
  - Fichiers de spécifications fonctionnelles dans `specs/process/01_specs_fonctionnelles/`.

### 2. **Spécifications Techniques (02_specs_techniques)**
- **Description** :
  - Le Senior Software Engineer définit les spécifications techniques pour les blueprints, les templates, et les bases de données.
  - Les spécifications techniques sont rédigées dans des fichiers `ST-<NUM>_<nom>.spec`.
- **Livrables** :
  - Fichiers de spécifications techniques dans `specs/process/02_specs_techniques/`.

### 3. **Rédaction des Tests (03_redaction_tests)**
- **Description** :
  - Le QA Senior Playwright définit les tests pour l'application en utilisant Playwright.
  - Les tests sont rédigés dans des fichiers `ST-<NUM>_<nom>.spec.ts`.
- **Livrables** :
  - Fichiers de tests dans `specs/process/03_redaction_tests/`.

### 4. **Développement de la Base de Données (04_developpement_bdd)**
- **Description** :
  - Le DBA développe la base de données selon les spécifications techniques.
  - La base de données est développée dans `app/marki.db`.
- **Livrables** :
  - Base de données dans `app/marki.db`.

### 5. **Développement du Backend (05_developpement_back)**
- **Description** :
  - Le Dev Senior Python développe le backend de l'application selon les spécifications techniques.
  - Le backend est développé dans `app/`.
- **Livrables** :
  - Code backend dans `app/`.

### 6. **Développement du Frontend (06_developpement_front)**
- **Description** :
  - Le Dev Senior AlpineJS développe le frontend de l'application selon les spécifications techniques.
  - Le frontend est développé dans `app/templates/`.
- **Livrables** :
  - Code frontend dans `app/templates/`.

### 7. **Exécution des Tests (07_execution_tests)**
- **Description** :
  - Le QA Senior Playwright exécute les tests pour s'assurer que l'application fonctionne correctement.
  - Les tests sont exécutés en utilisant Playwright.
- **Livrables** :
  - Rapports de tests dans `playwright-report/`.

### 8. **Tests Réussis (08_tests_reussis)**
- **Description** :
  - Les tests qui ont réussi sont déplacés dans ce dossier.
  - Les tests sont validés par le Global Manager.
- **Livrables** :
  - Fichiers de tests réussis dans `specs/process/08_tests_reussis/`.

### 9. **Tests Échoués (09_tests_echoues)**
- **Description** :
  - Les tests qui ont échoué sont déplacés dans ce dossier.
  - Les tests sont analysés et corrigés par les membres de l'équipe.
- **Livrables** :
  - Fichiers de tests échoués dans `specs/process/09_tests_echoues/`.

---

## 📌 Gestion des Todos

Le **Global Manager** est responsable de la gestion des todos pour le projet Marki. Les todos doivent être exhaustives et suivre une logique claire pour s'assurer que tous les membres de l'équipe savent ce qu'ils doivent faire.

### Rôles et Responsabilités

1. **Global Manager**
   - **Responsabilités** :
     - Définir les todos pour toutes les spécifications (fonctionnelles, techniques, tests, etc.).
     - Assigner les todos aux différents acteurs (Product Manager, Senior Software Engineer, DBA, Dev Senior Python, Dev Senior AlpineJS, QA Senior Playwright, etc.).
     - Mettre à jour les todos dans les fichiers de spécifications.
     - Superviser la gestion des todos.
     - Assurer la coordination entre les différents rôles.
     - Valider les todos avant qu'elles ne soient fusionnées.

2. **Product Manager**
   - **Responsabilités** :
     - Collaborer avec le Global Manager pour définir les todos liées aux spécifications fonctionnelles.
     - Signaler l'avancement des todos assignées.

3. **Senior Software Engineer**
   - **Responsabilités** :
     - Collaborer avec le Global Manager pour définir les todos liées aux spécifications techniques.
     - Signaler l'avancement des todos assignées.

4. **DBA (Database Administrator)**
   - **Responsabilités** :
     - Collaborer avec le Global Manager pour définir les todos liées à la gestion des bases de données.
     - Signaler l'avancement des todos assignées.

5. **Dev Senior Python**
   - **Responsabilités** :
     - Collaborer avec le Global Manager pour définir les todos liées au développement backend.
     - Signaler l'avancement des todos assignées.

6. **Dev Senior AlpineJS**
   - **Responsabilités** :
     - Collaborer avec le Global Manager pour définir les todos liées au développement frontend.
     - Signaler l'avancement des todos assignées.

7. **QA Senior Playwright**
   - **Responsabilités** :
     - Collaborer avec le Global Manager pour définir les todos liées à la rédaction et à l'exécution des tests.
     - Signaler l'avancement des todos assignées.

### Script de Gestion des Todos

Un script Python a été créé pour faciliter la gestion des todos. Le script est situé à `scripts/manage_todos_and_server.py`.

### Script de Gestion des Todos

Un script Python a été créé pour faciliter la gestion des todos. Le script est situé à `scripts/manage_todos_and_server.py`.

**Utilisation du Script** :

```bash
python scripts/manage_todos_and_server.py <command> [args]
```

**Commandes** :

- **Ajouter une todo** :
  ```bash
  python scripts/manage_todos_and_server.py add <description> <agent> [priority]
  ```
  **Exemple** :
  ```bash
  python scripts/manage_todos_and_server.py add "Créer la page d'inscription" "Dev Senior AlpineJS" high
  ```

- **Mettre à jour une todo** :
  ```bash
  python scripts/manage_todos_and_server.py update <id> [--status <status>] [--description <description>] [--agent <agent>] [--priority <priority>]
  ```
  **Exemple** :
  ```bash
  python scripts/manage_todos_and_server.py update 1 --status "in_progress"
  ```

- **Lister les todos** :
  ```bash
  python scripts/manage_todos_and_server.py list
  ```

- **Gérer le serveur** :
  ```bash
  python scripts/manage_todos_and_server.py server <action> (start, stop, restart)
  ```
  **Exemple** :
  ```bash
  python scripts/manage_todos_and_server.py server restart
  ```

### Exemple de Todo

**Fichier** : `.instructions/todos.json`

```json
[
  {
    "id": 1,
    "description": "Créer la page d'inscription",
    "agent": "Dev Senior AlpineJS",
    "priority": "high",
    "status": "in_progress",
    "created_at": "2026-01-20 12:00:00",
    "updated_at": "2026-01-20 12:00:00"
  },
  {
    "id": 2,
    "description": "Implémenter la logique de connexion",
    "agent": "Dev Senior Python",
    "priority": "high",
    "status": "pending",
    "created_at": "2026-01-20 12:00:00",
    "updated_at": "2026-01-20 12:00:00"
  },
  {
    "id": 3,
    "description": "Créer les tests pour la page d'inscription",
    "agent": "QA Senior Playwright",
    "priority": "medium",
    "status": "pending",
    "created_at": "2026-01-20 12:00:00",
    "updated_at": "2026-01-20 12:00:00"
  }
]
```

---

## 📌 Gestion du Serveur

Le Global Manager est responsable de la gestion du serveur pour le projet Marki. Le serveur doit toujours être lancé en utilisant le script `run_serveur`. Si le serveur tourne déjà, il doit être arrêté et redémarré en utilisant le script `run_serveur`.

### Script de Gestion du Serveur

Le script `manage_todos_and_server.py` inclut également des commandes pour gérer le serveur.

**Commandes** :

- **Démarrer le serveur** :
  ```bash
  python scripts/manage_todos_and_server.py server start
  ```

- **Arrêter le serveur** :
  ```bash
  python scripts/manage_todos_and_server.py server stop
  ```

- **Redémarrer le serveur** :
  ```bash
  python scripts/manage_todos_and_server.py server restart
  ```

### Exemple de Gestion du Serveur

**Démarrer le serveur** :

```bash
python scripts/manage_todos_and_server.py server start
```

**Sortie** :

```
Démarrage du serveur...
* Serving Flask app 'app'
* Debug mode: off
* Running on http://127.0.0.1:5000/
```

**Redémarrer le serveur** :

```bash
python scripts/manage_todos_and_server.py server restart
```

**Sortie** :

```
Redémarrage du serveur...
Arrêt du serveur...
Démarrage du serveur...
* Serving Flask app 'app'
* Debug mode: off
* Running on http://127.0.0.1:5000/
```

---

## 📌 Déplacement des Fichiers ST-

Le Global Manager est responsable du déplacement des fichiers ST- d'un sous-dossier à un autre pour refléter l'avancement du processus. Ce déplacement se fait uniquement après que le travail a été validé par l'acteur concerné.

### Script de Déplacement

Un script Python a été créé pour faciliter le déplacement des fichiers ST- et ajouter l'aval du Global Manager. Le script est situé à `scripts/move_st_file.py`.

**Utilisation du Script** :

```bash
python scripts/move_st_file.py <source_dir> <target_dir> <st_number>
```

**Exemple** :

```bash
python scripts/move_st_file.py 01_specs_fonctionnelles 02_specs_techniques 001
```

Ce script va :

1. Déplacer le fichier `ST-001_*.md` du dossier `specs/process/01_specs_fonctionnelles` vers le dossier `specs/process/02_specs_techniques`.
2. Ajouter l'aval du Global Manager au fichier avec la date et le statut.

### Exemple de Déplacement

#### Avant le Déplacement

**Fichier** : `specs/process/01_specs_fonctionnelles/ST-001_hello-world-functionnelles.md`

```markdown
# ST-001 : Hello World
**Date** : 2026-01-20
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte

Créer une page Hello World pour tester l'environnement.

---

## 📜 Règles Métier

- La page doit afficher "Hello World".
- La page doit être accessible à l'URL `/hello`.

---

## 🔧 Spécifications Techniques

### Fonctions

#### `display_hello_world()`
**Description** :
Affiche le message "Hello World".

**Retour** :
```json
{ "status": "success", "message": "Hello World" }
```

---

## 🎨 Maquettes UI

### Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] HELLO WORLD              |
|                                     |
|  Hello World!                        |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```
```

#### Après le Déplacement

**Fichier** : `specs/process/02_specs_techniques/ST-001_hello-world-functionnelles.md`

```markdown
# ST-001 : Hello World
**Date** : 2026-01-20
**UI** : Intégration des logos et couleurs Marki.

---

## 🎯 Contexte

Créer une page Hello World pour tester l'environnement.

---

## 📜 Règles Métier

- La page doit afficher "Hello World".
- La page doit être accessible à l'URL `/hello`.

---

## 🔧 Spécifications Techniques

### Fonctions

#### `display_hello_world()`
**Description** :
Affiche le message "Hello World".

**Retour** :
```json
{ "status": "success", "message": "Hello World" }
```

---

## 🎨 Maquettes UI

### Maquette ASCII

```
+-------------------------------------+
|  🏗 [MARKI] HELLO WORLD              |
|                                     |
|  Hello World!                        |
|                                     |
|  🎨 Powered by MARKI                 |
+-------------------------------------+
```

---

## 📌 Aval du Global Manager

**Date** : 2026-01-20
**Statut** : Validé
**Commentaires** : Le travail a été validé et le fichier a été déplacé vers le dossier suivant.
```

---

## 📌 Formats des Fichiers

Les fichiers produits par l'équipe de développement doivent suivre des formats spécifiques pour s'assurer qu'ils sont clairs, concis et alignés avec les objectifs du projet. Voici les formats des fichiers :

### 1. **Spécifications Fonctionnelles**
- **Format** : `.instructions/format_fichiers/st_file_format.md`
- **Exemple** : `specs/process/01_specs_fonctionnelles/ST-001_hello-world-functionnelles.md`

### 2. **Spécifications Techniques**
- **Format** : `.instructions/format_fichiers/blueprint_format.md`
- **Exemple** : `specs/process/02_specs_techniques/ST-001_blueprint-auth.spec`

### 3. **Tests Playwright**
- **Format** : `.instructions/format_fichiers/playwright_test_format.md`
- **Exemple** : `specs/process/03_redaction_tests/ST-001_inscription.spec.ts`

### 4. **Base de Données**
- **Format** : `.instructions/format_fichiers/bdd_documentation_rules.md`
- **Exemple** : `specs/_app/bdd/marki.db.spec`

### 5. **Code Backend**
- **Format** : `.instructions/format_fichiers/blueprint_format.md`
- **Exemple** : `app/blueprints/auth/routes.py`

### 6. **Code Frontend**
- **Format** : `.instructions/format_fichiers/partial_alpinejs_format.md`
- **Exemple** : `app/templates/partials/login_form.html`

---

## 📌 Bonnes Pratiques

1. **Clarté** : Utilisez des descriptions claires et concises pour la documentation et la communication.
2. **Consistance** : Maintenez une consistance dans les formats et les conventions.
3. **Exemples** : Fournissez des exemples pour illustrer les spécifications et le code.
4. **Mises à Jour** : Documentez toute mise à jour ou modification.
5. **Validation** : Assurez-vous que tous les livrables sont validés par l'équipe avant d'être fusionnés.
6. **Communication** : Maintenez une communication claire et concise avec tous les membres de l'équipe.
7. **Coordination** : Assurez-vous que tous les membres de l'équipe travaillent en harmonie et selon les objectifs du projet.

---

## 📌 Conclusion

L'équipe de développement de Steroids Studio suit une méthodologie structurée et bien définie pour s'assurer que tous les projets sont livrés à temps et selon les objectifs. Chaque membre de l'équipe a un rôle spécifique et des responsabilités claires, ce qui permet de maintenir une haute qualité de code et de documentation. Le Global Manager joue un rôle crucial dans la coordination et la gestion globale du projet, s'assurant que tous les membres de l'équipe travaillent en harmonie et selon les objectifs du projet.
