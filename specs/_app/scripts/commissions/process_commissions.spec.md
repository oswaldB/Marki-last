# Script : Traitement des Commissions
**Type** : Backend batch script
**Fichier cible** : `app/scripts/commissions/process_commissions.py`

---

## **Description**
Traite les commissions des techniciens à partir des factures et des missions associées. Valide la cohérence des données et gère les cas particuliers (factures mono-technicien, articles en pack, conflits).

---

## **Entrées**
- **Fichier JSON** (optionnel) : Format avec factures et leurs articles
- **Base de données** : `commissions.db` (PickleDB)

**Exemple d'entrée** :
```json
[
  {
    "nfacture": "FACT-2026-001",
    "montant_ht": 1500.00,
    "montant_ttc": 1800.00,
    "articles": [
      {"designation": "Dépannage", "montant": 500.00, "type_mission": "depannage"},
      {"designation": "Piézométrie", "montant": 1000.00, "type_mission": "piezo"}
    ],
    "intervenants": ["TECH-001", "TECH-002"]
  }
]
```

---

## **Flux Principal**

1. **Chargement** : Récupère les données des factures et missions
2. **Validation** : Vérifie cohérence articles/missions
3. **Traitement par cas** :
   - **Mono-intervenant** : Commission directe
   - **Multi-intervenant + articles lisibles** : Croisement article/mission → technicien
   - **Ambiguïté** : Marqué comme "conflit" → révision manuelle
4. **Enregistrement** : Stocke dans `commissions.db` ou `conflit_detail.db`
5. **Rapport** : Génère log avec statistiques

---

## **Règles Métier**

- **Commission mono-tech** : Si une seule personne sur la facture → enregistrement direct
- **Commission multi-tech** : Croiser articles avec types de mission pour attribuer à chaque tech
- **Conflit détecté** : Si impossible de mapper articles → techniciens, marqué comme `statut: "conflit"`
- **Validation montants** : Vérifier montant_ht + montant_ttc cohérents
- **Doublons** : Éviter importer 2x la même facture

---

## **Sortie (Log)**

Fichier : `reports/ST-[NUM]-process_commissions.log`

```
[2026-01-13 14:30:45] DÉBUT: Traitement des commissions
[2026-01-13 14:30:46] Factures chargées: 42
[2026-01-13 14:30:47] Commissions valides: 38
[2026-01-13 14:30:47] Commissions en conflit: 4
[2026-01-13 14:30:47] Montant traité: 85,500.00 €
[2026-01-13 14:30:47] FIN: Succès
```

---

## **Fonction Principale**

```python
def process_commissions(input_file=None, log_file='reports/ST-process_commissions.log', db_type='pickledb'):
    """
    Traite les commissions à partir des factures.
    
    Args:
        input_file (str): Chemin vers fichier JSON (optionnel)
        log_file (str): Chemin vers le fichier de log
        db_type (str): "pickledb" ou "sql"
    
    Returns:
        dict: Résultat avec {'total': N, 'valides': N, 'conflits': N, 'montant_total': X.XX}
    
    Raises:
        ValueError: Si données invalides
        IOError: Si fichier introuvable
    """
    logger = setup_logger(log_file)
    
    # Chargement des factures
    invoices = load_invoices(input_file)
    
    # Traitement
    commissions = []
    conflicts = []
    
    for invoice in invoices:
        result = process_single_invoice(invoice)
        if result['status'] == 'ok':
            commissions.append(result)
        else:
            conflicts.append(result)
    
    # Enregistrement
    save_commissions(commissions, db_type)
    save_conflicts(conflicts, db_type)
    
    # Log résultat
    logger.info(f"Commissions valides: {len(commissions)}")
    logger.info(f"Commissions en conflit: {len(conflicts)}")
    
    return {
        'total': len(invoices),
        'valides': len(commissions),
        'conflits': len(conflicts),
        'montant_total': sum(c['montant_ttc'] for c in commissions)
    }
```

---

## **Appel**

```bash
python app/scripts/commissions/process_commissions.py \
    --input data/factures.json \
    --log "reports/ST-001-process_commissions.log" \
    --db-type pickledb
```

---

## **Erreurs Possibles**

| Code | Message | Solution |
|------|---------|----------|
| 400 | Fichier JSON invalide | Vérifier format JSON |
| 404 | Fichier introuvable | Vérifier chemin d'accès |
| 422 | Montant invalide | Vérifier montant_ht, montant_ttc |
| 409 | Conflit détecté | Réviser manuellement via interface |
