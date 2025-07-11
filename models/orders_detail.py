from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OrdersDetail(Base):
    __tablename__ = "orders_detail"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order_id = Column(Integer, nullable=False, index=True)  # ForeignKey("orders_master.id")
    dish_id = Column(Integer, nullable=False)  # ForeignKey("dishes.id")
    count = Column(Integer, nullable=False, default=1)
