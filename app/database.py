from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
# Ruta de la base de datos SQLite
BASE_DIR = Path(__file__).resolve().parent.parent

SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"

# Opciones para SQLite (evitar problemas con múltiples hilos)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
