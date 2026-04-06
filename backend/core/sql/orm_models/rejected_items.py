from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class RejectedItem(Base):
    __tablename__ = "rejected_items"
    __table_args__ = {"extend_existing": True}
    rejected_id = Column(Integer, primary_key=True, autoincrement=True)
    item_type_id = Column(
        Integer, ForeignKey("rejected_item_types.rejected_item_type_id")
    )
    box_type_id = Column(Integer, ForeignKey("box_types.box_type_id"))
    dimension_id = Column(Integer, ForeignKey("dimensions.dimension_id"))
    length = Column(Float)
    breadth = Column(Float)
    height = Column(Float)
    ply = Column(String)
    plain_or_printed = Column(String)
    number_of_boxes_per_bundles = Column(Integer)
    number_of_bundles = Column(Integer)
    total_boxes = Column(Integer)
    rate_per_box = Column(Float)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    party_id = Column(Integer, ForeignKey("party_table.party_id"))
    job_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
