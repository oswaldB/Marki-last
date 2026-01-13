# tests/unit/sidebar/test_sidebar.py
import pytest
from app.blueprints.sidebar.routes import get_nav_links

def test_get_nav_links_success():
    result = get_nav_links({"user_id": 1})
    assert result["status"] == "success"
    assert isinstance(result["data"], list)

def test_get_nav_links_failure():
    with pytest.raises(ValueError):
        get_nav_links({"user_id": None})