from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GstConfigCreate(BaseModel):
    gst_percentage: float


class GstConfigUpdate(BaseModel):
    gst_config_id: int
    gst_percentage: float


class GstConfigResponse(BaseModel):
    gst_config_id: int
    gst_percentage: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
