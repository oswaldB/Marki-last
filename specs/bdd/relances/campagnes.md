# Base de Données : Campagnes de Relance
**Type** : PickleDB
**Fichier cible** : `app/data/relances/campagnes.db`

---

## **Structure**

### Clé Racine : `campagnes`

```json
{
  "campagnes": [
    {
      "id": 1,
      "nom": "Relance 30 jours",
      "description": "Relance automatique après 30 jours",
      "statut": "active",
      "type": "automatique",
      "date_creation": "2026-01-13T10:00:00Z",
      "nombre_relances": 15,
      "selection_type": "automatic",
      "min_amount": 100.00,
      "days_overdue": 30,
      "sequence": [
        {
          "delay": 0,
          "subject": "Rappel facture {{numero_facture}}",
          "content": "Bonjour {{proprietaire_prenom}},\n\nVotre facture {{numero_facture}} d'un montant de {{montant}} € est en attente de règlement..."
        },
        {
          "delay": 7,
          "subject": "Relance urgente - {{numero_facture}}",
          "content": "..."
        }
      ]
    }
  ]
}
```

---

## **Schéma des Champs**

| Champ | Type | Unique | Nullable | Description |
|-------|------|--------|----------|-------------|
| `id` | Integer | ✓ | ✗ | Identifiant unique auto-incrémenté |
| `nom` | String | ✓ | ✗ | Nom de la campagne (3-100 caractères) |
| `description` | String | | ✓ | Description optionnelle |
| `statut` | String | | ✗ | Statut : active\|paused\|completed |
| `type` | String | | ✗ | Type : automatique\|manuelle |
| `date_creation` | String (ISO 8601) | | ✗ | Date création |
| `nombre_relances` | Integer | | ✗ | Nombre de relances effectuées (défaut: 0) |
| `selection_type` | String | | ✗ | automatic\|manual |
| `min_amount` | Float | | ✓ | Montant minimum pour sélection auto |
| `days_overdue` | Integer | | ✓ | Jours de retard pour sélection auto |
| `sequence` | Array | | ✗ | Séquence d'emails avec structure: `{delay, subject, content}` |

---

## **Contraintes**

- `nom` : Unique, 3-100 caractères
- `statut` : Restreint à `active`, `paused`, `completed`
- `type` : Restreint à `automatique`, `manuelle`
- `selection_type` : Restreint à `automatic`, `manual`
- `nombre_relances` : Entier ≥ 0
- `sequence` : Au moins 1 étape avec `{delay: Integer, subject: String, content: String}`

---

## **Fonctions Obligatoires**

### `get_db()`
Charge la base de données PickleDB.

```python
def get_db():
    return db.PickleDB('app/data/relances/campagnes.db', auto_dump=True)
```

---

### `get_all_campaigns()`
Récupère toutes les campagnes.

```python
def get_all_campaigns(db):
    return db.get_all()['campagnes'] or []
```

---

### `get_campaign(db, campaign_id)`
Récupère une campagne par ID.

```python
def get_campaign(db, campaign_id):
    campaigns = db.get_all()['campagnes']
    return next((c for c in campaigns if c['id'] == campaign_id), None)
```

---

### `get_campaigns_by_status(db, status)`
Récupère les campagnes filtrées par statut.

```python
def get_campaigns_by_status(db, status):
    campaigns = db.get_all()['campagnes']
    return [c for c in campaigns if c['statut'] == status]
```

---

### `add_campaign(db, nom, description, selection_type, sequence, min_amount=None, days_overdue=None)`
Ajoute une campagne avec validation.

**Validations** :
- `nom` unique et valide (3-100 caractères)
- `sequence` non vide et valide
- `selection_type` valide

```python
def add_campaign(db, nom, description, selection_type, sequence, min_amount=None, days_overdue=None):
    # Validation
    if not nom or len(nom) < 3 or len(nom) > 100:
        raise ValueError("Nom invalide")
    
    campaigns = db.get_all()['campagnes']
    if any(c['nom'] == nom for c in campaigns):
        raise ValueError("Campagne existe déjà")
    
    if not sequence or not isinstance(sequence, list):
        raise ValueError("Séquence invalide")
    
    new_id = max((c['id'] for c in campaigns), default=0) + 1
    new_campaign = {
        "id": new_id,
        "nom": nom,
        "description": description,
        "statut": "paused",
        "type": "automatique" if selection_type == "automatic" else "manuelle",
        "date_creation": datetime.now().isoformat() + "Z",
        "nombre_relances": 0,
        "selection_type": selection_type,
        "min_amount": min_amount,
        "days_overdue": days_overdue,
        "sequence": sequence
    }
    
    campaigns.append(new_campaign)
    db.set('campagnes', campaigns)
    return new_campaign
```

---

### `update_campaign(db, campaign_id, **kwargs)`
Met à jour une campagne.

```python
def update_campaign(db, campaign_id, **kwargs):
    campaigns = db.get_all()['campagnes']
    campaign = next((c for c in campaigns if c['id'] == campaign_id), None)
    if not campaign:
        raise ValueError("Campagne introuvable")
    
    campaign.update(kwargs)
    db.set('campagnes', campaigns)
    return campaign
```

---

### `delete_campaign(db, campaign_id)`
Supprime une campagne (seulement si paused).

```python
def delete_campaign(db, campaign_id):
    campaigns = db.get_all()['campagnes']
    campaign = next((c for c in campaigns if c['id'] == campaign_id), None)
    if not campaign:
        raise ValueError("Campagne introuvable")
    
    if campaign['statut'] != 'paused':
        raise ValueError("Impossible de supprimer une campagne active")
    
    campaigns = [c for c in campaigns if c['id'] != campaign_id]
    db.set('campagnes', campaigns)
```

---

### `init_db()`
Initialise la base de données si vide.

```python
def init_db():
    db = PickleDB('app/data/relances/campagnes.db', auto_dump=True)
    if not db.get_all().get('campagnes'):
        db.set('campagnes', [])
    return db
```
