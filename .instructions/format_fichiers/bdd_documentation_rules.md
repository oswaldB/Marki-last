# Règles de Structuration des Documents de la Base de Données (BDD)

Ce document définit les règles et conventions pour la structuration des documents liés à la base de données (BDD) dans le projet Marki.

---

## 📂 Structure des Dossiers

Les documents liés à la BDD doivent être organisés selon la structure suivante :

```bash
specs/
└── _app/
    └── bdd/
        ├── <nom_de_la_bdd>.db.spec  # Spécifications techniques de la BDD
        └── README.md                  # Description générale des BDD du projet

app/
└── <nom_de_la_bdd>.db              # Base de données réelle (SQLite)
```

**Exemple** :
- Spécifications : `specs/_app/bdd/marki.db.spec`
- Base de données réelle : `app/marki.db`

---

## 📄 Fichiers de Spécifications Techniques

### Format du Fichier

Les fichiers de spécifications techniques doivent être nommés selon le format suivant :
- `<nom_de_la_bdd>.db.spec`

Exemple : `marki.db.spec`

### Contenu du Fichier

Chaque fichier de spécifications techniques doit contenir les sections suivantes :

#### 1. **En-tête**
```markdown
# <Nom de la BDD>
**Fichier** : `<nom_de_la_bdd>.db`
```

#### 2. **Tables**
Cette section doit lister toutes les tables de la BDD avec leurs colonnes, types de données, et descriptions.

```markdown
## 📋 Tables

### <Nom de la Table>

| Colonne       | Type         | Description                          | Exemple          |
|---------------|--------------|--------------------------------------|------------------|
| id            | INTEGER      | Identifiant unique auto-incrémenté   | 1                |
| email         | TEXT         | Adresse email de l'utilisateur       | test@example.com |
| password      | TEXT         | Mot de passe haché                   | <haché>          |
| name          | TEXT         | Nom complet de l'utilisateur         | Test User        |

**Clé primaire** : `id`
**Index** : `email` (UNIQUE)
```

#### 3. **Relations**
Cette section doit décrire les relations entre les tables.

```markdown
## 🔗 Relations

- **<Table1>** : Relation avec **<Table2>** via la clé étrangère `<colonne>`.
  - Description de la relation.
```


## 📄 Fichiers SQL

Les fichiers SQL ne sont pas nécessaires dans ce projet, car la base de données est directement gérée via SQLite dans le fichier `app/marki.db`. Les spécifications techniques dans `specs/_app/bdd/` suffisent pour décrire la structure de la BDD.

Si des scripts SQL sont nécessaires pour des opérations spécifiques (comme des migrations ou des mises à jour), ils peuvent être inclus dans le fichier de spécifications techniques ou dans un fichier séparé dans `specs/_app/bdd/`.

---

## 📝 Bonnes Pratiques

1. **Nommage** : Utilisez des noms clairs et descriptifs pour les tables et les colonnes.
2. **Consistance** : Maintenez une consistance dans les types de données et les conventions de nommage.
3. **Documentation** : Documentez chaque table, colonne, et relation pour faciliter la maintenance.
4. **Indexation** : Ajoutez des index pour améliorer les performances des requêtes.
5. **Sécurité** : Ne stockez jamais de mots de passe en clair. Utilisez toujours des fonctions de hachage.

---

## 🔄 Mises à Jour

Toute mise à jour de la structure de la BDD doit être documentée dans le fichier de spécifications techniques et dans le fichier SQL correspondant. Les modifications doivent être versionnées et testées avant d'être déployées.