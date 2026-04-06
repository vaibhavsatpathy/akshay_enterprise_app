from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UnitTypeCreate(BaseModel):
    unit_type_name: str


class UnitTypeUpdate(BaseModel):
    unit_type_id: int
    unit_type_name: str


class UnitTypeResponse(BaseModel):
    unit_type_id: int
    unit_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
