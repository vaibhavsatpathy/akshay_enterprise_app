from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class CorrugationJobCreate(BaseModel):
    order_id: Optional[int] = None
    ordered_sheets: Optional[int] = None
    actual_sheets: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None
    fluting_paper_gsm: Optional[int] = None
    fluting_paper_bf: Optional[int] = None
    plain_paper_gsm: Optional[int] = None
    plain_paper_bf: Optional[int] = None
    reels_used: Optional[List[Dict[str, Any]]] = None


class CorrugationJobUpdate(BaseModel):
    job_id: int
    order_id: Optional[int] = None
    ordered_sheets: Optional[int] = None
    actual_sheets: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None
    fluting_paper_gsm: Optional[int] = None
    fluting_paper_bf: Optional[int] = None
    plain_paper_gsm: Optional[int] = None
    plain_paper_bf: Optional[int] = None
    reels_used: Optional[List[Dict[str, Any]]] = None


class CorrugationJobResponse(BaseModel):
    job_id: int
    order_id: Optional[int] = None
    ordered_sheets: Optional[int] = None
    actual_sheets: Optional[int] = None
    employees: Optional[List[Dict[str, Any]]] = None
    fluting_paper_gsm: Optional[int] = None
    fluting_paper_bf: Optional[int] = None
    plain_paper_gsm: Optional[int] = None
    plain_paper_bf: Optional[int] = None
    reels_used: Optional[List[Dict[str, Any]]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
