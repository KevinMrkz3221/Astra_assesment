from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import JSONResponse, RedirectResponse

from app.database import get_db, Session

from .schemas import User, UserCreate
from .models import User

router = APIRouter()


@router.get('/', tags=['prueba'])
def prueba():
    return JSONResponse({'Hello' : 'World'}, status_code=200)


@router.post('/users/register/', tags=['Users'], status_code=201)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='User already registered')
    
    new_user = User(
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse({'msg': "User registered successfully"}, status_code=201)

