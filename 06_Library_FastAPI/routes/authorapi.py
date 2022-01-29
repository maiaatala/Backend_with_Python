# my package dependencies
from fastapi import APIRouter, Query, HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # generic error wrapper
from icecream import ic
from pydantic import ValidationError
from typing import List

# my package imports
import models as m
import schemas as s

# from config import Session

auth_api = APIRouter()

tag_metadata = [{"name": "Authors", "description": "CRUD operatons with Authors."}]

# show all books written by the author.


@auth_api.get("/authors", tags=["Authors"], response_model=List[s.GetAuthor])
def get_authors():
    """Show all authors"""
    try:
        return m.Author.get_all()
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@auth_api.get("/author/{id}", tags=["Authors"], response_model=s.GetAuthor)
def search_author(id: int):
    """search author by id"""
    try:
        return m.Author.get(id)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@auth_api.post("/create_authors", tags=["Authors"])
def create_authors(author: s.Author):
    """create author"""
    try:
        new_author = m.Author(**author.dict())
        new_author.add_and_save()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Author already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return "Author added succefully"


@auth_api.put("/update_author", tags=["Authors"])
def update_author(
    *, id: int = Query(..., description="author's id"), author: s.PutAuthor
):
    """Update author"""
    try:
        m.Author.update(id, **author.dict())
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "Author updated successfully"


@auth_api.delete("/delete_author", tags=["Authors"])
def delete_author(*, id: int = Query(..., description="author's id")):
    """Delete author"""
    try:
        m.Author.delete(id)
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "Author Deleted successfully"
