"""
AI gateway package.

Exports the gateway interface and the default implementation.
"""

from app.ai.gateway.base import AIGateway
from app.ai.gateway.gateway import DefaultAIGateway

__all__ = [
    "AIGateway",
    "DefaultAIGateway",
]