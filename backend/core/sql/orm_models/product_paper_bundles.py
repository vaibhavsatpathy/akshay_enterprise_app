from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductPaperBundle(Base):
    __tablename__ = "product_paper_bundles"
    __table_args__ = {"extend_existing": True}
    bundle_id = Column(Integer, primary_key=True, autoincrement=True)
    bundle_weight = Column(Float)
    number_of_bundles = Column(Integer)
    total_weight = Column(Float)
    total_papers = Column(Float)
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
