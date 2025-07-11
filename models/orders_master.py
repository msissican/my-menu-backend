from sqlalchemy import Boolean, Column, Date, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OrdersMaster(Base):
    __tablename__ = "orders_master"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # ForeignKey("user.id")
    dining_table = Column(Integer, nullable=False)
    complete = Column(Boolean, default=False, nullable=False, index=True)
    order_time = Column(Date, nullable=False)
    complete_time = Column(Date)
