from sqlalchemy import Column, String, Integer, DateTime
from sql import Base


class PrintPlainStyle(Base):
    __tablename__ = "print_plain_style"
    __table_args__ = {"extend_existing": True}
    print_plain_style_id = Column(Integer, primary_key=True, autoincrement=True)
    print_plain_style_value = Column(String)  # plain, printed
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
