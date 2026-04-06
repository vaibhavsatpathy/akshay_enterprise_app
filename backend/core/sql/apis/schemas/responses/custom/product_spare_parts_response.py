from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductSparePartCreate(BaseModel):
    part_name: Optional[str] = None
    quantity: Optional[int] = None
    unit_type_id: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductSparePartUpdate(BaseModel):
    part_id: int
    part_name: Optional[str] = None
    quantity: Optional[int] = None
    unit_type_id: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductSparePartResponse(BaseModel):
    part_id: int
    part_name: Optional[str] = None
    quantity: Optional[int] = None
    unit_type_id: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
