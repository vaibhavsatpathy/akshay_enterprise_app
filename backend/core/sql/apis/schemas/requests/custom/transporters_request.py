from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TransporterCreate(BaseModel):
    transporter_name: str
    contact: str


class TransporterUpdate(BaseModel):
    transporter_id: int
    transporter_name: str
    contact: str


class TransporterResponse(BaseModel):
    transporter_id: int
    transporter_name: str
    contact: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
