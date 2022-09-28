from datetime import datetime, timedelta

import bcrypt
import jwt
from decouple import config
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import app.persistent.user as crud
from app.database import engine, Base, SessionLocal
from app.schema import UserCreate

Base.metadata.create_all(bind=engine)
allow_all = ['*']

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=allow_all,
                   allow_credentials=True,
                   allow_methods=allow_all,
                   allow_headers=allow_all)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sign-up")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    return crud.create_user(db=db, user=user)


@app.post('/sign-in')
def authenticate(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print(form_data.username)
    print(form_data.password)
    user = crud.get_user_by_email(db, form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    if not bcrypt.checkpw(form_data.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    return {"access_token": jwt.encode({"user_id": user.user_id,
                                        "email": user.email,
                                        "exp": datetime.utcnow() + timedelta(days=30)},
                                       key=config('SIGN_IN_KEY'),
                                       algorithm="HS256"),
            "token_type": "bearer"}
