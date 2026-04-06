from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Vendor(Base):
    __tablename__ = "vendors"
    __table_args__ = {"extend_existing": True}
    vendor_id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_name = Column(String)
    address = Column(String)
    contact = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
