from utils.client import get
import pytest

@pytest.mark.test
def test_access_without_token():
    response = get("/profile")

    assert response.status_code == 401