from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductReel(Base):
    __tablename__ = "product_reels"
    __table_args__ = {"extend_existing": True}
    reel_id = Column(Integer, primary_key=True, autoincrement=True)
    shade_id = Column(Integer, ForeignKey("shades.shade_id"))
    gsm_id = Column(Integer, ForeignKey("gsms.gsm_id"))
    bf_id = Column(Integer, ForeignKey("bfs.bf_id"))
    dimension_id = Column(Integer, ForeignKey("dimensions.dimension_id"))
    size = Column(Float)
    weight = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
