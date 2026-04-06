from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class OrdersTableCreate(BaseModel):
    party_id: Optional[int] = None
    product_name: Optional[str] = None
    plt: Optional[int] = None
    flute_type: Optional[str] = None
    unit: Optional[str] = None
    box_type_id: Optional[int] = None
    box_length: Optional[float] = None
    box_breadth: Optional[float] = None
    box_height: Optional[float] = None
    single_two_piece_id: Optional[int] = None
    reel_size: Optional[float] = None
    sheet_size: Optional[float] = None
    die_id: Optional[int] = None
    die_reel_size: Optional[float] = None
    die_sheet_size: Optional[float] = None
    no_of_boxes_per_sheet: Optional[float] = None
    top_paper_gsm: Optional[int] = None
    top_paper_bf: Optional[int] = None
    flute_paper_gsm: Optional[int] = None
    flute_paper_bf: Optional[int] = None
    plain_paper_gsm: Optional[int] = None
    plain_paper_bf: Optional[int] = None
    print_plain_style_id: Optional[int] = None
    printer_name: Optional[str] = None
    company_name: Optional[str] = None


class OrdersTableUpdate(BaseModel):
    order_id: int
    party_id: Optional[int] = None
    product_name: Optional[str] = None
    plt: Optional[int] = None
    flute_type: Optional[str] = None
    unit: Optional[str] = None
    box_type_id: Optional[int] = None
    box_length: Optional[float] = None
    box_breadth: Optional[float] = None
    box_height: Optional[float] = None
    single_two_piece_id: Optional[int] = None
    reel_size: Optional[float] = None
    sheet_size: Optional[float] = None
    die_id: Optional[int] = None
    die_reel_size: Optional[float] = None
    die_sheet_size: Optional[float] = None
    no_of_boxes_per_sheet: Optional[float] = None
    top_paper_gsm: Optional[int] = None
    top_paper_bf: Optional[int] = None
    flute_paper_gsm: Optional[int] = None
    flute_paper_bf: Optional[int] = None
    plain_paper_gsm: Optional[int] = None
    plain_paper_bf: Optional[int] = None
    print_plain_style_id: Optional[int] = None
    printer_name: Optional[str] = None
    company_name: Optional[str] = None


class OrdersTableResponse(BaseModel):
    order_id: int
    party_id: Optional[int] = None
    product_name: Optional[str] = None
    plt: Optional[int] = None
    flute_type: Optional[str] = None
    unit: Optional[str] = None
    box_type_id: Optional[int] = None
    box_length: Optional[float] = None
    box_breadth: Optional[float] = None
    box_height: Optional[float] = None
    single_two_piece_id: Optional[int] = None
    reel_size: Optional[float] = None
    sheet_size: Optional[float] = None
    die_id: Optional[int] = None
    die_reel_size: Optional[float] = None
    die_sheet_size: Optional[float] = None
    no_of_boxes_per_sheet: Optional[float] = None
    top_paper_gsm: Optional[int] = None
    top_paper_bf: Optional[int] = None
    flute_paper_gsm: Optional[int] = None
    flute_paper_bf: Optional[int] = None
    plain_paper_gsm: Optional[int] = None
    plain_paper_bf: Optional[int] = None
    print_plain_style_id: Optional[int] = None
    printer_name: Optional[str] = None
    company_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
