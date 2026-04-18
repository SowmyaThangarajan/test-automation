from utils.client import get
import pytest

#🚦 Rate Limiting
@pytest.mark.test

def test_rate_limiting():
    responses = []

    for _ in range(50):
        res = get("/login")
        responses.append(res.status_code)

    assert 429 in responses