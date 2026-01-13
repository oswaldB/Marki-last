from flask import Flask, render_template, request
from app.blueprints.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Enregistrement du blueprint d'authentification
    app.register_blueprint(auth_bp)

    return app
