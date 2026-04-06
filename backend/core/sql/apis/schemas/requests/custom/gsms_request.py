from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GsmCreate(BaseModel):
    gsm_value: str


class GsmUpdate(BaseModel):
    gsm_id: int
    gsm_value: str


class GsmResponse(BaseModel):
    gsm_id: int
    gsm_value: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
