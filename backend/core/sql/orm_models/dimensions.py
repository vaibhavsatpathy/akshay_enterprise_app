from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Dimension(Base):
    __tablename__ = "dimensions"
    __table_args__ = {"extend_existing": True}
    dimension_id = Column(Integer, primary_key=True, autoincrement=True)
    dimension_value = Column(String)  # inch, mm, cm
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
