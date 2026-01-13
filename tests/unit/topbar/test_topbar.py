# tests/unit/topbar/test_topbar.py
import pytest
from app.blueprints.topbar.routes import get_user_info, get_notifications

def test_get_user_info_success():
    result = get_user_info({"user_id": 1})
    assert result["status"] == "success"
    assert "name" in result["data"]

def test_get_user_info_failure():
    with pytest.raises(ValueError):
        get_user_info({"user_id": None})

def test_get_notifications_success():
    result = get_notifications({"user_id": 1})
    assert result["status"] == "success"
    assert isinstance(result["data"], list)

def test_get_notifications_failure():
    with pytest.raises(ValueError):
        get_notifications({"user_id": None})