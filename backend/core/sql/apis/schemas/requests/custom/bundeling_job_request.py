from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class BundelingJobCreate(BaseModel):
    order_id: Optional[int] = None
    ordered_boxes: Optional[int] = None
    actual_boxes: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None


class BundelingJobUpdate(BaseModel):
    job_id: int
    order_id: Optional[int] = None
    ordered_boxes: Optional[int] = None
    actual_boxes: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None


class BundelingJobResponse(BaseModel):
    job_id: int
    order_id: Optional[int] = None
    ordered_boxes: Optional[int] = None
    actual_boxes: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
