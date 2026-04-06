from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Location(Base):
    __tablename__ = "locations"
    __table_args__ = {"extend_existing": True}
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    location_name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
