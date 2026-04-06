from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FileTypeCreate(BaseModel):
    file_type_name: str


class FileTypeUpdate(BaseModel):
    file_type_id: int
    file_type_name: str


class FileTypeResponse(BaseModel):
    file_type_id: int
    file_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
