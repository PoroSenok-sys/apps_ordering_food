from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from src.crud.cart import get_cart
from src.crud.user import update_user_balance
from src.db.models.user import Order, OrderItem
from src.db.session import async_session_factory


async def create_order(user_id: int) -> bool:
    async with async_session_factory() as session:
        cart_items = await get_cart(user_id)
        if not cart_items:
            return False
        total_price = sum(item.dish.price * item.quantity for item in cart_items)
        order = Order(user_id=user_id, price=total_price)
        session.add(order)
        print((total_price * -1))
        await update_user_balance(user_id, (total_price * -1))
        await session.commit()
        await session.refresh(order)

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                dish_id=item.dish_id,
                quantity=item.quantity,
                price=item.dish.price * item.quantity,
            )
            session.add(order_item)
            await session.delete(item)
        await session.commit()
        return True


async def get_orders(user_id: int) -> list[Order]:
    async with async_session_factory() as session:
        query = (
            select(Order)
            .where(Order.user_id == user_id)
            .options(joinedload(Order.positions).joinedload(OrderItem.ord_dish))
            .order_by(Order.time.desc())
        )

        result = await session.execute(query)
        return result.scalars().unique().all()
