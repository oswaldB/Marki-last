import os
import logging
from datetime import datetime
import psycopg2
from dotenv import load_dotenv
from pickledb import PickleDB

# Configuration
load_dotenv()
DB_HOST = os.getenv('ADN_DB_HOST')
DB_PORT = os.getenv('ADN_DB_PORT')
DB_NAME = os.getenv('ADN_DB_NAME')
DB_USER = os.getenv('ADN_DB_USER')
DB_PASSWORD = os.getenv('ADN_DB_PASSWORD')

def setup_logger(log_file):
    """Configure le logger."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger()

def connect_adn_database():
    """Connexion à la base ADN."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        raise ConnectionError(f"Connexion ADN échouée: {str(e)}")

def fetch_from_adn(conn):
    """Récupère les factures impayées depuis ADN."""
    cursor = conn.cursor()
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
    """
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    invoices = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    return invoices

def get_local_db(db_type='pickledb'):
    """Charge la base locale."""
    if db_type == 'pickledb':
        return PickleDB('app/data/relances/factures_impayees.db', auto_dump=True)
    else:
        raise ValueError("Type de base non supporté")

def get_existing_invoices(local_db):
    """Récupère les factures existantes."""
    existing = local_db.get('factures_impayees') or []
    return {inv['nfacture'] for inv in existing}

def save_invoices(invoices, local_db, db_type='pickledb'):
    """Sauvegarde les factures dans la base locale."""
    existing = local_db.get('factures_impayees') or []

    for inv in invoices:
        # Validation des données
        if inv['montant_ht'] <= 0 or inv['montant_ttc'] <= 0:
            raise ValueError(f"Montants invalides pour {inv['nfacture']}")

        # Ajout des champs supplémentaires
        inv.update({
            'date_import': datetime.utcnow().isoformat() + 'Z',
            'statut_relance': 'non_relancee'
        })

    existing.extend(invoices)
    local_db.set('factures_impayees', existing)

def fetch_unpaid_invoices(log_file='reports/ST-fetch_unpaid_invoices.log', db_type='pickledb'):
    """Récupère les factures impayées depuis ADN et les stocke localement."""
    logger = setup_logger(log_file)
    logger.info("DÉBUT: Récupération factures impayées")

    try:
        # Connexion ADN
        adn_conn = connect_adn_database()
        logger.info("Connexion ADN: OK")

        # Récupération
        invoices = fetch_from_adn(adn_conn)
        logger.info(f"Factures récupérées: {len(invoices)}")

        # Dédoublonnage
        local_db = get_local_db(db_type)
        existing = get_existing_invoices(local_db)

        new_invoices = [inv for inv in invoices if inv['nfacture'] not in existing]
        duplicates = len(invoices) - len(new_invoices)
        logger.info(f"Doublons ignorés: {duplicates}")

        # Enrichissement et validation
        valid_invoices = []
        no_email = 0

        for inv in new_invoices:
            if not inv.get('client_email'):
                no_email += 1
            valid_invoices.append(inv)

        # Stockage
        save_invoices(valid_invoices, local_db, db_type)
        logger.info(f"Factures importées: {len(valid_invoices)}")
        logger.info(f"Sans email: {no_email}")

        # Log
        total_amount = sum(inv['montant_ttc'] for inv in valid_invoices)
        logger.info(f"Montant total: {total_amount:.2f} €")
        logger.info("FIN: Succès")

        return {
            'total': len(invoices),
            'imported': len(valid_invoices),
            'duplicates': duplicates,
            'no_email': no_email,
            'amount': total_amount
        }

    except Exception as e:
        logger.error(f"ERREUR: {str(e)}", exc_info=True)
        raise

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default='reports/ST-fetch_unpaid_invoices.log')
    parser.add_argument('--db-type', default='pickledb')
    args = parser.parse_args()

    fetch_unpaid_invoices(log_file=args.log, db_type=args.db_type)