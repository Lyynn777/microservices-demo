from pydantic import BaseModel, PositiveInt
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: PositiveInt
    unit_price: float

class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]

class Order(BaseModel):
    id: str
    user_id: str
    total_amount: float
    status: str
    items: List[OrderItem]
