"""
Factory for creating AI providers.
"""

from app.ai.providers.base import AIProvider
from app.ai.providers.openrouter_provider import OpenRouterProvider
from app.core.settings import Settings


def create_ai_provider(settings: Settings) -> AIProvider:
    """
    Create the configured AI provider.
    """

    provider = settings.ai_provider.lower()

    if provider == "openrouter":
        return OpenRouterProvider(
            api_key=settings.openrouter_api_key,
            model=settings.ai_model,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
        )

    raise ValueError(
        f"Unsupported AI provider: {provider}"
    )