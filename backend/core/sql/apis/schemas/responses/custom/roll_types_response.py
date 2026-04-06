from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RollTypeCreate(BaseModel):
    roll_type_name: str


class RollTypeUpdate(BaseModel):
    roll_type_id: int
    roll_type_name: str


class RollTypeResponse(BaseModel):
    roll_type_id: int
    roll_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
