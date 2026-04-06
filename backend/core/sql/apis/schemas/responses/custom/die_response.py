from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class DieCreate(BaseModel):
    die_name: Optional[str] = None
    die_length: Optional[float] = None
    die_breadth: Optional[float] = None


class DieUpdate(BaseModel):
    die_id: int
    die_name: Optional[str] = None
    die_length: Optional[float] = None
    die_breadth: Optional[float] = None


class DieResponse(BaseModel):
    die_id: int
    die_name: Optional[str] = None
    die_length: Optional[float] = None
    die_breadth: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
