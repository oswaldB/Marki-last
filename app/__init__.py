from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from .blueprints.hello import hello_bp
    from .blueprints.auth import auth_bp
    app.register_blueprint(hello_bp)
    app.register_blueprint(auth_bp)
    
    return app