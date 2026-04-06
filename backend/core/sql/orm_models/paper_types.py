from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class PaperType(Base):
    __tablename__ = "paper_types"
    __table_args__ = {"extend_existing": True}
    paper_type_id = Column(Integer, primary_key=True, autoincrement=True)
    paper_type_value = Column(String)  # kraft, duplex, imported
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
