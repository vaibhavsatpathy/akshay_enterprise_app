from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Party(Base):
    __tablename__ = "party_table"
    __table_args__ = {"extend_existing": True}
    party_id = Column(Integer, primary_key=True, autoincrement=True)
    party_name = Column(String)
    address = Column(String)
    contact = Column(String)
    state = Column(String)
    gstin = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
