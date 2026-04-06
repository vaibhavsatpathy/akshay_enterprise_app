from sqlalchemy import Column, Integer, DateTime, JSON, ForeignKey
from sql import Base


class DiePunchingJob(Base):
    __tablename__ = "die_punching_job"
    __table_args__ = {"extend_existing": True}
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    ordered_sheets = Column(Integer)
    actual_sheets = Column(Integer)
    employees = Column(JSON)  # [{"employee_name":"","id":""}]
    no_of_boxes_per_sheet = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
