from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import building_schema, building_update_schema
from repository import building
import database

get_db = database.get_db

router = APIRouter(
    prefix="/building",
    tags=["building_management"]
)

# Read All
@router.get("/", status_code=status.HTTP_200_OK)
def read_all(db: Session = Depends(get_db)):
    return building.read_all(db)

# Read One
@router.get("/{bid}", status_code=status.HTTP_200_OK)
def read_one(bid: str, db: Session = Depends(get_db)):
    return building.read_one(bid, db)

# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: building_schema, db: Session = Depends(get_db)):
    return building.create(request, db)

# Update
@router.put("/{bid}", status_code=status.HTTP_202_ACCEPTED)
def update(bid: str, request: building_update_schema, db: Session = Depends(get_db)):
    return building.update(bid, request, db)

# Delete
@router.delete("/{bid}", status_code=status.HTTP_204_NO_CONTENT)
def delete(bid: str, db : Session = Depends(get_db)):
    return building.delete(bid, db)
    