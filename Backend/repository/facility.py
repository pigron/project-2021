from schemas import facility_schema, facility_update_schema
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Facility

# Read All
def read_all(db: Session):
    facility_list = db.query(Facility).all()
    return facility_list

# Read One
def read_one(fid: str, db: Session):
    one_facility = db.query(Facility).filter(Facility.fid == fid).first()
    if not one_facility:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"존재하지 않습니다.")
    return one_facility

# Create
def create(request: facility_schema, db: Session):
    if not len(request.fid) == 5:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="시설물 ID는 5자리여야 합니다.")
    if " " in request.fid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="시설물 ID는 공백을 넣을 수 없습니다.")
    if request.fname.isspace():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="시설물명을 입력하세요.")
    if request.fid == "" or request.fname == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="시설물 ID 또는 시설물명이 없습니다.")
    new_facility = Facility(fid=request.fid, fname=request.fname, fimage=request.fimage, fcontents=request.fcontents, bid=request.bid, ftypeid=request.ftypeid)
    db.add(new_facility)
    db.commit()
    db.refresh(new_facility)
    return "생성되었습니다."

# 문제점
# 1. 공백 처리는 어떻게 할건가? (bid, bname)
# 2. 에러 처리는 어떻게 할건가?
# 해결 (더 좋은 방안이 있는가?)

# Update
def update(fid: str, request: facility_update_schema, db: Session):
    if request.fname.isspace():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="시설물명을 입력하세요.")
    if request.fname == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="시설물 ID 또는 시설물명이 없습니다.")
    facility_update = db.query(Facility).filter(Facility.fid == fid)
    if not facility_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="존재하지 않습니다.}")
    facility_update.update(request.dict())
    db.commit()
    return "수정되었습니다."

# Delete
def delete(fid: str, db: Session):
    facility_delete = db.query(Facility).filter(Facility.fid == fid).delete(synchronize_session=False)
    if not facility_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"존재하지 않습니다.")
    db.commit()

