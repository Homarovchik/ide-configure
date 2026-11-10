
from sqlalchemy import String, Text, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.db import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    books: Mapped[list["Book"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="books"
    )
