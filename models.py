from database import Base
from sqlalchemy import Table, Column, Integer, Float, String


class Location(Base):
    __tablename__ = "point"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    name = Column(String)


class CommonQueryParams:
    def __init__(self, 
                 name: str | None = None, 
                 latitude: float | None = None,
                 longitude: float | None = None,
                 min_dist: float  | None= None, 
                 max_dist: float  | None= None):
          self.name = name
          self.latitude = latitude
          self.longitude = longitude
          self.max_dist = max_dist
          self.min_dist = min_dist

    def is_Needy_None(self):
        return all(value is None for value in [self.name, self.min_dist, self.max_dist])
    
    def is_Distance(self):
        return (self.max_dist or self.min_dist)
            

    def is_dists_suit(self):
        if (self.max_dist and self.min_dist):
            return (self.max_dist > self.min_dist)
        else:
            return True
    



