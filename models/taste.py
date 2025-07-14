from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Taste(Base):
    __tablename__ = "tastes"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    taste = Column(String(255), nullable=False, unique=True)
