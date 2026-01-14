# Base de Données : Commissions
**Type** : PickleDB
**Fichier cible** : `app/data/commissions.db`

---

## **Structure**

### Clé Racine : `commissions`

```json
{
  "commissions": [
    {
      "nfacture": "FACT-2026-001",
      "ndossier": "DOSS-2026-001",
      "reference_piece": "PIECE-2026-001",
      "intervenant": "tech_123",
      "montant_ht": 1500.00,
      "montant_ttc": 1800.00,
      "date_piece": "2026-01-12",
      "lien_facture": "/path/to/facture.pdf",
      "statut": "valide",
      "date_reglement": null,
      "conflit_detail": null,
      "monotech": true,
      "mono_dossier": true
    }
  ]
}
```

---

## **Schéma des Champs**

| Champ | Type | Unique | Nullable | Description |
|-------|------|--------|----------|-------------|
| `nfacture` | String | ✓ | ✗ | Numéro facture unique (FACT-YYYY-NNN) |
| `ndossier` | String | | ✗ | Numéro dossier associé |
| `reference_piece` | String | | ✗ | Référence de la pièce |
| `intervenant` | String | | ✗ | ID technicien/intervenant |
| `montant_ht` | Float | | ✗ | Montant HT (> 0) |
| `montant_ttc` | Float | | ✗ | Montant TTC (≥ montant_ht) |
| `date_piece` | String (YYYY-MM-DD) | | ✗ | Date de la pièce |
| `lien_facture` | String | | ✓ | Chemin vers PDF (optionnel) |
| `statut` | String | | ✗ | Statut : valide\|conflit\|archive |
| `date_reglement` | String (YYYY-MM-DD) | | ✓ | Date règlement (optionnel) |
| `conflit_detail` | String | | ✓ | Détails du conflit (optionnel) |
| `monotech` | Boolean | | ✗ | True si 1 seul technicien |
| `mono_dossier` | Boolean | | ✗ | True si 1 seul dossier |

---

## **Contraintes**

- `nfacture` : Format FACT-YYYY-NNN, **unique**
- `montant_ht`, `montant_ttc` : Doivent être > 0 et montant_ttc ≥ montant_ht
- `statut` : Restreint à `valide`, `conflit`, `archive`
- `date_reglement` : Null jusqu'à règlement
- `conflit_detail` : Non-null **seulement** si `statut='conflit'`

---

## **Fonctions Obligatoires**

### `get_db()`
Charge la base de données PickleDB.

```python
def get_db():
    return db.PickleDB('app/data/commissions.db', auto_dump=True)
```

---

### `get_all_commissions()`
Récupère toutes les commissions.

```python
def get_all_commissions(db):
    return db.get_all()['commissions'] or []
```

---

### `get_commission(db, nfacture)`
Récupère une commission par nfacture.

```python
def get_commission(db, nfacture):
    commissions = db.get_all()['commissions']
    return next((c for c in commissions if c['nfacture'] == nfacture), None)
```

---

### `get_commissions_by_status(db, status)`
Récupère les commissions filtrées par statut.

```python
def get_commissions_by_status(db, status):
    commissions = db.get_all()['commissions']
    return [c for c in commissions if c['statut'] == status]
```

---

### `add_commission(db, nfacture, ndossier, reference_piece, intervenant, montant_ht, montant_ttc, date_piece, lien_facture=None, monotech=True, mono_dossier=True)`
Ajoute une commission avec validation.

**Validations** :
- `nfacture` unique et format valide
- `montant_ttc` ≥ `montant_ht` et > 0
- `date_piece` format YYYY-MM-DD valide

```python
def add_commission(db, nfacture, ndossier, reference_piece, intervenant, 
                   montant_ht, montant_ttc, date_piece, lien_facture=None, 
                   monotech=True, mono_dossier=True):
    # Validation
    if not re.match(r'^FACT-\d{4}-\d{3}$', nfacture):
        raise ValueError("Format nfacture invalide")
    
    commissions = db.get_all()['commissions']
    if any(c['nfacture'] == nfacture for c in commissions):
        raise ValueError("nfacture existe déjà")
    
    if montant_ht <= 0 or montant_ttc < montant_ht:
        raise ValueError("Montants invalides")
    
    new_commission = {
        "nfacture": nfacture,
        "ndossier": ndossier,
        "reference_piece": reference_piece,
        "intervenant": intervenant,
        "montant_ht": montant_ht,
        "montant_ttc": montant_ttc,
        "date_piece": date_piece,
        "lien_facture": lien_facture,
        "statut": "valide",
        "date_reglement": None,
        "conflit_detail": None,
        "monotech": monotech,
        "mono_dossier": mono_dossier
    }
    
    commissions.append(new_commission)
    db.set('commissions', commissions)
    return new_commission
```

---

### `update_commission(db, nfacture, **kwargs)`
Met à jour une commission.

```python
def update_commission(db, nfacture, **kwargs):
    commissions = db.get_all()['commissions']
    commission = next((c for c in commissions if c['nfacture'] == nfacture), None)
    if not commission:
        raise ValueError("Commission introuvable")
    
    commission.update(kwargs)
    db.set('commissions', commissions)
    return commission
```

---

### `init_db()`
Initialise la base de données si vide.

```python
def init_db():
    db = PickleDB('app/data/commissions.db', auto_dump=True)
    if not db.get_all().get('commissions'):
        db.set('commissions', [])
    return db
```
