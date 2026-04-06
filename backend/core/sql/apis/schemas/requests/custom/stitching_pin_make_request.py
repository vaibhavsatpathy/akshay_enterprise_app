from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class StitchingPinMakeCreate(BaseModel):
    make_name: str


class StitchingPinMakeUpdate(BaseModel):
    make_id: int
    make_name: str


class StitchingPinMakeResponse(BaseModel):
    make_id: int
    make_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
