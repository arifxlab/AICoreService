"""
Input validation guardrails.
"""

from app.ai.schemas.ai import AIRequest


class InputGuardrail:
    """
    Validates AI requests before they are sent
    to the language model.
    """

    MAX_PROMPT_LENGTH: int = 5000

    def validate(
        self,
        request: AIRequest,
    ) -> AIRequest:
        """
        Validate the incoming AI request.

        Raises:
            ValueError:
                If the prompt is empty or exceeds
                the maximum allowed length.
        """

        prompt = request.user_prompt.strip()

        if not prompt:
            raise ValueError("User prompt cannot be empty.")

        if len(prompt) > self.MAX_PROMPT_LENGTH:
            raise ValueError("User prompt exceeds the maximum allowed length.")

        return request
