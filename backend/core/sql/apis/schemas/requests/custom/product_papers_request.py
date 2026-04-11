from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductPaperCreate(BaseModel):
    bundle_id: Optional[int] = None
    gsm_id: Optional[int] = None
    bf_id: Optional[int] = None
    reel_size: Optional[float] = None
    cutting_size: Optional[float] = None
    location_id: Optional[int] = None
    weight_per_gross: Optional[float] = None
    number_of_gross: Optional[int] = None
    number_of_paper_per_gross: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPaperUpdate(BaseModel):
    gross_id: int
    bundle_id: Optional[int] = None
    gsm_id: Optional[int] = None
    bf_id: Optional[int] = None
    reel_size: Optional[float] = None
    cutting_size: Optional[float] = None
    location_id: Optional[int] = None
    weight_per_gross: Optional[float] = None
    number_of_gross: Optional[int] = None
    number_of_paper_per_gross: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductPaperResponse(BaseModel):
    gross_id: int
    bundle_id: Optional[int] = None
    gsm_id: Optional[int] = None
    bf_id: Optional[int] = None
    reel_size: Optional[float] = None
    cutting_size: Optional[float] = None
    location_id: Optional[int] = None
    weight_per_gross: Optional[float] = None
    number_of_gross: Optional[int] = None
    number_of_paper_per_gross: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
