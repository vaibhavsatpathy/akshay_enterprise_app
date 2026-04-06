from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductStitchingPinCreate(BaseModel):
    material_id: Optional[int] = None
    pin_type_id: Optional[int] = None
    make_id: Optional[int] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductStitchingPinUpdate(BaseModel):
    pin_id: int
    material_id: Optional[int] = None
    pin_type_id: Optional[int] = None
    make_id: Optional[int] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductStitchingPinResponse(BaseModel):
    pin_id: int
    material_id: Optional[int] = None
    pin_type_id: Optional[int] = None
    make_id: Optional[int] = None
    quantity_kg: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
