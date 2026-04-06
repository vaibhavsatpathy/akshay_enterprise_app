from sqlalchemy import Column, String, Integer, DateTime, JSON, ForeignKey
from sql import Base


class PrintingJob(Base):
    __tablename__ = "printing_job"
    __table_args__ = {"extend_existing": True}
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    machine_used = Column(String)
    ordered_sheets = Column(Integer)
    actual_sheets = Column(Integer)
    employees = Column(JSON)  # [{"employee_name":"","id":""}]
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
