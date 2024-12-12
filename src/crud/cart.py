from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from src.db.models.order import CartItem
from src.db.models.restaurant import Dish
from src.db.session import async_session_factory


async def add_to_cart(user_id: int, dish_id: int, quantity: int) -> bool:
    async with async_session_factory() as session:
        stmp_dish = await session.execute(select(Dish).where(Dish.id == dish_id))
        dish = stmp_dish.scalar()
        if not dish:
            return False

        stmp_cart = await session.execute(
            select(CartItem).where(CartItem.user_id == user_id, CartItem.dish_id == dish_id)
        )
        cart_item = stmp_cart.scalar()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(user_id=user_id, dish_id=dish_id, quantity=quantity)
            session.add(cart_item)
        await session.commit()
        return True


async def remove_from_cart(user_id: int, dish_id: int, quantity: int) -> bool:
    async with async_session_factory() as session:
        result = await session.execute(
            select(CartItem).where(CartItem.user_id == user_id, CartItem.dish_id == dish_id)
        )
        cart_item = result.scalar()
        if not cart_item or cart_item.quantity < quantity:
            return False
        cart_item.quantity -= quantity
        if cart_item.quantity == 0:
            await session.delete(cart_item)
        await session.commit()
        return True


async def get_cart(user_id: int) -> list[CartItem]:
    async with async_session_factory() as session:
        result = await session.execute(
            select(CartItem).where(CartItem.user_id == user_id).options(joinedload(CartItem.dish))
        )
        return result.scalars().all()
