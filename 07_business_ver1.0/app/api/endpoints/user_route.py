from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List
from pydantic import ValidationError

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import core, schema, models, db
from app import auth


router = APIRouter(tags=["User"])


@router.get("/user/{uuid}", response_model=schema.GetUser)
def get_user_by_uuid(uuid: UUID4):
    """Search users by their UUID
    - **UUID**: uuid do responsavel a ser pesquisado"""

    try:
        return models.User.get(uuid)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())


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


@router.post("/registration")
def user_registration(user_json: schema.UserBase):
    """User Registration:
    - username: str, Not Null and unique Field
    - password: str, Not Null Field
    """
    try:
        # new_user = models.User(**user_json.dict())
        user_json.password = auth.get_hash_password(user_json.password)
        new_user = models.User(**user_json.dict())
        new_user.add_and_save()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="username already registered")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    else:
        return "User added Successfully"


@router.put("/user/update/{uuid}")
def update_user(uuid: UUID4, user_json: schema.PutUser):
    """Update user by their UUID
    - **UUID**: UUID of the user to be updated
    """
    try:
        user_json.password = auth.get_hash_password(user_json.password)
        models.User.update(uuid, **user_json.dict())
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "User updated successfully"


@router.delete("/user/delete/{uuid}")
def delete_user_by_uuid(uuid: UUID4):
    """Delete user by their UUID
    - **UUID**: UUID of the user to be deleted
    """
    try:
        models.User.delete(uuid)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        e = str(e)
        raise HTTPException(status_code=400, detail=e)
    else:
        return "User deleted successfully"
