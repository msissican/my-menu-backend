from loguru import logger as request_logger

request_logger.add(
    "logs/request_{time: YYYY-MM-DD}.log",
    level="INFO",
    rotation="00:00",
    retention="7 days",
    encoding="utf-8",
    enqueue=True,
)


if __name__ == "__main__":
    request_logger.debug({"log": "log debug"})
    request_logger.info({"log": "log info"})
    request_logger.warning({"log": "log warning"})
    request_logger.error({"log": "log error"})
