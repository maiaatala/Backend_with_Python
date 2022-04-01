# my package dependencies
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

# my package imports
from .auxiliar_schemas import CategoryB_Info, AuthorInfo


class Book(BaseModel):
    title: str
    photo: Optional[str]
    subtitle: Optional[str]
    publish_date: date
    author_id: int
    # category: list[str]


class PutBook(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]
    publish_date: Optional[date]
    photo: Optional[str]
    author_id: Optional[int]
    # category: Optional[list[str]]


class GetBook(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    photo: Optional[str] = None
    publish_date: Optional[date] = None
    author: Optional[AuthorInfo] = None
    categories_books: list[Optional[CategoryB_Info]] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class SearchBook(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    photo: Optional[str] = None
    publish_date: Optional[date] = None
    # author: Optional[AuthorInfo] = None
