from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SingleTwoPiecesTypeCreate(BaseModel):
    single_two_pieces_type_name: str


class SingleTwoPiecesTypeUpdate(BaseModel):
    single_two_pieces_type_id: int
    single_two_pieces_type_name: str


class SingleTwoPiecesTypeResponse(BaseModel):
    single_two_pieces_type_id: int
    single_two_pieces_type_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
