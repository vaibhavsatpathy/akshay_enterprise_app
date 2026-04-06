from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class Inventory(Base):
    __tablename__ = "inventory"
    __table_args__ = {"extend_existing": True}
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_number = Column(Integer)
    vendor_id = Column(Integer, ForeignKey("vendors.vendor_id"))
    entry_date = Column(DateTime)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    transporter_id = Column(Integer, ForeignKey("transporters.transporter_id"))
    vehicle_number = Column(String)
    vehicle_type = Column(String)
    driver_name = Column(String)
    freight_charges = Column(Float)
    basic_cost_of_material = Column(Float)
    total_weight_kg = Column(Float)
    per_kg_freight_charges = Column(Float)
    per_kg_cost_of_material = Column(Float)
    total_cost_of_material = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
