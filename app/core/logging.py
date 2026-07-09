"""
Application logging configuration.
"""

import structlog
from structlog.stdlib import LoggerFactory

_logger = None


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


def get_logger() -> structlog.BoundLogger:
    """
    Return the shared application logger.
    """

    global _logger

    if _logger is None:
        _logger = structlog.get_logger()

    return _logger
