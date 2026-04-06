from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductPlySheet(Base):
    __tablename__ = "product_ply_sheets"
    __table_args__ = {"extend_existing": True}
    sheet_id = Column(Integer, primary_key=True, autoincrement=True)
    reel_size = Column(Float)
    cutting_size = Column(Float)
    sheet_size = Column(Float)  # reel_size * cutting_size
    per_sheet_weight_calc = Column(Float)
    gsm_calc = Column(Float)
    per_sheet_weight_act = Column(Float)
    number_of_sheets = Column(Integer)
    variation_in_weight = Column(Float)
    total_weight_calc = Column(Float)
    total_weight_act = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
