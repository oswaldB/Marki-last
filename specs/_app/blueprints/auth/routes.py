from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer

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