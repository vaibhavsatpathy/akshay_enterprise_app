from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class OffsetPlate(Base):
    __tablename__ = "offset_plate"
    __table_args__ = {"extend_existing": True}
    plate_id = Column(Integer, primary_key=True, autoincrement=True)
    plate_type_id = Column(Integer, ForeignKey("plate_types.plate_type_id"))
    plate_size_id = Column(Integer, ForeignKey("plate_sizes.plate_size_id"))
    number_of_units = Column(Integer)
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
    printer_name = Column(String)
    paper_size_length = Column(Float)
    paper_size_width = Column(Float)
    paper_used_id = Column(Integer, ForeignKey("paper_types.paper_type_id"))
    gsm_id = Column(Integer, ForeignKey("gsms.gsm_id"))
    bf_id = Column(Integer, ForeignKey("bfs.bf_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
