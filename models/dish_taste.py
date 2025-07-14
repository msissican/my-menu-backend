from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DishTaste(Base):
    __tablename__ = "dishes_tastes"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dish_id = Column(Integer, nullable=False, index=True)
    taste_id = Column(Integer, nullable=False)
