from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class ProductType(Base):
    __tablename__ = "product_types"
    __table_args__ = {"extend_existing": True}
    product_type_id = Column(Integer, primary_key=True, autoincrement=True)
    product_type_value = Column(String)  # kraft_reel, duplex_reel, imported_reel, etc.
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
