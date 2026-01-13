import pytest
from bs4 import BeautifulSoup

def test_topbar_html_structure():
    """Test la structure HTML de la topbar."""
    with open('app/templates/partials/topbar.html', 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Test la présence des éléments principaux
    assert soup.find('header') is not None
    assert soup.find('button', class_='md:hidden') is not None  # Toggle mobile
    assert soup.find('div', class_='flex items-center gap-6') is not None  # Notifications & User Menu

    # Test les sections spécifiques
    assert soup.find('div', class_='relative') is not None  # Section notifications
    assert soup.find('div', class_='relative', recursive=False) is not None  # Section user menu

def test_topbar_alpine_components():
    """Test les composants Alpine.js de la topbar."""
    with open('app/templates/partials/topbar.html', 'r') as f:
        html = f.read()

    # Test le script Alpine.js
    assert 'topbarState()' in html
    assert 'showUserMenu' in html
    assert 'showNotifications' in html
    assert 'notifications' in html

    # Test les bindings Alpine.js
    assert '@click="showUserMenu = !showUserMenu"' in html
    assert '@click="showNotifications = !showNotifications"' in html
    assert 'x-show="notifications.length > 0"' in html
    assert 'x-text="user.username"' in html

def test_topbar_user_menu():
    """Test le menu utilisateur de la topbar."""
    with open('app/templates/partials/topbar.html', 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Test les éléments du menu utilisateur
    menu_items = soup.find_all('li')
    assert len(menu_items) >= 3  # Profil, Équipe, Déconnexion
    assert any('Mon Profil' in item.text for item in menu_items)
    assert any('Équipe' in item.text for item in menu_items)
    assert any('Déconnexion' in item.text for item in menu_items)

    # Test le formulaire de déconnexion
    logout_form = soup.find('form', action='/auth/logout')
    assert logout_form is not None
    assert logout_form.find('button', string='Déconnexion') is not None