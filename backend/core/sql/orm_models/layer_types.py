from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class LayerType(Base):
    __tablename__ = "layer_types"
    __table_args__ = {"extend_existing": True}
    layer_type_id = Column(Integer, primary_key=True, autoincrement=True)
    layer_type_value = Column(String)  # top, flute, plain, flute_1, plain_1, etc.
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
