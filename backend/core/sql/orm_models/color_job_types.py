from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class ColorJobType(Base):
    __tablename__ = "color_job_types"
    __table_args__ = {"extend_existing": True}
    color_job_type_id = Column(Integer, primary_key=True, autoincrement=True)
    color_job_type_value = Column(String)  # 1_color, 2_color, 3_color, 4_color
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
