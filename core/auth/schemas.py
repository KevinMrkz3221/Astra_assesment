from pydantic import BaseModel, Field, field_validator
from app.settings import pwd_context

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    username: str
    password: str


## User
class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    username: str = Field(min_length=10, max_length=100)
    password: str = Field(min_length=8)

    @field_validator('password')
    def hash_password(cls, value: str):
        return pwd_context.hash(value)
    

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
