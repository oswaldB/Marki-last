# Initialisation de l'application Flask
from flask import Flask
from flask_login import LoginManager
import sqlite3

# Initialisation de la base de données SQLite
def init_db():
    import os
    db_path = os.path.join(os.path.dirname(__file__), 'marki.db')
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    
    # Création des tables si elles n'existent pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            isAdmin BOOLEAN DEFAULT FALSE,
            isActive BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    

    
    db.commit()
    db.close()

# Initialisation de l'application Flask
def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key-here'
    
    # Initialisation de la base de données
    init_db()
    
    # Initialisation de la base de données PickleDB pour les logs
    from app.logs_db import init_logs_db
    init_logs_db()
    
    # Configuration de Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Fonction pour charger l'utilisateur actuel
    @login_manager.user_loader
    def load_user(user_id):
        return None  # Retourne None pour l'instant, à implémenter plus tard
    
    # Importation des blueprints
    from app.blueprints.hello.routes import bp as hello_bp
    from app.blueprints.auth.routes import bp as auth_bp
    from app.blueprints.users.routes import bp as users_bp
    from app.blueprints.dashboard.routes import bp as dashboard_bp
    
    # Enregistrement des blueprints
    app.register_blueprint(hello_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(dashboard_bp)
    
    return app
