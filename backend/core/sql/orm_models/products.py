from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"extend_existing": True}
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)  # References product_types
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
