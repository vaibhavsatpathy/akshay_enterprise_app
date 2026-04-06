from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductBlockPrinting(Base):
    __tablename__ = "product_block_printing"
    __table_args__ = {"extend_existing": True}
    print_id = Column(Integer, primary_key=True, autoincrement=True)
    block_type_id = Column(Integer, ForeignKey("block_types.block_type_id"))
    length = Column(Float)
    width = Column(Float)
    total_area = Column(Float)
    number_of_blocks = Column(Integer)
    rate_per_unit = Column(Float)
    number_of_color_job_id = Column(
        Integer, ForeignKey("color_job_types.color_job_type_id")
    )
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    party_id = Column(Integer, ForeignKey("party_table.party_id"))
    job_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
