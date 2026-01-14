#!/usr/bin/env python3
"""
Script Python pour lancer le serveur Flask avec des options de configuration.
Auteur: Mistral Vibe
Date: 2024
Version: 1.0
"""

import os
import sys
from app import create_app

def main():
    print("=" * 50)
    print("Lancement du serveur Flask (Mode DEBUG)")
    print("=" * 50)
    print()
    
    # Créer l'application Flask
    app = create_app()
    
    # Configuration du serveur
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = 'true'
    
    print(f"Configuration:")
    print(f"  Hôte: {host}")
    print(f"  Port: {port}")
    print(f"  Mode Debug: {'ACTIF' if debug else 'INACTIF'}")
    print()
    print(f"URL: http://{host}:{port}")
    print(f"Appuyez sur Ctrl+C pour arrêter le serveur.")
    print("=" * 50)
    print()
    
    # Lancer le serveur
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Serveur arrêté par l'utilisateur.")
        sys.exit(0)
    except Exception as e:
        print(f"Erreur lors du lancement du serveur: {e}")
        sys.exit(1)
