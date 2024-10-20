import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/api"

@pytest.fixture
def create_event():
    # Создание тестового события
    response = requests.post(f"{BASE_URL}/events/", json={
        "kind": "customer.created",
        "stripe_id": "cus_test123"
    })
    return response.json()

def test_create_event(create_event):
    assert create_event["kind"] == "customer.created"
    assert create_event["stripe_id"] == "cus_test123"
    assert "id" in create_event  # Убедиться, что ID созданного события присутствует

def test_get_events():
    response = requests.get(f"{BASE_URL}/events/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Убедиться, что ответ - это список
