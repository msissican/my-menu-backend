from contextlib import asynccontextmanager

import redis
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from dependcy.mysql_conn_denp import depend_mysql_session
from dependcy.redis_conn_denp import depend_redis_conn


@asynccontextmanager
async def lifespan(app: FastAPI):
    from db.mysql_conn import engine
    from db.redis_conn import redis_client

    yield

    engine.dispose()
    redis_client.close_pool()
    print("db engine close")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return JSONResponse(content={"message": "ok"}, status_code=200)


@app.get("/api/test-db")
def test_db(
    mysql_session: Session = Depends(depend_mysql_session),
    redis_conn: redis.Redis = Depends(depend_redis_conn),
):
    from sqlalchemy import text

    statement = text("select 1 from dual;")
    result = mysql_session.execute(statement).mappings().all()
    mysql_result = dict(result[0])

    redis_conn.set("test_key", "test_value")
    redis_result = redis_conn.get("test_key")

    return JSONResponse(
        content={
            "mysql_conn": mysql_result,
            "redis_conn": redis_result,
        },
        status_code=200,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
