from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class MiscellaneousCreate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    unit_type_id: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class MiscellaneousUpdate(BaseModel):
    misc_id: int
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    unit_type_id: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class MiscellaneousResponse(BaseModel):
    misc_id: int
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    unit_type_id: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
