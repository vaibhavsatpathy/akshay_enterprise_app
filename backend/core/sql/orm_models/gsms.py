from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class Gsm(Base):
    __tablename__ = "gsms"
    __table_args__ = {"extend_existing": True}
    gsm_id = Column(Integer, primary_key=True, autoincrement=True)
    gsm_value = Column(String)  # 120, 160, 180, 240, 350
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
