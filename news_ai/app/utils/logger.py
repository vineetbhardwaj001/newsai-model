# app/utils/logger.py

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = "app.log"


def setup_logger(name: str = "news_ai", level=logging.INFO):
    """
    Setup application logger

    Features:
    - Console logging
    - File logging (rotating)
    - Clean formatting
    """

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate logs
    if logger.handlers:
        return logger

    # ======================
    # FORMAT
    # ======================
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ======================
    # CONSOLE HANDLER
    # ======================
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # ======================
    # FILE HANDLER (ROTATING)
    # ======================
    file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, LOG_FILE),
        maxBytes=5 * 1024 * 1024,   # 5MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # ======================
    # ADD HANDLERS
    # ======================
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# ======================
# GLOBAL LOGGER ACCESS
# ======================
logger = setup_logger()