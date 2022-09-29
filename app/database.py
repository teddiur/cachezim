from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./cachezim.db"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:5432/{config('DB_NAME')}"

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
