from typing import List

from pydantic import BaseModel


class DishBase(BaseModel):
    id: int
    name: str
    price: float


class RestaurantBase(BaseModel):
    id: int
    name: str
    dishes: List[DishBase] = []  # Список блюд, связанных с рестораном
