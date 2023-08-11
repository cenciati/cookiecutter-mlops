# pylint: disable=line-too-long
import logging
import logging.config
import os
import sys
from pathlib import Path
from typing import Any, Dict

from rich.logging import RichHandler

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = Path(BASE_DIR, '../__logs__')
LOGS_DIR.mkdir(parents=True, exist_ok=True)

LOG_HANLER: Dict[str, str] = {
    'stream': 'logging.StreamHandler',
    'rotating_file': 'logging.handlers.RotatingFileHandler',
}
TEN_MB_IN_BYTES: int = 10_485_760
BACKUP_COUNT: int = 10
FORMATTER_TYPE: str = 'detailed'

logging_config: Dict[str, Any] = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'minimal': {'format': '%(levelname)s | %(message)s'},
        'detailed': {
            'format': '%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n'
        },
    },
    'handlers': {
        'console': {
            'class': LOG_HANLER['stream'],
            'stream': sys.stdout,
            'formatter': 'minimal',
            'level': logging.DEBUG,
        },
        'info': {
            'class': LOG_HANLER['rotating_file'],
            'filename': Path(LOGS_DIR, 'info.log'),
            'maxBytes': TEN_MB_IN_BYTES,
            'backupCount': BACKUP_COUNT,
            'formatter': FORMATTER_TYPE,
            'level': logging.INFO,
        },
        'error': {
            'class': LOG_HANLER['rotating_file'],
            'filename': Path(LOGS_DIR, 'error.log'),
            'maxBytes': TEN_MB_IN_BYTES,
            'backupCount': BACKUP_COUNT,
            'formatter': FORMATTER_TYPE,
            'level': logging.ERROR,
        },
        'critical': {
            'class': LOG_HANLER['rotating_file'],
            'filename': Path(LOGS_DIR, 'critical.log'),
            'maxBytes': TEN_MB_IN_BYTES,
            'backupCount': BACKUP_COUNT,
            'formatter': FORMATTER_TYPE,
            'level': logging.CRITICAL,
        },
    },
    'root': {
        'handlers': ['console', 'info', 'error', 'critical'],
        'level': logging.INFO,
        'propagate': True,
    },
}

logging.config.dictConfig(logging_config)
logger: logging.Logger = logging.getLogger()
logger.handlers[0] = RichHandler(markup=True)
