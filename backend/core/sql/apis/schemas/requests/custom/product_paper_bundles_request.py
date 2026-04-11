from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductPaperBundleCreate(BaseModel):
    bundle_weight: Optional[float] = None
    number_of_bundles: Optional[int] = None
    total_weight: Optional[float] = None
    total_papers: Optional[float] = None
    inventory_id: Optional[int] = None


class ProductPaperBundleUpdate(BaseModel):
    bundle_id: int
    bundle_weight: Optional[float] = None
    number_of_bundles: Optional[int] = None
    total_weight: Optional[float] = None
    total_papers: Optional[float] = None
    inventory_id: Optional[int] = None


class ProductPaperBundleResponse(BaseModel):
    bundle_id: int
    bundle_weight: Optional[float] = None
    number_of_bundles: Optional[int] = None
    total_weight: Optional[float] = None
    total_papers: Optional[float] = None
    inventory_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
