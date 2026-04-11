from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductPlySheetCreate(BaseModel):
    reel_size: Optional[float] = None
    cutting_size: Optional[float] = None
    sheet_size: Optional[float] = None
    per_sheet_weight_calc: Optional[float] = None
    gsm_calc: Optional[float] = None
    per_sheet_weight_act: Optional[float] = None
    number_of_sheets: Optional[int] = None
    variation_in_weight: Optional[float] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPlySheetUpdate(BaseModel):
    sheet_id: int
    reel_size: Optional[float] = None
    cutting_size: Optional[float] = None
    sheet_size: Optional[float] = None
    per_sheet_weight_calc: Optional[float] = None
    gsm_calc: Optional[float] = None
    per_sheet_weight_act: Optional[float] = None
    number_of_sheets: Optional[int] = None
    variation_in_weight: Optional[float] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPlySheetResponse(BaseModel):
    sheet_id: int
    reel_size: Optional[float] = None
    cutting_size: Optional[float] = None
    sheet_size: Optional[float] = None
    per_sheet_weight_calc: Optional[float] = None
    gsm_calc: Optional[float] = None
    per_sheet_weight_act: Optional[float] = None
    number_of_sheets: Optional[int] = None
    variation_in_weight: Optional[float] = None
    total_weight_calc: Optional[float] = None
    total_weight_act: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
