from fastapi import APIRouter, Depends, status
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db

from .schemas import User, UserBase, UserCreate, UserUpdate, LoginData
from .models import User
from .src import verify_password, create_access_token, get_current_user


router = APIRouter()


@router.get("/test", tags=["Auth"])
async def test_auth(user: User = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}. Your authentication is working!"}

@router.post('/auth/login', tags=['Auth'])
async def login(login_data: LoginData, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login_data.username).first()
    
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    

    access_token = create_access_token(data={"sub": user.username})
    return JSONResponse({"access_token": access_token, "token_type": "bearer"}, status_code=status.HTTP_200_OK)

@router.post('/auth/sign-up', tags=['Auth'], status_code=201)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='User already registered')
    
    new_user = User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        created_at = user.created_at,
        updated_at = datetime.utcnow(),
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse({'msg': "User registered successfully"}, status_code=201)

@router.put('/auth/user-update', tags=['Auth'], status_code=200)
async def update_user(user_update: UserUpdate, db: Session = Depends(get_db), user:User = Depends(get_current_user)):

    if user_update.username is not None:
        user.username = user_update.username
    if user_update.first_name is not None:
        user.first_name = user_update.first_name
    if user_update.last_name is not None:
        user.last_name = user_update.last_name
    if user_update.password is not None:
        user.password = user_update.password

    user.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(user)

    return JSONResponse(content={'detail': 'User has been updated'})