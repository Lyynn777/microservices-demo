import pytest
from fastapi.testclient import TestClient
from app import app, orders_db
import asyncio


class FakeUsersClient:
    async def get_user(self, user_id):
        await asyncio.sleep(0)
        if user_id == "u1":
            return {"id": "u1", "credit": 1000, "status": "active"}
        if user_id == "u2":
            return {"id": "u2", "credit": 5, "status": "active"}
        if user_id == "u3":
            return {"id": "u3", "credit": 100, "status": "suspended"}
        return None

@pytest.fixture(autouse=True)
def setup():
    app.state.users_client = FakeUsersClient()
    orders_db.clear()

def test_create_order_success():
    client = TestClient(app)
    res = client.post("/orders", json={
        "user_id": "u1",
        "items": [
            {"product_id": "A", "quantity": 2, "unit_price": 10},
            {"product_id": "B", "quantity": 1, "unit_price": 5}
        ]
    })
    assert res.status_code == 200
    assert res.json()["total_amount"] == 25

def test_user_not_found():
    client = TestClient(app)
    res = client.post("/orders", json={"user_id": "ghost", "items": []})
    assert res.status_code == 404

def test_insufficient_credit():
    client = TestClient(app)
    res = client.post("/orders", json={
        "user_id": "u2",
        "items": [{"product_id": "A", "quantity": 1, "unit_price": 10}]
    })
    assert res.status_code == 402

def test_inactive_user():
    client = TestClient(app)
    res = client.post("/orders", json={
        "user_id": "u3",
        "items": [{"product_id": "A", "quantity": 1, "unit_price": 10}]
    })
    assert res.status_code == 409
