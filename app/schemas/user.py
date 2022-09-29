from datetime import datetime
from string import ascii_lowercase, ascii_uppercase, digits

from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str
    created_at: datetime = datetime.utcnow()

    @validator('password')
    def password_must_contain_lowercase(cls, v):
        if not any([x in v for x in ascii_lowercase]):
            raise ValueError('A senha deve conter pelo menos uma letra minuscula')
        return v

    @validator('password')
    def password_must_contain_uppercase(cls, v):
        if not any([x in v for x in ascii_uppercase]):
            raise ValueError('A senha deve conter pelo menos uma letra maiuscula')

        return v

    @validator('password')
    def password_must_contain_digit(cls, v):
        if not any([x in v for x in digits]):
            raise ValueError('A senha deve conter pelo menos um digito')

        return v

    @validator('password')
    def password_length(cls, v):
        if not len(v) > 8:
            raise ValueError('A senha deve conter pelo menos pelo menos 8 caracteres')
        return v


class User(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
