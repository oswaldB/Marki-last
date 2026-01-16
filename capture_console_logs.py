#!/usr/bin/env python3
"""
Script pour capturer les logs de la console web et les afficher.
"""
import subprocess
import sys
import re

def capture_console_logs():
    """Capture les logs de la console web et les affiche."""
    try:
        # Lancement des tests Playwright
        test_process = subprocess.Popen(
            ['npx', 'playwright', 'test', 'tests/ST-008_superadmin_page.spec.ts'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Lecture des logs de la console
        logs = []
        while True:
            line = test_process.stdout.readline()
            if line:
                logs.append(line.strip())
                print(line.strip())
            else:
                break
        
        # Lecture des erreurs
        errors = []
        while True:
            line = test_process.stderr.readline()
            if line:
                errors.append(line.strip())
                print(line.strip(), file=sys.stderr)
            else:
                break
        
        # Attente de la fin des tests
        test_process.wait()
        
        # Analyse des logs
        print("\n=== Analyse des logs ===")
        for log in logs:
            if "Console log:" in log:
                print(f"Log de la console: {log}")
            elif "Page error:" in log:
                print(f"Erreur de la page: {log}")
        
        # Analyse des erreurs
        print("\n=== Analyse des erreurs ===")
        for error in errors:
            if "Error:" in error:
                print(f"Erreur: {error}")
            elif "Failed:" in error:
                print(f"Échec: {error}")
    except Exception as e:
        print(f"✗ Erreur lors de la capture des logs: {e}")

if __name__ == '__main__':
    capture_console_logs()