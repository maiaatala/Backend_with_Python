# my package dependencies
from pydantic import BaseModel
from typing import Optional
from datetime import date


class AuthorInfo(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:  # duuno exactly why, but i need it
        orm_mode = True


class CategoryInfo(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True


class CategoryB_Info(BaseModel):
    category: CategoryInfo

    class Config:
        orm_mode = True


class BookInfo(BaseModel):
    id: int
    title: str
    photo: Optional[str]
    # subtitle: Optional[str]
    # publish_date: date
    # author: AuthorInfo

    class Config:
        orm_mode = True


class C_BookInfo(BaseModel):
    book: BookInfo

    class Config:
        orm_mode = True
