from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class BundlingRope(Base):
    __tablename__ = "bundling_rope"
    __table_args__ = {"extend_existing": True}
    bundle_id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_bundles = Column(Integer)
    weight_per_bundle = Column(Float)
    rate_per_bundle = Column(Float)
    total_weight = Column(Float)
    rate_per_kg = Column(Float)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
