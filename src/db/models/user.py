from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from src.db.session import Base

if TYPE_CHECKING:
    from .order import CartItem, Order


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[float] = mapped_column(default=0)

    user_cart_item: Mapped[list["CartItem"]] = relationship(back_populates="user")
    order: Mapped[list["Order"]] = relationship(back_populates="user_order")
