from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import books, categories
from app.db import models
from app.db.db import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # При старте приложения создаём таблицы, если их ещё нет
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Books Catalog API", version="1.0.0", lifespan=lifespan)

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
