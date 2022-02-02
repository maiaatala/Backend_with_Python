from fastapi import APIRouter, HTTPException, Depends
from pydantic.types import UUID4
from typing import List
from pydantic import ValidationError

from app import core, schema, models, db


router = APIRouter(tags=["Users"])


@router.get(
    "/users/{uuid}",
)
def get_users_by_uuid(uuid: UUID4):
    pass
