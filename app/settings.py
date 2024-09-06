from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from typing import List
from pathlib import Path
import os

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

settings = Settings()




