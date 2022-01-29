# my package dependencies
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CategoryBook(BaseModel):
    books_id: int
    categories_id: int


class PutCategoryBook(BaseModel):
    books_id: Optional[int]
    categories_id: Optional[int]


class GetCategoryBook(CategoryBook):
    id: int
    created: datetime
    updated: Optional[datetime]

    class Config:
        orm_mode = True
