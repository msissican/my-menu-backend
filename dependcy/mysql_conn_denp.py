from collections.abc import Generator
from typing import Any

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from db.mysql_conn import SessionLocal


def depend_mysql_session() -> Generator[Session, Any, None]:
    db_session = SessionLocal()
    try:
        yield db_session

    except Exception as e:
        db_session.rollback()
        raise SQLAlchemyError(f"MySQL Database error: str({e})")

    finally:
        db_session.close()
