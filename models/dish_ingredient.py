from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DishIngredients(Base):
    __tablename__ = "dishes_ingredients"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dish_id = Column(Integer, nullable=False, index=True)  # ForeignKey("dishes.id")
    ingredient_id = Column(Integer, nullable=False)
