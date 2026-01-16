# Blueprint: auth/login.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_user, logout_user, login_required, current_user
import sqlite3
import datetime
import hashlib

bp = Blueprint('auth', __name__)

# Initialisation de la base de données
def get_db():
    db = sqlite3.connect('marki.db')
    db.row_factory = sqlite3.Row
    return db

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
                
                # Ajout d'un log
                cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)",
                               (user_data['id'], 'login', 'User logged in successfully'))
                db.commit()
                
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
    
    # Ajout d'un log
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO logs (user_id, action, details) VALUES (?, ?, ?)",
                   (current_user.id, 'logout', 'User logged out successfully'))
    db.commit()
    db.close()
    
    return redirect(url_for('auth.login'))

@bp.route('/forgot-password')
def forgot_password():
    """
    Affiche un drawer informatif pour le mot de passe oublié.
    """
    return render_template('login.html', forgot_password=True)