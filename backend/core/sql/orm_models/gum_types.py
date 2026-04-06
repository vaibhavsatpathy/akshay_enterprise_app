from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class GumType(Base):
    __tablename__ = "gum_types"
    __table_args__ = {"extend_existing": True}
    gum_type_id = Column(Integer, primary_key=True, autoincrement=True)
    gum_type_value = Column(String)  # pasting_gum, corrugation_gum, side_pasting_gum
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
