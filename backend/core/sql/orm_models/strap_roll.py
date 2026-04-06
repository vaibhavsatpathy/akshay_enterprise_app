from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class StrapRoll(Base):
    __tablename__ = "strap_roll"
    __table_args__ = {"extend_existing": True}
    roll_id = Column(Integer, primary_key=True, autoincrement=True)
    roll_type_id = Column(Integer, ForeignKey("roll_types.roll_type_id"))
    dimension_id = Column(
        Integer, ForeignKey("dimensions.dimension_id")
    )  # default metres
    per_roll_length = Column(Float)
    number_of_rolls = Column(Integer)
    weight_per_roll = Column(Float)
    rate_per_roll = Column(Float)
    total_weight = Column(Float)
    total_length = Column(Float)
    rate_per_kg = Column(Float)
    rate_per_length = Column(Float)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
