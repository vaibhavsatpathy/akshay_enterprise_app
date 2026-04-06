from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class Die(Base):
    __tablename__ = "die"
    __table_args__ = {"extend_existing": True}
    die_id = Column(Integer, primary_key=True, autoincrement=True)
    party_id = Column(Integer, ForeignKey("party_table.party_id"))
    job_name = Column(String)
    blade_length = Column(Float)
    blade_breadth = Column(Float)
    board_length = Column(Float)
    board_breadth = Column(Float)
    vendor_name = Column(String)
    date_of_receiving_die = Column(DateTime)
    status = Column(String)
    point_of_contact = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
