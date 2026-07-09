"""
Application logging configuration.
"""

from typing import cast

import structlog
from structlog.stdlib import BoundLogger, LoggerFactory

_logger: BoundLogger | None = None


def configure_logging() -> None:
    """
    Configure structured application logging.
    """

    structlog.configure(
        logger_factory=LoggerFactory(),
        processors=[
            structlog.processors.TimeStamper(
                fmt="iso",
            ),
            structlog.processors.JSONRenderer(),
        ],
    )


def get_logger() -> BoundLogger:
    """
    Return the shared application logger.
    """

    global _logger

    if _logger is None:
        _logger = cast(BoundLogger, structlog.get_logger())

    return _logger
