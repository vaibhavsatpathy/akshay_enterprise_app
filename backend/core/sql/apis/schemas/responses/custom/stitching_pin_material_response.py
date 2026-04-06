from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class StitchingPinMaterialCreate(BaseModel):
    material_name: str


class StitchingPinMaterialUpdate(BaseModel):
    material_id: int
    material_name: str


class StitchingPinMaterialResponse(BaseModel):
    material_id: int
    material_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
