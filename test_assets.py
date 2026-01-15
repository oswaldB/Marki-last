#!/usr/bin/env python3
"""
Test simple pour vérifier que les assets sont accessibles
"""
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, '/home/oswald/Desktop/Marki-last')

from app import app

def test_static_files():
    """Tester l'accès aux fichiers statiques"""
    with app.test_client() as client:
        # Tester l'accès au logo
        response = client.get('/static/images/logo.png')
        print(f"Status code for /static/images/logo.png: {response.status_code}")
        print(f"Content-Type: {response.content_type}")
        print(f"Content-Length: {len(response.data)}")
        
        if response.status_code == 200:
            print("✅ SUCCESS: Logo is accessible!")
            return True
        else:
            print("❌ FAILURE: Logo is not accessible")
            return False

def test_template_rendering():
    """Tester le rendu des templates avec les assets"""
    with app.test_client() as client:
        # Tester la page superadmin entrance
        response = client.get('/superadmin/entrance')
        print(f"\nStatus code for /superadmin/entrance: {response.status_code}")
        
        if response.status_code == 200:
            html = response.data.decode('utf-8')
            # Vérifier que le chemin statique correct est présent (résultat de url_for)
            if '/static/images/logo.png' in html:
                print("✅ SUCCESS: Template renders correct static path!")
                return True
            else:
                print("❌ FAILURE: Template doesn't render correct static path")
                print("HTML snippet:", html[html.find('<img'):html.find('>', html.find('<img'))+1] if '<img' in html else "No img tag found")
                return False
        else:
            print("❌ FAILURE: Template not accessible")
            return False

if __name__ == '__main__':
    print("Testing Flask static files configuration...")
    print("=" * 50)
    
    success1 = test_static_files()
    success2 = test_template_rendering()
    
    print("\n" + "=" * 50)
    if success1 and success2:
        print("🎉 ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("💥 SOME TESTS FAILED!")
        sys.exit(1)