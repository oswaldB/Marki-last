# Guide: Comment Ajouter un Nouveau Script

## 📋 Checklist Complète

Pour ajouter un nouveau script à la structure, suivez ces étapes:

### 1. **Créer la Spécification (specs)**

Fichier: `specs/_app/scripts/[categorie]/[nom_script].spec.md`

**Template minimal**:
```markdown
# Script : [Nom du Script]
**Type** : Backend batch script
**Fichier cible** : `app/scripts/[categorie]/[nom_script].py`

---

## **Description**
[Description en 1 phrase]

---

## **Entrées**
[Fichiers, BDD, variables d'environnement]

---

## **Flux Principal**
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

---

## **Sortie (Log)**
Fichier : `reports/ST-[NUM]-[nom_script].log`

---

## **Fonction Principale**
```python
def [nom_script](log_file='reports/ST-[nom_script].log', **kwargs):
    """Docstring"""
    pass
```

---

## **Appel**
```bash
python app/scripts/[categorie]/[nom_script].py \\
    --log "reports/ST-[NUM]-[nom_script].log"
```
```

### 2. **Créer le Script Python**

Fichier: `scripts/[categorie]/[nom_script].py`

**Structure minimale**:
```python
#!/usr/bin/env python3
"""
Script: [Nom Descriptif]
Fichier: app/scripts/[categorie]/[nom_script].py

[Description courte]

Usage:
    python app/scripts/[categorie]/[nom_script].py \\
        --log "reports/ST-[NUM]-[nom_script].log"
"""

import sys
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# ============================================================================
# CONFIGURATION & LOGGING
# ============================================================================

def setup_logger(log_file: str) -> logging.Logger:
    """Configure et retourne un logger."""
    log_path = Path(log_file).parent
    log_path.mkdir(parents=True, exist_ok=True)
    
    logger = logging.getLogger('[nom_script]')
    logger.setLevel(logging.INFO)
    
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    return logger

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def [function_1]():
    """Description"""
    pass

def [function_2]():
    """Description"""
    pass

# ============================================================================
# FONCTION PRINCIPALE
# ============================================================================

def [nom_script](log_file: str = 'reports/ST-[nom_script].log', **kwargs) -> Dict:
    """
    [Description complète]
    
    Args:
        log_file: Chemin vers le fichier de log
        **kwargs: Arguments supplémentaires
    
    Returns:
        Dict avec résultats
    
    Raises:
        [ExceptionType]: [Description]
    """
    logger = setup_logger(log_file)
    logger.info("DÉBUT: [description]")
    
    try:
        # Votre logique ici
        
        logger.info("FIN: Succès")
        return {
            'status': 'success',
            'message': 'Exécution réussie'
        }
    
    except Exception as e:
        logger.error(f"ERREUR: {str(e)}")
        raise

# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

def main():
    """Point d'entrée du script."""
    parser = argparse.ArgumentParser(
        description='[Description courte]'
    )
    
    parser.add_argument(
        '--log',
        help='Chemin vers le fichier de log',
        default='reports/ST-[nom_script].log'
    )
    
    args = parser.parse_args()
    
    result = [nom_script](log_file=args.log)
    print(json.dumps(result, indent=2))
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

### 3. **Mettre à Jour les Références**

#### 3.1 Mettre à jour `specs/specs/[module]_specs.md`

Ajouter une section sous "Scripts Backend":

```markdown
### [N]. [Nom du Script]
- **Script** : `app/scripts/[categorie]/[nom_script].py`
- **Description** : [Description courte]
- **Spécifications** : [Voir le script](../../_app/scripts/[categorie]/[nom_script].spec.md)
- **Exemple d'appel** :
  ```bash
  python app/scripts/[categorie]/[nom_script].py \
      --log "reports/ST-<NUM>-[nom_script].log"
  ```
```

#### 3.2 Mettre à jour `scripts/README.md`

Ajouter une section sous "Scripts Disponibles":

```markdown
### [N]. [Nom du Script]
**Fichier** : `scripts/[categorie]/[nom_script].py`

[Description]

**Usage** :
```bash
python app/scripts/[categorie]/[nom_script].py \
    --log reports/ST-[NUM]-[nom_script].log
```

**Spécifications** : Voir [[nom_script].spec.md](../specs/_app/scripts/[categorie]/[nom_script].spec.md)
```

### 4. **Ajouter des Tests** (Optionnel mais Recommandé)

Fichier: `tests/scripts/test_[nom_script].py`

```python
import pytest
from pathlib import Path
import sys

# Ajouter le chemin du script
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'scripts'))

from [categorie].[nom_script] import [nom_script], [function_1], [function_2]

class TestScript:
    """Tests pour [nom_script]"""
    
    def test_basic_execution(self):
        """Test l'exécution basique"""
        result = [nom_script]()
        assert result['status'] == 'success'
    
    def test_[something](self):
        """Test [quelque chose]"""
        assert [function_1]() == [expected_value]
```

### 5. **Vérifier la Structure Complète**

```bash
# Vérifier que tous les fichiers existent
ls -la scripts/[categorie]/[nom_script].py
ls -la specs/_app/scripts/[categorie]/[nom_script].spec.md

# Tester le script
python scripts/[categorie]/[nom_script].py --help

# Exécuter le script
python scripts/[categorie]/[nom_script].py --log reports/test-[nom_script].log
```

---

## 📂 Catégories Disponibles

| Catégorie | Utilité | Exemples |
|-----------|---------|----------|
| `auth/` | Authentification & sécurité | Création users, reset password |
| `commissions/` | Gestion des commissions | Process factures, split commissions |
| `relances/` | Gestion des relances | Fetch factures impayées, send reminders |
| `app/` (future) | App-wide utilities | Backups, migrations, monitoring |

---

## 🎯 Bonnes Pratiques

### Code
- ✅ Type hints systématiques (`def func(arg: str) -> Dict:`)
- ✅ Docstrings pour toutes les fonctions (JSDoc-style)
- ✅ Gestion d'erreurs complète (try/except)
- ✅ Logging à chaque étape importante

### Spécifications
- ✅ Décrire les entrées/sorties exactement
- ✅ Inclure des exemples concrets JSON/SQL
- ✅ Lister tous les codes d'erreur possibles
- ✅ Expliquer chaque règle métier

### Documentation
- ✅ README.md à jour avec tous les scripts
- ✅ Chemin d'exécution clair (command line examples)
- ✅ Variables d'environnement documentées (.env)
- ✅ Dépendances listées (pip install)

### Tests
- ✅ Au minimum 1 test par fonction publique
- ✅ Tests d'erreur (inputs invalides)
- ✅ Tests d'intégration (full workflow)

---

## 🚀 Exemple Complet : Nouveau Script de Nettoyage

### Fichier 1: Spec
`specs/_app/scripts/app/cleanup_old_logs.spec.md`

```markdown
# Script : Nettoyage des Anciens Logs
**Type** : Backend maintenance script
**Fichier cible** : `app/scripts/app/cleanup_old_logs.py`

---

## **Description**
Supprime les fichiers de log de plus de 30 jours.

---

## **Entrées**
- **Dossier** : `reports/`
- **Paramètre** : `--days` (défaut: 30)

---

## **Flux Principal**
1. Scanner le dossier `reports/`
2. Identifier les logs de plus de N jours
3. Supprimer les fichiers
4. Logger les opérations

---

## **Sortie (Log)**
Fichier : `reports/ST-cleanup-old-logs.log`

[FORMAT...]

---

## **Appel**
```bash
python app/scripts/app/cleanup_old_logs.py \
    --days 30 \
    --log "reports/ST-cleanup-old-logs.log"
```
```

### Fichier 2: Script
`scripts/app/cleanup_old_logs.py`

```python
#!/usr/bin/env python3
import sys
import os
import logging
from pathlib import Path
from datetime import datetime, timedelta
import json

def setup_logger(log_file: str):
    # [implementation...]
    pass

def cleanup_old_logs(days: int = 30, log_file: str = '...') -> dict:
    logger = setup_logger(log_file)
    logger.info("DÉBUT: Nettoyage des logs")
    
    reports_dir = Path('reports')
    cutoff_date = datetime.now() - timedelta(days=days)
    
    deleted = 0
    total_size = 0
    
    for log_file in reports_dir.glob('*.log'):
        if log_file.stat().st_mtime < cutoff_date.timestamp():
            size = log_file.stat().st_size
            log_file.unlink()
            deleted += 1
            total_size += size
            logger.info(f"Supprimé: {log_file.name}")
    
    logger.info(f"FIN: {deleted} fichiers supprimés")
    return {
        'deleted': deleted,
        'total_size_mb': total_size / 1024 / 1024
    }

def main():
    # [argparse...]
    pass

if __name__ == '__main__':
    sys.exit(main())
```

### Fichier 3: Test
`tests/scripts/test_cleanup_old_logs.py`

```python
import pytest
from pathlib import Path
import tempfile
from datetime import datetime, timedelta

def test_cleanup_removes_old_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Créer fichiers old et new
        old_file = Path(tmpdir) / 'old.log'
        old_file.write_text('old')
        old_file.touch()
        
        # Modifier timestamp
        old_time = (datetime.now() - timedelta(days=40)).timestamp()
        os.utime(old_file, (old_time, old_time))
        
        # Exécuter cleanup
        result = cleanup_old_logs(days=30)
        
        # Vérifier suppression
        assert not old_file.exists()
        assert result['deleted'] == 1
```

---

## ❓ FAQ

**Q: Où placer mon script?**
A: Dans `scripts/[categorie]/[nom].py` où `categorie` est l'une des catégories disponibles.

**Q: Comment importer depuis mon script?**
A: 
```python
from scripts.commissions.process_commissions import process_commissions
```

**Q: Comment tester avant de merger?**
A: 
```bash
python scripts/[categorie]/[nom].py --log /tmp/test.log
# Vérifier que le log a été créé et ne contient pas d'ERREUR
cat /tmp/test.log
```

**Q: Dois-je créer une spec?**
A: Oui! C'est obligatoire pour maintenir la cohérence du projet.

---

## 📞 Questions?

Consulter les scripts existants:
- `scripts/commissions/process_commissions.py`
- `scripts/relances/fetch_unpaid_invoices.py`

Consulter les specs existantes:
- `specs/_app/scripts/commissions/process_commissions.spec.md`
- `specs/_app/scripts/relances/fetch_unpaid_invoices.spec.md`
