from pydantic import BaseModel, ConfigDict, Field


# CATEGORY
class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True) 


#  BOOK
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    price: float = Field(..., gt=0)
    url: str | None = Field(default=None, max_length=500)
    category_id: int = Field(..., ge=1)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookOut(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
