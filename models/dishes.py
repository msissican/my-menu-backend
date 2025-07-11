from sqlalchemy import FLOAT, Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dishes(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dish_name = Column(String(255), nullable=False, index=True, unique=True)
    series = Column(String(255), nullable=False)
    score = Column(FLOAT, nullable=False, default=0.0)
    free_choose = Column(Boolean, nullable=False)
