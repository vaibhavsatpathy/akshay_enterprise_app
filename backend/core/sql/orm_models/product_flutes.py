from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sql import Base


class ProductFlute(Base):
    __tablename__ = "product_flutes"
    __table_args__ = {"extend_existing": True}
    flute_id = Column(Integer, primary_key=True, autoincrement=True)
    layer_type_id = Column(Integer, ForeignKey("layer_types.layer_type_id"))
    flute_type_id = Column(Integer, ForeignKey("flute_types.flute_type_id"))
    flute_percent = Column(Float)
    layer_gsm_id = Column(Integer, ForeignKey("gsms.gsm_id"))
    layer_bf_id = Column(Integer, ForeignKey("bfs.bf_id"))
    sheet_id = Column(Integer, ForeignKey("product_ply_sheets.sheet_id"))
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
