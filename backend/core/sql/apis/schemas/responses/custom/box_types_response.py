from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BoxTypeCreate(BaseModel):
    box_type_name: str


class BoxTypeUpdate(BaseModel):
    box_type_id: int
    box_type_name: str


class BoxTypeResponse(BaseModel):
    box_type_id: int
    box_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
