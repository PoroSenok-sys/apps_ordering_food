from datetime import datetime
from typing import List

from pydantic import BaseModel


class OrderItemBase(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


class OrderBase(BaseModel):
    id: int
    price: float
    time: datetime
    positions: List[OrderItemBase]


class OrdersResponse(BaseModel):
    total_count: int
    total_sum: float
    last_orders: List[OrderBase]
