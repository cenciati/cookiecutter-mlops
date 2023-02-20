# pylint: disable=line-too-long
# flake8: noqa
import logging
import logging.config
import os
import sys
from logging import Logger
from pathlib import Path
from typing import Any, Dict

from rich.logging import RichHandler

BASE_DIR: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logging_config: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(levelname)s | %(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "maxBytes": 10485760,
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
        "critical": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "critical.log"),
            "maxBytes": 10485760,
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.CRITICAL,
        },
    },
    "root": {
        "handlers": ["console", "info", "error", "critical"],
        "level": logging.INFO,
        "propagate": True,
    },
}

logging.config.dictConfig(logging_config)
logger: Logger = logging.getLogger()
logger.handlers[0] = RichHandler(markup=True)
