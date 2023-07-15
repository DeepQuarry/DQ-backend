import time
from logging import Logger
from typing import Optional

import requests
from core.log import generate_logger


def retry_request(
    url: str,
    default_retry_time: float,
    max_retries: int,
    logger: Logger = generate_logger(),
) -> Optional[requests.Response]:
    r = requests.get(url)
    if r.status_code == 429:
        retry_counter = 0
        while r.status_code == 429:
            logger.warn("Too many requests sent. Retrying in 60 seconds")
            try:
                retry_after = int(r.headers["retry-after"])
            except:
                retry_after = default_retry_time
            time.sleep(retry_after)
            r = requests.get(url)
            retry_counter += 1

            if retry_counter == max_retries:
                logger.error("Max crawler retries reached on page: %s", url)
                return False

    elif r.status_code == 404:
        logger.warn("Invalid URL: %s", url)
        return None

    return r
