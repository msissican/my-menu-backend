from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserExtend(Base):
    __tablename__ = "user_extend"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
