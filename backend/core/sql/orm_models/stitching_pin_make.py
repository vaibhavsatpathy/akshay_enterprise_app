from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class StitchingPinMake(Base):
    __tablename__ = "stitching_pin_make"
    __table_args__ = {"extend_existing": True}
    make_id = Column(Integer, primary_key=True, autoincrement=True)
    make_value = Column(String)  # drum_type, coil_type
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
