from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GumTypeCreate(BaseModel):
    gum_type_name: str


class GumTypeUpdate(BaseModel):
    gum_type_id: int
    gum_type_name: str


class GumTypeResponse(BaseModel):
    gum_type_id: int
    gum_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
