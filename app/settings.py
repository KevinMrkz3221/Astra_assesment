from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from typing import List
import importlib
import inspect


class Settings(BaseSettings):
    PROJECT_NAME: str = "Astra Test"
    DEBUG: bool = True
    VERSION: str = "1.0.0"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


    
    INSTALLED_ROUTERS: List[str] = [
        'core.users.routers',
        'core.auth.routers'
    ]

    MIDDLEWARES: List[str] = [
        
    ]

    def routers(self, app):
        for router_path in self.INSTALLED_ROUTERS:
            module = importlib.import_module(router_path)
            app.include_router(module.router)

    def middlewares(self, app):
        for middleware in self.MIDDLEWARES:
            module = importlib.import_module(middleware)
            for name in dir(module):
                member = getattr(module, name)
            
            # Verificar si el miembro es una clase
            if inspect.isclass(member):
                print(f'Member name: {name}')

                app.add_middleware(name)
                
    class Config:
        env_file = ".env"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = Settings()




