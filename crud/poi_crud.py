from sqlalchemy.orm import Session
from models import POI
from dto.poi_dto import POICreateDTO
import sqlalchemy as sa
from geoalchemy2.types import Geography


class PoiCRUD:
    def fetch_all(self, session: Session):
        return session.query(POI).all()

    def get_by_id(self, session: Session, poi_id: int):
        return session.get(POI, poi_id)

    def create_new(self, session: Session, point: POICreateDTO):
        db_loc = POI(
            name=point.name, latitude=point.latitude, longitude=point.longitude
        )
        session.add(db_loc)
        session.commit()
        return db_loc

    def remove_by_id(self, session: Session, poi_id: int):
        to_be_removed = session.get(POI, poi_id)
        if to_be_removed:
            session.delete(to_be_removed)
            session.commit()
            return to_be_removed

    def fetch_with_filters(
        self,
        session: Session,
        name: str | None,
        longitude: float | None,
        latitude: float | None,
        max_dist: float | None,
        min_dist: float | None,
    ):
        tbs_name = f"%{name}%"

        centre = sa.func.cast(
            sa.func.ST_MakePoint(longitude, latitude), Geography(srid=4326)
        )
        query_points = sa.func.cast(
            sa.func.ST_MakePoint(POI.longitude, POI.latitude),
            Geography(srid=4326),
        )
        distance = sa.func.ST_Distance(centre, query_points)

        query = session.query(POI)

        if name:
            query = query.filter(POI.name.like(tbs_name))
        if max_dist:
            query = query.filter(distance <= max_dist)
        if min_dist:
            query = query.filter(min_dist <= distance)

        return query.all()
