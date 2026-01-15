from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Enregistrer les blueprints
    from app.blueprints.hello.hello_world import bp as hello_bp
    app.register_blueprint(hello_bp)
    
    return app