from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PrintPlainStyleCreate(BaseModel):
    print_plain_style_name: str


class PrintPlainStyleUpdate(BaseModel):
    print_plain_style_id: int
    print_plain_style_name: str


class PrintPlainStyleResponse(BaseModel):
    print_plain_style_id: int
    print_plain_style_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
