from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dishes(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    dish_name = Column(String(255), nullable=False, index=True, unique=True)
    ingredients_id = Column(Integer, nullable=False)
    taste_id = Column(Integer, nullable=False)
    series = Column(String(255), nullable=False, index=True)
    score = Column(Integer, nullable=False)
    free_choose = Column(Boolean, nullable=False)
