from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FluteTypeCreate(BaseModel):
    flute_type_name: str


class FluteTypeUpdate(BaseModel):
    flute_type_id: int
    flute_type_name: str


class FluteTypeResponse(BaseModel):
    flute_type_id: int
    flute_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
