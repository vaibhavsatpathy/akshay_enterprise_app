from sqlalchemy import Column, Integer, DateTime, JSON, ForeignKey
from sql import Base


class BundelingJob(Base):
    __tablename__ = "bundeling_job"
    __table_args__ = {"extend_existing": True}
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    no_of_boxes_per_bundle = Column(Integer)
    no_of_bundles = Column(Integer)
    total_bundled_boxes = Column(Integer)
    boxes_left_outside_bundle = Column(Integer)
    total_boxes = Column(Integer)
    employees = Column(JSON)  # [{"employee_name":"","id":""}]
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
