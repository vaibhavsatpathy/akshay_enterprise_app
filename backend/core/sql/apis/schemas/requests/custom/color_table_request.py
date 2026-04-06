from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ColorTableCreate(BaseModel):
    color_name: Optional[str] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ColorTableUpdate(BaseModel):
    color_id: int
    color_name: Optional[str] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ColorTableResponse(BaseModel):
    color_id: int
    color_name: Optional[str] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
