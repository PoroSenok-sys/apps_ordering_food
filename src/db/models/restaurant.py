from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.session import Base


if TYPE_CHECKING:
    from .order import CartItem, OrderItem


class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

    dishes: Mapped[list["Dish"]] = relationship(back_populates="restaurant")


class Dish(Base):
    __tablename__ = "dishes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id", ondelete="CASCADE"))
    restaurant: Mapped["Restaurant"] = relationship(back_populates="dishes")

    order_item: Mapped[list["OrderItem"]] = relationship(back_populates="ord_dish")
    cart_item: Mapped[list["CartItem"]] = relationship(back_populates="dish")
