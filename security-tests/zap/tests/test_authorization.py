from utils.client import get
from config import VALID_USER_TOKEN
import pytest

#* Authorization bypass
@pytest.mark.test
def test_user_access_admin_endpoint():
    response = get("/admin", token=VALID_USER_TOKEN)

    assert response.status_code in [401, 403]