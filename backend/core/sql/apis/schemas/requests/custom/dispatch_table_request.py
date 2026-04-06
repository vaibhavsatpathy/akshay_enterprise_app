from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class DispatchTableCreate(BaseModel):
    order_id: Optional[int] = None
    dispatch_date: Optional[datetime] = None
    quantity: Optional[int] = None
    transporter_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    driver_name: Optional[str] = None
    freight_charges: Optional[float] = None


class DispatchTableUpdate(BaseModel):
    id: int
    order_id: Optional[int] = None
    dispatch_date: Optional[datetime] = None
    quantity: Optional[int] = None
    transporter_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    driver_name: Optional[str] = None
    freight_charges: Optional[float] = None


class DispatchTableResponse(BaseModel):
    id: int
    order_id: Optional[int] = None
    dispatch_date: Optional[datetime] = None
    quantity: Optional[int] = None
    transporter_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    driver_name: Optional[str] = None
    freight_charges: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
