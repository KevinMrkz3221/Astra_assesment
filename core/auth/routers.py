from fastapi import APIRouter, Depends, status
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.database import get_db

from .schemas import User, UserBase, UserCreate
from .models import User
from .src import verify_password, create_access_token, get_current_user


router = APIRouter()


@router.get("/test", tags=["Auth"])
async def test_auth(user: User = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}. Your authentication is working!"}

@router.post('/auth/login', tags=['Auth'])
async def login(login_data: UserBase, db: Session = Depends(get_db)):
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
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse({'msg': "User registered successfully"}, status_code=201)