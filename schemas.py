from pydantic import BaseModel


class LocationBase(BaseModel):
    name : str
    latitude : float
    longitude : float


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id : int 






