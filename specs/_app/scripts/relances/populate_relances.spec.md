# Spécifications du Script : Population des Relances
**Fichier cible** : `scripts/populate_relances.py`

---
## **Description**
Ce script peuple le tableau des relances à partir de la séquence des campagnes. Il génère les relances pour chaque facture correspondant aux critères de la campagne et les stocke dans la base de données des relances.

---
## **Entrées**
- **Bases de données** :
  - `campagnes.db` : Contient les campagnes et leurs séquences.
  - `relances.db` : Contient les factures et leurs relances associées.
- **Fichier de log** : `reports/relances_population.log`

---
## **Sorties**
- **Base de données mise à jour** : `relances.db` avec les nouvelles relances ajoutées.
- **Fichier de log** : `reports/relances_population.log` avec les détails de l'exécution.

---
## **Fonctions Principales**
### `populate_relances(campagnes_db_path, relances_db_path, log_file)`
- **Description** : Peupler le tableau des relances à partir de la séquence des campagnes.
- **Paramètres** :
  - `campagnes_db_path` : Chemin vers la base de données des campagnes.
  - `relances_db_path` : Chemin vers la base de données des relances.
  - `log_file` : Chemin vers le fichier de log.
- **Exceptions** :
  - `ValueError` : Si les données sont invalides.
  - `IOError` : Si les fichiers sont illisibles.

---
## **Exemple d'Appel**
```bash
python scripts/relances/populate_relances.py \
  --campagnes-db specs/bdd/relances/campagnes.db \
  --relances-db specs/bdd/relances/relances.db \
  --log reports/relances_population.log
```

---
## **Sortie en Cas de Succès**
```
2024-10-15 18:00:00 - INFO - Relance ajoutée pour la facture FACT-2024-001 (campagne CAMP-2024-001)
2024-10-15 18:00:00 - INFO - Population des relances terminée avec succès
```

---
## **Sortie en Cas d'Échec**
```
2024-10-15 18:00:00 - ERREUR - Erreur lors de la population des relances: Structure de base de données invalide
```
