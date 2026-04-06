from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class ColorTable(Base):
    __tablename__ = "color_table"
    __table_args__ = {"extend_existing": True}
    color_id = Column(Integer, primary_key=True, autoincrement=True)
    color_shade = Column(String)
    color_shade_number = Column(String)  # hex value
    number_of_liters = Column(Integer)
    rate_per_liter = Column(Float)
    total_weight = Column(Float)
    rate_per_kg = Column(Float)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
