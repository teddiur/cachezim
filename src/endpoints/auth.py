from datetime import datetime, timedelta

import jwt
from decouple import config
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src import persistent as crud
from src.database import get_db
from src.schemas import UserCreate

router = APIRouter(
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/sign-up")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    return crud.create_user(db=db, user=user)


@router.post('/sign-in')
def authenticate(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    if not crud.check_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    return {"access_token": jwt.encode({"user_id": user.user_id,
                                        "email": user.email,
                                        "exp": datetime.utcnow() + timedelta(days=30)},
                                       key=config('SIGN_IN_KEY'),
                                       algorithm="HS256"),
            "token_type": "bearer"}
