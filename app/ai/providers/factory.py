"""
AI provider factory.

Creates the correct AI provider based on application settings.
"""

from app.ai.providers.base import AIProvider
from app.ai.providers.openrouter_provider import OpenRouterProvider
from app.core.settings import Settings


def create_ai_provider(settings: Settings) -> AIProvider:
    """
    Create and return the configured AI provider.
    """

    if settings.ai_provider.lower() == "openrouter":
        return OpenRouterProvider(
            api_key=settings.openrouter_api_key,
            model=settings.ai_model,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
        )

    raise ValueError(
        f"Unsupported AI provider: {settings.ai_provider}"
    )