from utils.client import get
import pytest

@pytest.mark.test

def test_xss_attack():
    payload = "<script>alert('xss')</script>"
    response = get("/search", params={"q": payload})

    assert payload not in response.text