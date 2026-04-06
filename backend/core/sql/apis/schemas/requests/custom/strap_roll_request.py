from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class StrapRollCreate(BaseModel):
    roll_type_id: Optional[int] = None
    size: Optional[float] = None
    weight_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class StrapRollUpdate(BaseModel):
    roll_id: int
    roll_type_id: Optional[int] = None
    size: Optional[float] = None
    weight_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class StrapRollResponse(BaseModel):
    roll_id: int
    roll_type_id: Optional[int] = None
    size: Optional[float] = None
    weight_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
