
from app.db.db import SessionLocal
from app.db import crud


def main():
    with SessionLocal() as db:

        categories = crud.get_categories(db)

        print("=" * 50)
        print("КАТАЛОГ КНИГ")
        print("=" * 50)

        for category in categories:
            print(f"\nКатегория: {category.title}")
            print("-" * 50)

            for book in category.books:
                print(f"Название: {book.title}")
                print(f"Описание: {book.description}")
                print(f"Цена: {book.price} руб.")
                print(f"Ссылка: {book.url or 'Не указана'}")
                print()


if __name__ == "__main__":
    main()

