import hashlib
from os import urandom
from string import ascii_uppercase, ascii_lowercase, digits
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


class User(BaseModel):
    errors: List = []
    name: str
    password: str
    hashed_password: bytes = None
    salt: bytes = None
    email: str

    def is_valid(self):
        if not any([x in self.password for x in ascii_uppercase]):
            self.errors.append({"field": "A senha deve ter pelo menos uma letra maiuscula"})
        if not any([x in self.password for x in ascii_lowercase]):
            self.errors.append({"field": "A senha deve ter pelo menos uma letra minuscula"})
        if not any([x in self.password for x in digits]):
            self.errors.append({"field": "A senha deve ter pelo menos um número"})
        if len(self.password) < 8:
            self.errors.append({"field": "A senha deve ter pelo menos 8 caracteres"})

        return len(self.errors) > 0

    def hash_password(self):
        salt = urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), salt, 100_000)
        self.hashed_password = key
        self.salt = salt


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/sign-up")
def create_user(user: User):
    print(user)
