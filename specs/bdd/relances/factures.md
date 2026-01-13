# Base de Données : Factures Impayées
**Type** : PickleDB
**Fichier cible** : `app/data/relances/factures_impayees.db`

---

## **Structure**

### Clé Racine : `factures_impayees`

```json
{
  "factures_impayees": [
    {
      "id": 1,
      "numero_facture": "FACT-2026-001",
      "montant": 1500.00,
      "reste_a_payer": 1500.00,
      "date_echeance": "2025-12-15",
      "statut": "impayee",
      "proprietaire_prenom": "Jean",
      "proprietaire_nom": "Dupont",
      "proprietaire_email": "jean.dupont@example.com",
      "apporteur_affaire_prenom": "Marie",
      "apporteur_affaire_nom": "Martin",
      "apporteur_affaire_email": "marie.martin@example.com",
      "notaire_prenom": "Pierre",
      "notaire_nom": "Bernard",
      "notaire_email": "pierre.bernard@example.com",
      "payeur": "proprietaire",
      "date_ajout": "2026-01-13T17:00:00Z"
    }
  ]
}
```

---

## **Schéma des Champs**

| Champ | Type | Unique | Nullable | Description |
|-------|------|--------|----------|-------------|
| `id` | Integer | ✓ | ✗ | Identifiant unique auto-incrémenté |
| `numero_facture` | String | ✓ | ✗ | Numéro de facture (FACT-YYYY-NNN) |
| `montant` | Float | | ✗ | Montant total (> 0) |
| `reste_a_payer` | Float | | ✗ | Montant restant à payer (≥ 0) |
| `date_echeance` | String (YYYY-MM-DD) | | ✗ | Date d'échéance |
| `statut` | String | | ✗ | impayee\|partially_paid |
| `proprietaire_prenom` | String | | ✗ | Prénom du propriétaire |
| `proprietaire_nom` | String | | ✗ | Nom du propriétaire |
| `proprietaire_email` | String | | ✓ | Email du propriétaire |
| `apporteur_affaire_prenom` | String | | ✓ | Prénom apporteur d'affaires |
| `apporteur_affaire_nom` | String | | ✓ | Nom apporteur d'affaires |
| `apporteur_affaire_email` | String | | ✓ | Email apporteur d'affaires |
| `notaire_prenom` | String | | ✓ | Prénom du notaire |
| `notaire_nom` | String | | ✓ | Nom du notaire |
| `notaire_email` | String | | ✓ | Email du notaire |
| `payeur` | String | | ✗ | Responsable paiement : proprietaire\|notaire\|apporteur_affaire |
| `date_ajout` | String (ISO 8601) | | ✗ | Date d'ajout à la liste |

---

## **Contraintes**

- `numero_facture` : Format FACT-YYYY-NNN, **unique**
- `montant`, `reste_a_payer` : > 0, reste_a_payer ≤ montant
- `statut` : Restreint à impayee, partially_paid
- `payeur` : Restreint à proprietaire, notaire, apporteur_affaire
- Au moins un email doit être présent (proprietaire, apporteur ou notaire)

---

## **Fonctions Obligatoires**

### `get_db()`
Charge la base de données PickleDB.

```python
def get_db():
    return db.PickleDB('app/data/relances/factures_impayees.db', auto_dump=True)
```

---

### `get_all_invoices()`
Récupère toutes les factures impayées.

```python
def get_all_invoices(db):
    return db.get_all()['factures_impayees'] or []
```

---

### `get_invoice(db, invoice_id)`
Récupère une facture par ID.

```python
def get_invoice(db, invoice_id):
    invoices = db.get_all()['factures_impayees']
    return next((i for i in invoices if i['id'] == invoice_id), None)
```

---

### `get_invoice_by_numero(db, numero_facture)`
Récupère une facture par numéro.

```python
def get_invoice_by_numero(db, numero_facture):
    invoices = db.get_all()['factures_impayees']
    return next((i for i in invoices if i['numero_facture'] == numero_facture), None)
```

---

### `get_invoices_without_email()`
Récupère les factures sans email valide.

```python
def get_invoices_without_email(db):
    invoices = db.get_all()['factures_impayees']
    return [i for i in invoices if not i.get('proprietaire_email') and 
            not i.get('apporteur_affaire_email') and 
            not i.get('notaire_email')]
```

---

### `add_invoice(db, numero_facture, montant, reste_a_payer, date_echeance, proprietaire_info, apporteur_info, notaire_info, payeur)`
Ajoute une facture avec validation.

**Validations** :
- `numero_facture` unique et format valide
- `montant`, `reste_a_payer` > 0
- Au moins un email présent

```python
def add_invoice(db, numero_facture, montant, reste_a_payer, date_echeance, 
               proprietaire_info, apporteur_info, notaire_info, payeur):
    # Validations...
    invoices = db.get_all()['factures_impayees']
    
    if any(i['numero_facture'] == numero_facture for i in invoices):
        raise ValueError("Facture existe déjà")
    
    new_id = max((i['id'] for i in invoices), default=0) + 1
    new_invoice = {
        "id": new_id,
        "numero_facture": numero_facture,
        "montant": montant,
        "reste_a_payer": reste_a_payer,
        "date_echeance": date_echeance,
        "statut": "impayee",
        **proprietaire_info,
        **apporteur_info,
        **notaire_info,
        "payeur": payeur,
        "date_ajout": datetime.now().isoformat() + "Z"
    }
    
    invoices.append(new_invoice)
    db.set('factures_impayees', invoices)
    return new_invoice
```

---

### `update_invoice(db, invoice_id, **kwargs)`
Met à jour une facture.

```python
def update_invoice(db, invoice_id, **kwargs):
    invoices = db.get_all()['factures_impayees']
    invoice = next((i for i in invoices if i['id'] == invoice_id), None)
    if not invoice:
        raise ValueError("Facture introuvable")
    
    invoice.update(kwargs)
    db.set('factures_impayees', invoices)
    return invoice
```

---

### `delete_invoice(db, invoice_id)`
Supprime une facture de la liste.

```python
def delete_invoice(db, invoice_id):
    invoices = db.get_all()['factures_impayees']
    invoices = [i for i in invoices if i['id'] != invoice_id]
    db.set('factures_impayees', invoices)
```

---

### `sync_from_external_db(db, query_func)`
Synchronise depuis une base de données externe.

**Query func** : Fonction qui retourne une liste de factures impayées depuis la source externe.

```python
def sync_from_external_db(db, query_func):
    """
    Synchronise les factures impayées depuis une base externe.
    query_func doit retourner une liste de dict avec les champs:
    numero_facture, montant, reste_a_payer, date_echeance, 
    proprietaire_*, apporteur_*, notaire_*, payeur
    """
    external_invoices = query_func()
    current_invoices = db.get_all()['factures_impayees']
    
    # Ajouter ou mettre à jour
    for ext_inv in external_invoices:
        existing = next((i for i in current_invoices 
                        if i['numero_facture'] == ext_inv['numero_facture']), None)
        if existing:
            existing.update(ext_inv)
        else:
            add_invoice(db, **ext_inv)
```

---

### `init_db()`
Initialise la base de données si vide.

```python
def init_db():
    db = PickleDB('app/data/relances/factures_impayees.db', auto_dump=True)
    if not db.get_all().get('factures_impayees'):
        db.set('factures_impayees', [])
    return db
```
