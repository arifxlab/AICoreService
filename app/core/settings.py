"""
Application configuration.

Loads settings from the environment and caches them for the
lifetime of the application.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application configuration.
    """

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    app_name: str = Field(
        description="Application name.",
    )

    app_version: str = Field(
        description="Application version.",
    )

    environment: str = Field(
        description="Deployment environment.",
    )

    debug: bool = Field(
        default=False,
        description="Enable debug mode.",
    )

    # ---------------------------------------------------------
    # AI Provider
    # ---------------------------------------------------------

    ai_provider: str = Field(
        description="Configured AI provider.",
    )

    openrouter_api_key: str = Field(
        description="OpenRouter API key.",
    )

    # ---------------------------------------------------------
    # Model Configuration
    # ---------------------------------------------------------

    ai_model: str = Field(
        description="Default AI model.",
    )

    temperature: float = Field(
        default=0.0,
        description="Model temperature.",
    )

    max_tokens: int = Field(
        default=512,
        description="Maximum response tokens.",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Return the cached application settings.

    Settings are loaded from environment variables only once.
    """

    # mypy cannot understand that BaseSettings reads values
    # from the environment at runtime.
    return Settings()  # type: ignore[call-arg]
