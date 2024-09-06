from sqlalchemy import Column, Integer, String
from app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

