from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Bf(Base):
    __tablename__ = "bfs"
    __table_args__ = {"extend_existing": True}
    bf_id = Column(Integer, primary_key=True, autoincrement=True)
    bf_value = Column(String)  # 80, 120
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
