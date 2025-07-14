from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    config_item = Column(String(32), nullable=False)
    config_value = Column(String(255), nullable=False)
