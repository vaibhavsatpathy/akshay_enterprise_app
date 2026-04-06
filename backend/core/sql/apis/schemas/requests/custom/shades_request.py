from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ShadeCreate(BaseModel):
    shade_value: str
    product_type_id: int


class ShadeUpdate(BaseModel):
    shade_id: int
    shade_value: str
    product_type_id: int


class ShadeResponse(BaseModel):
    shade_id: int
    shade_value: str
    product_type_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
