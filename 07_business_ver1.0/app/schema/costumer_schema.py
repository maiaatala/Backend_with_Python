from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, SecretStr, validator, Field
from typing import Optional

# from app import util  # create util to validate stuff


class CostumerBase(BaseModel):
    # full_name: str = Field(max_length=128)
    email: EmailStr
    name: str


class PutCostumer(BaseModel):
    # full_name: Optional[str] = Field(max_length=128)
    email: Optional[EmailStr]
    name: Optional[str]

    # class Config:
    #     orm_mode = True


class GetCostumer(CostumerBase):
    uuid: UUID
    created: datetime
    updated: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
