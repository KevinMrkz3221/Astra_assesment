from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import JSONResponse, RedirectResponse

from app.database import get_db, Session

from core.users.models import User 
from core.auth.src import get_current_user

from .schemas import NoteCreate
from .models import Note


router = APIRouter()

@router.post("/notes", tags=['Notes'])
async def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_note = Note(
        title=note.title,
        description=note.description,
        user_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note