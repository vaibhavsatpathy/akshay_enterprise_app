from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class UnitType(Base):
    __tablename__ = "unit_types"
    __table_args__ = {"extend_existing": True}
    unit_type_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_type_value = Column(
        String
    )  # liter, kilogram, pouch, drum, single_numbers, set_numbers, bundle, roll
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
