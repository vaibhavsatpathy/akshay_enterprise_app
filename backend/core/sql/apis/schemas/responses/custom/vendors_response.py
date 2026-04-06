from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VendorCreate(BaseModel):
    vendor_name: str
    address: str
    contact: str


class VendorUpdate(BaseModel):
    vendor_id: int
    vendor_name: str
    address: str
    contact: str


class VendorResponse(BaseModel):
    vendor_id: int
    vendor_name: str
    address: str
    contact: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
