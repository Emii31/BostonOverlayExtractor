from __future__ import annotations

"""
Boston Overlay Extractor

Logging utilities.

Provides a centralized logging system for both console and file output.
"""

import logging
from pathlib import Path

from rich.logging import RichHandler

from boe.core.constants import (
    DATE_FORMAT,
    DEFAULT_LOG_LEVEL,
    LOG_FILENAME,
    LOG_FORMAT,
)

_INITIALIZED = False


def initialize_logger(log_directory: Path) -> None:
    """
    Configure the application's logging system.

    This function should only be called once during application startup.

    Parameters
    ----------
    log_directory
        Directory where the log file will be written.
    """

    global _INITIALIZED

    if _INITIALIZED:
        return

    log_directory.mkdir(parents=True, exist_ok=True)

    log_file = log_directory / LOG_FILENAME

    root_logger = logging.getLogger()

    root_logger.setLevel(DEFAULT_LOG_LEVEL)

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    file_handler = logging.FileHandler(
        filename=log_file,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        show_path=False,
    )

    console_handler.setFormatter(
        logging.Formatter("%(message)s")
    )

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    _INITIALIZED = True


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Parameters
    ----------
    name
        Logger name, normally __name__.

    Returns
    -------
    logging.Logger
    """

    return logging.getLogger(name)
