"""
Schemas shared across the AI Core Service.
"""

from pydantic import BaseModel, Field


class AIRequest(BaseModel):
    """
    Request sent to an AI provider.
    """

    system_prompt: str | None = Field(
        default=None,
        description="Optional system prompt.",
    )

    user_prompt: str = Field(
        ...,
        description="User prompt.",
    )

    model: str = Field(
        ...,
        description="Model name.",
    )

    temperature: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Sampling temperature.",
    )

    max_tokens: int = Field(
        default=1024,
        gt=0,
        description="Maximum response tokens.",
    )


class AIResponse(BaseModel):
    """
    Standard AI response.
    """

    content: str

    provider: str

    model: str

    stop_reason: str | None = None