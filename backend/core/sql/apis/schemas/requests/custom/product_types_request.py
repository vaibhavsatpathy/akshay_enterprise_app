from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductTypeCreate(BaseModel):
    product_type_name: str


class ProductTypeUpdate(BaseModel):
    product_type_id: int
    product_type_name: str


class ProductTypeResponse(BaseModel):
    product_type_id: int
    product_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
