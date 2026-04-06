from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sql import Base


class FilePlacing(Base):
    __tablename__ = "file_placing"
    __table_args__ = {"extend_existing": True}
    file_id = Column(Integer, primary_key=True, autoincrement=True)
    file_type_id = Column(Integer, ForeignKey("file_types.file_type_id"))
    year = Column(Integer)
    file_number = Column(Integer)
    point_of_contact = Column(String)  # potentially an employee name drop down
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
