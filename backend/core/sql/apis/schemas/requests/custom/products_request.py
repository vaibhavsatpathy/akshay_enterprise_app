from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    product_name: str


class ProductUpdate(BaseModel):
    product_id: int
    product_name: str


class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
