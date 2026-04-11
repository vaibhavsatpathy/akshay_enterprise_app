from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductSparePartCreate(BaseModel):
    part_name: Optional[str] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    reference_machine: Optional[str] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductSparePartUpdate(BaseModel):
    part_id: int
    part_name: Optional[str] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    reference_machine: Optional[str] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductSparePartResponse(BaseModel):
    part_id: int
    part_name: Optional[str] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    reference_machine: Optional[str] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
