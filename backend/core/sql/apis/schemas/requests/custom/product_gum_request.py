from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductGumCreate(BaseModel):
    gum_name: Optional[str] = None
    gum_type_id: Optional[int] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    weight_per_bag: Optional[float] = None
    ratio_prescribed: Optional[str] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    variation_in_weight: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductGumUpdate(BaseModel):
    gum_id: int
    gum_name: Optional[str] = None
    gum_type_id: Optional[int] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    weight_per_bag: Optional[float] = None
    ratio_prescribed: Optional[str] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    variation_in_weight: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductGumResponse(BaseModel):
    gum_id: int
    gum_name: Optional[str] = None
    gum_type_id: Optional[int] = None
    unit_type_id: Optional[int] = None
    number_of_units: Optional[int] = None
    rate_per_unit: Optional[float] = None
    weight_per_bag: Optional[float] = None
    ratio_prescribed: Optional[str] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    variation_in_weight: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
