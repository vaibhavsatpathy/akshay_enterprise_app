from sqlalchemy import Column, String, Integer, DateTime, JSON, ForeignKey
from sql import Base


class PaperCuttingJob(Base):
    __tablename__ = "paper_cutting_job"
    __table_args__ = {"extend_existing": True}
    job_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    ordered_sheets = Column(Integer)
    actual_sheets = Column(Integer)
    employees = Column(JSON)  # [{"employee_name":"","id":""}]
    fluting_paper_gsm = Column(Integer)
    fluting_paper_bf = Column(Integer)
    plain_paper_gsm = Column(Integer)
    plain_paper_bf = Column(Integer)
    reels_used = Column(JSON)  # [{"reel_id":""}]
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
