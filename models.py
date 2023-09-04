from database import Base
from sqlalchemy import Table, Column, Integer, Float, String


class POI(Base):
    __tablename__ = "poi"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    name = Column(String)
