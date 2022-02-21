from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, SecretStr, validator, Field
from typing import Optional

# from app import util  # create util to validate stuff


class MerchantBase(BaseModel):
    # full_name: str = Field(max_length=128)
    email: EmailStr
    corporate_name: str


class PutMerchant(BaseModel):
    # full_name: Optional[str] = Field(max_length=128)
    email: Optional[EmailStr]
    corporate_name: Optional[str]

    # class Config:
    #     orm_mode = True


class GetMerchant(MerchantBase):
    uuid: UUID
    created: datetime
    updated: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
