from pydantic import BaseModel, model_validator, field_validator


class POIFilterParameters(BaseModel):
    name: str | None = None
    latitude: float | None = None  # TODO >= 0
    longitude: float | None = None
    min_dist: float | None = None
    max_dist: float | None = None

    def has_required_params(self):
        return all(value is None for value in [self.name, self.min_dist, self.max_dist])

    def _has_min_or_max_distance(self):
        return self.max_dist is not None or self.min_dist is not None

    def _has_valid_distances(self):
        if self.max_dist is not None and self.min_dist is not None:
            return self.max_dist >= self.min_dist
        else:
            return True

    def _has_location(self):
        return self.latitude is not None or self.longitude is not None

    def _has_valid_location(self):
        return self.latitude is not None and self.longitude is not None

    @model_validator(mode="after")
    def _param_validator(self):
        if self._has_location():
            if not self._has_valid_location():
                raise ValueError("both longitude and latitude should be specified")
            if not self._has_min_or_max_distance():
                raise ValueError(
                    "minimum or maximum distance should be specified with location"
                )
            if not self._has_valid_distances():
                raise ValueError(
                    "minimum distance can't be greater than maximum distance"
                )
        return self

    @field_validator("max_dist", "min_dist")
    @classmethod
    def _validate_distances(cls, v):
        if v is None:
            return v
        if v < 0:
            raise ValueError("distance can't be negative")
        return v

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
