from sqlalchemy import Column, String, Integer, DateTime, JSON, ForeignKey
from sql import Base


class StitchingJob(Base):
    __tablename__ = "stitching_job"
    __table_args__ = {"extend_existing": True}
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    no_of_pins_used = Column(Integer)
    box_size = Column(JSON)  # {Lxbxh} dropdown - maybe from job details or small/large
    stitching_coil_used = Column(Integer)  # barcode entry??
    no_of_boxes = Column(Integer)
    machine_used = Column(String)
    ordered_sheets = Column(Integer)
    actual_sheets = Column(Integer)
    employees = Column(JSON)  # [{"employee_name":"","id":""}]
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
