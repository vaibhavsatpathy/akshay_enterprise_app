from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class BindingClothCreate(BaseModel):
    quantity_meter: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class BindingClothUpdate(BaseModel):
    cloth_id: int
    quantity_meter: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class BindingClothResponse(BaseModel):
    cloth_id: int
    quantity_meter: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
