from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sql import Base


class BlockPrintColor(Base):
    __tablename__ = "block_print_colors"
    __table_args__ = {"extend_existing": True}
    color_id = Column(Integer, primary_key=True, autoincrement=True)
    color_name = Column(String)
    job_id = Column(Integer, ForeignKey("product_block_printing.print_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
