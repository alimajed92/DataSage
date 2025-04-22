import logging
import colorlog
import os
from datetime import datetime


def setup_logger():
    base_log_dir = "logs"
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    logger = logging.getLogger("AI_Agent")

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)

    # Console Handler with Colors
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)
    c_formatter = colorlog.ColoredFormatter(
        "%(asctime)s - %(name)s - %(log_color)s%(levelname)s - %(message)s%(reset)s",
        log_colors={
            "DEBUG": "blue",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    c_handler.setFormatter(c_formatter)
    logger.addHandler(c_handler)

    # Separate file handlers per log level
    for level_name, level_value in log_levels.items():
        log_subdir = os.path.join(base_log_dir, level_name.lower())
        os.makedirs(log_subdir, exist_ok=True)
        log_filename = os.path.join(
            log_subdir, datetime.now().strftime("%Y-%m-%d") + ".log"
        )

        f_handler = logging.FileHandler(log_filename)
        f_handler.setLevel(logging.DEBUG)  # Handle all and filter later

        f_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        f_handler.setFormatter(f_formatter)

        # Custom filter to match only this exact level
        class ExactLevelFilter(logging.Filter):
            def __init__(self, level):
                super().__init__()
                self.level = level

            def filter(self, record):
                return record.levelno == self.level

        f_handler.addFilter(ExactLevelFilter(level_value))
        logger.addHandler(f_handler)

    return logger


ai_agent_logger = setup_logger()
