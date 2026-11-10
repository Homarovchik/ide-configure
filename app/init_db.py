
from app.db.db import Base, engine, SessionLocal
from app.db import crud


# Создаём таблицы
Base.metadata.create_all(bind=engine)


# Открываем сессию
with SessionLocal() as db:

    # Создаём категории
    categories_data = [
        "Программирование",
        "Художественная литература"
    ]

    categories = {}

    for title in categories_data:
        category = next(
            (c for c in crud.get_categories(db) if c.title == title),
            None
        )

        if category is None:
            category = crud.create_category(db, title)

        categories[title] = category

    # Данные книг
    books_data = [
        {
            "title": "Python. К вершинам мастерства",
            "description": "Продвинутое руководство по Python",
            "price": 1800,
            "category": "Программирование"
        },
        {
            "title": "Изучаем Python",
            "description": "Книга для изучения языка Python",
            "price": 1500,
            "category": "Программирование"
        },
        {
            "title": "Чистый код",
            "description": "Практики написания качественного кода",
            "price": 2100,
            "category": "Программирование"
        },
        {
            "title": "1984",
            "description": "Антиутопический роман Джорджа Оруэлла",
            "price": 700,
            "category": "Художественная литература"
        },
        {
            "title": "Мастер и Маргарита",
            "description": "Роман Михаила Булгакова",
            "price": 850,
            "category": "Художественная литература"
        },
        {
            "title": "Преступление и наказание",
            "description": "Роман Фёдора Достоевского",
            "price": 900,
            "category": "Художественная литература"
        }
    ]

    # Добавляем книги, если их ещё нет
    existing_titles = {
        book.title for book in crud.get_books(db)
    }

    for item in books_data:
        if item["title"] not in existing_titles:
            crud.create_book(
                db=db,
                title=item["title"],
                description=item["description"],
                price=item["price"],
                category_id=categories[item["category"]].id
            )

print("База данных успешно инициализирована!")
