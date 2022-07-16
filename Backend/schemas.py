from pydantic import BaseModel
from typing import Optional

class building_schema(BaseModel):
    bid: str
    bname: str
    bimage: Optional[str] = None
    bcontents: Optional[str] = None

class building_update_schema(BaseModel):
    bname: str
    bimage: Optional[str] = None
    bcontents: Optional[str] = None

class facility_schema(BaseModel):
    fid: str
    fname: str
    fcontents: Optional[str] = None
    fimage: Optional[str] = None
    bid: str
    ftypeid: str

class facility_update_schema(BaseModel):
    fname: str
    fcontents: Optional[str] = None
    fimage: Optional[str] = None
    bid: str
    ftypeid: str