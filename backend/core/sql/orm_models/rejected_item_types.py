from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class RejectedItemType(Base):
    __tablename__ = "rejected_item_types"
    __table_args__ = {"extend_existing": True}
    rejected_item_type_id = Column(Integer, primary_key=True, autoincrement=True)
    rejected_item_type_value = Column(String)  # paper, sheet, boxes
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
