from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from pickledb import PickleDB
import json

bp = Blueprint('auth', __name__)

db = PickleDB('admins.db')

# Helper function to get all admins
def get_all_admins():
    """Get all admins from database"""
    admins = []
    all_data = db.all()
    for key in all_data:
        if key.startswith('admin:'):
            admin_data = db.get(key)
            admin_id = key.split(':')[1]
            admins.append({**admin_data, 'id': int(admin_id)})
    return admins

# Helper function to validate admin data
def validate_admin_data(data):
    """Validate admin data"""
    errors = []
    if not data.get('username'):
        errors.append('username')
    if not data.get('password'):
        errors.append('password')
    if not data.get('name'):
        errors.append('name')
    return errors

@bp.route('/superadmin/entrance', methods=['GET', 'POST'])
def entrance():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'Citron6-Mustang9':
            session['authenticated'] = True
            return redirect(url_for('auth.superadmin'))
        else:
            return render_template('superadmin/entrance.html', error='Mot de passe incorrect')
    return render_template('superadmin/entrance.html')

@bp.route('/superadmin')
def superadmin():
    if not session.get('authenticated'):
        return redirect(url_for('auth.entrance'))
    admins = get_all_admins()
    return render_template('superadmin/superadmin.html', admins=admins)

# API Endpoints
@bp.route('/api/admins', methods=['GET'])
def api_get_admins():
    """Get all admins - API endpoint"""
    if not session.get('authenticated'):
        return jsonify({
            "success": False,
            "error": "Non autorisé",
            "message": "Veuillez vous authentifier"
        }), 401
    
    admins = get_all_admins()
    # Remove passwords from response
    admins_safe = [{k: v for k, v in admin.items() if k != 'password'} for admin in admins]
    
    return jsonify({
        "success": True,
        "admins": admins_safe
    })

@bp.route('/api/admins/<int:admin_id>', methods=['GET'])
def api_get_admin(admin_id):
    """Get single admin - API endpoint"""
    if not session.get('authenticated'):
        return jsonify({
            "success": False,
            "error": "Non autorisé",
            "message": "Veuillez vous authentifier"
        }), 401
    
    admin_data = db.get(f'admin:{admin_id}')
    if not admin_data:
        return jsonify({
            "success": False,
            "error": "Non trouvé",
            "message": "Admin non trouvé"
        }), 404
    
    # Remove password from response
    admin_safe = {k: v for k, v in admin_data.items() if k != 'password'}
    admin_safe['id'] = admin_id
    
    return jsonify({
        "success": True,
        "admin": admin_safe
    })

@bp.route('/api/admins', methods=['POST'])
def api_create_admin():
    """Create new admin - API endpoint"""
    if not session.get('authenticated'):
        return jsonify({
            "success": False,
            "error": "Non autorisé",
            "message": "Veuillez vous authentifier"
        }), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "error": "Requête invalide",
                "message": "Données JSON requises"
            }), 400
        
        # Validate data
        errors = validate_admin_data(data)
        if errors:
            return jsonify({
                "success": False,
                "error": "Champs manquants",
                "message": f"Les champs suivants sont requis: {', '.join(errors)}"
            }), 400
        
        # Check if username already exists
        all_data = db.all()
        for key in all_data:
            if key.startswith('admin:'):
                existing_admin = db.get(key)
                if existing_admin.get('username') == data.get('username'):
                    return jsonify({
                        "success": False,
                        "error": "Conflit",
                        "message": "Un admin avec ce username existe déjà"
                    }), 409
        
        # Get next ID
        admin_id = 1
        while db.get(f'admin:{admin_id}') is not None:
            admin_id += 1
        
        # Create admin
        admin_data = {
            'username': data.get('username'),
            'password': data.get('password'),
            'name': data.get('name'),
            'isAdmin': True
        }
        
        db.set(f'admin:{admin_id}', admin_data)
        
        # Return response (without password)
        admin_safe = {k: v for k, v in admin_data.items() if k != 'password'}
        admin_safe['id'] = admin_id
        
        return jsonify({
            "success": True,
            "admin": admin_safe,
            "message": "Admin créé avec succès"
        }), 201
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Erreur serveur",
            "message": str(e)
        }), 500

@bp.route('/api/admins/<int:admin_id>', methods=['PUT'])
def api_update_admin(admin_id):
    """Update admin - API endpoint"""
    if not session.get('authenticated'):
        return jsonify({
            "success": False,
            "error": "Non autorisé",
            "message": "Veuillez vous authentifier"
        }), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "error": "Requête invalide",
                "message": "Données JSON requises"
            }), 400
        
        # Check if admin exists
        if db.get(f'admin:{admin_id}') is None:
            return jsonify({
                "success": False,
                "error": "Non trouvé",
                "message": "Admin non trouvé"
            }), 404
        
        # Validate data
        errors = validate_admin_data(data)
        if errors:
            return jsonify({
                "success": False,
                "error": "Champs manquants",
                "message": f"Les champs suivants sont requis: {', '.join(errors)}"
            }), 400
        
        # Update admin
        admin_data = {
            'username': data.get('username'),
            'password': data.get('password'),
            'name': data.get('name'),
            'isAdmin': True
        }
        
        db.set(f'admin:{admin_id}', admin_data)
        
        # Return response (without password)
        admin_safe = {k: v for k, v in admin_data.items() if k != 'password'}
        admin_safe['id'] = admin_id
        
        return jsonify({
            "success": True,
            "admin": admin_safe,
            "message": "Admin mis à jour avec succès"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Erreur serveur",
            "message": str(e)
        }), 500

@bp.route('/api/admins/<int:admin_id>', methods=['DELETE'])
def api_delete_admin(admin_id):
    """Delete admin - API endpoint"""
    if not session.get('authenticated'):
        return jsonify({
            "success": False,
            "error": "Non autorisé",
            "message": "Veuillez vous authentifier"
        }), 401
    
    try:
        # Check if admin exists
        if db.get(f'admin:{admin_id}') is None:
            return jsonify({
                "success": False,
                "error": "Non trouvé",
                "message": "Admin non trouvé"
            }), 404
        
        # Delete admin
        db.remove(f'admin:{admin_id}')
        
        return jsonify({
            "success": True,
            "message": "Admin supprimé avec succès"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Erreur serveur",
            "message": str(e)
        }), 500

@bp.route('/superadmin/create', methods=['POST'])
def create_admin():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    admin_id = db.incr('admin_counter')
    db.set(f'admin:{admin_id}', {'username': username, 'password': password, 'name': name, 'isAdmin': True})
    return redirect(url_for('auth.superadmin'))

@bp.route('/superadmin/update/<int:admin_id>', methods=['POST'])
def update_admin(admin_id):
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    db.set(f'admin:{admin_id}', {'username': username, 'password': password, 'name': name, 'isAdmin': True})
    return redirect(url_for('auth.superadmin'))

@bp.route('/superadmin/delete/<int:admin_id>')
def delete_admin(admin_id):
    db.rem(f'admin:{admin_id}')
    return redirect(url_for('auth.superadmin'))