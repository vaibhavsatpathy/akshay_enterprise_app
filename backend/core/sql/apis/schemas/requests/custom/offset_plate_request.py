from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class OffsetPlateCreate(BaseModel):
    order_id: Optional[int] = None
    plate_type_id: Optional[int] = None
    plate_size_id: Optional[int] = None
    number_of_plates: Optional[int] = None


class OffsetPlateUpdate(BaseModel):
    plate_id: int
    order_id: Optional[int] = None
    plate_type_id: Optional[int] = None
    plate_size_id: Optional[int] = None
    number_of_plates: Optional[int] = None


class OffsetPlateResponse(BaseModel):
    plate_id: int
    order_id: Optional[int] = None
    plate_type_id: Optional[int] = None
    plate_size_id: Optional[int] = None
    number_of_plates: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
