from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sql import Base


class AppConfig(Base):
    __tablename__ = "app_config"
    __table_args__ = {"extend_existing": True}
    config_id = Column(Integer, autoincrement=True)
    config_parameter = Column(String, primary_key=True)
    config_value = Column(String)
    creds = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
