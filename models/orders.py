from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, nullable=False, index=True)
    dining_table = Column(Integer, nullable=False, index=True)
    complete = Column(Boolean, default=False, nullable=False)
    dish_id = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False, default=1)
