# Blueprint: auth/login.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_user, logout_user, login_required, current_user
import sqlite3
import datetime
import hashlib

bp = Blueprint('auth', __name__)

# Initialisation de la base de données
import pickledb

def get_db():
    db = sqlite3.connect('/app/marki.db')
    db.row_factory = sqlite3.Row
    return db

from pickledb import PickleDB

def get_logs_db():
    logs_db = PickleDB('/app/logs.db')
    return logs_db

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Gère la connexion des utilisateurs via un formulaire de connexion.
    """
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        redirect_url = request.args.get('redirect', '/app/dashboard')
        
        # Validation des champs
        if not id or not password:
            flash('Identifiant et mot de passe sont requis.', 'error')
            return redirect(url_for('auth.login'))
        
        # Vérification des informations de connexion
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (id,))
        user_data = cursor.fetchone()
        
        if user_data and user_data['isActive']:
            # Vérification du mot de passe
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user_data['password'] == hashed_password:
                # Création d'une session
                session['user_id'] = user_data['id']
                
                # Ajout d'un log dans PickleDB
                logs_db = get_logs_db()
                log_key = f"user_{user_data['id']}"
                log_entry = {
                    "action": "login",
                    "details": "User logged in successfully",
                    "created_at": datetime.datetime.now().isoformat()
                }
                if log_key not in logs_db.getall():
                    logs_db.set(log_key, [log_entry])
                else:
                    logs = logs_db.get(log_key)
                    logs.append(log_entry)
                    logs_db.set(log_key, logs)
                logs_db.dump()
                
                db.close()
                return redirect(redirect_url)
            else:
                flash('Identifiant ou mot de passe incorrect.', 'error')
        else:
            flash('Identifiant ou mot de passe incorrect.', 'error')
        
        db.close()
    
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    """
    Gère la déconnexion des utilisateurs.
    """
    # Suppression de la session
    session.pop('user_id', None)
    
    # Ajout d'un log dans PickleDB
    logs_db = get_logs_db()
    log_key = f"user_{current_user.id}"
    log_entry = {
        "action": "logout",
        "details": "User logged out successfully",
        "created_at": datetime.datetime.now().isoformat()
    }
    if log_key not in logs_db.getall():
        logs_db.set(log_key, [log_entry])
    else:
        logs = logs_db.get(log_key)
        logs.append(log_entry)
        logs_db.set(log_key, logs)
    logs_db.dump()
    
    return redirect(url_for('auth.login'))

@bp.route('/forgot-password')
def forgot_password():
    """
    Affiche un drawer informatif pour le mot de passe oublié.
    """
    return render_template('login.html', forgot_password=True)