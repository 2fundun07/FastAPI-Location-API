from fastapi import FastAPI, HTTPException, Depends
from fastapi.exception_handlers import request_validation_exception_handler
from pydantic import ValidationError
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
from typing import Tuple, Annotated
from crud.poi_crud import PoiCRUD
from dto.poi_dto import POICreateDTO, POIDTO

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


poi_crud = PoiCRUD()


# reads all points
@app.get("/api/poi", response_model=list[POIDTO], tags=["Locations"])
def read_all(session: Session = Depends(get_db)):
    result = poi_crud.fetch_all(session)
    return result


# reads point matching id
@app.get("/api/poi/{id}", response_model=POIDTO, tags=["Locations"])
def read_by_id(id: int, session: Session = Depends(get_db)):
    result = poi_crud.get_by_id(session, id)
    if result is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return result


# creates new point
@app.post("/api/poi", response_model=POIDTO, tags=["Locations"], status_code=201)
def create(point: POICreateDTO, session: Session = Depends(get_db)):
    return poi_crud.create_new(session, point)


# removes existing point
@app.delete("/api/poi/{id}", response_model=POIDTO, tags=["Locations"])
def remove(id: int, session: Session = Depends(get_db)):
    result = poi_crud.remove_by_id(session, id)
    if result is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return result


# reads point with matching attributes
@app.get("/api/poi/filter/", response_model=list[POIDTO], tags=["Locations"])
def filter(
    q: Annotated[schemas.POIFilterParameters, Depends(schemas.POIFilterParameters)],
    session: Session = Depends(get_db),
):
    result = poi_crud.fetch_with_filters(session, **q.model_dump())
    return result


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)
