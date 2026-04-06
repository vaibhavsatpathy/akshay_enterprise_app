from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DimensionCreate(BaseModel):
    dimension_value: str


class DimensionUpdate(BaseModel):
    dimension_id: int
    dimension_value: str


class DimensionResponse(BaseModel):
    dimension_id: int
    dimension_value: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
