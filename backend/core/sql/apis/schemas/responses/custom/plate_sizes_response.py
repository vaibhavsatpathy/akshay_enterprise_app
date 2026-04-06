from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PlateSizeCreate(BaseModel):
    plate_size_value: str


class PlateSizeUpdate(BaseModel):
    plate_size_id: int
    plate_size_value: str


class PlateSizeResponse(BaseModel):
    plate_size_id: int
    plate_size_value: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
