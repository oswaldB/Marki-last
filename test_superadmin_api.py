#!/usr/bin/env python3
"""
Test complet pour l'API Superadmin et l'interface Alpine.js
"""
import sys
import os
import json

# Ajouter le chemin du projet
sys.path.insert(0, '/home/oswald/Desktop/Marki-last')

from app import app

def test_api_endpoints():
    """Tester tous les endpoints API"""
    print("Testing Superadmin API Endpoints...")
    print("=" * 60)
    
    with app.test_client() as client:
        # Simuler l'authentification
        with client.session_transaction() as sess:
            sess['authenticated'] = True
        
        # Test 1: GET /api/admins (liste vide initialement)
        print("\n1. Testing GET /api/admins")
        response = client.get('/api/admins')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Admins count: {len(data.get('admins', []))}")
        assert response.status_code == 200
        assert data['success'] == True
        
        # Test 2: POST /api/admins (créer un admin)
        print("\n2. Testing POST /api/admins")
        new_admin = {
            'username': 'test_admin',
            'password': 'test_password',
            'name': 'Test Admin'
        }
        response = client.post('/api/admins', 
                              data=json.dumps(new_admin),
                              content_type='application/json')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Admin ID: {data.get('admin', {}).get('id')}")
        assert response.status_code == 201
        assert data['success'] == True
        assert data['admin']['username'] == 'test_admin'
        admin_id = data['admin']['id']
        
        # Test 3: GET /api/admins (vérifier que l'admin a été ajouté)
        print("\n3. Testing GET /api/admins (after creation)")
        response = client.get('/api/admins')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Admins count: {len(data.get('admins', []))}")
        assert response.status_code == 200
        assert len(data['admins']) == 1
        
        # Test 4: GET /api/admins/<id> (récupérer un admin spécifique)
        print(f"\n4. Testing GET /api/admins/{admin_id}")
        response = client.get(f'/api/admins/{admin_id}')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Admin username: {data.get('admin', {}).get('username')}")
        assert response.status_code == 200
        assert data['admin']['username'] == 'test_admin'
        
        # Test 5: PUT /api/admins/<id> (mettre à jour un admin)
        print(f"\n5. Testing PUT /api/admins/{admin_id}")
        updated_admin = {
            'username': 'updated_admin',
            'password': 'new_password',
            'name': 'Updated Admin'
        }
        response = client.put(f'/api/admins/{admin_id}',
                             data=json.dumps(updated_admin),
                             content_type='application/json')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Updated username: {data.get('admin', {}).get('username')}")
        assert response.status_code == 200
        assert data['admin']['username'] == 'updated_admin'
        
        # Test 6: DELETE /api/admins/<id> (supprimer un admin)
        print(f"\n6. Testing DELETE /api/admins/{admin_id}")
        response = client.delete(f'/api/admins/{admin_id}')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        assert response.status_code == 200
        assert data['success'] == True
        
        # Test 7: GET /api/admins (vérifier que l'admin a été supprimé)
        print("\n7. Testing GET /api/admins (after deletion)")
        response = client.get('/api/admins')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Admins count: {len(data.get('admins', []))}")
        assert response.status_code == 200
        assert len(data['admins']) == 0
        
        # Test 8: Erreur 404 (admin non trouvé)
        print("\n8. Testing GET /api/admins/999 (not found)")
        response = client.get('/api/admins/999')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Error: {data.get('error')}")
        assert response.status_code == 404
        assert data['success'] == False
        
        # Test 9: Erreur 400 (données invalides)
        print("\n9. Testing POST /api/admins (invalid data)")
        response = client.post('/api/admins',
                              data=json.dumps({}),
                              content_type='application/json')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Error: {data.get('error')}")
        assert response.status_code == 400
        assert data['success'] == False
        
        print("\n✅ All API tests passed!")
        return True

def test_template_rendering():
    """Tester le rendu du template"""
    print("\n" + "=" * 60)
    print("Testing Template Rendering...")
    print("=" * 60)
    
    with app.test_client() as client:
        # Simuler l'authentification
        with client.session_transaction() as sess:
            sess['authenticated'] = True
        
        # Test 1: Accès à la page superadmin
        print("\n1. Testing GET /superadmin")
        response = client.get('/superadmin')
        html = response.data.decode('utf-8')
        print(f"   Status: {response.status_code}")
        print(f"   Template contains Alpine.js: {'x-data' in html}")
        print(f"   Template contains fetch API: {'fetch' in html}")
        print(f"   Template contains admin table: {'Liste des Admins' in html}")
        assert response.status_code == 200
        assert 'x-data="superadminApp()"' in html
        assert 'fetch' in html
        assert 'Liste des Admins' in html
        
        # Test 2: Vérifier les fonctionnalités Alpine.js
        print("\n2. Testing Alpine.js functionality in template")
        assert 'loadAdmins' in html
        assert 'createAdmin' in html
        assert 'updateAdmin' in html
        assert 'deleteAdmin' in html
        assert 'prepareEdit' in html
        print("   ✅ All Alpine.js functions present")
        
        # Test 3: Vérifier les boutons d'action
        print("\n3. Testing action buttons")
        assert 'Nouveau Admin' in html
        assert 'Modifier' in html
        assert 'Supprimer' in html
        assert 'Créer' in html
        assert 'Mettre à jour' in html
        print("   ✅ All action buttons present")
        
        print("\n✅ All template tests passed!")
        return True

def test_authentication():
    """Tester l'authentification"""
    print("\n" + "=" * 60)
    print("Testing Authentication...")
    print("=" * 60)
    
    with app.test_client() as client:
        # Test 1: Accès non authentifié
        print("\n1. Testing unauthenticated access to API")
        response = client.get('/api/admins')
        data = json.loads(response.data)
        print(f"   Status: {response.status_code}")
        print(f"   Success: {data.get('success')}")
        print(f"   Error: {data.get('error')}")
        assert response.status_code == 401
        assert data['success'] == False
        assert data['error'] == 'Non autorisé'
        
        # Test 2: Accès non authentifié à la page
        print("\n2. Testing unauthenticated access to page")
        response = client.get('/superadmin')
        print(f"   Status: {response.status_code}")
        print(f"   Redirect: {response.status_code in [301, 302, 303, 307, 308]}")
        # Should redirect to entrance
        assert response.status_code in [301, 302, 303, 307, 308]
        
        print("\n✅ All authentication tests passed!")
        return True

if __name__ == '__main__':
    print("🚀 Starting Superadmin API and Template Tests")
    print("=" * 60)
    
    try:
        success1 = test_api_endpoints()
        success2 = test_template_rendering()
        success3 = test_authentication()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        print("=" * 60)
        print("\n✅ API Endpoints: Working")
        print("✅ Template Rendering: Working")
        print("✅ Authentication: Working")
        print("✅ Alpine.js Integration: Working")
        print("✅ CRUD Operations: Working")
        
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)