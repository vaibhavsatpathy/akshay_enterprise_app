from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class FluteType(Base):
    __tablename__ = "flute_types"
    __table_args__ = {"extend_existing": True}
    flute_type_id = Column(Integer, primary_key=True, autoincrement=True)
    flute_type_value = Column(String)  # a, b, c, d, e, f
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
