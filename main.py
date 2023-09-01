from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schemas
from typing import Tuple, Annotated

models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()

#reads all points
@app.get("/api/poi", response_model = list[schemas.Location], tags=["Locations"])
def read_all(db : Session = Depends(get_db)):
    result = crud.readAll(db)
    if not result:
        raise HTTPException(status_code=404, detail="There is no point around")
    return result

#reads point matching id
@app.get("/api/poi/{id}", response_model = schemas.Location, tags=["Locations"])
def read_by_id(id : int, db: Session = Depends(get_db)):
    result = crud.readByID(db= db, ID= id)
    if not result:
        raise HTTPException(status_code=404, detail="Location not found")
    return result

#creates new point
@app.post("/api/poi", response_model= schemas.Location, tags=["Locations"], status_code=201)
def create(point : schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.createNew(db = db, point = point)

#removes existing point 
@app.delete("/api/poi/{id}", response_model= schemas.Location, tags=["Locations"])
def remove(id: int, db: Session = Depends(get_db)):
    result = crud.removeByID(db= db, ID= id)
    if not result: 
        raise HTTPException(status_code=404, detail="Location not found")
    return result

#reads point with matching attributes
@app.get("/api/poi/filter/", response_model= list[schemas.Location], tags=["Locations"])
def filter(q: Annotated[models.CommonQueryParams, Depends(models.CommonQueryParams)], db: Session= Depends(get_db)):
    if (q.is_Needy_None()):
        raise HTTPException(status_code=400)
     
    if (q.is_dists_suit() == False):
        raise HTTPException(status_code=400, detail="Minimum distance must be greater than maximum distance!")
    
    result = crud.filter(db= db, name= q.name, longitude= q.longitude, latitude= q.latitude, max_dist = q.max_dist, min_dist= q.min_dist)
    if (result == []):
        raise HTTPException(status_code=404, detail="No point is found") # it never applies this piece
    return result      
        
