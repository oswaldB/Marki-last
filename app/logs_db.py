# Initialisation de la base de données PickleDB pour les logs
from pickledb import PickleDB
import os

def init_logs_db():
    """
    Initialise la base de données PickleDB pour les logs.
    """
    logs_db_path = os.path.join(os.path.dirname(__file__), 'logs.db')
    logs_db = PickleDB(logs_db_path)
    return logs_db

if __name__ == '__main__':
    init_logs_db()
    print("Base de données PickleDB pour les logs initialisée avec succès.")
