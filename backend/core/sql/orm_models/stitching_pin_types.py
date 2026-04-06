from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class StitchingPinType(Base):
    __tablename__ = "stitching_pin_types"
    __table_args__ = {"extend_existing": True}
    pin_type_id = Column(Integer, primary_key=True, autoincrement=True)
    pin_type_value = Column(String)  # 17x25, 13x25, 12x25, 14x25
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
