from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class StitchingPinTypeCreate(BaseModel):
    pin_type_name: str


class StitchingPinTypeUpdate(BaseModel):
    pin_type_id: int
    pin_type_name: str


class StitchingPinTypeResponse(BaseModel):
    pin_type_id: int
    pin_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
