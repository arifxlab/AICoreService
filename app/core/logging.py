"""
Application logging configuration.
"""

import structlog


def configure_logging() -> None:
    """
    Configure structured logging.
    """

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(
                fmt="iso"
            ),
            structlog.processors.JSONRenderer(),
        ]
    )


def get_logger():
    """
    Return application logger.
    """

    return structlog.get_logger()