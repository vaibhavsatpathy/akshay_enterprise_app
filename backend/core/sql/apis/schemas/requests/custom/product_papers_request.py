from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductPaperCreate(BaseModel):
    shade_id: Optional[int] = None
    gsm_id: Optional[int] = None
    bf_id: Optional[int] = None
    dimension_id: Optional[int] = None
    size: Optional[float] = None
    number_of_sheets: Optional[int] = None
    weight: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPaperUpdate(BaseModel):
    gross_id: int
    shade_id: Optional[int] = None
    gsm_id: Optional[int] = None
    bf_id: Optional[int] = None
    dimension_id: Optional[int] = None
    size: Optional[float] = None
    number_of_sheets: Optional[int] = None
    weight: Optional[float] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPaperResponse(BaseModel):
    gross_id: int
    shade_id: Optional[int] = None
    gsm_id: Optional[int] = None
    bf_id: Optional[int] = None
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
