from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[float] = mapped_column(default=0)

    user_cart_item: Mapped[list["CartItem"]] = relationship(back_populates="user")
    order: Mapped[list["Order"]] = relationship(back_populates="user_order")


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    quantity: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="user_cart_item")

    dish: Mapped["Dish"] = relationship(back_populates="cart_item")


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

    order_item: Mapped["OrderItem"] = relationship(back_populates="ord_dish")
    cart_item: Mapped[list["CartItem"]] = relationship(back_populates="dish")
