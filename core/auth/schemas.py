from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from app.settings import pwd_context

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    username: str
    password: str


## User
class UserBase(BaseModel):
    username: str = Field(min_length=5, max_length=50)
    first_name: str = Field(min_length=5, max_length=50)
    last_name: str = Field(min_length=5, max_length=50)
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 
    password: str = Field(min_length=8)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=5, max_length=50)
    first_name: Optional[str] = Field(None, min_length=5, max_length=50)
    last_name: Optional[str] = Field(None, min_length=5, max_length=50)
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 
    password: Optional[str] = Field(None, min_length=8)

    @field_validator('password', mode='before')
    def hash_password(cls, value: str):
        return pwd_context.hash(value)

class UserCreate(UserBase):

    # Validador para `created_at` para usar la fecha y hora actual si no se proporciona
    @field_validator('created_at', mode='before', check_fields=False)
    def set_created_at(cls, value):
        return value or datetime.utcnow()

    # Validador para `password` para hashear la contraseña
    @field_validator('password', mode='before')
    def hash_password(cls, value: str):
        return pwd_context.hash(value)

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
