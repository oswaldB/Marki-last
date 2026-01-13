# Script : Récupération des Factures Impayées
**Type** : Backend batch script  
**Fichier cible** : `app/scripts/relances/fetch_unpaid_invoices.py`

---

## **Description**
Récupère les factures impayées depuis une base de données externe (ADN) et les stocke dans `factures_impayees.db` (PickleDB) pour être utilisées par les campagnes de relance.

---

## **Entrées**

- **Connexion externe** : Base ADN (PostgreSQL)
  - Host : `adn-database-server`
  - Database : `adn_adti`
  - User/Password : Depuis `.env`

---

## **Flux Principal**

1. **Connexion** : Se connecte à la base ADN
2. **Requête** : Récupère factures avec `date_echéance < aujourd'hui` et `statut_paiement = 'impayée'`
3. **Enrichissement** : Ajoute détails client (email, téléphone) depuis plusieurs tables
4. **Dédoublonnage** : Élimine doublons basé sur `nfacture`
5. **Stockage** : Enregistre dans `factures_impayees.db`
6. **Rapport** : Log avec statistiques (N factures importées, doublons ignorés, etc.)

---

## **Requête SQL (ADN)**

```sql
SELECT 
    p.nfacture,
    p.idproduitmetier AS ndossier,
    p.refpiece,
    p.montant_ht,
    p.montant_ttc,
    p.date_echéance,
    p.date_emission,
    c.raison_sociale AS client_name,
    c.email AS client_email,
    c.telephone AS client_phone,
    u.prenom || ' ' || u.nom AS commercial_name,
    u.email AS commercial_email
FROM factures p
JOIN clients c ON p.idclient = c.idclient
LEFT JOIN utilisateurs u ON p.idcommercial = u.idutilisateur
WHERE 
    p.date_echéance < CURRENT_DATE 
    AND p.statut_paiement = 'impayée'
    AND p.date_creation > CURRENT_DATE - INTERVAL '2 years'
ORDER BY p.date_echéance DESC
```

---

## **Format de Stockage (PickleDB)**

```json
{
  "factures_impayees": [
    {
      "id": 1,
      "nfacture": "FACT-2025-12345",
      "ndossier": "DOSS-001",
      "refpiece": "REF-001",
      "montant_ht": 1500.00,
      "montant_ttc": 1800.00,
      "date_echéance": "2025-06-30",
      "date_emission": "2025-05-15",
      "client_name": "ClientX SARL",
      "client_email": "contact@clientx.fr",
      "client_phone": "+33612345678",
      "commercial_name": "Jean Dupont",
      "commercial_email": "jean.dupont@company.fr",
      "date_import": "2026-01-13T14:30:45Z",
      "statut_relance": "non_relancee"
    }
  ]
}
```

---

## **Règles Métier**

- **Doublons** : Ignorer si `nfacture` existe déjà dans `factures_impayees.db`
- **Validation** : Montant HT et TTC doivent être > 0
- **Email manquant** : Marquer comme "email_manquant" si pas de client_email
- **Historique** : Garder 2 ans de données maximum
- **Statut initial** : Toujours `"non_relancee"` à l'import

---

## **Sortie (Log)**

Fichier : `reports/ST-[NUM]-fetch_unpaid_invoices.log`

```
[2026-01-13 14:30:45] DÉBUT: Récupération factures impayées
[2026-01-13 14:30:46] Connexion ADN: OK
[2026-01-13 14:30:47] Factures récupérées: 127
[2026-01-13 14:30:48] Doublons ignorés: 5
[2026-01-13 14:30:48] Factures sans email: 12
[2026-01-13 14:30:48] Factures importées: 122
[2026-01-13 14:30:48] Montant total: 185,400.50 €
[2026-01-13 14:30:48] FIN: Succès
```

---

## **Fonction Principale**

```python
def fetch_unpaid_invoices(log_file='reports/ST-fetch_unpaid_invoices.log', db_type='pickledb'):
    """
    Récupère les factures impayées depuis ADN et les stocke localement.
    
    Args:
        log_file (str): Chemin vers le fichier de log
        db_type (str): "pickledb" ou "sql"
    
    Returns:
        dict: Résultat avec {'total': N, 'imported': N, 'duplicates': N, 'amount': X.XX}
    
    Raises:
        ConnectionError: Si connexion ADN échoue
        ValueError: Si données invalides
    """
    logger = setup_logger(log_file)
    
    # Connexion ADN
    adn_conn = connect_adn_database()
    
    # Récupération
    invoices = fetch_from_adn(adn_conn)
    logger.info(f"Factures récupérées: {len(invoices)}")
    
    # Dédoublonnage
    local_db = get_local_db(db_type)
    existing = get_existing_invoices(local_db)
    
    new_invoices = [inv for inv in invoices if inv['nfacture'] not in existing]
    duplicates = len(invoices) - len(new_invoices)
    
    # Enrichissement et validation
    valid_invoices = []
    no_email = 0
    
    for inv in new_invoices:
        if not inv.get('client_email'):
            no_email += 1
        valid_invoices.append(inv)
    
    # Stockage
    save_invoices(valid_invoices, local_db, db_type)
    
    # Log
    logger.info(f"Factures importées: {len(valid_invoices)}")
    logger.info(f"Doublons ignorés: {duplicates}")
    logger.info(f"Sans email: {no_email}")
    
    return {
        'total': len(invoices),
        'imported': len(valid_invoices),
        'duplicates': duplicates,
        'no_email': no_email,
        'amount': sum(inv['montant_ttc'] for inv in valid_invoices)
    }
```

---

## **Appel**

```bash
python app/scripts/relances/fetch_unpaid_invoices.py \
    --log "reports/ST-002-fetch_unpaid_invoices.log" \
    --db-type pickledb
```

---

## **Configuration (.env)**

```env
ADN_DB_HOST=adn-database-server
ADN_DB_PORT=5432
ADN_DB_NAME=adn_adti
ADN_DB_USER=adn_user
ADN_DB_PASSWORD=your_password_here
```

---

## **Erreurs Possibles**

| Code | Message | Solution |
|------|---------|----------|
| 503 | Connexion ADN échouée | Vérifier serveur ADN, identifiants .env |
| 422 | Données invalides | Vérifier montants > 0 |
| 409 | Conflit de doublons | Vérifier `nfacture` dans base locale |
| 500 | Erreur interne | Vérifier logs détaillés |
