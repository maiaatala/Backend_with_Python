# my package dependencies
from fastapi import APIRouter, Query, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # generic error wrapper
from icecream import ic
from pydantic import ValidationError
from typing import List


# my package imports
import models as m
import schemas as s

book_api = APIRouter()

tag_metadata = [{"name": "Books", "description": "CRUD operatons with Books."}]


@book_api.post("/generic_search", tags=["Books"], response_model=List[s.GetBook])
def generic_search(book: s.SearchBook):
    """Generic Book Search"""
    try:
        return m.Book.generic_get(book.dict(exclude_unset=True))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@book_api.get(
    "/books", tags=["Books"], response_model=List[s.GetBook]
)  # , response_model=List[s.GetBook]
def get_books():
    """Show all Books"""
    try:
        return m.Book.get_all()
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@book_api.get("/books/{id}", tags=["Books"], response_model=s.GetBook)
def search_book(id: int):
    """search Book by id"""
    try:
        book = m.Book.get(1)
        ic(book.categories_books)
        return m.Book.get(id)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@book_api.post("/create_books", tags=["Books"])
def create_book(book: s.Book):
    """create Book"""
    try:
        new_book = m.Book(**book.dict())
        new_book.add_and_save()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Book already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return "Book added successfully"


@book_api.put("/update_book", tags=["Books"])
def update_book(*, id: int = Query(..., description="Book's id"), book: s.PutBook):
    """Update Book"""
    try:
        m.Book.update(id, **book.dict())
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "Book updated successfully"


@book_api.delete("/delete_book", tags=["Books"])
def delete_book(*, id: int = Query(..., description="book's id")):
    """Delete Book"""
    try:
        m.Book.delete(id)
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "Book Deleted successfully"
