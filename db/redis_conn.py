from contextlib import contextmanager
from typing import Any, Generator

import redis

# 创建 redis 连接池
pool = redis.ConnectionPool(host="localhost", port=6379, db=0)


class RedisClient:
    def __init__(self) -> None:
        self.pool = redis.ConnectionPool(
            host="localhost",
            port=6379,
            db=0,
            max_connections=20,
            decode_responses=True,
        )
        self.redis_conn = redis.Redis(connection_pool=self.pool)

    def get_connection(self) -> redis.Redis:
        if self.pool is None:
            raise RuntimeError("Redis Connection Pool Not Initialized")
        return redis.Redis(connection_pool=self.pool)

    def close_pool(self):
        if self.pool:
            self.pool.disconnect()
            self.pool = None


print("redis connection create")
redis_client = RedisClient()


@contextmanager
def context_redis_conn() -> Generator[redis.Redis, Any, None]:
    redis_conn = redis_client.get_connection()
    try:
        yield redis_conn

    except Exception as e:
        raise redis.RedisError(f"Redis Database error: str({e})")

    finally:
        pass
