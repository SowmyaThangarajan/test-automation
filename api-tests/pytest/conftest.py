import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def client():
    client = APIClient("https://api.demo.com")
    client.login("test", "test123")
    return client