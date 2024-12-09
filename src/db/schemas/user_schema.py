from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    first_name: str
    last_name: str

    id: int
    balance: float


class CartItemBase(BaseModel):
    id: int
    name: str
    quantity: int
    price: float  # Суммарная стоимость за это блюдо


class CartResponse(BaseModel):
    total_price: float
    positions: List[CartItemBase]
