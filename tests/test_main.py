from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "CI/CD Demo App is running!"}


def test_hello_endpoint_with_name():
    response = client.get("/hello", params={"name": "Anjan"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Anjan!"}


def test_hello_endpoint_default():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_version_endpoint():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
