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
        default="AI Core Service",
        description="Application name.",
    )

    app_version: str = Field(
        default="0.1.0",
        description="Application version.",
    )

    environment: str = Field(
        default="development",
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
        default="openrouter",
        description="Configured AI provider.",
    )

    openrouter_api_key: str = Field(
        default="dummy-key",
        description="OpenRouter API key.",
    )

    # ---------------------------------------------------------
    # Model Configuration
    # ---------------------------------------------------------

    ai_model: str = Field(
        default="openai/gpt-4.1-mini",
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
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Return the cached application settings.

    Settings are loaded once and reused throughout the
    application's lifetime.
    """

    # MyPy cannot infer that BaseSettings loads values
    # from environment variables at runtime.
    return Settings()
