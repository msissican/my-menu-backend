from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ingredients(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ingredient = Column(String(255), nullable=False, unique=True)
    has = Column(Boolean, nullable=False)
    count = Column(Integer, nullable=False)
    in_refrigerator = Column(Boolean, nullable=False)
