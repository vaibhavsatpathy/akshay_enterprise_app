from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class DispatchTable(Base):
    __tablename__ = "dispatch_table"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders_table.order_id"))
    rate_per_box = Column(Float)
    units_requested = Column(Integer)
    units_dispatched = Column(Integer)
    units_pending = Column(Integer)
    created_by = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
