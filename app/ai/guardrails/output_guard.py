"""
Output validation guardrails.
"""

from app.ai.schemas.ai import AIResponse


class OutputGuardrail:
    """
    Validates AI responses.
    """

    MAX_RESPONSE_LENGTH = 10000

    def validate(
        self,
        response: AIResponse,
    ) -> AIResponse:
        """
        Validate AI output.
        """

        if not response.content.strip():
            raise ValueError(
                "AI response is empty."
            )

        if len(response.content) > self.MAX_RESPONSE_LENGTH:
            raise ValueError(
                "AI response exceeds limit."
            )

        return response