from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class PrintingPaperBlockScreenCreate(BaseModel):
    order_id: Optional[int] = None
    number_of_sheets: Optional[int] = None
    color_job_type_id: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None


class PrintingPaperBlockScreenUpdate(BaseModel):
    print_id: int
    order_id: Optional[int] = None
    number_of_sheets: Optional[int] = None
    color_job_type_id: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None


class PrintingPaperBlockScreenResponse(BaseModel):
    print_id: int
    order_id: Optional[int] = None
    number_of_sheets: Optional[int] = None
    color_job_type_id: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
