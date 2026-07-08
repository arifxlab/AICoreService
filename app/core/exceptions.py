"""
Application exceptions.
"""


class AIProviderError(Exception):
    """
    Raised when an AI provider fails.
    """

    def __init__(
        self,
        message: str,
        provider: str | None = None,
    ) -> None:
        self.message = message
        self.provider = provider

        super().__init__(
            message
        )