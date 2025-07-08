from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from config.settings import get_settings

settings = get_settings()

DATABASE_URL = (
    f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=5,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,  # need session.commit() to save changes
    autoflush=False,  # need session.flush() or session.commit() to send change to database
    expire_on_commit=False,  # expire object after commit
    future=True,  # use the SQLAlchemy 2.0 API
)


@contextmanager
def context_mysql_session() -> Generator[Session, Any, None]:
    db_session = SessionLocal()
    try:
        yield db_session

    except Exception as e:
        db_session.rollback()
        raise SQLAlchemyError(f"MySQL Database error: str({e})")

    finally:
        db_session.close()
