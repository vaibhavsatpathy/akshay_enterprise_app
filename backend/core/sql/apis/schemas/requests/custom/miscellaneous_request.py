from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class MiscellaneousCreate(BaseModel):
    misc_name: Optional[str] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class MiscellaneousUpdate(BaseModel):
    misc_id: int
    misc_name: Optional[str] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class MiscellaneousResponse(BaseModel):
    misc_id: int
    misc_name: Optional[str] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
