from fastapi import APIRouter, HTTPException

from src.crud.cart import add_to_cart, remove_from_cart, get_cart
from src.db.schemas.user_schema import CartResponse

router = APIRouter(
    prefix="/cart",
    tags=["Действия с корзиной"]
)


@router.post("/add", status_code=200)
async def add_item_to_cart(user_id: int, dish_id: int, quantity: int):
    """
    Добавляет блюдо в корзину пользователя.
    """
    success = await add_to_cart(user_id=user_id, dish_id=dish_id, quantity=quantity)
    if not success:
        raise HTTPException(status_code=404, detail="Блюдо не найдено.")
    return {"message": "Блюдо добавлено в корзину."}


@router.post("/remove", status_code=200)
async def remove_item_from_cart(user_id: int, dish_id: int, quantity: int):
    """
    Удаляет блюдо из корзины пользователя.
    """
    success = await remove_from_cart(user_id=user_id, dish_id=dish_id, quantity=quantity)
    if not success:
        raise HTTPException(status_code=404, detail="Блюдо не найдено или количество меньше указанного.")
    return {"message": "Блюдо удалено из корзины."}


@router.get("/", response_model=CartResponse)
async def view_cart(user_id: int):
    """
    Возвращает содержимое корзины пользователя.
    """
    cart_items = await get_cart(user_id)
    total_price = sum(item.dish.price * item.quantity for item in cart_items)
    positions = [
        {"id": item.dish.id, "name": item.dish.name, "quantity": item.quantity, "price": item.dish.price * item.quantity}
        for item in cart_items
    ]
    return {"total_price": total_price, "positions": positions}
