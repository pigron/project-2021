from schemas import building_schema, building_update_schema
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Building

# Read All
def read_all(db: Session):
    building_list = db.query(Building).all()
    return building_list

# Read One
def read_one(bid: str, db: Session):
    one_building = db.query(Building).filter(Building.bid == bid).first()
    if not one_building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"존재하지 않습니다.")
    return one_building

# Create
def create(request: building_schema, db: Session):
    if not len(request.bid) == 4:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="건물ID는 4자리여야 합니다.")
    if " " in request.bid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="건물 ID는 공백을 넣을 수 없습니다.")
    if request.bname.isspace():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="건물명을 입력하세요.")
    if request.bid == "" or request.bname == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="건물ID 또는 건물 명이 없습니다.")
    new_building = Building(bid=request.bid, bname=request.bname, bimage=request.bimage, bcontents=request.bcontents)
    db.add(new_building)
    db.commit()
    db.refresh(new_building)
    return "생성되었습니다."

# 문제점
# 1. 공백 처리는 어떻게 할건가? (bid, bname)
# 2. 에러 처리는 어떻게 할건가?
# 해결 (더 좋은 방안이 있는가?)

# Update
def update(bid: str, request: building_update_schema, db: Session):
    if request.bname.isspace():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="건물명을 입력하세요.")
    if request.bname == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="건물ID 또는 건물 명이 없습니다.")
    building_update = db.query(Building).filter(Building.bid == bid)
    if not building_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="존재하지 않습니다.}")
    building_update.update(request.dict())
    db.commit()
    return "수정되었습니다."

# Delete
def delete(bid: str, db: Session):
    building_delete = db.query(Building).filter(Building.bid == bid).delete(synchronize_session=False)
    if not building_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"존재하지 않습니다.")
    db.commit()

