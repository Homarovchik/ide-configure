from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.db import get_db

router = APIRouter(prefix="/books", tags=["Books"])


def _check_category_exists(db: Session, category_id: int) -> None:
    if crud.get_category(db, category_id) is None:
        raise HTTPException(status_code=404, detail=f"Категория с id={category_id} не найдена")


@router.get("", response_model=list[schemas.BookOut])
def list_books(
    category_id: int | None = Query(default=None, ge=1),
    db: Session = Depends(get_db),
):
    if category_id is not None:
        _check_category_exists(db, category_id)
    return crud.get_books(db, category_id=category_id)


@router.get("/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.post("", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
def create_book(payload: schemas.BookCreate, db: Session = Depends(get_db)):
    _check_category_exists(db, payload.category_id)
    return crud.create_book(
        db=db,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        category_id=payload.category_id,
        url=payload.url,
    )


@router.put("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, payload: schemas.BookUpdate, db: Session = Depends(get_db)):
    _check_category_exists(db, payload.category_id)
    book = crud.update_book(
        db=db,
        book_id=book_id,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        category_id=payload.category_id,
        url=payload.url,
    )
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Книга не найдена")
