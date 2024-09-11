from pydantic import BaseModel, Field
from typing import Optional

class NoteBase(BaseModel):
    title: str
    description: Optional[str] = None 

class NoteCreate(NoteBase):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=5)

class NoteUpdate(NoteBase):
    pass

class NoteSchema(NoteBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  
