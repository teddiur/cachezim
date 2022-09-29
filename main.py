from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import engine, Base
from routes import router

Base.metadata.create_all(bind=engine)
allow_all = ['*']

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=allow_all,
                   allow_credentials=True,
                   allow_methods=allow_all,
                   allow_headers=allow_all)

app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
