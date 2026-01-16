# Blueprint: users.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
import sqlite3
import datetime
import hashlib

bp = Blueprint('users', __name__)

# Initialisation de la base de données
def get_db():
    db = sqlite3.connect('marki.db')
    db.row_factory = sqlite3.Row
    return db

@bp.route('/api/users', methods=['GET'])
def get_users():
    """
    Récupère la liste des utilisateurs depuis la base de données.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()
    
    return jsonify({'users': [dict(user) for user in users]})

@bp.route('/api/users', methods=['POST'])
def create_user():
    """
    Crée un nouvel utilisateur dans la base de données.
    """
    data = request.json
    id = data.get('id')
    password = data.get('password')
    isAdmin = data.get('isAdmin', False)
    
    # Validation des champs
    if not id or not password:
        return jsonify({'status': 'error', 'message': 'Identifiant et mot de passe sont requis.'}), 400
    
    # Hachage du mot de passe
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Insertion de l'utilisateur
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, isAdmin, isActive) VALUES (?, ?, ?, ?)",
                       (id, hashed_password, isAdmin, True))
        db.commit()
        
        db.close()
        return jsonify({'status': 'success', 'message': 'Utilisateur créé avec succès.'})
    except sqlite3.IntegrityError:
        db.close()
        return jsonify({'status': 'error', 'message': 'Identifiant déjà utilisé.'}), 400

@bp.route('/api/users/<user_id>/activate', methods=['POST'])
def activate_user(user_id):
    """
    Active un utilisateur dans la base de données.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET isActive = TRUE WHERE id = ?", (user_id,))
    db.commit()
    
    db.close()
    return jsonify({'status': 'success', 'message': 'Utilisateur activé avec succès.'})

@bp.route('/api/users/<user_id>/modify', methods=['POST'])
@login_required
def modify_user_password(user_id):
    """
    Modifie le mot de passe d'un utilisateur dans la base de données.
    """
    data = request.json
    password = data.get('password')
    
    # Validation des champs
    if not password:
        return jsonify({'status': 'error', 'message': 'Mot de passe est requis.'}), 400
    
    # Hachage du mot de passe
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Mise à jour du mot de passe
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user_id))
    db.commit()
    
    # Ajout d'un log
    cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)",
                   (current_user.id, 'modify_user_password', f'User {user_id} password modified successfully'))
    db.commit()
    
    db.close()
    return jsonify({'status': 'success', 'message': 'Mot de passe modifié avec succès.'})

@bp.route('/superadmin')
def superadmin():
    """
    Affiche la page SuperAdmin pour la gestion des utilisateurs.
    """
    return render_template('superadmin.html')