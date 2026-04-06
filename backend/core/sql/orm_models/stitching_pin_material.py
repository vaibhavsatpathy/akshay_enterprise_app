from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class StitchingPinMaterial(Base):
    __tablename__ = "stitching_pin_material"
    __table_args__ = {"extend_existing": True}
    material_id = Column(Integer, primary_key=True, autoincrement=True)
    material_value = Column(String)  # steel, rustproof, silver, copper, brass
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
