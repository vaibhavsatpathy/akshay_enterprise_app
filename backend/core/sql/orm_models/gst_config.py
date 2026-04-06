from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class GstConfig(Base):
    __tablename__ = "gst_config"
    __table_args__ = {"extend_existing": True}
    gst_config_id = Column(Integer, primary_key=True, autoincrement=True)
    gst_value = Column(String)  # 0, 5, 12, 18, 28
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
