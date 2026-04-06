from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sql import Base


class ScreenPrinting(Base):
    __tablename__ = "screen_printing"
    __table_args__ = {"extend_existing": True}
    print_id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_tracings = Column(Integer)
    number_of_colors = Column(Integer)
    colors_used = Column(String)
    total_base_cost = Column(Float)
    total_gst_cost = Column(Float)
    total_cost = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    party_id = Column(Integer, ForeignKey("party_table.party_id"))
    job_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
