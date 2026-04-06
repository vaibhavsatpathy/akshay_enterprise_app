from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductPaper(Base):
    __tablename__ = "product_papers"
    __table_args__ = {"extend_existing": True}
    gross_id = Column(Integer, primary_key=True, autoincrement=True)
    bundle_id = Column(Integer, ForeignKey("product_paper_bundles.bundle_id"))
    gsm_id = Column(Integer, ForeignKey("gsms.gsm_id"))
    bf_id = Column(Integer, ForeignKey("bfs.bf_id"))
    reel_size = Column(Float)
    cutting_size = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    weight_per_gross = Column(Float)
    number_of_gross = Column(Integer)
    number_of_paper_per_gross = Column(Integer)  # default 144
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
