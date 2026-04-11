from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductFluteCreate(BaseModel):
    layer_type_id: Optional[int] = None
    flute_type_id: Optional[int] = None
    flute_percent: Optional[float] = None
    layer_gsm_id: Optional[int] = None
    layer_bf_id: Optional[int] = None
    sheet_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductFluteUpdate(BaseModel):
    flute_id: int
    layer_type_id: Optional[int] = None
    flute_type_id: Optional[int] = None
    flute_percent: Optional[float] = None
    layer_gsm_id: Optional[int] = None
    layer_bf_id: Optional[int] = None
    sheet_id: Optional[int] = None
    inventory_id: Optional[int] = None


class ProductFluteResponse(BaseModel):
    flute_id: int
    layer_type_id: Optional[int] = None
    flute_type_id: Optional[int] = None
    flute_percent: Optional[float] = None
    layer_gsm_id: Optional[int] = None
    layer_bf_id: Optional[int] = None
    sheet_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
