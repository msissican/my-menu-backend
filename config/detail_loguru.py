from loguru import logger as detail_logger

detail_logger.add(
    "logs/detail_{time: YYYY-MM-DD}.log",
    level="INFO",
    rotation="00:00",
    retention="7 days",
    encoding="utf-8",
    enqueue=True,
)


if __name__ == "__main__":
    detail_logger.debug({"log": "log debug"})
    detail_logger.info({"log": "log info"})
    detail_logger.warning({"log": "log warning"})
    detail_logger.error({"log": "log error"})
