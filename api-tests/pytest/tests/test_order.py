import time
import pytest

from utils.schema_validator import validate_schema

# Validate performance threshold
def test_create_order(client):
    start = time.time()

    response = client.post("/order/create", {
        "product_id": 1,
        "quantity": 2
    })

    duration = time.time() - start

    assert response.status_code == 201
    assert duration < 2

    validate_schema(response.json(), "schemas/order_schema.json")

# ❌ Missing required field
def test_create_order_missing_quantity(client):
    response = client.post("/order/create", {
        "product_id": 1
    })

    assert response.status_code == 400
    assert "quantity" in response.text.lower()


# ❌ Invalid data type
def test_create_order_invalid_type(client):
    response = client.post("/order/create", {
        "product_id": "abc",
        "quantity": 2
    })

    assert response.status_code == 400


# ❌ Boundary test
def test_create_order_zero_quantity(client):
    response = client.post("/order/create", {
        "product_id": 1,
        "quantity": 0
    })

    assert response.status_code in [400, 422]


# ❌ Unauthorized access
def test_order_without_token():
    import requests

    response = requests.post(
        "https://api.demo.com/order/create",
        json={"product_id": 1, "quantity": 2}
    )

    assert response.status_code == 401


# ❌ Invalid product ID
def test_create_order_invalid_product(client):
    response = client.post("/order/create", {
        "product_id": 999999,
        "quantity": 1
    })

    assert response.status_code in [400, 404]

def test_contract_lightweight(client):
    response = client.post("/order/create", {
        "product_id": 1,
        "quantity": 2
    })

    data = response.json()

    assert isinstance(data["order_id"], int)
    assert data["status"] in ["created", "confirmed"]
    assert data["total_amount"] >= 0