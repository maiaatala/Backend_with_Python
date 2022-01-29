# my package dependencies
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

from models import category_books

# my package imports
from .auxiliar_schemas import C_BookInfo


class Category(BaseModel):
    name: str


class PutCategory(BaseModel):
    name: Optional[str]


class GetCategory(BaseModel):
    id: int
    name: str
    categories_books: list[Optional[C_BookInfo]]
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True
