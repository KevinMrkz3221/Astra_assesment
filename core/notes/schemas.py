from pydantic import BaseModel
from typing import Optional

class NoteBase(BaseModel):
    title: str
    description: Optional[str] = None 

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  
