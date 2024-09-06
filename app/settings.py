from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "Astra Test"
    DEBUG: bool = True
    VERSION: str = "1.0.0"


    
    INSTALLED_ROUTERS: List[str] = [
        'core.users.routers'
    ]

    MIDDLEWARES: List[str] = [
        
    ]

    class Config:
        env_file = ".env"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = Settings()




