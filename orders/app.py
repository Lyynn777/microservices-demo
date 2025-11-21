from fastapi import FastAPI, HTTPException, Request
from uuid import uuid4
from .models import OrderCreate, Order
from .db import orders_db
from .users_client import UsersClient

app = FastAPI(title="Orders Service")

app.state.users_client = UsersClient()

def calc_total(items):
    return sum(i.quantity * i.unit_price for i in items)

@app.post("/orders", response_model=Order)
async def create_order(payload: OrderCreate, request: Request):
    users = request.app.state.users_client

    user = await users.get_user(payload.user_id)
    if not user:
        raise HTTPException(404, "user not found")

    if user["status"] != "active":
        raise HTTPException(409, "user not active")

    total = calc_total(payload.items)

    if user["credit"] < total:
        raise HTTPException(402, "insufficient credit")

    order = Order(
        id=str(uuid4()),
        user_id=payload.user_id,
        total_amount=total,
        items=payload.items,
        status="created",
    )

    orders_db[order.id] = order
    return order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str):
    order = orders_db.get(order_id)
    if not order:
        raise HTTPException(404, "order not found")
    return order

@app.get("/orders")
def list_orders():
    return list(orders_db.values())
