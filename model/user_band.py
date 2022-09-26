from sqlalchemy import Column, Integer, ForeignKey, DateTime, PrimaryKeyConstraint

from database import Base


class UserBand(Base):
    __tablename__ = "user_band"

    band_id = Column(Integer, ForeignKey('band.band_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    created_at = Column(DateTime)

    __table_args__ = (
        PrimaryKeyConstraint(band_id, user_id),
        {},
    )
