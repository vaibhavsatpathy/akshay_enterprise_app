from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class BindingCloth(Base):
    __tablename__ = "binding_cloth"
    __table_args__ = {"extend_existing": True}
    cloth_id = Column(Integer, primary_key=True, autoincrement=True)
    color_shade = Column(String)
    cloth_type_id = Column(Integer, ForeignKey("unit_types.unit_type_id"))
    rate_per_unit = Column(Float)
    number_of_units = Column(Integer)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
