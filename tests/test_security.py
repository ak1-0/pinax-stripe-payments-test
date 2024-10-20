import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/api"

def test_sql_injection():
    payload = {
        "kind": "'; DROP TABLE events; --",  # Пример SQL-инъекции
        "stripe_id": "cus_test_sql_injection"
    }
    response = requests.post(f"{BASE_URL}/events/", json=payload)
    assert response.status_code != 200  # Ожидаем ошибку
