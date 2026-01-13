import logging
from datetime import datetime
from pickledb import PickleDB

def setup_logger(log_file):
    """Configure le logger."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger()

def load_campagnes(campagnes_db_path):
    """Charge les campagnes depuis la base de données."""
    campagnes_db = PickleDB(campagnes_db_path, auto_dump=False)
    campagnes = campagnes_db.get('campagnes') or []
    campagnes_db.dump()
    return campagnes

def load_relances(relances_db_path):
    """Charge les relances depuis la base de données."""
    relances_db = PickleDB(relances_db_path, auto_dump=False)
    relances = relances_db.get('relances') or []
    relances_db.dump()
    return relances

def save_relances(relances, relances_db_path):
    """Sauvegarde les relances dans la base de données."""
    relances_db = PickleDB(relances_db_path, auto_dump=True)
    relances_db.set('relances', relances)

def populate_relances(campagnes_db_path, relances_db_path, log_file):
    """Peuple le tableau des relances à partir de la séquence des campagnes."""
    logger = setup_logger(log_file)
    logger.info("DÉBUT: Population des relances")

    try:
        # Chargement des données
        campagnes = load_campagnes(campagnes_db_path)
        relances = load_relances(relances_db_path)

        # Génération des relances
        new_relances = []

        for campagne in campagnes:
            if campagne['statut'] != 'active':
                continue

            for facture in campagne['factures']:
                if facture['statut_relance'] == 'non_relancee':
                    relance = {
                        'id': len(relances) + len(new_relances) + 1,
                        'campaign_id': campagne['id'],
                        'numero_facture': facture['nfacture'],
                        'montant': facture['montant_ttc'],
                        'reste_a_payer': facture['montant_ttc'],
                        'date_echeance': facture['date_echeance'],
                        'proprietaire_prenom': facture['client_name'].split()[0],
                        'proprietaire_nom': ' '.join(facture['client_name'].split()[1:]),
                        'proprietaire_email': facture['client_email'],
                        'payeur': 'proprietaire',
                        'recipient': facture['client_email'],
                        'statut': 'pending',
                        'content': f"Bonjour {facture['client_name']},\n\nVotre facture {facture['nfacture']}...",
                        'date': datetime.now().isoformat(),
                        'open_date': None,
                        'error_message': None
                    }
                    new_relances.append(relance)
                    logger.info(f"Relance ajoutée pour la facture {facture['nfacture']} (campagne {campagne['id']})")

        # Sauvegarde des nouvelles relances
        relances.extend(new_relances)
        save_relances(relances, relances_db_path)

        logger.info(f"Population des relances terminée avec succès. {len(new_relances)} relances ajoutées.")
        return len(new_relances)

    except Exception as e:
        logger.error(f"ERREUR: {str(e)}", exc_info=True)
        raise

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--campagnes-db', required=True)
    parser.add_argument('--relances-db', required=True)
    parser.add_argument('--log', default='reports/relances_population.log')
    args = parser.parse_args()

    populate_relances(
        campagnes_db_path=args.campagnes_db,
        relances_db_path=args.relances_db,
        log_file=args.log
    )