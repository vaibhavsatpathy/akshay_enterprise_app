from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sql import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False)
    full_name = Column(String)
    password = Column(String, nullable=False)
    email_id = Column(String)
    role_id = Column(Integer, ForeignKey("user_roles.role_id"), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
