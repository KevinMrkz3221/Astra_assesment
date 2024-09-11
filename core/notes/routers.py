from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import JSONResponse, RedirectResponse

from app.database import get_db, Session

from core.users.models import User 
from core.auth.src import get_current_user

from .schemas import NoteCreate, NoteUpdate, NoteSchema
from .models import Note


router = APIRouter()


@router.get("/notes", tags=['Notes'], response_model=List[NoteSchema])
async def get_notes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    notes = db.query(Note).filter(Note.user_id == current_user.id)
    if notes is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notes not found")
    return notes


@router.get("/notes/{id}", tags=['Notes'], response_model=NoteSchema)
async def get_notes(id: int,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == id and Note.user_id == current_user.id).first()

    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    
    return note


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

@router.put('/notes/{id}', tags=['Notes'], response_model=NoteSchema)
async def update_note(id: int, note_update: NoteUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == id, Note.user_id == current_user.id).first()

    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    # Actualizar los campos solo si han sido proporcionados
    if note_update.title is not None:
        note.title = note_update.title
    if note_update.description is not None:
        note.description = note_update.description


    db.commit()
    db.refresh(note)
    return note


@router.delete('/notes/{id}', tags=['Notes'])
async def update_note(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == id, Note.user_id == current_user.id).first()
    
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}