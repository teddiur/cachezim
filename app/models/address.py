from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, index=True)
    stats = Column(String)
    city = Column(String)
    gig_place = Column(String)
    created_at = Column(DateTime)
