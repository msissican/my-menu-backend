from contextlib import contextmanager
from typing import Any, Generator

import redis

# 创建 redis 连接池
pool = redis.ConnectionPool(host="localhost", port=6379, db=0)


class RedisConn:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 6379
        self.db = 0
        self.pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db,
            decode_responses=True,
        )
        self.redis_conn = redis.Redis(connection_pool=self.pool)


redis_client = RedisConn()


@contextmanager
def context_redis_conn() -> Generator[redis.Redis, Any, None]:
    redis_conn = redis_client.redis_conn
    try:
        yield redis_conn

    except Exception as e:
        raise redis.RedisError(f"Redis Database error: str({e})")

    finally:
        pass
