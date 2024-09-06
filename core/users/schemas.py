from pydantic import BaseModel, EmailStr, Field, field_validator
from app.settings import pwd_context

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    name: str = Field(min_length=10, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator('password')
    def hash_password(cls, value: str):
        return pwd_context.hash(value)

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
