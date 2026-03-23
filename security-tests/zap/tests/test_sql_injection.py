from utils.client import get
import pytest

@pytest.mark.test

def test_sql_injection_login():
    payload = "' OR '1'='1"
    response = get("/users", params={"username": payload})

    assert response.status_code in [400, 401, 403]
    assert "error" in response.text.lower()