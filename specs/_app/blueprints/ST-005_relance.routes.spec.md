# Routes : Relance des Impayées
**Fichier cible** : `app/blueprints/relance/routes.py`

---

## **Endpoints**

| URL | Méthode | Paramètres | Retour | Description |
|-----|---------|-----------|--------|-------------|
| `/relances` | GET | `?status=en_attente\|reglees`, `?delai=30\|60\|90` | HTML | Liste des relances |
| `/api/relances` | GET | `?status=`, `?page=`, `?limit=` | JSON | API liste paginée |
| `/api/relances/<id>` | GET | - | JSON | Détail d'une relance |
| `/api/relances/<id>/envoi` | POST | - | JSON | Envoie relance par email |
| `/api/relances/<id>/archive` | POST | - | JSON | Archive relance |

---

## **Structure de Données**

### Relance
```json
{
  "id": 1,
  "commission_id": "FACT-2026-001",
  "client": "Client ABC",
  "montant": 1800.00,
  "date_relance": "2026-01-13",
  "statut": "en_attente",
  "email": "contact@client.com",
  "delai_jours": 30
}
```

---

## **Règles Métier**

### Statuts
- `en_attente` : Relance à envoyer
- `reglees` : Facture réglée
- `archivee` : Relance archivée

### Génération Automatique
- Relances générées automatiquement pour commissions non réglées après délai
- Délais : 30, 60, 90 jours après `date_piece`
- Une relance par délai

### Envoi Email
- Email requis pour envoyer relance
- Historique d'envoi conservé

---

## **Codes d'Erreur**

| Code | Message | Contexte |
|------|---------|----------|
| `400` | Email invalide | Format email incorrect |
| `404` | Relance introuvable | `id` inexistant |
| `500` | Erreur email | Échec envoi SMTP |
