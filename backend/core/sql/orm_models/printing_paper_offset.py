from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class PrintingPaperOffset(Base):
    __tablename__ = "printing_paper_offset"
    __table_args__ = {"extend_existing": True}
    print_id = Column(Integer, primary_key=True, autoincrement=True)
    paper_used_id = Column(Integer, ForeignKey("paper_types.paper_type_id"))
    dimension_id = Column(Integer, ForeignKey("dimensions.dimension_id"))
    length = Column(Float)
    width = Column(Float)
    total_area = Column(Float)
    number_of_paper = Column(Integer)
    per_paper_weight_calc = Column(Float)
    total_paper_weight_calc = Column(Float)
    number_of_color_job_id = Column(
        Integer, ForeignKey("color_job_types.color_job_type_id")
    )
    quantity_on_challan_received = Column(Integer)
    total_paper_weight_act = Column(Float)
    per_paper_weight_act = Column(Float)
    per_impression_charges = Column(Float)
    per_lamination_charges = Column(Float)
    variation_in_weight = Column(Float)
    total_weight_calc = Column(Float)
    total_weight_act = Column(Float)
    job_send_date = Column(DateTime)
    job_receive_date = Column(DateTime)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    party_id = Column(Integer, ForeignKey("party_table.party_id"))
    job_id = Column(Integer)
    printer_name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
