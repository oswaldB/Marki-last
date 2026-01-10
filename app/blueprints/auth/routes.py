from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import check_password_hash
from app.blueprints.auth.services.database import get_user_by_username, update_password

auth_bp = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_data = get_user_by_username(username)
        if user_data and check_password_hash(user_data[3], password):
            login_user(User(*user_data))
            flash('Utilisateur connecté avec succès')
            return redirect(url_for('main.index'))
        flash('Identifiant ou mot de passe incorrect.')
    return render_template('login.html')

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form.get('email')
        # Générer un token et envoyer un email
        flash('Lien de réinitialisation envoyé.')
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html')

@auth_bp.route('/set_new_password/<token>', methods=['GET', 'POST'])
def set_new_password(token):
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        if new_password == confirm_password:
            # Mettre à jour le mot de passe dans la base de données
            update_password(email, new_password)
            flash('Mot de passe réinitialisé avec succès.')
            return redirect(url_for('auth.login'))
        flash('Les mots de passe ne correspondent pas.')
    return render_template('set_new_password.html', token=token)