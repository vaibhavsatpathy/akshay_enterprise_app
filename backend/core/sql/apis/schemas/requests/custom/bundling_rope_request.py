from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class BundlingRopeCreate(BaseModel):
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class BundlingRopeUpdate(BaseModel):
    bundle_id: int
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class BundlingRopeResponse(BaseModel):
    bundle_id: int
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
