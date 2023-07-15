import inspect
import logging
import os
from typing import Optional


class _CustomFormatter(logging.Formatter):
    reset = "\x1b[0m"
    bold_red = "\x1b[31;1m"
    grey = "\x1b[0;37m"
    green = "\x1b[1;32m"
    yellow = "\x1b[1;33m"
    red = "\x1b[1;31m"
    purple = "\x1b[1;35m"
    blue = "\x1b[1;34m"
    light_blue = "\x1b[1;36m"
    reset = "\x1b[0m"
    blink_red = "\x1b[5m\x1b[1;31m"

    format = "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
    date = "%Y-%m-%d %H:%M:%S"

    FORMATS = {
        logging.DEBUG: purple + format + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.date)
        return formatter.format(record)


def generate_logger(name: Optional[str] = None):
    if not name:
        caller_frame = inspect.stack()[1]
        caller_filename_full = caller_frame.filename.split("/")
        module = caller_filename_full[-2] + "."
        if module == "app.":
            module = ""
        name = os.path.splitext(caller_filename_full[-1])[0]
        name = module + name

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(_CustomFormatter())

    logger.addHandler(ch)
    return logger
