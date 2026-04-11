from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductStitchingPinCreate(BaseModel):
    pin_material_id: Optional[int] = None
    pin_type_id: Optional[int] = None
    pin_make_id: Optional[int] = None
    rate_per_kg: Optional[float] = None
    weight_per_coil: Optional[float] = None
    number_of_coils: Optional[int] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    variation_in_weight: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductStitchingPinUpdate(BaseModel):
    pin_id: int
    pin_material_id: Optional[int] = None
    pin_type_id: Optional[int] = None
    pin_make_id: Optional[int] = None
    rate_per_kg: Optional[float] = None
    weight_per_coil: Optional[float] = None
    number_of_coils: Optional[int] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    variation_in_weight: Optional[float] = None
    total_base_cost: Optional[float] = None
    total_gst_cost: Optional[float] = None
    total_cost: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductStitchingPinResponse(BaseModel):
    pin_id: int
    pin_material_id: Optional[int] = None
    pin_type_id: Optional[int] = None
    pin_make_id: Optional[int] = None
    rate_per_kg: Optional[float] = None
    weight_per_coil: Optional[float] = None
    number_of_coils: Optional[int] = None
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
