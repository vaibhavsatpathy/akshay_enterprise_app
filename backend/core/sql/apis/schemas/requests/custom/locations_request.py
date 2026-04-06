from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LocationCreate(BaseModel):
    location_name: str


class LocationUpdate(BaseModel):
    location_id: int
    location_name: str


class LocationResponse(BaseModel):
    location_id: int
    location_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
