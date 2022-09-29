from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_router
from app.core.config import settings
from app.database import engine, Base

Base.metadata.create_all(bind=engine)
allow_all = ['*']

app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(CORSMiddleware,
                   allow_origins=allow_all,
                   allow_credentials=True,
                   allow_methods=allow_all,
                   allow_headers=allow_all)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"Hello": "World"}
