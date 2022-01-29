# my package dependencies
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


# my package imports


class Author(BaseModel):
    name: str
    # lastname: Optional[str] = None
    birthdate: Optional[date]


class PutAuthor(BaseModel):
    name: Optional[str]
    birthdate: Optional[date]


class CategoryInfo(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BookInfo(BaseModel):
    title: str
    subtitle: Optional[str]
    publish_date: date
    # category: list[CategoryInfo]

    class Config:
        orm_mode = True


class GetAuthor(BaseModel):
    id: int
    name: str
    birthdate: Optional[date]
    books: list[BookInfo]
    created: datetime
    updated: Optional[datetime]

    class Config:  # duuno exactly why, but i need it
        orm_mode = True


# class GetAuthor(Author):
#     id: int
#     created: datetime
#     updated: Optional[datetime]

#     class Config:
#         orm_mode = True
