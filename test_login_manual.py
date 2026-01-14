#!/usr/bin/env python3
"""
Script pour tester manuellement la fonctionnalité de login
"""

import requests
import sys

def test_login():
    base_url = "http://localhost:5000"
    
    # Test 1: Connexion avec des identifiants invalides
    print("Test 1: Connexion avec des identifiants invalides")
    login_data = {
        'email': 'invalid@example.com',
        'password': 'wrongpassword'
    }
    
    try:
        response = requests.post(f"{base_url}/login", data=login_data, allow_redirects=False)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ La page de login est affichée (comportement attendu)")
        else:
            print(f"❌ Comportement inattendu: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur lors du test 1: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Connexion avec des identifiants valides
    print("Test 2: Connexion avec des identifiants valides")
    login_data = {
        'email': 'admin@example.com',
        'password': 'adminpassword'
    }
    
    try:
        # Créer une session pour gérer les cookies
        session = requests.Session()
        response = session.post(f"{base_url}/login", data=login_data, allow_redirects=False)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        
        if response.status_code == 302:
            location = response.headers.get('Location', '')
            print(f"Redirection vers: {location}")
            
            if '/dashboard' in location:
                print("✅ Redirection vers le dashboard (comportement attendu)")
            elif '/logout' in location:
                print("❌ Redirection vers logout (problème identifié)")
            else:
                print(f"❌ Redirection inattendue vers: {location}")
        else:
            print(f"❌ Pas de redirection: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erreur lors du test 2: {e}")

if __name__ == "__main__":
    test_login()