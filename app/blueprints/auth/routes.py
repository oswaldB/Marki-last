from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('app.dashboard'))
        else:
            flash('Email ou mot de passe incorrect', 'error')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/superadmin', methods=['GET', 'POST'])
def superadmin():
    if request.method == 'POST':
        # Vérifier le mot de passe superadmin
        if request.form['superadmin_password'] != 'Citron6-Mustang9':
            flash('Mot de passe superadmin incorrect.', 'error')
            return redirect(url_for('auth.superadmin'))

        # Vérifier si un administrateur existe déjà
        if User.query.filter_by(is_admin=True).first():
            flash('Un administrateur existe deja.', 'error')
            return redirect(url_for('auth.login'))

        # Créer le premier administrateur
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Valider les champs
        if not username:
            flash('Le nom d utilisateur est requis.', 'error')
            return redirect(url_for('auth.superadmin'))
        if not password:
            flash('Le mot de passe est requis.', 'error')
            return redirect(url_for('auth.superadmin'))
        if password != confirm_password:
            flash('Les mots de passe ne correspondent pas.', 'error')
            return redirect(url_for('auth.superadmin'))

        # Créer l'utilisateur
        new_user = User(
            username=username,
            email=f'{username}@example.com',
            password_hash=generate_password_hash(password),
            is_admin=True,
            is_active=True
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Administrateur cree avec succes.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/superadmin.html')