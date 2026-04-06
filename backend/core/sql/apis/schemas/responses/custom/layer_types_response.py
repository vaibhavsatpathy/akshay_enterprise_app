from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LayerTypeCreate(BaseModel):
    layer_type_name: str


class LayerTypeUpdate(BaseModel):
    layer_type_id: int
    layer_type_name: str


class LayerTypeResponse(BaseModel):
    layer_type_id: int
    layer_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
