# my package dependencies
from fastapi import APIRouter, Query, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # generic error wrapper
from icecream import ic
from pydantic import ValidationError
from typing import List


# my package imports
import models as m
import schemas as s

category_api = APIRouter()

tag_metadata = [
    {"name": "Categories", "description": "CRUD operatons with Categories."}
]


@category_api.get(
    "/categories", tags=["Categories"], response_model=List[s.GetCategory]
)  # , response_model=List[s.GetCategory]
def get_categorys():
    """Show all categories"""
    try:
        return m.Category.get_all()
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@category_api.get("/categories/{id}", tags=["Categories"], response_model=s.GetCategory)
def search_category(id: int):
    """search Category by id"""
    try:
        return m.Category.get(id)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@category_api.post("/create_category", tags=["Categories"])
def create_category(cat: s.Category):
    """create category"""
    try:
        new_category = m.Category(**cat.dict())
        new_category.add_and_save()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Category already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return "category added succefully"


@category_api.put("/update_category", tags=["Categories"])
def update_category(
    *, id: int = Query(..., description="category's id"), category: s.PutCategory
):
    """Update category"""
    try:
        m.Category.update(id, **category.dict())
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "category updated successfully"


@category_api.delete("/delete_category", tags=["Categories"])
def delete_category(*, id: int = Query(..., description="category's id")):
    """Delete category"""
    try:
        m.Category.delete(id)
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "category Deleted successfully"
