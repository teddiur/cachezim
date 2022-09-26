from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, Boolean

from database import Base


class UserBand(Base):
    __tablename__ = "user_band"

    gig_id = Column(Integer, primary_key=True, index=True)
    band_id = Column(Integer, ForeignKey('band.band_id'))
    address_id = Column(Integer, ForeignKey('address.user_id'))
    gig_date = Column(DateTime)
    total_amount = Column(Numeric(2, 19))
    is_gig_performed = Column(Boolean)
    is_amount_received = Column(Boolean)
    created_at = Column(DateTime)
