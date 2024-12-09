from sqlalchemy import select

from src.db.models.user import User
from src.db.session import async_session_factory


async def get_user(user_id: int) -> User | None:
    async with async_session_factory() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar()


async def create_user(first_name: str, last_name: str) -> User:
    async with async_session_factory() as session:
        user = User(first_name=first_name, last_name=last_name)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def update_user_balance(user_id: int, amount: float) -> bool:
    async with async_session_factory() as session:
        user = await get_user(user_id)
        if not user or user.balance + amount < 0:
            return False
        user.balance += amount
        session.add(user)
        await session.commit()
        return True
