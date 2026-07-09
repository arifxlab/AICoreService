"""
Metrics endpoint.
"""

from fastapi import APIRouter

from app.core.metrics import metrics

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.get("/")
async def get_metrics() -> dict[str, int | float]:
    """
    Return application metrics.

    Provides basic runtime statistics including request counts,
    tool usage, provider usage, and average provider latency.
    """

    return {
        "total_requests": metrics.total_requests,
        "successful_requests": metrics.successful_requests,
        "failed_requests": metrics.failed_requests,
        "tool_calls": metrics.tool_calls,
        "provider_calls": metrics.provider_calls,
        "average_latency_ms": metrics.average_latency_ms,
    }