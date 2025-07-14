from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = Column(String(16), nullable=False, index=True, unique=True)
    password = Column(String(32), nullable=False)
    user_role = Column(String(16), nullable=False)
    phone = Column(String(32), nullable=True)
