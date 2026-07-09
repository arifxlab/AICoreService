"""
Shared request and response schemas used throughout the AI Core Service.
"""

from pydantic import BaseModel, Field


class AIRequest(BaseModel):
    """
    Represents a request sent to an AI provider.
    """

    system_prompt: str | None = Field(
        default=None,
        description="Optional system instruction provided to the language model.",
    )

    user_prompt: str = Field(
        ...,
        description="The user's input prompt.",
    )

    model: str = Field(
        ...,
        description="Identifier of the AI model to use.",
    )

    temperature: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description=(
            "Sampling temperature controlling response randomness. "
            "Lower values produce more deterministic outputs."
        ),
    )

    max_tokens: int = Field(
        default=1024,
        gt=0,
        description="Maximum number of tokens the model may generate.",
    )


class AIResponse(BaseModel):
    """
    Standardized response returned by an AI provider or tool.
    """

    content: str = Field(
        ...,
        description="Generated response content.",
    )

    provider: str = Field(
        ...,
        description="Provider that generated the response.",
    )

    model: str = Field(
        ...,
        description="Model that generated the response.",
    )

    stop_reason: str | None = Field(
        default=None,
        description="Reason generation stopped, if provided by the AI provider.",
    )