from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class FileType(Base):
    __tablename__ = "file_types"
    __table_args__ = {"extend_existing": True}
    file_type_id = Column(Integer, primary_key=True, autoincrement=True)
    file_type_value = Column(
        String
    )  # sale_file, voucher_file, purchase_file, bank_statement_file, others
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
