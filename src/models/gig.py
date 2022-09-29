from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, Boolean

from src.database import Base


class Gig(Base):
    __tablename__ = "gig"

    gig_id = Column(Integer, primary_key=True, index=True)
    band_id = Column(Integer, ForeignKey('band.band_id'))
    address_id = Column(Integer, ForeignKey('address.address_id'))
    gig_date = Column(DateTime)
    total_amount = Column(Numeric(10, 2))
    is_gig_performed = Column(Boolean)
    is_amount_received = Column(Boolean)
    created_at = Column(DateTime)
