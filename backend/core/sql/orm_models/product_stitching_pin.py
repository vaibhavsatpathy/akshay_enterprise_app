from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductStitchingPin(Base):
    __tablename__ = "product_stitching_pin"
    __table_args__ = {"extend_existing": True}
    pin_id = Column(Integer, primary_key=True, autoincrement=True)
    pin_material_id = Column(Integer, ForeignKey("stitching_pin_material.material_id"))
    pin_type_id = Column(Integer, ForeignKey("stitching_pin_types.pin_type_id"))
    pin_make_id = Column(Integer, ForeignKey("stitching_pin_make.make_id"))
    rate_per_kg = Column(Float)
    weight_per_coil = Column(Float)
    number_of_coils = Column(Integer)
    total_weight_calc = Column(Float)
    total_weight_act = Column(Float)
    variation_in_weight = Column(Float)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
