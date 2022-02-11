from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List
from pydantic import ValidationError

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import core, schema, models, db
from app import auth


router = APIRouter(tags=["User"])


@router.post("/registration")
def user_registration(user_json: schema.UserBase):
    """User Registration:
    - email: Not Null, unique Field
    - password: Not Null str field.
    """
    try:
        # new_user = models.User(**user_json.dict())
        user_json.password = auth.get_hash_password(user_json.password)
        new_user = models.User(**user_json.dict())
        new_user.add_and_save()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="email already registered")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return "User added Successfully"


@router.get("/all/user", response_model=List[schema.GetUser])
def get_all_users():
    """Lists all users"""
    try:
        # _db = db.Session()
        # user_data = _db.query(models.User).all()
        return models.User.get_all()
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    # else:
    #     return user_data
