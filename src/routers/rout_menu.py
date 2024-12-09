from fastapi import APIRouter
from typing import List

from src.crud.restaurant import get_restaurants_with_dishes
from src.db.schemas.restaurant_schema import RestaurantBase

router = APIRouter(
    prefix="/menu",
    tags=["Действия с меню ресторана"]
)


@router.get("/", response_model=List[RestaurantBase])
async def get_menu(filters: str | None = None):
    """
    Возвращает список ресторанов с блюдами.
    Поддерживает фильтрацию по названию ресторана.
    """
    return await get_restaurants_with_dishes(filter_query=filters)
