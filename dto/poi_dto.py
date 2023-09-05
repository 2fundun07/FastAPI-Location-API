from pydantic import BaseModel, field_validator


class POIBaseDTO(BaseModel):
    name: str
    latitude: float
    longitude: float
    #is there any other cases to consider?-> if lat/long are given as str, it returns validationError itself
    @field_validator("latitude")
    @classmethod
    def _validate_lat(cls, v):
        if v is None:
            return v
        if not -90 <= v <= 90:
            raise ValueError("latitude should be in range [-90, 90]")
        return v
    
    @field_validator("longitude")
    @classmethod
    def _validate_long(cls, v):
        if v is None:
            return v
        if not -180 <= v <= 180:
            raise ValueError("longitude should be in range [-180, 180]")
        return v
    


class POICreateDTO(POIBaseDTO):
    pass


class POIDTO(POIBaseDTO):
    id: int
