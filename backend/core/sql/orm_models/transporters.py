from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Transporter(Base):
    __tablename__ = "transporters"
    __table_args__ = {"extend_existing": True}
    transporter_id = Column(Integer, primary_key=True, autoincrement=True)
    transporter_name = Column(String)
    contact = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
