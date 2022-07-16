from sqlalchemy import Column, String, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Building(Base):
    __tablename__ = "building"
    __table_args__ = {'schema': 'facility'}
    bid = Column(String(3), primary_key=True, index=True, nullable=False)
    bname = Column(String(10), nullable=False)
    bimage = Column(String(30))
    bcontents = Column(String(300))

    facility = relationship("Facility", back_populates="building")

class FacilityType(Base):
    __tablename__ = "facilitytype"
    __table_args__ = {'schema': 'facility'}
    ftypeid = Column(String(2), primary_key=True, index=True, nullable=False)
    ftypename = Column(String(10), nullable=False)

    facility = relationship("Facility", back_populates="facilitytype")

class Facility(Base):
    __tablename__ = "facility"
    __table_args__ = {'schema': 'facility'}
    fid = Column(String(4), primary_key=True, index=True, nullable=False)
    fname = Column(String(10), nullable=False)
    fcontents = Column(String(300))
    fimage = Column(String(30))
    bid = Column(String(3), ForeignKey('facility.building.bid')) # 스키마.테이블.컬럼
    ftypeid = Column(String(2), ForeignKey('facility.facilitytype.ftypeid')) # 스키마.테이블.컬럼

    building = relationship("Building", back_populates="facility")
    facilitytype = relationship("FacilityType", back_populates="facility")

class Reservation(Base):
    __tablename__ = "reservation"
    __table_args__ = {'schema': 'facility'}
    rid = Column(BigInteger, primary_key=True, index=True, nullable=False)
    rname = Column(String(20), nullable=False)
    fid = Column(String(5), nullable=False)
    ruser = Column(String(7), nullable=False)
    rstarttime = Column(DateTime, nullable=False)
    rendtime = Column(DateTime, nullable=False)
    rcontents = Column(String(300))
    attendees = Column(String(200))

class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'facility'}
    uid = Column(BigInteger, primary_key=True, index=True)
    password = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    department = Column(String(20), nullable=False)
    grade = Column(String(1), nullable=False)
    phonenumber = Column(String(11), nullable=False)
    auth = Column(String(1), nullable=False)
    bid = Column(String(4))

