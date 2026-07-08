"""
Input validation guardrails.
"""

from app.ai.schemas.ai import AIRequest


class InputGuardrail:
    """
    Validates incoming AI requests.
    """

    MAX_PROMPT_LENGTH = 5000

    def validate(
        self,
        request: AIRequest,
    ) -> AIRequest:
        """
        Validate user input before sending to AI.
        """

        if not request.user_prompt.strip():
            raise ValueError(
                "User prompt cannot be empty."
            )

        if len(request.user_prompt) > self.MAX_PROMPT_LENGTH:
            raise ValueError(
                "User prompt exceeds maximum length."
            )

        return request