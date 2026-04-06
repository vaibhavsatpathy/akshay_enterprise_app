from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PaperTypeCreate(BaseModel):
    paper_type_name: str


class PaperTypeUpdate(BaseModel):
    paper_type_id: int
    paper_type_name: str


class PaperTypeResponse(BaseModel):
    paper_type_id: int
    paper_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
