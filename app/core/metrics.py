"""
Application metrics.
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    """
    Stores runtime application metrics.

    These metrics are updated throughout the application's
    lifecycle and exposed through the metrics endpoint.
    """

    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0

    tool_calls: int = 0
    provider_calls: int = 0

    total_latency_ms: float = 0.0

    @property
    def average_latency_ms(self) -> float:
        """
        Return the average provider request latency.

        Returns:
            Average latency in milliseconds rounded to
            two decimal places.
        """

        if self.provider_calls == 0:
            return 0.0

        return round(
            self.total_latency_ms / self.provider_calls,
            2,
        )


# Global metrics instance shared across the application.
metrics = Metrics()
