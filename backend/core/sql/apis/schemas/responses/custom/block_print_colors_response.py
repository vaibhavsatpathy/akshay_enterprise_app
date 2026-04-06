from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class BlockPrintColorCreate(BaseModel):
    block_type_id: Optional[int] = None
    color_name: Optional[str] = None


class BlockPrintColorUpdate(BaseModel):
    color_id: int
    block_type_id: Optional[int] = None
    color_name: Optional[str] = None


class BlockPrintColorResponse(BaseModel):
    color_id: int
    block_type_id: Optional[int] = None
    color_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
