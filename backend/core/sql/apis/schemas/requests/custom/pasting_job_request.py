from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class PastingJobCreate(BaseModel):
    order_id: Optional[int] = None
    ordered_sheets: Optional[int] = None
    actual_sheets: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None


class PastingJobUpdate(BaseModel):
    job_id: int
    order_id: Optional[int] = None
    ordered_sheets: Optional[int] = None
    actual_sheets: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None


class PastingJobResponse(BaseModel):
    job_id: int
    order_id: Optional[int] = None
    ordered_sheets: Optional[int] = None
    actual_sheets: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
