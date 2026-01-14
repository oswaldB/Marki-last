# Routes : Gestion des Commissions
**Fichier cible** : `app/blueprints/commissions/routes.py`

---

## **Endpoints**

| URL | Méthode | Paramètres | Retour | Description |
|-----|---------|-----------|--------|-------------|
| `/commissions` | GET | `?status=valide\|conflit\|archive`, `?filtre=...` | HTML | Liste des commissions |
| `/api/commissions` | GET | `?status=`, `?page=`, `?limit=` | JSON | API liste paginée |
| `/api/commissions/<nfacture>` | GET | - | JSON | Détail d'une commission |
| `/api/commissions/<nfacture>` | PUT | `statut`, `date_reglement` | JSON | Met à jour commission |
| `/api/commissions/<nfacture>/split` | POST | `subdivisions` | JSON | Subdivise une ligne |
| `/api/commissions/<nfacture>/archive` | POST | - | JSON | Archive une commission |
| `/api/get-file` | GET | `?url=...` | File | Retourne le fichier PDF |

---

## **Structure de Données**

### Commission
```json
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
```

---

## **Règles Métier**

### Statuts
- `valide` : Commission validée, prête à régler
- `conflit` : Commission en conflit, intervention manuelle nécessaire
- `archive` : Commission archivée, inactive

### Validation
- `nfacture` doit être **unique**
- `montant_ttc` ≥ `montant_ht`
- `statut` restreint aux 3 valeurs ci-dessus
- `date_reglement` peut être `null` ou format YYYY-MM-DD

### Cas Spéciaux
- **Mono-technicien** (`monotech=true`) : Facture avec 1 seul intervenant
- **Mono-dossier** (`mono_dossier=true`) : Facture associée à 1 seul dossier
- **Conflit** : Impossible de déterminer les intervenants → `statut='conflit'`

---

## **Codes d'Erreur**

| Code | Message | Contexte |
|------|---------|----------|
| `400` | Données invalides | Montants incohérents ou statut invalide |
| `404` | Commission introuvable | `nfacture` inexistante |
| `409` | Conflit | Commission en conflit, subdivision requise |
| `500` | Erreur serveur | Exception non gérée |
