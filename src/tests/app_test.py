"""Module app_test"""
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)


def test_read_main():
    """Function test app"""
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"app_name": "Vil", "admin_email": "admin@vil.com"}
