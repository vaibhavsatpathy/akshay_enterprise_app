from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductGumCreate(BaseModel):
    gum_type_id: Optional[int] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductGumUpdate(BaseModel):
    gum_id: int
    gum_type_id: Optional[int] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductGumResponse(BaseModel):
    gum_id: int
    gum_type_id: Optional[int] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
