"""
Output validation guardrails.
"""

from app.ai.schemas.ai import AIResponse


class OutputGuardrail:
    """
    Validates AI-generated responses before they are returned
    to the client.
    """

    MAX_RESPONSE_LENGTH: int = 10_000

    def validate(
        self,
        response: AIResponse,
    ) -> AIResponse:
        """
        Validate the AI response content.

        Ensures that:
        - The response is not empty.
        - The response does not exceed the maximum allowed length.
        - Whitespace is normalized before returning.
        """

        content = response.content.strip()

        if not content:
            raise ValueError(
                "AI response is empty."
            )

        if len(content) > self.MAX_RESPONSE_LENGTH:
            raise ValueError(
                "AI response exceeds the maximum allowed length."
            )

        response.content = content

        return response