"""
Base class for AI tools.
"""

from abc import ABC, abstractmethod


class AITool(ABC):
    """
    Abstract AI tool.
    """

    name: str
    description: str

    @abstractmethod
    async def execute(
        self,
        input_text: str,
    ) -> str:
        """
        Execute tool.
        """
        pass