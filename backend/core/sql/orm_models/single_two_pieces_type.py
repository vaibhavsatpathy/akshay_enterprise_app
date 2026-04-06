from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class SingleTwoPiecesType(Base):
    __tablename__ = "single_two_pieces_type"
    __table_args__ = {"extend_existing": True}
    single_two_pieces_type_id = Column(Integer, primary_key=True, autoincrement=True)
    single_two_pieces_type_value = Column(String)  # single, two_piece
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
