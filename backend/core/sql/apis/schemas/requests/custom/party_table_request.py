from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PartyCreate(BaseModel):
    party_name: str
    address: str
    contact: str
    state: str
    gstin: str


class PartyUpdate(BaseModel):
    party_id: int
    party_name: str
    address: str
    contact: str
    state: str
    gstin: str


class PartyResponse(BaseModel):
    party_id: int
    party_name: str
    address: str
    contact: str
    state: str
    gstin: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
