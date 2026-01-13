import pytest
from bs4 import BeautifulSoup

def test_sidebar_html_structure():
    """Test la structure HTML de la sidebar."""
    with open('app/templates/partials/sidebar.html', 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Test la présence des éléments principaux
    assert soup.find('div', class_='sidebar-container') is not None
    assert soup.find('aside') is not None
    assert soup.find('nav') is not None
    assert soup.find('div', class_='absolute bottom-0') is not None

    # Test les liens de navigation
    nav_links = soup.find_all('a')
    assert len(nav_links) >= 4  # Dashboard, Commissions, Relances, Équipe
    assert any('Dashboard' in link.text for link in nav_links)
    assert any('Commissions' in link.text for link in nav_links)
    assert any('Relances' in link.text for link in nav_links)

def test_sidebar_responsive_behavior():
    """Test le comportement responsive de la sidebar."""
    with open('app/templates/partials/sidebar.html', 'r') as f:
        html = f.read()

    # Test la classe de toggle mobile
    assert 'md:hidden' in html
    assert 'fixed top-4 left-4' in html

    # Test le script Alpine.js
    assert 'sidebarState()' in html
    assert 'toggleOpen()' in html
    assert 'isOpen' in html
    assert 'isLarge' in html