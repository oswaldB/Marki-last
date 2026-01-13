#!/usr/bin/env python3
"""
Script: Récupération des Factures Impayées
Fichier: app/scripts/relances/fetch_unpaid_invoices.py

Récupère les factures impayées depuis une base de données externe (ADN)
et les stocke dans factures_impayees.db pour les campagnes de relance.

Usage:
    python app/scripts/relances/fetch_unpaid_invoices.py \\
        --log "reports/ST-002-fetch_unpaid_invoices.log"
"""

import sys
import logging
import argparse
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
from functools import lru_cache

# Configuration logging
def setup_logger(log_file: str) -> logging.Logger:
    """Configure et retourne un logger."""
    log_path = Path(log_file).parent
    log_path.mkdir(parents=True, exist_ok=True)
    
    logger = logging.getLogger('fetch_unpaid_invoices')
    logger.setLevel(logging.INFO)
    
    # Handler fichier
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    
    # Format
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    return logger


def get_adn_connection_config() -> Dict:
    """
    Retourne la configuration de connexion ADN depuis .env ou variables d'environnement.
    
    Returns:
        Dict avec 'host', 'port', 'database', 'user', 'password'
    
    Raises:
        ValueError: Si configurations manquantes
    """
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    config = {
        'host': os.getenv('ADN_DB_HOST', 'adn-database-server'),
        'port': int(os.getenv('ADN_DB_PORT', '5432')),
        'database': os.getenv('ADN_DB_NAME', 'adn_adti'),
        'user': os.getenv('ADN_DB_USER', 'adn_user'),
        'password': os.getenv('ADN_DB_PASSWORD', '')
    }
    
    if not config['password']:
        raise ValueError("ADN_DB_PASSWORD non configuré dans .env")
    
    return config


def connect_adn_database(config: Dict):
    """
    Établit une connexion à la base de données ADN.
    
    Args:
        config: Configuration de connexion
    
    Returns:
        Connexion PostgreSQL
    
    Raises:
        ConnectionError: Si connexion échoue
    """
    try:
        import psycopg2
        
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )
        
        return conn
    
    except ImportError:
        raise ImportError("psycopg2 non installé: pip install psycopg2-binary")
    except Exception as e:
        raise ConnectionError(f"Connexion ADN échouée: {str(e)}")


def fetch_from_adn(conn, logger: logging.Logger) -> List[Dict]:
    """
    Récupère les factures impayées depuis ADN.
    
    Args:
        conn: Connexion à la base ADN
        logger: Logger pour tracer l'exécution
    
    Returns:
        Liste des factures
    
    Raises:
        Exception: Si requête échoue
    """
    query = """
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
        COALESCE(u.prenom || ' ' || u.nom, '') AS commercial_name,
        COALESCE(u.email, '') AS commercial_email
    FROM factures p
    JOIN clients c ON p.idclient = c.idclient
    LEFT JOIN utilisateurs u ON p.idcommercial = u.idutilisateur
    WHERE 
        p.date_echéance < CURRENT_DATE 
        AND p.statut_paiement = 'impayée'
        AND p.date_creation > CURRENT_DATE - INTERVAL '2 years'
    ORDER BY p.date_echéance DESC
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        
        # Récupérer les noms de colonnes
        columns = [desc[0] for desc in cursor.description]
        
        # Convertir en liste de dictionnaires
        invoices = []
        for row in cursor.fetchall():
            invoice = dict(zip(columns, row))
            invoices.append(invoice)
        
        cursor.close()
        logger.info(f"Factures récupérées: {len(invoices)}")
        
        return invoices
    
    except Exception as e:
        logger.error(f"Erreur lors de la récupération: {str(e)}")
        raise


def get_local_db(db_type: str = 'pickledb'):
    """
    Retourne une instance de la base de données locale.
    
    Args:
        db_type: Type de base ("pickledb" ou "sql")
    
    Returns:
        Instance DB
    """
    if db_type == 'pickledb':
        try:
            import pickledb
            return pickledb.load('app/data/factures_impayees.db', auto_dump=True)
        except ImportError:
            raise ImportError("pickledb non installé: pip install pickledb")
    else:
        raise ValueError(f"Type de base non supporté: {db_type}")


def get_existing_nfactures(db, db_type: str = 'pickledb') -> set:
    """
    Retourne l'ensemble des nfacture existants dans la base locale.
    
    Args:
        db: Instance de la base de données
        db_type: Type de base
    
    Returns:
        Set de nfacture
    """
    if db_type == 'pickledb':
        existing = db.get('factures_impayees') or []
        return set(inv['nfacture'] for inv in existing if 'nfacture' in inv)
    
    return set()


def validate_invoice(invoice: Dict) -> Tuple[bool, str]:
    """
    Valide une facture impayée.
    
    Args:
        invoice: Données de la facture
    
    Returns:
        (is_valid, error_message)
    """
    # Champs obligatoires
    required_fields = ['nfacture', 'montant_ht', 'montant_ttc', 'date_echéance']
    
    for field in required_fields:
        if field not in invoice:
            return False, f"Champ obligatoire manquant: {field}"
    
    # Validation montants
    try:
        ht = float(invoice['montant_ht'])
        ttc = float(invoice['montant_ttc'])
        
        if ht <= 0 or ttc <= 0:
            return False, "Montants invalides (doit être > 0)"
        
        if ttc < ht:
            return False, "Montant TTC inférieur à HT"
    except (ValueError, TypeError):
        return False, "Montants non numériques"
    
    return True, ""


def enrich_invoice(invoice: Dict) -> Dict:
    """
    Enrichit une facture avec métadonnées.
    
    Args:
        invoice: Données de la facture
    
    Returns:
        Facture enrichie
    """
    enriched = invoice.copy()
    
    # Ajouter statut de relance initial
    enriched['statut_relance'] = 'non_relancee'
    
    # Ajouter date d'import
    enriched['date_import'] = datetime.now().isoformat() + 'Z'
    
    # Ajouter flag si email manquant
    if not enriched.get('client_email'):
        enriched['email_status'] = 'missing'
    else:
        enriched['email_status'] = 'ok'
    
    return enriched


def save_invoices(invoices: List[Dict], db, db_type: str = 'pickledb', logger: logging.Logger = None):
    """
    Enregistre les factures dans la base de données.
    
    Args:
        invoices: Liste des factures
        db: Instance de la base de données
        db_type: Type de base
        logger: Logger optionnel
    """
    if db_type == 'pickledb':
        existing = db.get('factures_impayees') or []
        existing.extend(invoices)
        db.set('factures_impayees', existing)
        
        if logger:
            logger.info(f"Factures enregistrées: {len(invoices)}")
    else:
        raise ValueError(f"Type de base non supporté: {db_type}")


def fetch_unpaid_invoices(log_file: str = 'reports/ST-fetch_unpaid_invoices.log', db_type: str = 'pickledb') -> Dict:
    """
    Récupère les factures impayées depuis ADN et les stocke localement.
    
    Args:
        log_file: Chemin vers le fichier de log
        db_type: Type de base ("pickledb" ou "sql")
    
    Returns:
        Dict avec résultat: {'total': N, 'imported': N, 'duplicates': N, 'no_email': N, 'amount': X}
    
    Raises:
        ConnectionError: Si connexion ADN échoue
        ValueError: Si données invalides
    """
    logger = setup_logger(log_file)
    logger.info("DÉBUT: Récupération factures impayées")
    
    try:
        # Configuration et connexion
        config = get_adn_connection_config()
        logger.info("Configuration ADN: OK")
        
        adn_conn = connect_adn_database(config)
        logger.info("Connexion ADN: OK")
        
        # Récupération depuis ADN
        invoices = fetch_from_adn(adn_conn, logger)
        adn_conn.close()
        
        # Chargement base locale
        local_db = get_local_db(db_type)
        existing_nfactures = get_existing_nfactures(local_db, db_type)
        logger.info(f"Factures existantes: {len(existing_nfactures)}")
        
        # Dédoublonnage
        new_invoices = [
            inv for inv in invoices 
            if inv.get('nfacture') not in existing_nfactures
        ]
        duplicates = len(invoices) - len(new_invoices)
        logger.info(f"Doublons ignorés: {duplicates}")
        
        # Validation et enrichissement
        valid_invoices = []
        no_email_count = 0
        invalid_count = 0
        
        for inv in new_invoices:
            is_valid, error = validate_invoice(inv)
            
            if not is_valid:
                logger.warning(f"Facture invalide {inv.get('nfacture')}: {error}")
                invalid_count += 1
                continue
            
            enriched = enrich_invoice(inv)
            
            if enriched.get('email_status') == 'missing':
                no_email_count += 1
                logger.warning(f"Facture {inv.get('nfacture')}: email client manquant")
            
            valid_invoices.append(enriched)
        
        # Enregistrement
        if valid_invoices:
            save_invoices(valid_invoices, local_db, db_type, logger)
        
        # Résumé
        total_amount = sum(inv.get('montant_ttc', 0) for inv in valid_invoices)
        
        logger.info(f"Factures importées: {len(valid_invoices)}")
        logger.info(f"Sans email: {no_email_count}")
        logger.info(f"Invalides: {invalid_count}")
        logger.info(f"Montant total: {total_amount:,.2f} €")
        logger.info("FIN: Succès")
        
        return {
            'total': len(invoices),
            'imported': len(valid_invoices),
            'duplicates': duplicates,
            'no_email': no_email_count,
            'invalid': invalid_count,
            'amount': total_amount
        }
    
    except Exception as e:
        logger.error(f"ERREUR: {str(e)}")
        raise


def main():
    """Point d'entrée du script."""
    parser = argparse.ArgumentParser(
        description='Récupère les factures impayées depuis ADN'
    )
    
    parser.add_argument(
        '--log',
        help='Chemin vers le fichier de log',
        default='reports/ST-fetch_unpaid_invoices.log'
    )
    
    parser.add_argument(
        '--db-type',
        help='Type de base de données',
        choices=['pickledb', 'sql'],
        default='pickledb'
    )
    
    args = parser.parse_args()
    
    result = fetch_unpaid_invoices(
        log_file=args.log,
        db_type=args.db_type
    )
    
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
