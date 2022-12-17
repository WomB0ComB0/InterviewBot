import logging
import time
import uuid


def generate_uuid() -> str:
    return uuid.uuid4().hex


def time_now() -> int:
    return int(time.time())


# build and return a new logger instance
def new_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(stream_handler)
    return logger
