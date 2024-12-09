from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from src.db.models.user import Restaurant, Dish
from src.db.session import async_session_factory


async def get_restaurants_with_dishes(filter_query: str | None = None) -> list[Restaurant]:
    async with async_session_factory() as session:
        if filter_query:
            query = select(Restaurant).options(joinedload(Restaurant.dishes)).filter(
                Restaurant.name.ilike(f"%{filter_query}%"))
        else:
            query = select(Restaurant).options(joinedload(Restaurant.dishes))

        result = await session.execute(query)
        return result.scalars().unique().all()


async def add_restaurant(name: str) -> Restaurant:
    async with async_session_factory() as session:
        restaurant = Restaurant(name=name)
        session.add(restaurant)
        await session.commit()
        await session.refresh(restaurant)
        return restaurant


async def add_dish(name: str, price: float, restaurant_id: int) -> Dish:
    async with async_session_factory() as session:
        dish = Dish(name=name, price=price, restaurant_id=restaurant_id)
        session.add(dish)
        await session.commit()
        await session.refresh(dish)
        return dish
