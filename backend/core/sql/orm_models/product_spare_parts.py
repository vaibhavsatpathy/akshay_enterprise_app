from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductSparePart(Base):
    __tablename__ = "product_spare_parts"
    __table_args__ = {"extend_existing": True}
    part_id = Column(Integer, primary_key=True, autoincrement=True)
    part_name = Column(String)
    unit_type_id = Column(Integer, ForeignKey("unit_types.unit_type_id"))
    number_of_units = Column(Integer)
    rate_per_unit = Column(Float)
    reference_machine = Column(String)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
