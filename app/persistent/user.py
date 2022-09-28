import bcrypt
from sqlalchemy.orm import Session

from app import schema, model


def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = model.User(name=user.name,
                         email=user.email,
                         created_at=user.created_at,
                         hashed_password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
