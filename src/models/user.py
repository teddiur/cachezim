from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

user_band = Table('user_band',
                  Base.metadata,
                  Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
                  Column('band_id', Integer, ForeignKey('band.band_id'), primary_key=True))


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    created_at = Column(DateTime)

    bands = relationship("Band", secondary=user_band, back_populates='users')
    # tags = db.relationship('Tag', secondary=post_tag, backref='posts')
