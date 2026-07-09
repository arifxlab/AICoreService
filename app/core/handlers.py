"""
Custom FastAPI exception handlers.
"""

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AIProviderError


async def ai_provider_exception_handler(
    _request: Request,
    exc: AIProviderError,
) -> JSONResponse:
    """
    Handle AI provider failures.

    Returns a standardized JSON response whenever an
    AI provider request cannot be completed.
    """

    return JSONResponse(
        status_code=503,
        content={
            "error": "AI_PROVIDER_ERROR",
            "message": exc.message,
            "provider": exc.provider,
        },
    )