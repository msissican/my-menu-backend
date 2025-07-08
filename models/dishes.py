from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    dish_name = Column(String(255), nullable=False, index=True)
    ingredients_id = Column(Integer, nullable=False)
    cuisine = Column(String(255), nullable=False, index=True)
    score = Column(Integer, nullable=False)
