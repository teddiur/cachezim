from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud as crud
from app.core.config import settings
from app.database import get_db
from app.schemas import UserCreate

router = APIRouter()


@router.post("/sign-up")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
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
                                       key=settings.SIGN_IN_KEY,
                                       algorithm="HS256"),
            "token_type": "bearer"}
