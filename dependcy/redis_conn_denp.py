from db.redis_conn import redis_client
import redis
from typing import Any
from collections.abc import Generator


def depend_redis_conn() -> Generator[redis.Redis, Any, None]:
    redis_conn = redis_client.redis_conn
    try:
        yield redis_conn

    except Exception as e:
        raise redis.RedisError(f"Redis Database error: str({e})")

    finally:
        # 在使用连接池的情况下，Redis 连接在使用完毕后会自动释放回连接池，
        # 因此不需要在 finally 块中手动调用 redis_conn.close()。
        pass
