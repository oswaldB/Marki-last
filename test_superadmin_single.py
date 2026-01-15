#!/usr/bin/env python3
"""
Test pour la version single-screen du superadmin avec authentification frontend
"""
import sys
import os

# Ajouter le chemin du projet
sys.path.insert(0, '/home/oswald/Desktop/Marki-last')

from app import app

def test_single_screen_rendering():
    """Tester le rendu du template single screen"""
    print("Testing Superadmin Single Screen...")
    print("=" * 60)
    
    with app.test_client() as client:
        # Test 1: Accès à la page superadmin (devrait fonctionner sans authentification)
        print("\n1. Testing GET /superadmin (no authentication required)")
        response = client.get('/superadmin')
        html = response.data.decode('utf-8')
        print(f"   Status: {response.status_code}")
        print(f"   Template contains auth form: {'Accès Superadmin' in html}")
        print(f"   Template contains admin interface: {'Gestion des Admins' in html}")
        print(f"   Template contains Alpine.js: {'x-data' in html}")
        print(f"   Template contains frontend auth: {'SUPERADMIN_PASSWORD' in html}")
        
        assert response.status_code == 200
        assert 'Accès Superadmin' in html
        assert 'Gestion des Admins' in html
        assert 'x-data="superadminSingleScreen()"' in html
        assert 'SUPERADMIN_PASSWORD' in html
        assert 'Citron6-Mustang9' in html
        
        print("   ✅ Single screen template renders correctly")
        
        # Test 2: Vérifier que l'API est toujours accessible
        print("\n2. Testing API still works (no authentication)")
        response = client.get('/api/admins')
        data = response.get_json()
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        
        # Should return 401 because no session
        assert response.status_code == 401
        assert data['success'] == False
        assert data['error'] == 'Non autorisé'
        
        print("   ✅ API authentication still required")
        
        print("\n✅ All single screen tests passed!")
        return True

def test_frontend_authentication_logic():
    """Tester la logique d'authentification frontend"""
    print("\n" + "=" * 60)
    print("Testing Frontend Authentication Logic...")
    print("=" * 60)
    
    with app.test_client() as client:
        # Test 1: Vérifier que le mot de passe est dans le code
        print("\n1. Checking password in source code")
        response = client.get('/superadmin')
        html = response.data.decode('utf-8')
        
        # Vérifier que le mot de passe est bien présent
        assert 'Citron6-Mustang9' in html
        assert 'SUPERADMIN_PASSWORD' in html
        
        print("   ✅ Password found in source code (development only)")
        
        # Test 2: Vérifier les fonctions Alpine.js
        print("\n2. Checking Alpine.js functions")
        assert 'authenticate()' in html
        assert 'logout()' in html
        assert 'checkAuth()' in html
        assert 'localStorage.setItem' in html
        assert 'localStorage.getItem' in html
        
        print("   ✅ All authentication functions present")
        
        print("\n✅ Frontend authentication logic verified!")
        return True

def test_api_with_session():
    """Tester que l'API fonctionne toujours avec une session"""
    print("\n" + "=" * 60)
    print("Testing API with Session...")
    print("=" * 60)
    
    with app.test_client() as client:
        # Simuler une session authentifiée
        with client.session_transaction() as sess:
            sess['authenticated'] = True
        
        # Test 1: Créer un admin
        print("\n1. Creating admin with authenticated session")
        import json
        response = client.post('/api/admins',
                              data=json.dumps({'username': 'test', 'password': 'test', 'name': 'Test'}),
                              content_type='application/json')
        data = response.get_json()
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        
        assert response.status_code == 201
        assert data['success'] == True
        
        print("   ✅ Admin created successfully")
        
        # Test 2: Lister les admins
        print("\n2. Listing admins")
        response = client.get('/api/admins')
        data = response.get_json()
        print(f"   Status: {response.status_code}")
        print(f"   Admins count: {len(data.get('admins', []))}")
        
        assert response.status_code == 200
        assert len(data['admins']) == 1
        
        print("   ✅ Admins listed successfully")
        
        print("\n✅ API with session works correctly!")
        return True

if __name__ == '__main__':
    print("🚀 Starting Superadmin Single Screen Tests")
    print("=" * 60)
    
    try:
        success1 = test_single_screen_rendering()
        success2 = test_frontend_authentication_logic()
        success3 = test_api_with_session()
        
        print("\n" + "=" * 60)
        print("🎉 ALL SINGLE SCREEN TESTS PASSED!")
        print("=" * 60)
        print("\n✅ Single screen rendering: Working")
        print("✅ Frontend authentication: Working")
        print("✅ API with session: Working")
        print("\n📝 Important: This is for DEVELOPMENT ONLY")
        print("   - Password is visible in source code")
        print("   - No real security")
        print("   - Use only for development/demos")
        
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)