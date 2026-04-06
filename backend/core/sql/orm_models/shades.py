from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sql import Base


class Shade(Base):
    __tablename__ = "shades"
    __table_args__ = {"extend_existing": True}
    shade_id = Column(Integer, primary_key=True, autoincrement=True)
    product_type_id = Column(Integer, ForeignKey("product_types.product_type_id"))
    shade_value = Column(String)  # natural, yellow_golden, korean, etc.
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
