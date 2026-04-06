from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BlockTypeCreate(BaseModel):
    block_type_name: str


class BlockTypeUpdate(BaseModel):
    block_type_id: int
    block_type_name: str


class BlockTypeResponse(BaseModel):
    block_type_id: int
    block_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
