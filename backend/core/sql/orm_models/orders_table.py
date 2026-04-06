from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class OrdersTable(Base):
    __tablename__ = "orders_table"
    __table_args__ = {"extend_existing": True}
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    party_id = Column(Integer, ForeignKey("party_table.party_id"))
    product_name = Column(String)
    plt = Column(Integer)
    flute_type = Column(String)
    unit = Column(String)
    box_type_id = Column(Integer, ForeignKey("box_types.box_type_id"))
    box_length = Column(Float)
    box_breadth = Column(Float)
    box_height = Column(Float)
    single_two_piece_id = Column(
        Integer, ForeignKey("single_two_pieces_type.single_two_pieces_type_id")
    )
    reel_size = Column(Float)  # calculate based on formula
    sheet_size = Column(Float)  # calculate based on formula
    die_id = Column(Integer, ForeignKey("die.die_id"))
    die_reel_size = Column(Float)  # calculate based on formula
    die_sheet_size = Column(Float)  # calculate based on formula
    no_of_boxes_per_sheet = Column(Float)
    top_paper_gsm = Column(Integer)
    top_paper_bf = Column(Integer)
    flute_paper_gsm = Column(Integer)
    flute_paper_bf = Column(Integer)
    plain_paper_gsm = Column(Integer)
    plain_paper_bf = Column(Integer)
    print_plain_style_id = Column(
        Integer, ForeignKey("print_plain_style.print_plain_style_id")
    )
    printer_name = Column(String)
    company_name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
