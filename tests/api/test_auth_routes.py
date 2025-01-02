import pytest
import requests

from .config import DEMO_KING


def test_authenticate(client):
    """test anonymous access"""
    response = client.get("api/auth/")
    assert response.status_code == 401
    assert response.json == {"errors": {"message": "Unauthorized"}}


def test_signup_success(client):
    """test successful user signup"""
    client.get("api/auth/")
    signup_data = {
        "nick": "kingifer",
        "email": "kingeth@example.com",
        "password": "password",
    }

    response = client.post(
        "/api/auth/signup",
        json=signup_data,
    )

    assert response.status_code == 200
    data = response.json

    assert "king" in data
    king = list(data["king"].values())[0]

    assert king["nick"] == signup_data["nick"]
    assert king["email"] == signup_data["email"]
    assert "id" in king
