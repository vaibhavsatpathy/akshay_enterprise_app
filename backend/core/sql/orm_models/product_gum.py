from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductGum(Base):
    __tablename__ = "product_gum"
    __table_args__ = {"extend_existing": True}
    gum_id = Column(Integer, primary_key=True, autoincrement=True)
    gum_name = Column(String)
    gum_type_id = Column(Integer, ForeignKey("gum_types.gum_type_id"))
    unit_type_id = Column(Integer, ForeignKey("unit_types.unit_type_id"))
    number_of_units = Column(Integer)
    rate_per_unit = Column(Float)
    weight_per_bag = Column(Float)
    ratio_prescribed = Column(String)
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
