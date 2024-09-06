from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

from app.settings import pwd_context
from app.database import get_db, Session

from .schemas import (
    User,
    UserCreate
)
from .models import User

router = APIRouter()


@router.get('/', tags=['prueba'])
def prueba():
    return JSONResponse({'Hello' : 'World'}, status_code=200)


@router.post('/users/register/', tags=['Users'], status_code=201)
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

@router.get('/users/', tags=['Users'])
async def get_user( db: Session = Depends(get_db), status_code=200) -> JSONResponse:
    db_users = db.query(User).all()
    results = jsonable_encoder(db_users)

    return JSONResponse(results, status_code=200)


@router.get('/users/{id}', tags=['Users'], status_code=200)
async def get_user(id: int = Path(ge=0), db: Session = Depends(get_db)) -> JSONResponse:
    db_user = db.query(User).filter(User.id == id).first()
    results = jsonable_encoder(db_user)
    
    if not db_user:
        raise HTTPException(status_code=404, detail='User not Found')
    return JSONResponse(results, status_code=200)


@router.put('/users/{id}', tags=['Users'], status_code=200)
async def update_user(id: int, user: UserCreate,db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail='User not Found')
    
    db_user.email = user.email
    db_user.name = user.name
    db_user.password = pwd_context.hash(user.password)
    
    db.commit()
    db.refresh(db_user)
    

    return RedirectResponse(f'/users/{id}', status_code=200)


@router.delete('/users/{id}', tags=['Users'], status_code=200)
async def update_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == id).first()
    
    if not db_user:
        print(db_user)
        raise HTTPException(status_code=404, detail='User not found')
    
    db.delete(db_user)
    db.commit()
    

    return JSONResponse({'msg' : 'User has been deleted'}, status_code=200)