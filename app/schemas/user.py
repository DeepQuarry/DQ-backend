from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr]
    is_active: Optional[bool] = None
    # this way we will always know if a User is a superuser or not
    is_superuser: bool = False
    username: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
