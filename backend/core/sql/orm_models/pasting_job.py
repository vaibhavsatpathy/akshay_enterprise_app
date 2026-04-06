from sqlalchemy import Column, String, Integer, DateTime, Float, JSON, ForeignKey
from sql import Base


class PastingJob(Base):
    __tablename__ = "pasting_job"
    __table_args__ = {"extend_existing": True}
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    machine_used = Column(String)
    ordered_sheets = Column(Integer)
    actual_sheets = Column(Integer)
    employees = Column(JSON)  # [{"employee_name":"","id":""}]
    pu_steel_roll = Column(String)
    pressure_roll = Column(Float)
    gum_roll = Column(Float)
    humidity = Column(Float)
    gum_type = Column(String)  # mix ratio from gum inventory
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
