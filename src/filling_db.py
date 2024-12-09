# import asyncio
#
# from src.db.models.restaurant import Restaurant, Dish
# from src.db.models.user import User
# from src.db.session import async_session_factory
#
#
# async def add_restaurant():
#     async with async_session_factory() as session:
#         rest_1 = Restaurant(id=1, name="Бургерная")
#         rest_2 = Restaurant(id=2, name="Итальянская кухня")
#         session.add_all([rest_1, rest_2])
#         await session.flush()
#         await session.commit()
#
#
# async def add_dishes():
#     async with async_session_factory() as session:
#         dish_1 = Dish(id=1, name="Грибной", price=350.0, restaurant_id=1)
#         dish_2 = Dish(id=2, name="Сырный", price=400, restaurant_id=1)
#         dish_3 = Dish(id=3, name="Пицца Маргарита", price=450.0, restaurant_id=2)
#         session.add_all([dish_1, dish_2, dish_3])
#         await session.flush()
#         await session.commit()
#
#
# async def add_users():
#     async with async_session_factory() as session:
#         rest_1 = User(id=1, first_name="Первый", last_name="Клиент")
#         rest_2 = User(id=2, first_name="Второй", last_name="Посетитель")
#         session.add_all([rest_1, rest_2])
#         await session.flush()
#         await session.commit()
#
# asyncio.run(add_users())
