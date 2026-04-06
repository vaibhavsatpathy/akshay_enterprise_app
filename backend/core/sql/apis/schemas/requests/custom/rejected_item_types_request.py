from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RejectedItemTypeCreate(BaseModel):
    rejected_item_type_name: str


class RejectedItemTypeUpdate(BaseModel):
    rejected_item_type_id: int
    rejected_item_type_name: str


class RejectedItemTypeResponse(BaseModel):
    rejected_item_type_id: int
    rejected_item_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
