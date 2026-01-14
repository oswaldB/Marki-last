import pytest
from flask import url_for
from app.models import User
from app import db, create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
    
    yield app
    
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_superadmin_route_get(client):
    """Test la route GET /superadmin."""
    response = client.get('/superadmin')
    assert response.status_code == 200
    assert b'Creer le Premier Administrateur' in response.data
    assert b'Marki - Gestion des Commissions' in response.data


def test_superadmin_route_post_invalid_password(client):
    """Test la route POST /superadmin avec un mot de passe superadmin incorrect."""
    response = client.post('/superadmin', data={
        'superadmin_password': 'MauvaisMotDePasse',
        'username': 'admin',
        'password': 'MonMotDePasse123!',
        'confirm_password': 'MonMotDePasse123!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Mot de passe superadmin incorrect.' in response.data


def test_superadmin_route_post_password_mismatch(client):
    """Test la route POST /superadmin avec des mots de passe non correspondants."""
    response = client.post('/superadmin', data={
        'superadmin_password': 'Citron6-Mustang9',
        'username': 'admin',
        'password': 'MotDePasse1',
        'confirm_password': 'MotDePasse2'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Les mots de passe ne correspondent pas.' in response.data


def test_superadmin_route_post_success(client):
    """Test la route POST /superadmin avec succès."""
    # Supprimer tous les utilisateurs pour simuler une base vide
    with client.application.app_context():
        db.session.query(User).delete()
        db.session.commit()

    response = client.post('/superadmin', data={
        'superadmin_password': 'Citron6-Mustang9',
        'username': 'admin',
        'password': 'MonMotDePasse123!',
        'confirm_password': 'MonMotDePasse123!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

    # Vérifier que l'utilisateur a été créé
    with client.application.app_context():
        user = User.query.filter_by(username='admin').first()
        assert user is not None
        assert user.is_admin is True


def test_superadmin_route_post_admin_exists(client):
    """Test la route POST /superadmin quand un administrateur existe déjà."""
    # Créer un administrateur existant
    with client.application.app_context():
        existing_admin = User(
            username='existing_admin',
            email='existing_admin@example.com',
            password_hash='hashed_password',
            is_admin=True,
            is_active=True
        )
        db.session.add(existing_admin)
        db.session.commit()

    response = client.post('/superadmin', data={
        'superadmin_password': 'Citron6-Mustang9',
        'username': 'new_admin',
        'password': 'MonMotDePasse123!',
        'confirm_password': 'MonMotDePasse123!'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Un administrateur existe deja.' in response.data