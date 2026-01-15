from flask import Flask

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')

# Configuration de la clé secrète pour les sessions
app.secret_key = 'votre_cle_secrete_ici_changer_en_production_12345'

# Configuration des assets statiques
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600  # Cache 1 heure pour les assets

from app.blueprints.app.routes import bp as app_bp
from app.blueprints.auth.routes import bp as auth_bp

app.register_blueprint(app_bp)
app.register_blueprint(auth_bp)