from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Band(Base):
    __tablename__ = "band"

    band_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime)
