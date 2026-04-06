from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BfCreate(BaseModel):
    bf_value: str


class BfUpdate(BaseModel):
    bf_id: int
    bf_value: str


class BfResponse(BaseModel):
    bf_id: int
    bf_value: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
