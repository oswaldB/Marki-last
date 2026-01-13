# Script pour peupler le tableau des relances à partir de la séquence des campagnes
# Auteur: Oswald Bernard
# Date: 2024-10-15

import pickle
from datetime import datetime, timedelta
import logging

def load_db(db_path):
    """Charge la base de données PickleDB."""
    try:
        with open(db_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_db(db_path, data):
    """Sauvegarde les données dans la base de données PickleDB."""
    with open(db_path, 'wb') as f:
        pickle.dump(data, f)

def populate_relances(campagnes_db_path, relances_db_path, log_file):
    """
    Peupler le tableau des relances à partir de la séquence des campagnes.

    Args:
        campagnes_db_path (str): Chemin vers la base de données des campagnes.
        relances_db_path (str): Chemin vers la base de données des relances.
        log_file (str): Chemin vers le fichier de log.

    Raises:
        ValueError: Si les données sont invalides.
        IOError: Si les fichiers sont illisibles.
    """
    # Configuration du logging
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Charger les bases de données
        campagnes_db = load_db(campagnes_db_path)
        relances_db = load_db(relances_db_path)

        if 'campagnes' not in campagnes_db or 'relances' not in relances_db:
            raise ValueError("Structure de base de données invalide")

        campagnes = campagnes_db['campagnes']
        relances = relances_db['relances']

        # Pour chaque campagne active, générer les relances
        for campagne in campagnes:
            if campagne['statut'] == 'active':
                sequence = campagne['sequence']
                criteres = campagne['criteres']

                # Trouver les factures correspondant aux critères
                factures = [r for r in relances if all(r[k] == v for k, v in criteres.items())]

                # Générer les relances pour chaque facture
                for facture in factures:
                    for i, email in enumerate(sequence):
                        relance_date = datetime.now() + timedelta(days=i)
                        relance_id = f"{facture['id']}_{i}"

                        # Vérifier si la relance existe déjà
                        if relance_id not in [r['id'] for r in facture.get('relances', [])]:
                            new_relance = {
                                'id': relance_id,
                                'facture_id': facture['id'],
                                'campagne_id': campagne['id'],
                                'date_envoi': relance_date.strftime('%Y-%m-%d'),
                                'contenu': email['contenu'],
                                'statut': 'en_attente'
                            }

                            if 'relances' not in facture:
                                facture['relances'] = []
                            facture['relances'].append(new_relance)

                            logging.info(f"Relance ajoutée pour la facture {facture['id']} (campagne {campagne['id']})")

        # Sauvegarder les modifications
        save_db(relances_db_path, relances_db)
        logging.info("Population des relances terminée avec succès")

    except Exception as e:
        logging.error(f"Erreur lors de la population des relances: {str(e)}")
        raise

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Peupler le tableau des relances à partir de la séquence des campagnes.')
    parser.add_argument('--campagnes-db', required=True, help='Chemin vers la base de données des campagnes')
    parser.add_argument('--relances-db', required=True, help='Chemin vers la base de données des relances')
    parser.add_argument('--log', required=True, help='Chemin vers le fichier de log')

    args = parser.parse_args()

    populate_relances(args.campagnes_db, args.relances_db, args.log)
