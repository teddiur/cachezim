from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import app.persistent.user as crud
from app.database import engine, Base, SessionLocal
from app.schema import UserCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


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
        raise HTTPException(status_code=400, detail="email já registrado")
    return crud.create_user(db=db, user=user)
