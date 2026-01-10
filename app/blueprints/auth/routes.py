from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/login')
def login():
    return "Page de connexion - à implémenter"

@auth_bp.route('/auth/register')
def register():
    return "Page d'inscription - à implémenter"