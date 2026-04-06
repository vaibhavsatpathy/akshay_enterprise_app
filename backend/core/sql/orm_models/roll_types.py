from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class RollType(Base):
    __tablename__ = "roll_types"
    __table_args__ = {"extend_existing": True}
    roll_type_id = Column(Integer, primary_key=True, autoincrement=True)
    roll_type_value = Column(String)  # 5mm, 6mm, 8mm, 10mm
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
