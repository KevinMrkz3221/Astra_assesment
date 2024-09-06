from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.settings import pwd_context
from app.database import get_db, Session

from .schemas import (
    User,
    UserBase,
    UserCreate,
)
from .models import User

router = APIRouter()


@router.get('/', tags=['prueba'])
def prueba():
    return JSONResponse({'Hello' : 'World'}, status_code=200)


@router.post('/register/', tags=['Users'])
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse({'msg': "User registered successfully"}, status_code=201)