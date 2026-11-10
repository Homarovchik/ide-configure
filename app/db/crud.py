
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Category, Book


# CATEGORY CRUD

def create_category(db: Session, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db: Session):
    return db.scalars(select(Category)).all()


def get_category(db: Session, category_id: int):
    return db.get(Category, category_id)


def update_category(db: Session, category_id: int, title: str):
    category = db.get(Category, category_id)

    if category:
        category.title = title
        db.commit()
        db.refresh(category)

    return category


def delete_category(db: Session, category_id: int):
    category = db.get(Category, category_id)

    if category:
        db.delete(category)
        db.commit()
        return True

    return False


# BOOK CRUD

def create_book(
    db: Session,
    title: str,
    description: str,
    price: float,
    category_id: int,
    url: str | None = None
):
    book = Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session):
    return db.scalars(select(Book)).all()


def get_book(db: Session, book_id: int):
    return db.get(Book, book_id)


def update_book(
    db: Session,
    book_id: int,
    title: str,
    description: str,
    price: float,
    category_id: int,
    url: str | None = None
):
    book = db.get(Book, book_id)

    if book:
        book.title = title
        book.description = description
        book.price = price
        book.category_id = category_id
        book.url = url

        db.commit()
        db.refresh(book)

    return book


def delete_book(db: Session, book_id: int):
    book = db.get(Book, book_id)

    if book:
        db.delete(book)
        db.commit()
        return True

    return False
