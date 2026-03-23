import jwt
from utils.client import get
import pytest

@pytest.mark.test

def test_jwt_tampering():
    fake_token = jwt.encode({"user": "admin"}, "invalid-secret", algorithm="HS256")

    response = get("/admin", token=fake_token)

    assert response.status_code == 401