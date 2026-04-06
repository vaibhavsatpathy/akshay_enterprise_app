from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductPlySheetCreate(BaseModel):
    layer_type_id: Optional[int] = None
    dimension_id: Optional[int] = None
    size: Optional[float] = None
    number_of_sheets: Optional[int] = None
    weight: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPlySheetUpdate(BaseModel):
    sheet_id: int
    layer_type_id: Optional[int] = None
    dimension_id: Optional[int] = None
    size: Optional[float] = None
    number_of_sheets: Optional[int] = None
    weight: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPlySheetResponse(BaseModel):
    sheet_id: int
    layer_type_id: Optional[int] = None
    dimension_id: Optional[int] = None
    size: Optional[float] = None
    number_of_sheets: Optional[int] = None
    weight: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
