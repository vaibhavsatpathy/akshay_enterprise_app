from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class PlateSize(Base):
    __tablename__ = "plate_sizes"
    __table_args__ = {"extend_existing": True}
    plate_size_id = Column(Integer, primary_key=True, autoincrement=True)
    plate_size_value = Column(String)  # 19x25, 22x32, 23x36, 28x40, 36x52, 44x64
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
