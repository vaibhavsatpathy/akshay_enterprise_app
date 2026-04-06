from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class PlateType(Base):
    __tablename__ = "plate_types"
    __table_args__ = {"extend_existing": True}
    plate_type_id = Column(Integer, primary_key=True, autoincrement=True)
    plate_type_value = Column(String)  # normal, thermal
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
