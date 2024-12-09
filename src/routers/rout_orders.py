from fastapi import APIRouter, HTTPException

from src.crud.order import create_order, get_orders
from src.crud.user import update_user_balance
from src.db.schemas.order_schema import OrdersResponse

router = APIRouter(
    prefix="/order",
    tags=["Действия с заказами"]
)


@router.post("/pay", status_code=200)
async def pay_for_order(user_id: int):
    """
    Списывает стоимость корзины с баланса пользователя и создает заказ.
    """
    success = await create_order(user_id=user_id)
    if not success:
        raise HTTPException(status_code=400, detail="Корзина пуста.")
    return {"message": "Заказ успешно оплачен."}


@router.get("/", response_model=OrdersResponse)
async def get_user_orders(user_id: int):
    """
    Возвращает список последних 10 заказов пользователя и статистику.
    """
    orders = await get_orders(user_id)
    total_count = len(orders)
    total_sum = sum(order.price for order in orders)
    last_orders = [
        {
            "id": order.id,
            "price": order.price,
            "time": order.time.timestamp(),
            "positions": [
                {"id": item.dish_id, "name": item.ord_dish.name, "price": item.price, "quantity": item.quantity}
                for item in order.positions
            ],
        }
        for order in orders[:10]
    ]
    return {"total_count": total_count, "total_sum": total_sum, "last_orders": last_orders}
