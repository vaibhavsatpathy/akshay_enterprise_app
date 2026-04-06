from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PlateTypeCreate(BaseModel):
    plate_type_name: str


class PlateTypeUpdate(BaseModel):
    plate_type_id: int
    plate_type_name: str


class PlateTypeResponse(BaseModel):
    plate_type_id: int
    plate_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
