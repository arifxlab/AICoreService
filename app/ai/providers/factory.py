"""
Factory for creating AI providers.
"""

from app.ai.providers.base import AIProvider
from app.ai.providers.openrouter_provider import OpenRouterProvider
from app.core.settings import Settings

SUPPORTED_PROVIDER = "openrouter"


def create_ai_provider(settings: Settings) -> AIProvider:
    """
    Create and return the configured AI provider.

    Args:
        settings: Application settings.

    Returns:
        An initialized AI provider instance.

    Raises:
        ValueError: If the configured provider is not supported.
    """

    provider = settings.ai_provider.strip().lower()

    if provider == SUPPORTED_PROVIDER:
        return OpenRouterProvider(
            api_key=settings.openrouter_api_key,
            model=settings.ai_model,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
        )

    raise ValueError(
        f"Unsupported AI provider '{provider}'. "
        f"Supported providers: {SUPPORTED_PROVIDER}."
    )