from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.session import Base


if TYPE_CHECKING:
    from .user import User
    from .restaurant import Dish


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    time: Mapped[datetime] = mapped_column(default=datetime.now())

    user_order: Mapped["User"] = relationship(back_populates="order")
    positions: Mapped[list["OrderItem"]] = relationship(back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.id"))
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    order: Mapped["Order"] = relationship(back_populates="positions")
    ord_dish: Mapped["Dish"] = relationship(back_populates="order_item")


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    quantity: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="user_cart_item")
    dish: Mapped["Dish"] = relationship(back_populates="cart_item")
