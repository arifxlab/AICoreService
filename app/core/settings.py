from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    """

    app_name: str
    app_version: str
    environment: str
    debug: bool

    ai_provider: str
    openrouter_api_key: str

    ai_model: str
    temperature: float
    max_tokens: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.
    """
    return Settings()