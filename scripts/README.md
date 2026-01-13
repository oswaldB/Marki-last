# Scripts Backend - Documentation

Structure organisée par thématique des scripts Python pour Marki.

## 📁 Architecture

```
scripts/
├── auth/                          # Scripts d'authentification
│   └── __init__.py
├── commissions/                   # Scripts de gestion des commissions
│   ├── __init__.py
│   └── process_commissions.py    # Traitement des commissions
├── relances/                      # Scripts de gestion des relances
│   ├── __init__.py
│   └── fetch_unpaid_invoices.py  # Récupération factures impayées
└── fetch_and_import_commissions.py # [LEGACY] À déplacer dans commissions
```

## 📋 Scripts Disponibles

### 1. Traitement des Commissions
**Fichier** : `scripts/commissions/process_commissions.py`

Traite les commissions des techniciens à partir des factures.

**Usage** :
```bash
python app/scripts/commissions/process_commissions.py \
    --input data/factures.json \
    --log reports/ST-001-process_commissions.log \
    --db-type pickledb
```

**Spécifications** : Voir [process_commissions.spec.md](../specs/_app/scripts/commissions/process_commissions.spec.md)

---

### 2. Récupération des Factures Impayées
**Fichier** : `scripts/relances/fetch_unpaid_invoices.py`

Récupère les factures impayées depuis une base ADN externe.

**Usage** :
```bash
python app/scripts/relances/fetch_unpaid_invoices.py \
    --log reports/ST-002-fetch_unpaid_invoices.log \
    --db-type pickledb
```

**Configuration** : Ajouter dans `.env` :
```env
ADN_DB_HOST=adn-database-server
ADN_DB_PORT=5432
ADN_DB_NAME=adn_adti
ADN_DB_USER=adn_user
ADN_DB_PASSWORD=your_password
```

**Spécifications** : Voir [fetch_unpaid_invoices.spec.md](../specs/_app/scripts/relances/fetch_unpaid_invoices.spec.md)

---

## 🔧 Installation des Dépendances

```bash
# Pour PickleDB
pip install pickledb

# Pour PostgreSQL (ADN database)
pip install psycopg2-binary

# Pour les variables d'environnement
pip install python-dotenv

# Ou tout d'un coup
pip install pickledb psycopg2-binary python-dotenv
```

---

## 📝 Conventions

### Logging
- Tous les scripts créent des logs dans `reports/ST-[NUM]-[nom].log`
- Format : `[YYYY-MM-DD HH:MM:SS] LEVEL: message`
- Niveaux : INFO, WARNING, ERROR

### Retour (stdout)
- Format JSON avec les statistiques du script
- Exemple :
  ```json
  {
    "total": 127,
    "imported": 122,
    "duplicates": 5,
    "amount": 185400.50
  }
  ```

### Codes de Sortie
- `0` : Succès
- `1` : Erreur (voir logs)

---

## 🚀 Exécution en Production

### Via Cron
```bash
# Tous les jours à 2h du matin
0 2 * * * cd /path/to/marki && python app/scripts/relances/fetch_unpaid_invoices.py --log reports/$(date +\%Y-\%m-\%d)-fetch.log

# Tous les jours à 3h du matin
0 3 * * * cd /path/to/marki && python app/scripts/commissions/process_commissions.py --log reports/$(date +\%Y-\%m-\%d)-process.log
```

### Via Celery (optionnel)
À implémenter pour les tâches asynchrones.

---

## 📊 Base de Données

### PickleDB (format JSON)

**Location** : `app/data/`

**Fichiers** :
- `commissions.db` : Commissions traitées
- `factures_impayees.db` : Factures impayées
- `conflicts.db` : Commissions en conflit

**Structure exemple** :
```json
{
  "commissions": [
    {
      "nfacture": "FACT-2026-001",
      "montant_ttc": 1800.00,
      "type": "mono|multi|conflit",
      "statut": "ok|conflit",
      "date_traitement": "2026-01-13T14:30:45Z"
    }
  ]
}
```

---

## ⚠️ Gestion des Erreurs

Voir les fichiers spec (`.spec.md`) pour la liste complète des codes d'erreur possibles.

Exemple de gestion d'erreur courante :
```python
try:
    result = fetch_unpaid_invoices(log_file=logfile)
    print(json.dumps(result))
except ConnectionError as e:
    print(f"Erreur ADN: {e}", file=sys.stderr)
    sys.exit(1)
except ValueError as e:
    print(f"Données invalides: {e}", file=sys.stderr)
    sys.exit(1)
```

---

## 📝 À Faire

- [ ] Déplacer `fetch_and_import_commissions.py` dans `/commissions/`
- [ ] Créer scripts d'authentification dans `/auth/`
- [ ] Implémenter workers Celery pour exécution asynchrone
- [ ] Ajouter tests unitaires pour chaque script
- [ ] Créer dashboard pour monitoring des scripts

---

## 📖 Lectures Complémentaires

- [Architecture générale](../../README.md)
- [Spécifications des templates](../specs/_app/templates/)
- [Schémas de base de données](../specs/bdd/)
- [Routes et APIs](../specs/_app/blueprints/)
