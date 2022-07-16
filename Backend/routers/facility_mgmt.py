from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import facility_schema, facility_update_schema
from repository import facility
import database

get_db = database.get_db

router = APIRouter(
    prefix="/facility",
    tags=["facility_management"]
)

# Read All
@router.get("/", status_code=status.HTTP_200_OK)
def read_all(db: Session = Depends(get_db)):
    return facility.read_all(db)

# Read One
@router.get("/{fid}", status_code=status.HTTP_200_OK)
def read_one(fid: str, db: Session = Depends(get_db)):
    return facility.read_one(fid, db)

# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: facility_schema, db: Session = Depends(get_db)):
    return facility.create(request, db)

# Update
@router.put("/{fid}", status_code=status.HTTP_202_ACCEPTED)
def update(fid: str, request: facility_update_schema, db: Session = Depends(get_db)):
    return facility.update(fid, request, db)

# Delete
@router.delete("/{fid}", status_code=status.HTTP_204_NO_CONTENT)
def delete(fid: str, db : Session = Depends(get_db)):
    return facility.delete(fid, db)
    