# tests/unit/app_layout/test_app_layout.py
import pytest
from app.blueprints.app.routes import get_layout

def test_get_layout_success():
    result = get_layout({"user_id": 1})
    assert result["status"] == "success"
    assert "sidebar" in result["data"]
    assert "topbar" in result["data"]

def test_get_layout_failure():
    with pytest.raises(ValueError):
        get_layout({"user_id": None})