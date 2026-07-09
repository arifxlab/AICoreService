"""
Custom application exceptions.
"""


class AIProviderError(Exception):
    """
    Raised when an AI provider request fails.
    """

    def __init__(
        self,
        message: str,
        provider: str | None = None,
    ) -> None:
        """
        Initialize the provider exception.

        Args:
            message: Human-readable error message.
            provider: Name of the AI provider that failed.
        """
        self.message: str = message
        self.provider: str | None = provider

        super().__init__(message)

    def __str__(self) -> str:
        """
        Return a readable exception message.
        """
        if self.provider:
            return f"[{self.provider}] {self.message}"

        return self.message
