from typing import List
from sqlalchemy.orm import Session 
import models, schemas 
from sqlalchemy.sql import func
from geoalchemy2.types import Geography
import sqlalchemy as alc


def readAll(db: Session):
    return db.query(models.Location).all() 


def readByID(db: Session, ID: int):
    return db.query(models.Location).filter(ID == models.Location.id).first()


def createNew(db: Session, point: schemas.LocationCreate):
    db_loc = models.Location(name= point.name, latitude= point.latitude, longitude = point.longitude)
    db.add(db_loc)
    db.commit()
    return db_loc


def removeByID(db: Session, ID: int):
    tbremoved = db.query(models.Location).filter(ID == models.Location.id).first() #use one()
    if tbremoved:
        db.delete(tbremoved)
        db.commit()
        return tbremoved


def filter(db: Session, name:str | None, longitude: float, latitude: float, max_dist: float | None, min_dist: float | None):
    tbs_name = f'%{name}%'
    
    centre = func.cast(func.ST_MakePoint(longitude, latitude), Geography)
    query_points = func.cast(func.ST_MakePoint(models.Location.longitude, models.Location.latitude), Geography)
    Distance = func.ST_Distance(centre, query_points)

    query = db.query(models.Location)
    
    if (name):
        query = query.filter(models.Location.name.like(tbs_name))
    if(max_dist):
        query = query.filter(Distance <= max_dist)
    if(min_dist):
        query = query.filter(min_dist <= Distance)
        
    return query.all()
    
    
    

