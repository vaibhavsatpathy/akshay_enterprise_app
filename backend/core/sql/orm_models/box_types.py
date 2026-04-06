from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class BoxType(Base):
    __tablename__ = "box_types"
    __table_args__ = {"extend_existing": True}
    box_type_id = Column(Integer, primary_key=True, autoincrement=True)
    box_type_value = Column(String)  # universal, die_punch
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
