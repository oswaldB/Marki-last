import pytest
from flask import url_for
from app.blueprints.app.routes import bp as app_bp

@pytest.fixture
def client(app):
    app.register_blueprint(app_bp)
    with app.test_client() as client:
        yield client

def test_index_redirect(client):
    """Test que la route racine redirige vers le dashboard."""
    response = client.get(url_for('app.index'))
    assert response.status_code == 302
    assert response.location == url_for('app.dashboard', _external=True)

def test_dashboard_render(client):
    """Test le rendu de la page dashboard."""
    response = client.get(url_for('app.dashboard'))
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_user_info_api(client):
    """Test l'API des infos utilisateur."""
    response = client.get(url_for('app.user_info'))
    assert response.status_code == 200
    data = response.get_json()
    assert 'user' in data
    assert all(key in data['user'] for key in ['username', 'email', 'isAdmin'])