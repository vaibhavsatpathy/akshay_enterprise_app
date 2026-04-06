from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from sql import Base


class UserRole(Base):
    __tablename__ = "user_roles"
    __table_args__ = {"extend_existing": True}
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String)  # admin, manager, labor
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    users = relationship("User", cascade="all,delete", backref="user_roles")
