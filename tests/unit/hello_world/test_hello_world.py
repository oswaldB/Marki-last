import pytest
from flask import Flask, template_rendered
from app import create_app
from app.blueprints.app.routes import app_bp

@pytest.fixture
def app():
    app = create_app()
    app.register_blueprint(app_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_route(client):
    """Test that the hello route returns a successful response."""
    response = client.get('/hello')
    assert response.status_code == 200

def test_hello_content(client):
    """Test that the hello page contains the expected content."""
    response = client.get('/hello')
    assert b'Hello, World!' in response.data
    assert b'<img src="/public/logo.png"' in response.data
    assert b'class="logo"' in response.data
    assert b'class="message"' in response.data

def test_hello_styles(client):
    """Test that the hello page contains the expected styles."""
    response = client.get('/hello')
    assert b'max-width: 200px' in response.data
    assert b'margin-bottom: 20px' in response.data
    assert b'font-size: 24px' in response.data
    assert b'text-align: center' in response.data

def test_hello_title(client):
    """Test that the hello page has the correct title."""
    response = client.get('/hello')
    assert b'<title>Hello World - Marki</title>' in response.data

def test_hello_font_family(client):
    """Test that the hello page uses the correct font family."""
    response = client.get('/hello')
    assert b'font-family: \'Inter\', sans-serif' in response.data

def test_hello_body_styles(client):
    """Test that the hello page has the correct body styles."""
    response = client.get('/hello')
    assert b'margin-top: 50px' in response.data
    assert b'color: #333333' in response.data

def test_hello_message_color(client):
    """Test that the hello page has the correct message color."""
    response = client.get('/hello')
    assert b'color: #333333' in response.data
