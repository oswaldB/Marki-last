# Base de Données : Relances et Factures
**Type** : PickleDB
**Fichier cible** : `app/data/relances/relances.db`

---

## **Structure**

### Clé Racine : `relances`

```json
{
  "relances": [
    {
      "id": 1,
      "campaign_id": 1,
      "numero_facture": "FACT-2026-001",
      "montant": 1500.00,
      "reste_a_payer": 1500.00,
      "date_echeance": "2025-12-15",
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
      "recipient": "jean.dupont@example.com",
      "statut": "pending",
      "content": "Bonjour Jean,\n\nVotre facture FACT-2026-001...",
      "date": "2026-01-13T18:00:00Z",
      "open_date": null,
      "error_message": null
    }
  ]
}
```

---

## **Schéma des Champs**

| Champ | Type | Unique | Nullable | Description |
|-------|------|--------|----------|-------------|
| `id` | Integer | ✓ | ✗ | Identifiant unique auto-incrémenté |
| `campaign_id` | Integer | | ✗ | ID de la campagne associée |
| `numero_facture` | String | | ✗ | Numéro de facture (FACT-YYYY-NNN) |
| `montant` | Float | | ✗ | Montant total (> 0) |
| `reste_a_payer` | Float | | ✗ | Montant restant à payer (≥ 0) |
| `date_echeance` | String (YYYY-MM-DD) | | ✗ | Date d'échéance |
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
| `recipient` | String | | ✗ | Email destinataire |
| `statut` | String | | ✗ | pending\|sent\|failed\|opened |
| `content` | String | | ✗ | Contenu du message envoyé |
| `date` | String (ISO 8601) | | ✗ | Date d'envoi prévue/effectuée |
| `open_date` | String (ISO 8601) | | ✓ | Date d'ouverture de l'email |
| `error_message` | String | | ✓ | Message d'erreur si échec |

---

## **Contraintes**

- `numero_facture` : Format FACT-YYYY-NNN
- `montant`, `reste_a_payer` : > 0, reste_a_payer ≤ montant
- `payeur` : Restreint à proprietaire, notaire, apporteur_affaire
- `recipient` : Format email valide
- `statut` : Restreint à pending, sent, failed, opened

---

## **Fonctions Obligatoires**

### `get_db()`
Charge la base de données PickleDB.

```python
def get_db():
    return db.PickleDB('app/data/relances/relances.db', auto_dump=True)
```

---

### `get_all_reminders()`
Récupère toutes les relances.

```python
def get_all_reminders(db):
    return db.get_all()['relances'] or []
```

---

### `get_reminder(db, reminder_id)`
Récupère une relance par ID.

```python
def get_reminder(db, reminder_id):
    relances = db.get_all()['relances']
    return next((r for r in relances if r['id'] == reminder_id), None)
```

---

### `get_reminders_by_status(db, status)`
Récupère les relances filtrées par statut.

```python
def get_reminders_by_status(db, status):
    relances = db.get_all()['relances']
    return [r for r in relances if r['statut'] == status]
```

---

### `get_reminders_by_campaign(db, campaign_id)`
Récupère les relances d'une campagne.

```python
def get_reminders_by_campaign(db, campaign_id):
    relances = db.get_all()['relances']
    return [r for r in relances if r['campaign_id'] == campaign_id]
```

---

### `add_reminder(db, campaign_id, numero_facture, montant, reste_a_payer, date_echeance, proprietaire_info, apporteur_info, notaire_info, payeur, recipient, content, date_envoi)`
Ajoute une relance avec validation.

```python
def add_reminder(db, campaign_id, numero_facture, montant, reste_a_payer, 
                date_echeance, proprietaire_info, apporteur_info, notaire_info, 
                payeur, recipient, content, date_envoi):
    # Validations...
    relances = db.get_all()['relances']
    new_id = max((r['id'] for r in relances), default=0) + 1
    
    new_reminder = {
        "id": new_id,
        "campaign_id": campaign_id,
        "numero_facture": numero_facture,
        "montant": montant,
        "reste_a_payer": reste_a_payer,
        "date_echeance": date_echeance,
        **proprietaire_info,
        **apporteur_info,
        **notaire_info,
        "payeur": payeur,
        "recipient": recipient,
        "statut": "pending",
        "content": content,
        "date": date_envoi,
        "open_date": None,
        "error_message": None
    }
    
    relances.append(new_reminder)
    db.set('relances', relances)
    return new_reminder
```

---

### `update_reminder(db, reminder_id, **kwargs)`
Met à jour une relance.

```python
def update_reminder(db, reminder_id, **kwargs):
    relances = db.get_all()['relances']
    reminder = next((r for r in relances if r['id'] == reminder_id), None)
    if not reminder:
        raise ValueError("Relance introuvable")
    
    reminder.update(kwargs)
    db.set('relances', relances)
    return reminder
```

---

### `init_db()`
Initialise la base de données si vide.

```python
def init_db():
    db = PickleDB('app/data/relances/relances.db', auto_dump=True)
    if not db.get_all().get('relances'):
        db.set('relances', [])
    return db
```
