from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class FilePlacingCreate(BaseModel):
    file_type_id: Optional[int] = None
    quantity: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class FilePlacingUpdate(BaseModel):
    file_id: int
    file_type_id: Optional[int] = None
    quantity: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None


class FilePlacingResponse(BaseModel):
    file_id: int
    file_type_id: Optional[int] = None
    quantity: Optional[int] = None
    location_id: Optional[int] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
