#!/usr/bin/env python3
"""
Script pour démarrer le serveur Flask et capturer ses logs.
"""
import subprocess
import sys
import time

def start_server():
    """Démarre le serveur Flask et capture ses logs."""
    # Démarrage du serveur Flask
    server_process = subprocess.Popen(
        [sys.executable, 'app.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Attente pour permettre au serveur de démarrer
    time.sleep(3)
    
    return server_process

if __name__ == '__main__':
    server_process = start_server()
    
    try:
        # Lecture des logs du serveur
        while True:
            line = server_process.stdout.readline()
            if line:
                print(line.strip())
            else:
                break
    except KeyboardInterrupt:
        # Arrêt du serveur lors de l'interruption
        server_process.terminate()
        server_process.wait()
        print("Serveur arrêté.")