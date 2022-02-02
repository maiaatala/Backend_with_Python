from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, SecretStr, validator, Field
from typing import Optional

# from app import util  # create util to validate stuff


class UserBase(BaseModel):
    full_name: str = Field(max_length=128)
    email: EmailStr
    password: str


class PutUser(BaseModel):
    full_name: Optional[str] = Field(max_length=128)
    password: Optional[str]

    class Config:
        orm_mode = True


class GetUser(UserBase):
    uuid: UUID
    password: SecretStr
    created: datetime
    updated: Optional[datetime]

    class Config:
        orm_mode: True
