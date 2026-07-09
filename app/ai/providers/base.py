"""
Provider interface for AI model integrations.
"""

from typing import Protocol, runtime_checkable

from app.ai.schemas.ai import AIRequest, AIResponse


@runtime_checkable
class AIProvider(Protocol):
    """
    Defines the contract that every AI provider implementation
    must follow.
    """

    async def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """
        Generate a response from the configured AI model.

        Args:
            request: The AI request containing prompts and
                generation parameters.

        Returns:
            An AIResponse containing the generated output.
        """
        ...
