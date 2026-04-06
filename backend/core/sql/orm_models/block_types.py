from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class BlockType(Base):
    __tablename__ = "block_types"
    __table_args__ = {"extend_existing": True}
    block_type_id = Column(Integer, primary_key=True, autoincrement=True)
    block_type_value = Column(String)  # 3mm, 5mm
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
