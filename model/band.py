from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base
from model import user_band


class Band(Base):
    __tablename__ = "band"

    band_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime)

    users = relationship("User", secondary=user_band, back_populates='bands')
