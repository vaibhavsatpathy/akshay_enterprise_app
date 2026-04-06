from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class InventoryCreate(BaseModel):
    invoice_number: Optional[int] = None
    vendor_id: Optional[int] = None
    entry_date: Optional[datetime] = None
    product_id: Optional[int] = None
    transporter_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    vehicle_type: Optional[str] = None
    driver_name: Optional[str] = None
    freight_charges: Optional[float] = None
    basic_cost_of_material: Optional[float] = None
    total_weight_kg: Optional[float] = None
    per_kg_freight_charges: Optional[float] = None
    per_kg_cost_of_material: Optional[float] = None
    total_cost_of_material: Optional[float] = None


class InventoryUpdate(BaseModel):
    inventory_id: int
    invoice_number: Optional[int] = None
    vendor_id: Optional[int] = None
    entry_date: Optional[datetime] = None
    product_id: Optional[int] = None
    transporter_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    vehicle_type: Optional[str] = None
    driver_name: Optional[str] = None
    freight_charges: Optional[float] = None
    basic_cost_of_material: Optional[float] = None
    total_weight_kg: Optional[float] = None
    per_kg_freight_charges: Optional[float] = None
    per_kg_cost_of_material: Optional[float] = None
    total_cost_of_material: Optional[float] = None


class InventoryResponse(BaseModel):
    inventory_id: int
    invoice_number: Optional[int] = None
    vendor_id: Optional[int] = None
    entry_date: Optional[datetime] = None
    product_id: Optional[int] = None
    transporter_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    vehicle_type: Optional[str] = None
    driver_name: Optional[str] = None
    freight_charges: Optional[float] = None
    basic_cost_of_material: Optional[float] = None
    total_weight_kg: Optional[float] = None
    per_kg_freight_charges: Optional[float] = None
    per_kg_cost_of_material: Optional[float] = None
    total_cost_of_material: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
