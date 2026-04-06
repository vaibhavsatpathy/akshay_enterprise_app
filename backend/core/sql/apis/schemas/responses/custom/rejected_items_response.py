from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class RejectedItemCreate(BaseModel):
    rejected_item_type_id: Optional[int] = None
    quantity: Optional[int] = None
    weight_kg: Optional[float] = None
    location_id: Optional[int] = None


class RejectedItemUpdate(BaseModel):
    rejected_id: int
    rejected_item_type_id: Optional[int] = None
    quantity: Optional[int] = None
    weight_kg: Optional[float] = None
    location_id: Optional[int] = None


class RejectedItemResponse(BaseModel):
    rejected_id: int
    rejected_item_type_id: Optional[int] = None
    quantity: Optional[int] = None
    weight_kg: Optional[float] = None
    location_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
