from pydantic import BaseModel


class POIBaseDTO(BaseModel):
    name: str
    latitude: float
    longitude: float


class POICreateDTO(POIBaseDTO):
    pass


class POIDTO(POIBaseDTO):
    id: int
