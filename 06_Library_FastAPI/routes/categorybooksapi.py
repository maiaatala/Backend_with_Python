# my package dependencies
from fastapi import APIRouter, Query, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # generic error wrapper
from icecream import ic
from pydantic import ValidationError
from typing import List


# my package imports
import models as m
import schemas as s

cat_book_api = APIRouter()

tag_metadata = [
    {"name": "Link_Category_Book", "description": "CRUD operatons with Categories."}
]


@cat_book_api.get(
    "/categoriesbooks",
    tags=["Link_Category_Book"],
    response_model=List[s.GetCategoryBook],
)  # , response_model=List[s.Getcat_book]
def get_cat_books():
    """Show all categories"""
    try:
        return m.Category_Book.get_all()
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@cat_book_api.get(
    "/categoriesbooks/{id}",
    tags=["Link_Category_Book"],
    response_model=s.GetCategoryBook,
)
def search_cat_book(id: int):
    """search cat_book by id"""
    try:
        return m.Category_Book.get(id)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@cat_book_api.post("/create_cat_book", tags=["Link_Category_Book"])
def Link_cat_book(link: s.CategoryBook):
    """create cat_book"""
    try:
        new_cat_book = m.Category_Book(**link.dict())
        new_cat_book.add_and_save()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="cat_book already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return "cat_book added succefully"


@cat_book_api.put("/update_cat_book", tags=["Link_Category_Book"])
def update_cat_book(
    *, id: int = Query(..., description="cat_book's id"), cat_book: s.PutCategoryBook
):
    """Update cat_book"""
    try:
        ic(m.Category_Book.get(id).categories_id)
        m.Category_Book.update(id, **cat_book.dict())
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "cat_book updated successfully"


@cat_book_api.delete("/delete_cat_book", tags=["Link_Category_Book"])
def delete_cat_book(*, id: int = Query(..., description="cat_book's id")):
    """Delete cat_book"""
    try:
        m.Category_Book.delete(id)
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "cat_book Deleted successfully"
