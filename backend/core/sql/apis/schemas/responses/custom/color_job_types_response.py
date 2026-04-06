from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ColorJobTypeCreate(BaseModel):
    color_job_type_name: str


class ColorJobTypeUpdate(BaseModel):
    color_job_type_id: int
    color_job_type_name: str


class ColorJobTypeResponse(BaseModel):
    color_job_type_id: int
    color_job_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
